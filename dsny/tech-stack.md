# Technology & Vendor Inventory — nyc.gov/site/dsny

What the NYC Department of Sanitation's web presence is built on and which services it depends on — fingerprinted from response headers, page markup, and the DSNY React form bundle during the crawl (2026-07-13). DSNY is the **fourth distinct pattern** in this project (after Parks' Smarty/PHP, DOE's Sitefinity/.NET, and Council's WordPress).

## Platform & hosting

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CMS | **Oracle WebCenter Sites** (FatWire) | `.page` URLs, `livesite-version` header, `/site/dsny/...index.page` pattern |
| Web server / edge | **nginx** + **Akamai** | `server: nginx`, `mpulse_cdn_cache`, `alt-svc: h3` |
| Interactive forms | **React SPA** | `/assets/dsny/forms/…` bundles `static/js/index-*.js` (collection schedule, rate calculator, service-request status) |
| Content delivery | **NYC content API** | `apps.nyc.gov/content-api/v1/content/dsny/` (open JSON, 200) |
| Performance monitoring | **Dynatrace** (OneAgent) + **Akamai mPulse** (Boomerang) | `x-oneagent-js-injection`, `go-mpulse.net`, `dtagent` in etag |
| Translation | **Google Translate** widget | `translate.google.com/translate_a/element.js` |

## The backend APIs (the important part)

DSNY's transactional and lookup capabilities are **not** static pages — the React forms call **real first-party backend APIs**, all **undocumented** and reachable only by reading the form bundle:

| API | Host / path | Role |
|---|---|---|
| **Collection-schedule geocoder** | `dsnypublic.nyc.gov/dsny/api/geocoder/DSNYCollection` | Resolve an address → DSNY district + refuse/recycling/organics days |
| Commercial-waste geocoder | `dsnypublic.nyc.gov/dsny/api/geocoder/BCW` | Address → commercial-waste zone (rate calculator) |
| DSNY services API | `a827-donatenyc.nyc.gov/DSNYApi/api` | ASP.NET Web API backing the DSNY forms |
| **ePickups API** | `a827-donatenyc.nyc.gov/ePickupsAPI/api/PickupRequest/*` | `AddUpdatePickUpRequest`, `GetUnavailableDates`, `IsDistrictActive` — schedules bulk/large-item pickups |
| **CFC appointment API** | `dsnydonate.nyc.gov/cfc/api/appointment` | Special-waste (CFC appliance) drop-off appointment booking |

Backend stack: **Microsoft-IIS/10.0**, **ASP.NET 4.0** Web API, behind **ARR/3.0** reverse proxy, with permissive CORS (`access-control-allow-origin: *`). Non-`.nyc.gov` staging hosts (`donatedev/donatestg.dsnyad.nycnet`, `msswvw-dnsdnyvp.csc.nycnet`) leak through the bundle.

## Data & maps

| Capability | Vendor / source |
|---|---|
| Open data | **Socrata / Tyler** — 51 DSNY datasets on `data.cityofnewyork.us` |
| Commercial-waste-zone maps | **Esri ArcGIS** REST layers |
| Complaints / service requests | **NYC 311** (`portal.311.nyc.gov`) — separate system |

## Contrast with Parks, DOE & Council

- **The APIs already exist — and they're first-party.** Unlike Council (whose legislative API is a *vendor's*, Granicus/Legistar), DSNY's lookup and scheduling APIs are **NYC-owned** (`dsnypublic.nyc.gov`, `ePickupsAPI`, the CFC appointment API). The problem is not ownership and not vendor lock-in.
- **The problem is they're hidden.** No documentation, no OpenAPI, no schemas, no versioning, no agent surface — they exist only as the private backends of React forms, discoverable only by reverse-engineering a JS bundle.

## Modernization implications

1. **Expose and document, don't build.** DSNY should publish the collection-schedule geocoder, the ePickups scheduling API, and the CFC appointment API as one owned, versioned, documented contract ([OpenAPI](openapi/dsny.yaml)) — turning private form backends into public resources.
2. **Promote the write surface.** `AddUpdatePickUpRequest` already exists; give it a first-class, documented **BulkPickupRequest** resource so residents and agents can schedule pickups without scraping a form.
3. **Join Open Data to the live APIs.** The 51 datasets (tonnage, drop-off sites, districts/frequencies, litter baskets) describe the same geography the geocoder resolves to — surface them behind the same resource model instead of as disconnected exports.
