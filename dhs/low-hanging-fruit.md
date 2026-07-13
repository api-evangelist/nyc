# Low-Hanging Fruit Index — DHS

**Agency:** NYC Department of Homeless Services (DHS)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/dhs` (Akamai + nginx + NYC.gov "Livesite" platform + Dynatrace) and confirmed DHS has **no self-service portal** — its transactions route through **NYC311** ("Homeless Person Assistance") and in-person intake centers. Verified the NYC Open Data agency label `Department of Homeless Services (DHS)` via the Socrata Discovery API and pulled all **23** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-dhs.md](opendata-dhs.md).

## Headline findings

1. **DHS is an observational-data agency.** Its informational site is the shared NYC.gov chassis; it ships no application of its own. Every transaction happens on NYC311, 911, or at a front desk.
2. **The reference data is unusually open.** **23 NYC Open Data datasets** are led by the flagship **DHS Daily Report** — the daily shelter census, DHS's single most-viewed asset — plus drop-in centers, DHS contacts/intake centers, buildings and individual census, the Shelter Repair Scorecard, and years of unsheltered street-count history.
3. **But there is no service layer to expose.** Applying for shelter is in-person; **reporting a person on the street for outreach** is a NYC311 call. Neither has a machine-readable contract, and DHS does not even own the 311 channel that stands in for one.
4. **People stay private by design.** Shelter and street figures are published only in aggregate; no individual person is ever exposed.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search; Council = *consolidate + own* fragmented APIs; NYCHA = *unlock* a service layer locked in a vendor CRM; **DHS = connect the action.** Here the data is already open and there is no transaction system at all — the work is to give the **human-services action** (above all, requesting street outreach) an owned, agent-native API instead of a 311 phone menu.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Daily Shelter Census | `ShelterCensus` | SODA | ✅ DHS Daily Report (`k46n-sa2m`, 13c) |
| 2 | Homeless Drop-In Centers | `DropInCenter` | SODA | ✅ Drop-In Centers (`bmxf-3rd4`, 13c) |
| 3 | Shelter Facilities & Repair Scorecard | `ShelterFacility` | SODA | ✅ Shelter Repair Scorecard (`dvaj-b7yx`, 55c) |
| 4 | DHS Contacts & Intake Centers | `DHSContact` | SODA | ✅ Directory Of DHS Contacts (`cete-9g3v`, 14c) |
| 5 | Unsheltered Street Counts | `StreetHomelessCount` | SODA | 🟡 Unsheltered ratio 2009–2012 (`483x-fy9e`…) — aggregate only |
| 6 | Apply for shelter | — (intake) | Intake center (PATH / adult) | ❌ gap (no API) |
| 7 | **Report a person for outreach** | `OutreachRequest` | NYC311 + phone | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 23 DHS datasets (the one real, open API; observational data only).
- **NYC311** — the "Homeless Person Assistance" outreach channel; a phone/webform DHS does not own, with no API.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, Dynatrace RUM) — the same chassis seen on NYCHA's informational site.

## Reverse-engineered entities

`ShelterCensus` (DailyReport) · `DropInCenter` · `ShelterFacility` (buildings + repair scorecard) · `DHSContact` (offices/intake centers) · `StreetHomelessCount` (aggregate; never individual) · `OutreachRequest` (net-new write; also stands in for the 311-locked shelter-application transaction) — join keys: **date of census**, **DHS Building ID**, **BIN/BBL**, the geography spine.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (Date of Census, DHS_Bld_ID, BBL/BIN, the geography spine) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open reference data as clean resources + the net-new `POST /outreach-requests` (request outreach) — done ([openapi/dhs.yaml](openapi/dhs.yaml)).
3. **MCP** artifact: `find_shelter_census`, `get_shelter_census`, `find_drop_in_centers`, `find_facilities`, `get_facility`, `find_contacts`, `find_street_homeless_counts`, `list_my_outreach_requests`, `request_outreach` — done ([mcp/dhs-mcp.json](mcp/dhs-mcp.json)).
