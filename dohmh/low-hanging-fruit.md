# Low-Hanging Fruit Index — nyc.gov/site/doh (DOHMH)

**Agency:** NYC Department of Health and Mental Hygiene (DOHMH)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `www.nyc.gov` only disallows `/html/misc/`). Crawled the DOH section of the shared NYC.gov "LiveSite" WCM (`/site/doh/*.page`): homepage, `services/birth-death-records`, `services/restaurant-grades`, `services/allclinics`, `services/sexual-health-clinics`, `business/permits-licenses`. Fingerprinted the transactional back-office apps on `a816-*.nyc.gov` (ABC Eats, eVital VRRTS, Accela Citizen Access, NYC Health Map). Open Data enumerated via the Socrata Discovery API filtered on `Dataset-Information_Agency = "Department of Health and Mental Hygiene (DOHMH)"` (**81 assets**, verified).

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-dohmh.md](opendata-dohmh.md).

## Headline findings

1. **DOHMH is the most data-rich domain in the project.** 81 datasets on NYC Open Data, led by **"DOHMH New York City Restaurant Inspection Results"** (`43nn-pn8j`, ~406k views) — among the single most-viewed datasets in all of NYC Open Data.
2. **But its transactional services are siloed** in a fleet of separate legacy apps with no open, agent-native API: **ABC Eats** (restaurant grade lookup; AngularJS + ASP.NET MVC), **eVital VRRTS** + **VitalChek** (birth/death certificate orders), and **Accela Citizen Access** (health permits & licenses).
3. **The famous data is served twice, the transaction zero times.** Restaurant grades are both an ABC Eats SPA *and* an open Socrata dataset — yet ordering a birth certificate has no API at all.
4. **The one true net-new write surface is ordering a vital record** (birth/death certificate) — a paid transaction locked inside eVital/VitalChek.

> **Reframe (fourth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search; Council = *consolidate + own* three APIs; **DOHMH = transact.** The open data is solved; the work here is least about liberating data and most about **agent-native, transactional services**.

## The fruit

| # | Name | Entity | Scale | Where the data lives | Open Data twin |
|---|---|---|---|---|---|
| 1 | Restaurant / food-establishment grades | `FoodEstablishment` | ~27k | ABC Eats SPA + Open Data | ✅ Restaurant Inspections (`43nn-pn8j`) |
| 2 | Restaurant inspections & violations | `Inspection` | millions of rows | Open Data | ✅ `43nn-pn8j` (31c) |
| 3 | Rodent (rat) inspections | `RodentInspection` | millions of rows | Open Data | ✅ Rodent Inspection (`p937-wjvj`) |
| 4 | Childcare center inspections | `ChildcareCenter` | — | Open Data | ✅ Childcare Inspections (`dsg6-ifza`) |
| 5 | Health clinics & service sites | `HealthFacility` | — | NYC Health Map | ❌ gap (finder only) |
| 6 | Indoor environmental / health complaints | `EnvironmentalComplaint` | — | 311 → Open Data | ✅ Indoor Env. Complaints (`9jgj-bmct`) |
| 7 | Health permits & licenses | `FoodEstablishment` | — | Accela Citizen Access | ❌ gap (COTS-only) |
| 8 | Order a birth / death certificate | `VitalRecordRequest` | — | eVital / VitalChek | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **NYC Open Data SODA** — 81 DOHMH datasets (open, machine-readable); **ABC Eats** private Web API (restaurant grades, undocumented); **eVital VRRTS** + **VitalChek** (vital records, no API); **Accela Citizen Access** (permits, COTS); **311** (complaint intake).
- Public platform: **NYC.gov "LiveSite" WCM** behind **Akamai** + **nginx**, monitored by **Dynatrace** (fourth distinct platform after Parks' Smarty/PHP, DOE's Sitefinity, and Council's WordPress).
- Back-office estate: a fleet of **ASP.NET/IIS** apps + **Accela** COTS on `a816-*.nyc.gov`.

## Reverse-engineered entities

`FoodEstablishment` · `Inspection` (with `Violation[]`) · `RodentInspection` · `ChildcareCenter` · `HealthFacility` · `EnvironmentalComplaint` · `VitalRecordRequest` (net-new) — join keys: **camis** (establishment), **bbl/bin** (tax lot/building), **dc_id** (childcare), plus the shared NYC geography spine (**communityBoard, councilDistrict, censusTract, nta**).

## Next

1. **JSON Schema** per entity, reconciled to real Socrata column names (done — see [schemas/](schemas/)).
2. **OpenAPI** fronting the open data for reads + the net-new vital-record ordering write (done — [openapi/dohmh.yaml](openapi/dohmh.yaml)).
3. **MCP** artifact: `find_food_establishments`, `get_food_establishment_inspections`, `find_rodent_inspections`, `find_childcare_centers`, `find_health_facilities`, `find_complaints`, `order_vital_record`, `track_vital_record_request` (done — [mcp/dohmh-mcp.json](mcp/dohmh-mcp.json)).
