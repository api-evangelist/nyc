# Low-Hanging Fruit Index — nyc.gov/site/dsny

**Agency:** New York City Department of Sanitation (DSNY)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — only `/html/misc/` disallowed). Homepage + section pages fingerprinted from headers; the `/assets/dsny/forms/` React SPA bundle (`index-*.js`) reverse-engineered to recover the undocumented first-party backend APIs. Socrata catalog API queried for the DSNY agency footprint (`Dataset-Information_Agency = "Department of Sanitation (DSNY)"`, verified) → 51 datasets.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-dsny.md](opendata-dsny.md).

## Headline findings

1. **DSNY already runs real, first-party APIs — they're just hidden.** The collection-schedule lookup (`dsnypublic.nyc.gov/dsny/api/geocoder/DSNYCollection`), the **ePickups** bulk-pickup scheduling API (`ePickupsAPI/api/PickupRequest/AddUpdatePickUpRequest`, `GetUnavailableDates`, `IsDistrictActive`), and the CFC special-waste **appointment** API are all live NYC-owned backends — reachable only by reverse-engineering the DSNY React forms.
2. **None is documented, versioned, or agent-native.** No OpenAPI, no schemas, no developer surface. Staging hostnames (`*.dsnyad.nycnet`) even leak through the JS bundle.
3. **The write capability is real but buried.** Scheduling a bulk / large-item pickup already works through `AddUpdatePickUpRequest`; it just isn't an owned, callable resource.
4. **51 Open Data datasets (356K views)** describe the same geography — led by DSNY Monthly Tonnage (`ebb7-mvp5`, 58K), Public Recycling Bins, Recycling Diversion & Capture Rates, and the e-waste / food-scrap / special-waste drop-off directories — but sit disconnected from the live APIs.

> **Reframe (fourth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* outsourced search + a hidden backend; Council = *consolidate + own* three existing APIs; **DSNY = expose + document** first-party APIs that already run in production. The work here is least about building or reclaiming and most about **surfacing what already exists** as a documented, agent-native contract.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Collection schedule lookup | `CollectionSchedule` | React form → `geocoder/DSNYCollection` (undocumented) | 🟡 Frequencies (`rv63-53db`), Districts (`i6mn-amj2`) |
| 2 | DSNY districts / zones / frequencies | `SanitationDistrict` | Open Data + maps | ✅ `i6mn-amj2`, `ak2e-nbe8`, `rv63-53db` |
| 3 | E-waste / food-scrap / special-waste drop-off | `DropOffSite` | Open Data + CFC appointment API | ✅ `wshr-5vic`, `if26-z6xq`, `242c-ru4i` |
| 4 | Litter basket inventory | `LitterBasket` | Open Data | ✅ `8znf-7b2c`, map `d6m8-cwh9` |
| 5 | Monthly tonnage & recycling rates | `Tonnage` | Open Data | ✅ `ebb7-mvp5` (58K), `gaq9-z3hz` |
| 6 | Public recycling bins | `DropOffSite` | Open Data | ✅ `sxx4-xhzg` |
| 7 | Commercial waste zones + rate calculator | `SanitationDistrict` | form → `geocoder/BCW` + ArcGIS | ✅ `8ev8-jjxq`, map `a7bv-5698` |
| 8 | Bulk / special-waste pickup request | `BulkPickupRequest` | React form → **ePickups API** | ❌ **net-new contract** |
| 9 | Missed-collection complaint | `Complaint` | NYC 311 (separate system) | ❌ off-surface |
| 10 | Sanitation enforcement / violations | `Violation` | OATH/ECB | ❌ gap |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **First-party backends (undocumented):** collection-schedule geocoder, `geocoder/BCW`, the **ePickups** scheduling API, the **CFC appointment** API, `DSNYApi`.
- **Open:** `apps.nyc.gov/content-api` (content), `data.cityofnewyork.us` SODA (51 datasets).
- Platform: **Oracle WebCenter Sites** (`.page`, `livesite-version`) with **React** forms; backends **ASP.NET / IIS / ARR**, CORS `*`. Fourth distinct platform after Parks (Smarty/PHP), DOE (Sitefinity), Council (WordPress).
- Vendors: Esri ArcGIS (maps), Akamai mPulse + Dynatrace (monitoring), Google Translate, NYC 311.

## Reverse-engineered entities

`CollectionSchedule` · `SanitationDistrict` (district/section/zone + frequencies) · `DropOffSite` (e-waste / food scrap / special waste / recycling bin) · `LitterBasket` · `Tonnage` · `BulkPickupRequest` (net-new write) — join keys: **DSNY district code** (e.g. `MN01`), **community district**, **DSNY zone**.

## Next

1. **JSON Schema** per entity, reconciling the geocoder/ePickups payloads with the Open Data column names.
2. **OpenAPI** documenting the existing backends (collection schedule, ePickups, CFC appointment) + Open Data behind one owned contract (+ the net-new `BulkPickupRequest` write).
3. **MCP** artifact: `get_collection_schedule`, `find_districts`, `get_district`, `find_drop_off_sites`, `find_litter_baskets`, `find_tonnage`, `schedule_bulk_pickup`.
