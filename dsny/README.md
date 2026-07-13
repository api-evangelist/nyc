# dsny (nyc.gov/site/dsny) — Low-Hanging Fruit Assessment

Fourth domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **New York City Department of Sanitation (DSNY)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (collection schedules, districts, drop-off sites, litter baskets, tonnage, bulk pickups).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (Oracle WebCenter Sites, React forms, ASP.NET/IIS backends, Esri, Akamai/Dynatrace).
- [apis-observed.md](apis-observed.md) — the **existing first-party backend APIs** (collection-schedule geocoder, ePickups scheduling, CFC appointment) + Open Data + vendors.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (51 DSNY datasets) with coverage verdicts.
- [opendata-dsny.md](opendata-dsny.md) / [opendata-dsny.json](opendata-dsny.json) — the 51 DSNY Open Data datasets + column schemas.
- [schemas/](schemas/) — individual JSON Schema per object: `sanitation-district` · `collection-schedule` · `drop-off-site` · `litter-basket` · `tonnage` · `bulk-pickup-request` (+ shared `_common`).
- [openapi/dsny.yaml](openapi/dsny.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/dsny-mcp.json](mcp/dsny-mcp.json) — design-first MCP server definition (7 agent tools; artifact, not a deployment).

## What was found — the fourth distinct pattern

DSNY is the domain where **the APIs already exist and are first-party — they're just hidden.** Its interactive forms call real NYC-owned backends:

1. **Collection-schedule geocoder** (`dsnypublic.nyc.gov/dsny/api/geocoder/DSNYCollection`) — resolves an address to a DSNY district and refuse/recycling/organics days. Live, undocumented.
2. **ePickups API** (`a827-donatenyc.nyc.gov/ePickupsAPI/api/PickupRequest/AddUpdatePickUpRequest`, plus `GetUnavailableDates`, `IsDistrictActive`) — already schedules bulk/large-item pickups. Live, undocumented.
3. **CFC appointment API** (`dsnydonate.nyc.gov/cfc/api/appointment`) — books special-waste drop-off appointments. Live, undocumented.

**None is documented, versioned, or agent-native.** They're the private backends of React forms, discoverable only by reverse-engineering a JS bundle. Alongside sit **51 Open Data datasets** (356K views) describing the same geography — disconnected from the live APIs.

**Reframe (vs. the first three domains):**

| | Parks | DOE | Council | **DSNY** |
|---|---|---|---|---|
| Platform | Smarty/PHP | Sitefinity (.NET) | WordPress | **Oracle WebCenter Sites + React** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned/unified | **first-party APIs exist but undocumented/hidden** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **expose + document** |

## Reverse-engineered entities

`CollectionSchedule` · `SanitationDistrict` (district/section/zone + frequencies) · `DropOffSite` (e-waste / food scrap / special waste / recycling bin) · `LitterBasket` · `Tonnage` · `BulkPickupRequest` (net-new write) — join keys **DSNY district code** (e.g. `MN01`), **community district**, **DSNY zone**.

## Method & caveats

Outside-in crawl (browser UA; `robots.txt` disallows only `/html/misc/`). The DSNY React form bundle was read to recover backend endpoints; those backends were probed (they returned 500/404 without the exact params the SPA sends — documented as live-but-undocumented, not exercised). Socrata catalog verified the agency label and enumerated 51 datasets. A sample, not a full spider.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed (3 hidden first-party APIs + Open Data) ✅ · Open Data crosswalk (51 DSNY datasets) ✅ · JSON Schemas (6 + `_common`) ✅ · OpenAPI 3.1 (10 paths/11 ops) ✅ · MCP artifact (7 tools) ✅.
- **Next:** publish the existing backends as one documented, versioned contract; promote `BulkPickupRequest` to a first-class write resource; join Open Data to the live geocoder; then the fifth domain from [../domains.md](../domains.md).
