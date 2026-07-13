# Low-Hanging Fruit Index — OTI

**Agency:** NYC Office of Technology & Innovation (OTI, formerly DoITT)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the OTI informational site `nyc.gov/content/oti` (Akamai + nginx + NYC.gov "Livesite" v22 + mPulse + Dynatrace) and probed the citywide platforms OTI **operates**: the **api.nyc.gov** gateway (Microsoft **Azure API Management** — `Request-Context appId` + `401 "missing subscription key"`; GeoClient/GeoSearch key-gated), the open **GeoSearch/Pelias** geocoder at `geosearch.planninglabs.nyc` (HTTP 200), and **NYC Open Data** on **Socrata**/Tyler (`X-Socrata-Region`/`RequestId`). Verified the NYC Open Data agency label `Office of Technology and Innovation (OTI)` via the Socrata Discovery API and pulled all **221** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-oti.md](opendata-oti.md).

## Headline findings

1. **OTI is the META case.** It is not an agency with data trapped in HTML — it **operates the city's data infrastructure**: NYC Open Data (data.cityofnewyork.us / Socrata), the **api.nyc.gov gateway** (Azure APIM; GeoClient/GeoSearch), NYC.gov itself, LinkNYC, municipal broadband, public Wi-Fi, and the **311** pipeline.
2. **As a publisher it is enormous.** **221 datasets** under the OTI label — including the **most-viewed dataset in the whole city** (311 Service Requests, `erm2-nwe9`, 1.26M+ views), the **catalog of itself** (LL251 Published Data Asset Inventory `5tqd-u88y` + Release Tracker `qj2z-ibhs`), LinkNYC, broadband, Wi-Fi, and the entire planimetric base map.
3. **The gateway is real but not productized.** api.nyc.gov runs on Azure APIM, but has **no owned, machine-readable catalog of its services and no self-service key API** — GeoClient answers `401 "missing subscription key"` and keys come from a developer portal.
4. **The gap is a product, not data or plumbing.** Because the data is open and the gateway exists, the modernization is to **productize the operator role**: one owned, unified gateway + catalog API, plus the two operator writes (register a dataset, request a key).

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a service layer locked in a vendor CRM; **OTI = productize the operator role.** OTI already runs the catalog, the gateway, and 311 — the work is least about liberating data and most about packaging the platform operator as a first-class, agent-native citywide API product, and making OTI the registry anchor the other NYC domains point at.

## The fruit

| # | Name | Entity | Where it lives | Open Data / API twin |
|---|---|---|---|---|
| 1 | NYC Open Data catalog (the catalog itself) | `OpenDataset` | Socrata + Discovery | 🟡 open, not owned — LL251 Inventory (`5tqd-u88y`) |
| 2 | api.nyc.gov gateway services | `APIGatewayService` | Azure APIM | ❌ key-gated, no catalog / no key API |
| 3 | Geocoding (GeoClient / GeoSearch) | `APIGatewayService` | api.nyc.gov + GeoSearch | ✅ GeoSearch open (`geosearch.planninglabs.nyc`) |
| 4 | LinkNYC kiosks | `LinkNYCKiosk` | SODA (×4) | ✅ Locations (`s4kf-3yrf`) + Status (`n6c5-95xh`) |
| 5 | Municipal broadband assets | `BroadbandAsset` | SODA (×3) | ✅ Broadband Asset (`2bsr-c6qq`) |
| 6 | Public Wi-Fi hotspots | `WiFiHotspot` | SODA | ✅ Wi-Fi Hotspot Locations (`yjub-udmw`) |
| 7 | 311 Service Requests | `ServiceRequest` | SODA | ✅ 311 SR (`erm2-nwe9`, 1.26M views) |
| 8 | **Register a dataset** | `OpenDataset` | internal Socrata workflow | ❌ **net-new write** |
| 9 | **Request a gateway key** | `APIGatewayService` | developer portal | ❌ **net-new write** |
| 10 | Planimetric base map & footprints | `OpenDataset` | SODA + map/raster | ✅ BUILDING (`5zhs-2jue`), Centerline (`inkn-q76z`), DEM/Land Cover |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **api.nyc.gov** — the citywide **API gateway** OTI operates on **Microsoft Azure API Management** (GeoClient, GeoSearch); key-gated, no self-service key API.
- **Socrata SODA + Discovery** — the NYC Open Data platform OTI runs for the whole city; 221 OTI datasets, 2,300+ citywide.
- **GeoSearch (Pelias)** — open geocoder over GeoSupport, the open twin of GeoClient.
- Platform: the OTI informational site sits on the **NYC.gov "Livesite" v22** chassis (Akamai + nginx + mPulse + Dynatrace) — the same chassis OTI itself operates.

## Reverse-engineered entities

`OpenDataset` (catalog entry — the META entity) · `APIGatewayService` (GeoClient/GeoSearch on api.nyc.gov) · `LinkNYCKiosk` · `BroadbandAsset` · `WiFiHotspot` · `ServiceRequest` (311) — join keys: **Socrata UID (four-by-four)**, **serviceId**, **Site ID**, **BBL/BIN**, **Unique Key**, and the shared NYC **geography spine**.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (Socrata UID, LL251 compliance flags, LinkNYC Site ID + live status, broadband fiber flags, 311 fields) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the catalog + gateway + geocoder as clean resources + the net-new `POST /datasets` (register) and `POST /gateway/keys` (request key) — done ([openapi/oti.yaml](openapi/oti.yaml)).
3. **MCP** artifact: `search_datasets`, `get_dataset`, `register_dataset`, `list_gateway_services`, `get_gateway_service`, `request_api_key`, `geocode`, `find_linknyc_kiosks`, `find_broadband_assets`, `find_wifi_hotspots`, `find_service_requests` — done ([mcp/oti-mcp.json](mcp/oti-mcp.json)).
