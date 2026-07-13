# Crosswalk — Website Fruit ↔ NYC Open Data (DOE)

Maps the low-hanging fruit on **schools.nyc.gov** to the **638 DOE assets** on **NYC Open Data** (`data.cityofnewyork.us`, agency *Department of Education (DOE)*). Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-doe.json](opendata-doe.json).

## The reframe (Parks pattern + an extra twist)

Like Parks, most website data has a machine-readable twin already published — and DOE's is *bigger* (638 assets vs. 237; directories with **462 columns**). The disconnect is the same: the website renders its own JS pages and never consumes the open data.

**The extra twist for DOE:** two core capabilities are **outsourced or hidden**, not just disconnected —

- **Search is rented** from HawkSearch (a vendor), so there's no DOE-owned school-search API.
- **The backend is hidden** behind an internal `/CustomApi/*` (robots-blocked, undocumented).

So modernization here also means **reclaiming** discovery and the backend into an owned, public, agent-native API — not only wiring open data to the front end.

Coverage: ✅ strong twin · 🟡 partial/Excel-only · ❌ true gap.

## Core entities

| Website fruit | Entity | Open Data twin(s) | Cov. |
|---|---|---|---|
| School Directory (`/schools/*`, 3,343 pages) | `School` | School Locations (e.g. `9ck8-h43e`-class, 41–48c); **DOE High School Directory (462c)**; **Middle School Directory (251c)**; Universal Pre-K Locations (`kiyv-ks3f`, 26c) | ✅ |
| Demographics (per school) | `SchoolDemographics` | 2017-18–2021-22 Demographic Snapshot (`c7ru-d68s`, 44c); 2013-2018 Demographic Snapshot School (39c) | ✅ |
| Test results | `TestResult` | 2012 SAT Results; SAT (College Board) School Level; AP School Level; Specialized HS Admissions Test Results | ✅ |
| School Quality Reports | `SchoolQualityReport` | Quality/Framework datasets (Open Data + InfoHub Excel) | 🟡 |
| School Year Calendar | `CalendarEvent` | — | ❌ gap |
| Find a School (search) | `School` | — (HawkSearch vendor) | ❌ not open |
| Enrollment / MySchools | `EnrollmentApplication` | — (directories exist; applications don't) | ❌ **net-new** |

## Bonus: operational DOE datasets with little/no public web face

Rich operational data on Open Data that the public site doesn't surface as such: **Bus Breakdown and Delays** (`21c`, 50k views), Bus Routes & Transportation Sites, Daily/Annual Attendance, School Safety Report, Bilingual Program List, Energy Usage from DOE Buildings, Graduation Outcomes, Regents. Same argument as Parks — one API should serve public + operational consumers.

## Coverage tally

- **✅ Strong twin:** School directory, demographics, test results (the reporting core).
- **🟡 Excel-only / partial:** school quality reports (InfoHub spreadsheets).
- **❌ True gaps:** the **school-year calendar**, an **owned search API** (rented to HawkSearch), and the **enrollment application** workflow (net-new, transactional).

## Implications for the API-first + MCP proposal

1. **Unify + reclaim.** Wrap the DOE Open Data (directories, locations, demographics, results) in one resource-oriented **School API** keyed on **DBN**, and bring **search in-house** (replace the HawkSearch dependency with an owned, documented, agent-callable endpoint).
2. **Publish the calendar** as a simple dataset/endpoint (trivial; closes an everyday gap).
3. **Build the enrollment-application API** (read: status/offers; write: submit/rank choices) — the MySchools workflow has no machine-readable surface today and the highest family value.
4. **MCP server** exposing `find_schools`, `get_school`, `find_calendar_events`, `submit_enrollment_application`, `check_application_status` — turning a vendor-searched CMS into an agent-native civic service.
