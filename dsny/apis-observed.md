# APIs Observed While Crawling — nyc.gov/site/dsny

Backend/service APIs the DSNY web presence calls or exposes, surfaced during the crawl (2026-07-13). DSNY is unusual in the opposite direction from Council: **real first-party APIs already exist** — a collection-schedule geocoder, a bulk-pickup scheduling API, and a special-waste appointment API — but every one is **undocumented and hidden behind React forms**, with no OpenAPI, schemas, versioning, or agent surface. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`dsnypublic.nyc.gov/dsny/api/geocoder/DSNYCollection`** | Collection-schedule geocoder | **NYC DSNY** | **Live, undocumented** (500 without valid params) | Resolves an address → DSNY district + refuse/recycling/organics days. The engine behind the "collection schedule" form. First-party, but forms-only. |
| `dsnypublic.nyc.gov/dsny/api/geocoder/BCW` | Commercial-waste-zone geocoder | NYC DSNY | Live, undocumented | Address → commercial-waste zone; powers the rate calculator. |
| **`a827-donatenyc.nyc.gov/ePickupsAPI/api/PickupRequest/*`** | Bulk-pickup scheduling API | **NYC DSNY** | **Live, undocumented** | `AddUpdatePickUpRequest`, `GetUnavailableDates`, `IsDistrictActive`. Already schedules bulk/large-item pickups (`AppointmentDate`/`AppointmentTime`/`AppointmentItems`/`BulkPickup`). ASP.NET Web API, `access-control-allow-origin: *`. The backend behind the net-new `BulkPickupRequest`. |
| `dsnydonate.nyc.gov/cfc/api/appointment` | Special-waste appointment API | NYC DSNY | Live, undocumented | CFC / special-waste drop-off appointment booking. |
| `a827-donatenyc.nyc.gov/DSNYApi/api` | DSNY services API | NYC DSNY | Live, undocumented | ASP.NET Web API (IIS 10, ARR/3.0) backing the DSNY forms. |
| `apps.nyc.gov/content-api/v1/content/dsny/` | Content API | NYC (DoITT) | **Yes — open** | Open JSON content API (200) serving DSNY page/form content. |
| `data.cityofnewyork.us` (SODA) | Open data API | NYC (Socrata/Tyler) | Yes | 51 DSNY datasets — tonnage, recycling rates, drop-off sites, litter baskets, districts/zones/frequencies. |
| ArcGIS REST (`services.arcgis.com/.../DSNY_commercial_waste_zones`) | Maps/geo API | Esri / DSNY | Vendor | Commercial-waste-zone map layers. |
| `portal.311.nyc.gov` | Service-request portal | NYC 311 | HTML/API | Where missed-collection and sanitation complaints are filed — a separate system, not a DSNY API. |
| `go-mpulse.net`, Dynatrace (`x-oneagent`), Google Translate | RUM / APM / i18n | Akamai / Dynatrace / Google | Vendor | Performance monitoring and page translation. |

## Takeaways

- **The API problem here is exposure, not absence or ownership.** DSNY already operates first-party lookup and scheduling APIs — the opposite of Council, whose legislative API belongs to a *vendor* (Granicus). Nobody has to build these or wrest them back from a vendor.
- **They're private form backends.** No documentation, no OpenAPI, no versioning, no agent surface — discoverable only by reverse-engineering the React form bundle (`/assets/dsny/forms/static/js/index-*.js`). Staging hostnames (`*.dsnyad.nycnet`, `*.csc.nycnet`) even leak through it.
- **The write surface is real but buried.** `ePickupsAPI/api/PickupRequest/AddUpdatePickUpRequest` already schedules bulk pickups; it just isn't a documented, owned resource anyone can call.
- **An owned, agent-native contract.** The [OpenAPI](openapi/dsny.yaml) + [MCP artifact](mcp/dsny-mcp.json) here propose documenting and consolidating these existing backends — plus the 51 Open Data datasets — behind one resource model.
