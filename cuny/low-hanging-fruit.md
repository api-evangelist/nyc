# Low-Hanging Fruit Index — CUNY

**Agency:** City University of New York (CUNY)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `cuny.edu/robots.txt` sets a 30s crawl-delay and disallows `/search/`, `/wp-admin/`, `/wp-content/plugins/`, etc.). Fingerprinted `www.cuny.edu` as **WordPress Multisite** (nginx; `wp-json` → 200; `wp-content/uploads/sites/<n>/`; WPBakery + Slider Revolution generators). Identified **CUNYfirst** as **Oracle PeopleSoft Campus Solutions** from its PIA URLs (`/psc/…GBL`, `PT_LANDINGPAGE`, `NUI_FRAMEWORK`, `SSS_BROWSE_CATLG`, `CU_E1385_CNSLR_FL`; behind an F5 BIG-IP). Verified the NYC Open Data agency label `City University of New York (CUNY)` via the Socrata Discovery API: it returns **exactly one** asset, and that asset is an external link, not a dataset.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-cuny.md](opendata-cuny.md).

## Headline findings

1. **CUNY is a federated system.** ~25 colleges and schools, each with its own website, all on a shared **WordPress Multisite** (`cuny.edu`) and a single shared **Oracle PeopleSoft** SIS branded **CUNYfirst**.
2. **CUNY is a state entity, not a NYC agency.** As a New York **State** public benefit corporation it publishes **nothing** under a CUNY agency label on NYC Open Data — the label returns one external link, not a dataset.
3. **The reference data is scattered.** Campus directories and program search are HTML on `cuny.edu`; enrollment/demographics are PDF/Excel data books (OIRA); state enrollment tables live on `data.ny.gov`. None is a clean API.
4. **Every transaction is locked in CUNYfirst.** Applications, course catalog, enrollment, and financial aid are reachable only through PeopleSoft guest self-service screens. No public API.
5. **Students stay private by design.** Enrollment is published only in aggregate; no individual `StudentRecord` is ever exposed (FERPA).

> **Reframe (fifth distinct pattern):** Parks = *replatform*; DOE = *reclaim*; Council = *consolidate + own*; NYCHA = *unlock*; **CUNY = federate.** Here the reference data exists but is spread across 25 campuses with no open-data twin, and the transactions are hidden in a shared ERP — so the work is to give the whole system **one owned, agent-native contract** that federates the reference data and unlocks the application.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Colleges & Schools (~25) | `Campus` | cuny.edu + CUNYfirst | ❌ none |
| 2 | Degree & Certificate Programs | `DegreeProgram` | Explore Programs (client-rendered) | ❌ none |
| 3 | Course Catalog | `Course` | CUNYfirst catalog browse | ❌ none |
| 4 | Enrollment & Demographics | `EnrollmentStatistics` | OIRA data books (PDF/Excel) | 🟡 data.ny.gov, aggregate |
| 5 | Faculty & Research | `FacultyResearch` | directories + Academic Works (OAI-PMH) | 🟡 OAI-PMH |
| 6 | Community-college budget | `EnrollmentStatistics` | NYC Open Data | 🟡 `wusu-mzmq` (tagged OMB) |
| 7 | **Apply to CUNY** | `AdmissionsApplication` | CUNYfirst | ❌ **net-new** |
| 8 | Check application status | `AdmissionsApplication` | CUNYfirst | ❌ gap |
| 9 | Register for classes | `Course` | CUNYfirst | ❌ gap |
| 10 | Financial aid application | `AdmissionsApplication` | CUNYfirst | ❌ gap |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Oracle PeopleSoft Campus Solutions (CUNYfirst)** — the SIS/ERP; guest/login PeopleSoft screens, no API.
- **WordPress Multisite** — `cuny.edu` + ~25 college subsites (nginx; WPBakery + Slider Revolution); `wp-json` is content-only.
- **CUNY Academic Works** — bepress Digital Commons repository; OAI-PMH, no unified REST.
- **NYC Open Data** — effectively empty for CUNY (one external-link asset); the fifth distinct platform pattern after Parks' Smarty/PHP, DOE's Sitefinity/.NET, Council's WordPress, and NYCHA's Livesite + Siebel.

## Reverse-engineered entities

`Campus` (~25 colleges/schools) · `DegreeProgram` · `Course` (catalog) · `EnrollmentStatistics` (aggregate; never individual student) · `FacultyResearch` · `AdmissionsApplication` (net-new write; also stands in for the CUNYfirst-locked enrollment / financial-aid transactions) — federation keys: **institution code**, **program code / CIP / HEGIS**, **term**.

## Next

1. **JSON Schema** per entity, reconciling cuny.edu HTML, the OIRA data-book fields, and CUNYfirst codes — done ([schemas/](schemas/)).
2. **OpenAPI** federating the reference data as clean resources + the net-new `POST /applications` (submit a CUNY application) — done ([openapi/cuny.yaml](openapi/cuny.yaml)).
3. **MCP** artifact: `find_campuses`, `get_campus`, `find_programs`, `get_program`, `find_courses`, `find_enrollment_statistics`, `find_faculty_research`, `list_my_applications`, `submit_application` — done ([mcp/cuny-mcp.json](mcp/cuny-mcp.json)).
