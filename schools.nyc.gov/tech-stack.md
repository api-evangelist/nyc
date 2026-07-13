# Technology & Vendor Inventory — schools.nyc.gov

What the New York City Public Schools (NYCPS / DOE) website is built on and which third parties it depends on — fingerprinted from response headers and page markup during the crawl (2026-07-13). Part of the modernization picture: vendor lock-in and outsourced capabilities are as much a modernization constraint as the data itself.

## Platform & hosting

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CMS | **Progress Sitefinity** (.NET) | 39 `Sitefinity` refs; `/Sitefinity/*`, `/CustomApi/*` in robots.txt; `PersonalizationTracker` script |
| Asset / blob storage | **Azure Blob Storage** (`pwsblobprd.schools.nyc`, container `prd-pws`) | 69 references (images, docs, logos) |
| Edge cache / CDN | Caching layer (`x-cache: TCP_HIT`, `x-cache-info: L1_T2`); **Cloudflare** cdnjs for libs | response headers; `cdnjs.cloudflare.com` |
| Fonts | Google Fonts | `fonts.googleapis.com`, `fonts.gstatic.com` |
| Identity | **NYC Schools Account (NYCSA)** on `nycenet.edu` (`pwsauth.nycenet.edu`) | auth subdomain |

## Capabilities outsourced to vendors

| Capability | Vendor | Notes |
|---|---|---|
| **Site search / "Find a School"** | **HawkSearch** (`lusearchapi-na.hawksearch.com/sites/nycdoe`, `nycdoe.tracking-na.hawksearch.com`) | The school directory search is a **proprietary vendor search API**, not a public/productized DOE API. Key modernization finding. |
| Analytics / tag mgmt | **Google Tag Manager** / gtag | 9 refs |
| Accessibility & analytics | **Siteimprove** | 3 refs |
| Social pixel | **Meta / Facebook Pixel** | `connect.facebook.net` |
| Mapping | **Esri ArcGIS JS** (`js.arcgis.com`) + Google Maps | school locator maps |

## Related DOE / NYCPS properties (distinct apps & subdomains)

| Property | Domain | Role |
|---|---|---|
| Enrollment / applications | **`myschools.nyc`** | 3K–12 admissions & application system (the transactional core) |
| Data hub | **`infohub.nyced.org`** | DOE data & reports (demographics, results) — largely Excel downloads |
| Teacher portal | `teachhub.schools.nyc` | staff apps |
| Support | `supporthub.schools.nyc` | help desk |
| Parent portal | `parentu.schools.nyc`, `www.schoolsaccount.nyc` | families |
| Legacy tools | `tools.nycenet.edu`, `nycenet.edu` | legacy DOE apps + auth |
| Construction surveys | `survey.nycsca.org` | School Construction Authority |

## Modernization implications

1. **Search is a black box.** "Find a School" runs on HawkSearch — a vendor index, not an API DOE controls. A modern school API would let DOE own discovery and expose it to agents rather than renting it.
2. **The real backend is hidden.** School profile pages are JS-rendered from an internal `/CustomApi/*` (robots-disallowed) — the machine-readable data exists server-side but is neither public nor documented.
3. **Fragmented identity & apps.** Enrollment, data, staff, and parent tools each live on their own subdomain/vendor with separate auth (`nycenet.edu` NYCSA) — a unified API + identity is the integration opportunity.
4. **Data offloaded to Excel.** InfoHub distributes reports as spreadsheets; NYC Open Data has the structured twins (see [crosswalk.md](crosswalk.md)).
