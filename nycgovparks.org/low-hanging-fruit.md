# Low-Hanging Fruit Index — nycgovparks.org

**Agency:** NYC Department of Parks & Recreation (NYC Parks)
**Assessed:** 2026-07-13
**Method:** Bounded outside-in crawl (browser user-agent, respecting robots.txt — `crawler4j` and admin/`/xml/` paths are disallowed, so those were avoided). Section landing pages plus a representative sample of listing, form, and database pages were fetched and analyzed for HTML tables (>10 rows), div-based record listings, forms (with field counts), and links to machine-readable files. Counts marked **verified** were observed directly; unmarked facility/permit rows are extrapolated from their section index pages and still need a per-page confirmation pass.

Machine-readable = a CSV / XLS / XLSX / XML / JSON / GeoJSON download link. See the JSON version at [fruit.json](fruit.json).

## Headline findings

1. **On the domain itself, data is everywhere but machine-readable data is nowhere.** NYC Parks renders deep, structured, citywide data as HTML tables, div listings, and PDFs — **zero** CSV/XLS/XML/JSON download links anywhere on the domain.
2. **But the machine-readable twins already exist off-domain.** Cross-checking NYC Open Data (`data.cityofnewyork.us`) found **237 DPR assets** (147 datasets, 51 maps, 36 export links) — a twin for **most** website resources, including literal "Directory of Basketball Courts / Tennis Courts / Dog Runs / Recreation Centers / Playgrounds / Pools." **The website just never links to or consumes them.** Two disconnected worlds. → see [crosswalk.md](crosswalk.md) and [opendata-parks.md](opendata-parks.md).
3. **The declared sitemap is broken.** `robots.txt` points to `https://www.nycgovparks.org/sitemap.xml`, which returns the site's 404 page.
4. **Legacy backends leak into URLs** — e.g. the Historical Signs database runs on `/sub_your_park/historical_signs/hs_with_monument.php`.
5. **No developer / API / open-data page exists on the domain.** The interactive [NYC Tree Map](https://tree-map.nycgovparks.org/) is the only app-like data surface, and it talks to an undocumented internal JSON API.
6. **The real gaps are narrow and specific:** ~12 facility types (Bocce, Horseback, Fishing, Barbecue, Historic Houses, Nature Centers, Media Labs, Pickleball, WiFi, Zoo…), the Rules, and — most importantly — **all permit *applications*** (login-gated on the site; Open Data only has permit *areas* + granted-permit logs, no application API).

> **Reframe:** this is not a data-liberation problem, it's an **integration + API-productization** problem. Unify the existing Open Data behind one resource-oriented Parks API + MCP, close the ~12 gaps, and build the missing permit-application API.

## The fruit

### Core directories & databases (highest-value API candidates)

| # | Name | Type | Entity | Rows / fields | Machine-readable? | URL |
|---|---|---|---|---|---|---|
| 1 | Parks Directory ("Find a Park") | search-form + listing | `Park` | 1,700+ properties | ❌ | [/parks](https://www.nycgovparks.org/parks) |
| 2 | Capital Project Tracker | HTML table | `CapitalProject` | 6 tables / 535 rows ✅ | ❌ | [/planning-and-building/capital-project-tracker](https://www.nycgovparks.org/planning-and-building/capital-project-tracker) |
| 3 | Events Calendar | search-form + listing | `Event` | 91 filter inputs ✅ | ❌ | [/events](https://www.nycgovparks.org/events) |
| 4 | Historical Signs Database | search-form + DB (legacy `.php`) | `HistoricalSign` | thousands | ❌ | [/about/history/historical-signs](https://www.nycgovparks.org/about/history/historical-signs) |
| 5 | NYC Tree Map | map app (internal JSON API) | `Tree` | ~650,000+ | ⚠️ app-internal | [tree-map.nycgovparks.org](https://tree-map.nycgovparks.org/) |
| 6 | Rules & Regulations | HTML + PDF | `Rule` | — | ❌ | [/rules](https://www.nycgovparks.org/rules) |

### Facility directories (~42 types, one citywide directory each)

Each is a >10-row structured listing (HTML table or repeated div records). Row counts below are **confirmed** from the confirmation pass. Open Data coverage: ✅ strong twin · 🟡 partial/rolled-up · ❌ true gap (on site, not in Open Data). Full mapping in [crosswalk.md](crosswalk.md).

| Facility type | Rows | Open Data twin | Cov. |
|---|---|---|---|
| Basketball | 582 | Directory of Basketball Courts (`b937-zdky`) | ✅ |
| Handball | 552 | Athletic Facilities (`qnem-b8re`) | 🟡 |
| Spray Showers | 594 | NYC Parks Spray Showers | ✅ |
| Restrooms | 1,275 | Directory Of Toilets In Public Parks (`hjae-yuav`) | ✅ |
| Soccer | 405 | Athletic Facilities; Synthetic Turf Fields | 🟡 |
| Baseball | 249 | Athletic Facilities; Synthetic Turf | 🟡 |
| Fitness Equipment | 192 | Adult Exercise Equipment (partial) | 🟡 |
| WiFi | 205 | — | ❌ |
| Great Trees | 124 | 2015 Street Tree Census (partial) | 🟡 |
| Tennis | 116 | Directory of Tennis Courts (`dies-sqgi`) | ✅ |
| Barbecue | 78 | — | ❌ |
| Recreation Centers | 73 | Directory of Recreation Centers (`ydj7-rk56`) | ✅ |
| Football | 60 | Athletic Facilities | 🟡 |
| Volleyball | 49 | Athletic Facilities | 🟡 |
| Bocce | 41 | — | ❌ |
| Running Tracks | 41 | Athletic Facilities | 🟡 |
| Fishing | 33 | — | ❌ |
| Kayak/Canoe | 27 | KayakCanoeLaunch_20190417 | ✅ |
| Hockey | 24 | Athletic Facilities (partial) | 🟡 |
| Cricket | 20 | Athletic Facilities | 🟡 |
| Golf | 16 | Golf Courses; DPR_GolfCourses_001 | ✅ |
| Horseback | 12 | — | ❌ |
| Outdoor Pools | 11 | NYC Parks Pools (`y5rm-wagw`); Directory of Outdoor Pools | ✅ |
| Ice Skating | 11 | IceSkatingRinks_20190417 | ✅ |
| Dog Areas | div-listing | Directory of Dog Runs (`ipbu-mtcs`); Dog Runs (`hxx3-bwgv`) | ✅ |
| Playgrounds | div-listing | Directory of Playgrounds (`59gn-q4ai`); DPR_PlayAreas_001 | ✅ |
| Beaches | div-listing | Beaches; DPR_Beaches_001 | ✅ |
| Skate Parks | div-listing | NYC Parks SkateParks | ✅ |
| Model Aircraft | div-listing | DPR_ModelAircraftFields_001 | ✅ |
| Food/Concessions | div-listing | Parks Concessions | ✅ |
| Water Fountains | (404 on site) | NYC Parks Drinking Fountains; Cool It! NYC | ✅ |
| Indoor Pools | div-listing | Directory of Indoor Swimming Pools (`x57r-az25`) | ✅ |
| Hiking Trails | div-listing | Parks Trails (partial) | 🟡 |
| Bikeways/Greenways | div-listing | Greenstreets (partial) | 🟡 |
| Historic Houses | div-listing | — | ❌ |
| Nature Centers | div-listing | — | ❌ |
| Media Labs | div-listing | — | ❌ |
| Pickleball | div-listing | — | ❌ |
| Zoo | div-listing | — | ❌ |
| Boating / Rowboats | div-listing | (see Kayak / Pools) | 🟡 |

**Facility column model (from confirmed page headers):** common core `Name · Location · Accessible`, plus type-specific attributes — `# of Courts` / `# of Fields`, `Type of Surface`, `In/Outdoor`, `Phone`, `Number`. Feeds the `Facility` JSON Schema.

### Permit / application forms (one workflow each)

Each is a form (or PDF form) collecting an application. **The athletic/field-and-court application is login-gated** (the visible fields are the account login, not the application), confirming these are transactional workflows behind auth. Open Data exposes only permit *areas* (`c5vm-g2dk`) and granted-permit logs (`Research Permits` `nnf6-km2a`) — **there is no permit-application API.** This is the highest-value net-new API/MCP surface. Prime candidates for API-driven submission + status.

| Permit | Entity | Evidence | URL |
|---|---|---|---|
| Field & Court (athletic) | `PermitApplication:FieldAndCourt` | 12 inputs ✅ | [/permits/field-and-court/request](https://www.nycgovparks.org/permits/field-and-court/request) |
| Tennis Permit | `PermitApplication:Tennis` | form + PDF ✅ | [/permits/tennis-permits](https://www.nycgovparks.org/permits/tennis-permits) |
| Film & Photo | `PermitApplication:FilmPhoto` | form | [/permits/film-and-photo-guidelines](https://www.nycgovparks.org/permits/film-and-photo-guidelines) |
| Metal Detector | `PermitApplication:MetalDetector` | form | [/permits/metal-detector](https://www.nycgovparks.org/permits/metal-detector) |
| Summer Day Camp | `PermitApplication:SummerDayCamp` | form | [/permits/summer-day-camp](https://www.nycgovparks.org/permits/summer-day-camp) |
| Research | `PermitApplication:Research` | form | [/permits/research/](https://www.nycgovparks.org/permits/research/) |
| Boating & Marinas | `PermitApplication:BoatingMarinas` | form | [/permits/boating-marinas-permits](https://www.nycgovparks.org/permits/boating-marinas-permits) |
| Farmers Market | `PermitApplication:FarmersMarket` | form | [/permits/farmers-market](https://www.nycgovparks.org/permits/farmers-market) |
| Construction | `PermitApplication:Construction` | form | [/permits/construction](https://www.nycgovparks.org/permits/construction) |
| Tree Work | `PermitApplication:TreeWork` | form | [/services/forestry/tree-work-permit](https://www.nycgovparks.org/services/forestry/tree-work-permit) |

### PDF documents/forms (sampled)

- Tennis Purchase Form (2023) — `/pagefiles/174/2023-Tennis-Purchase-Form__...pdf`
- Extended Use Guidelines for Organizations — `/pagefiles/213/Extended-Use-Guidelines...pdf`
- Rockaway Surf Beach Rules — `/sub_things_to_do/facilities/images/pdf/RockawaySurfBeachRules.pdf`

## Entities that fall out of the fruit

The reverse-engineered information architecture — the objects NYC Parks publishes and therefore should model as API resources:

`Park` · `Facility` (≈42 subtypes) · `CapitalProject` · `Event` · `HistoricalSign` / `Monument` · `Tree` · `PermitApplication` (≈10 subtypes) · `Rule` · `Program` · `Concession` · `NewsItem`

## Companion files

- [crosswalk.md](crosswalk.md) — fruit ↔ Open Data mapping with coverage verdicts (the analytical centerpiece).
- [opendata-parks.md](opendata-parks.md) / [opendata-parks.json](opendata-parks.json) — full index of all 237 DPR Open Data assets, with column schemas.
- [tech-stack.md](tech-stack.md) — technology & vendor inventory. [apis-observed.md](apis-observed.md) — backend/service APIs seen while crawling.
- [fruit.json](fruit.json) — machine-readable fruit index, enriched with `confirmed_rows`, `website_columns`, `opendata_match`, and `apis_observed`.

## Next steps

1. **JSON Schema** per entity (start with `Park`, `Facility`, `CapitalProject`, `Event`, `PermitApplication`) — reconcile the **website columns** with the **Open Data column schemas** (both captured) into one canonical schema per entity.
2. ~~Confirmation pass~~ ✅ done — facility directories row-counted, facility column model + permit login-gating captured.
3. ~~Cross-reference NYC Open Data~~ ✅ done — see [crosswalk.md](crosswalk.md); 27 fruit items have a machine-readable twin, 11 are true gaps.
4. **API-first + MCP proposal** — OpenAPI for read (unify existing Open Data behind one resource-oriented Parks API) + write (the missing permit-application API), plus an MCP server exposing the same resources as agent tools. Close the ~12 facility gaps + Rules. (See [crosswalk.md § Implications](crosswalk.md#implications-for-the-api-first--mcp-proposal).)
