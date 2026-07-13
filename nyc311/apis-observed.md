# APIs Observed While Crawling — NYC311

Backend/service APIs surfaced during the crawl (2026-07-13). NYC311 is unusual: the **data** API is the most-used in the city, a real **API gateway** exists, and the domain-specific **open standard** (Open311) once ran here but is now retired. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| `data.cityofnewyork.us/resource/erm2-nwe9.json` (SODA) | Open Data API | NYC / OTI | **Yes** | The 311 Service Requests dataset — **1.26M views, 590k downloads**; live SODA endpoint over tens of millions of records. The flagship civic dataset. |
| **`api.nyc.gov`** (Azure API Management) | API gateway | NYC (OTI) | **Key-gated** | A real central gateway. `api.nyc.gov/geoclient/v2` → **401**; fronts **GeoClient** (geocoding), not 311. The nearest thing NYC has to a unified API gateway. |
| **Open311 GeoReport v2** (`311api.cityofnewyork.us`, `api.311.nyc.gov`) | Open-standard 311 API | NYC | **Retired** (does not resolve) | NYC was an early Open311 adopter; the standard endpoints are gone. The open contract exists — the implementation lapsed. |
| Dynamics 365 Web API (portal backend) | CRM REST | NYC (Microsoft) | Internal | Drives report-a-problem / check-status on `portal.311.nyc.gov`. Not public. |
| `www.googletagmanager.com` | Analytics API | Google | Vendor | Tag management. |

## Takeaways

- **The reporting feed is world-class open; the interactive standard was abandoned.** NYC kept publishing 311 *data* to Open Data (huge) but let its **Open311** *service* API lapse — so you can analyze every past request but not submit or track one via a public API.
- **A gateway already exists** (`api.nyc.gov`) but is scoped to GeoClient geocoding and key-gated — under-used relative to its potential as the citywide API front door.
- **The transactional service runs on a vendor CRM** (Dynamics 365) with no public API — the same write-workflow gap seen in every other domain, here made sharper because an open standard for exactly this once existed.
- The [OpenAPI](openapi/nyc-311.yaml) + [MCP artifact](mcp/nyc-311-mcp.json) here are **Open311-aligned** — proposing to re-adopt the standard rather than invent a new contract.
