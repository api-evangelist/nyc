# oti — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Office of Technology & Innovation (OTI, formerly DoITT)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (the catalog itself, api.nyc.gov gateway, geocoding, LinkNYC, broadband, Wi-Fi, 311, and the two net-new operator writes).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" site; **the platforms OTI operates** — Socrata Open Data, **api.nyc.gov on Azure API Management**, GeoSearch/Pelias).
- [apis-observed.md](apis-observed.md) — the inverse finding: OTI **runs the city's APIs** (Open Data, the gateway, 311) but has **no owned, unified contract** and **no self-service write**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (221 OTI datasets) with coverage verdicts.
- [opendata-oti.md](opendata-oti.md) / [opendata-oti.json](opendata-oti.json) — all 221 OTI Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `open-dataset` · `api-gateway-service` · `linknyc-kiosk` · `broadband-asset` · `wifi-hotspot` · `service-request` (+ shared `_common`).
- [openapi/oti.yaml](openapi/oti.yaml) — OpenAPI 3.1 contract `$ref`ing each object (read catalog + gateway + geocode; write register-dataset + request-key).
- [mcp/oti-mcp.json](mcp/oti-mcp.json) — design-first MCP server definition (11 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

OTI is the **META case**, and that is the finding:

1. **OTI operates the city's data infrastructure.** It runs **NYC Open Data** (data.cityofnewyork.us / Socrata-Tyler), the **api.nyc.gov gateway** (Microsoft Azure API Management; GeoClient/GeoSearch), NYC.gov itself, LinkNYC, municipal broadband, public Wi-Fi, and the **311** pipeline.
2. **As a publisher it is enormous** — 221 datasets, including the **most-viewed dataset in the whole city** (311, `erm2-nwe9`, 1.26M+ views) and the **catalog of itself** (the LL251 Published Data Asset Inventory).
3. **But the operator role is not productized.** The gateway is key-gated with a 401 and a portal; the catalog is queryable only through Socrata's generic API; there is **no single owned contract** spanning "find a dataset → find a gateway service → geocode → register an asset," and **no self-service write** for either operator workflow.

**The gap here is a product, not data or plumbing.** A developer or agent asking "what services run on api.nyc.gov and how do I get a key?" or "register this dataset for my agency" has no owned API to call.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **OTI** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | Livesite + Oracle Siebel | **operates Socrata + Azure APIM + Livesite** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked | **runs the infra, never productized it** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **productize** |

## Reverse-engineered entities

`OpenDataset` (catalog entry — the META entity) · `APIGatewayService` (GeoClient/GeoSearch on api.nyc.gov) · `LinkNYCKiosk` · `BroadbandAsset` · `WiFiHotspot` · `ServiceRequest` (311) — join keys **Socrata UID (four-by-four)**, **serviceId**, **Site ID**, **BBL/BIN**, **Unique Key**, and the shared NYC **geography spine**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite v22, mPulse, Dynatrace). The **api.nyc.gov** gateway was identified as Microsoft Azure API Management from `Request-Context appId` and the `401 "missing subscription key"` body (GeoClient is key-gated; not authenticated). **GeoSearch** (`geosearch.planninglabs.nyc`) returned live geocoding (200). The **Open Data** platform was confirmed as Socrata from `X-Socrata-Region`/`RequestId`; the agency label `Office of Technology and Innovation (OTI)` (221 assets) was verified via the Socrata Discovery API and all 221 pulled with columns. A sample, not a full spider; the gateway's internal service list and key-issuance workflow are inferred, not scraped behind the portal.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (221 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (12 paths/13 ops, 2 writes) ✅ · MCP artifact (11 tools) ✅.
- **Next:** an example implementation fronting api.nyc.gov + Socrata for `search_datasets` / `list_gateway_services` / `register_dataset`; wire OTI as the **registry anchor** (nyc-commons) for the other NYC domains; then the next domain from [../domains.md](../domains.md).
