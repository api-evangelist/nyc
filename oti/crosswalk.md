# Crosswalk — Platform Fruit ↔ APIs ↔ NYC Open Data (OTI)

Maps the low-hanging fruit on **nyc.gov/content/oti** and the **platforms OTI operates** to (a) the **existing APIs** (the api.nyc.gov gateway; GeoSearch; Socrata SODA/Discovery) and (b) the **221 OTI datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-oti.json](opendata-oti.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** the reference data is open, but resident transactions are locked in a vendor CRM → *unlock the service layer.*
- **OTI:** the agency that **operates all of the above infrastructure** — Open Data, the gateway, 311 — where the data is already open and the gateway already runs → **productize the operator role.**

OTI is the META case. The problem is not that data is trapped in HTML (OTI publishes 221 datasets, including the catalog of the entire corpus and the city's most-viewed dataset). It is not that there is no gateway (OTI runs api.nyc.gov on Azure APIM). It is that the **platform operator has never packaged itself as a product**: there is no single owned API that lets a developer or agent discover a dataset, discover a gateway service, geocode an address, and register an asset — and no self-service way to get a gateway key. A developer meets Socrata's generic API on one side and a 401-and-a-portal on the other.

Coverage: ✅ strong open twin · 🟡 open but no owned/unified contract · ❌ gap (no API).

## Entity crosswalk

| Entity | Platform surface | API today | Open Data | Cov. |
|---|---|---|---|---|
| `OpenDataset` (catalog itself) | Open Data catalog | Socrata Discovery (generic) | LL251 Inventory (`5tqd-u88y`, 26c); Release Tracker (`qj2z-ibhs`); Help Desk (`63us-eqtq`) | 🟡 open, not owned |
| `APIGatewayService` (GeoClient/GeoSearch) | `api.nyc.gov` | **Azure APIM, key-gated** | — | ❌ no catalog / no key API |
| geocoding | GeoClient / GeoSearch | GeoClient (key) · **GeoSearch open** | — | ✅ open twin (GeoSearch) |
| `LinkNYCKiosk` | LinkNYC franchise | SODA | Locations (`s4kf-3yrf`, 32c); Status (`n6c5-95xh`, 39c); Usage (`69wu-b929`); Permits (`xp25-gxux`) | ✅ |
| `BroadbandAsset` | Municipal broadband / Internet Master Plan | SODA | Broadband Asset (`2bsr-c6qq`, 31c); Target Neighborhoods (`2qqs-crk2`); Master Plan (`fg5j-q5nk`, 77c) | ✅ |
| `WiFiHotspot` | Public Wi-Fi | SODA | NYC Wi-Fi Hotspot Locations (`yjub-udmw`, 38c) | ✅ |
| `ServiceRequest` (311) | 311 pipeline | SODA | 311 SR 2020-Present (`erm2-nwe9`, 48c, 1.26M views); 2010-2019 (`76ig-c548`); SLA (`cs9t-e3x8`) | ✅ |
| Register a dataset | Open Data publishing | **internal Socrata workflow** | — | ❌ **net-new write** |
| Request a gateway key | api.nyc.gov developer portal | **portal only** | — | ❌ **net-new write** |
| Planimetric base map | GIS division | SODA + map/raster services | BUILDING (`5zhs-2jue`); Centerline (`inkn-q76z`, 64c); DEM/Land Cover | ✅ (dozens of assets) |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA + Discovery (221 datasets)** | Open, machine-readable; the whole catalog incl. 311, LinkNYC, broadband, base map | Generic vendor API, not an OTI-owned contract; catalog querying is Socrata's shape, not the city's |
| **api.nyc.gov gateway (Azure APIM)** | A real, running citywide gateway (GeoClient, GeoSearch, agency APIs) | Key-gated with a 401; no owned catalog of services; **no self-service key API** |
| **GeoSearch (Pelias)** | Open geocoding over GeoSupport, no key | Owned by a sibling (Planning Labs), not surfaced as an OTI product |

## Implications for the API-first + MCP proposal

1. **Publish one owned, unified contract over what OTI already runs.** Datasets, gateway services, geocoding, LinkNYC, broadband, Wi-Fi, and 311 behind one OTI API ([OpenAPI](openapi/oti.yaml)) — so consumers learn one model, not "Socrata + a portal."
2. **Add the two operator writes.** `registerDataset` (publish an asset to the LL251 catalog) and `requestApiKey` (self-service gateway key) — the programmatic surfaces a platform operator should own.
3. **Front the gateway, don't replace it.** The api.nyc.gov Azure APIM gateway stays; the owned API gives it a catalog and a key workflow, and fronts GeoClient/GeoSearch as one `geocode` operation.
4. **Make OTI the registry anchor.** As the platform operator, OTI is the natural home for the project's **nyc-commons + registry** ideas — the place the other 60+ NYC domains register their own APIs, schemas, and MCP servers.
5. **MCP server** so an agent can answer "which dataset has LinkNYC status?", "what services run on api.nyc.gov and how do I get a key?", "geocode 120 Broadway", and "register this dataset for my agency."
