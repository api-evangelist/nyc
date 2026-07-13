# Low-Hanging Fruit Index — DCAS

**Agency:** NYC Department of Citywide Administrative Services (DCAS)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/dcas` (Akamai + nginx + NYC.gov "Livesite" platform + Dynatrace) and the **aNNN application layer**: the **City Jobs portal** (`cityjobs.nyc.gov`, where `a127-jobs.nyc.gov` now 301-redirects; **ASP.NET Core / Kestrel on Azure**), **Employee Self-Service** (`a127-ess.nyc.gov`, identified as **PeopleSoft/NYCAPS**), and the **CityStore** (`a856-citystore.nyc.gov`, identified as **Shopify**). Verified the NYC Open Data agency label `Department of Citywide Administrative Services (DCAS)` via the Socrata Discovery API and pulled all **32** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-dcas.md](opendata-dcas.md).

## Headline findings

1. **DCAS is a fragmented domain.** An informational site on the shared NYC.gov chassis, plus a sprawl of **separate aNNN vendor apps** — City Jobs (Azure/.NET), Employee Self-Service (PeopleSoft/NYCAPS), the exam **OASys**, and the CityStore (Shopify) — none sharing an API.
2. **The reference data is broadly open.** **32 NYC Open Data datasets** cover job postings (Jobs NYC Postings, 30 columns), civil-service titles, active/terminated/certified **eligible lists** (the top two datasets, 3.5M and 1.1M views), the annual **exam schedule**, DCAS-managed buildings and their energy, and the municipal fleet.
3. **But the transaction layer is locked.** Registering for an exam, applying to a posting, and even buying from the CityStore — the things people actually *do* — live only inside login-walled or vendor-tenant apps. None has a machine-readable contract.
4. **The read/write split is stark.** You can read the exam schedule as open data; you cannot *register* through any API. The write half of every workflow is missing.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* the service layer; **DCAS = transact.** Here the data is already open and the careers front door is even replatformed onto .NET/Azure — the work is least about liberating datasets and most about giving the **citizen transaction layer** (above all, registering for a civil-service exam) an owned, agent-native API instead of three separate vendor screens.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Citywide Job Postings | `JobPosting` | SODA + City Jobs portal | ✅ Jobs NYC Postings (`kpav-sd4t`, 30c) |
| 2 | Civil Service Titles | `CivilServiceTitle` | SODA | ✅ NYC Civil Service Titles (`nzjr-3966`, 11c) |
| 3 | Civil Service Eligible Lists | `EligibleListEntry` | SODA | ✅ Active (`vx8i-nprf`) + Certification/Terminated/Civil List |
| 4 | Annual Examination Schedule | `ExamSchedule` | SODA | ✅ Annual Exam Schedule (`4ptz-hmtc`, 7c) |
| 5 | DCAS-Managed Buildings & Energy | `CityBuilding` | SODA + map | ✅ Managed Public Buildings (`xx2p-4jnq`) + energy |
| 6 | Municipal Fleet | `FleetVehicle` | SODA + map | ✅ Daily Service (`5rzx-3686`) + auction/fuel/EV |
| 7 | CityStore purchase | — (Shopify) | Shopify store | 🟡 catalog only (`mqdy-gu73`) |
| 8 | Employee self-service | — (portal) | PeopleSoft/NYCAPS | ❌ gap (no API) |
| 9 | Apply to a job posting | `JobApplication` | City Jobs portal | ❌ gap (no API) |
| 10 | **Register for a civil-service exam** | `ExamRegistration` | OASys / City Jobs portal | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 32 DCAS datasets (the one real, open API; reference data only).
- **City Jobs / OASys** — `cityjobs.nyc.gov` (ASP.NET Core on Azure); careers + exam application; login-walled, no API.
- **PeopleSoft / NYCAPS** — `a127-ess.nyc.gov` employee self-service; legacy vendor HR, no API.
- **Shopify** — `a856-citystore.nyc.gov`; the CityStore; vendor tenant, no DCAS API.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, Dynatrace RUM).

## Reverse-engineered entities

`JobPosting` · `CivilServiceTitle` · `EligibleListEntry` · `ExamSchedule` · `CityBuilding` · `FleetVehicle` · `ExamRegistration` (net-new write; also stands in for the OASys-locked JobApplication) — join keys: **Title Code**, **Exam Number**, **List Number**, **Agency Code**, **BIN/BBL**.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (Title Code, Exam Number, List No, BBL/BIN, the geography spine) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open reference data as clean resources + the net-new `POST /exam-registrations` (register for an exam) — done ([openapi/dcas.yaml](openapi/dcas.yaml)).
3. **MCP** artifact: `find_job_postings`, `find_civil_service_titles`, `find_eligible_list_entries`, `find_exam_schedule`, `find_buildings`, `find_fleet`, `list_my_exam_registrations`, `register_for_exam` — done ([mcp/dcas-mcp.json](mcp/dcas-mcp.json)).
