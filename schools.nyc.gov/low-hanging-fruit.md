# Low-Hanging Fruit Index — schools.nyc.gov

**Agency:** New York City Public Schools (NYCPS / DOE)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `/CustomApi`, `/Sitefinity`, `/System` disallowed and avoided). The sitemap (gzip) decompressed to **4,617 URLs**; section, school, calendar, and search pages sampled. Page data is largely **JS-rendered from an internal `/CustomApi` backend**, so raw HTML table/row counts understate the underlying records — the counts here come from the sitemap and the Open Data twins.

Companion artifacts: [tech-stack.md](tech-stack.md) (vendors), [apis-observed.md](apis-observed.md) (backend APIs), [crosswalk.md](crosswalk.md) (fruit ↔ Open Data), [opendata-doe.md](opendata-doe.md) (638 DOE assets).

## Headline findings

1. **The school directory is 3,343 pages.** Each `/schools/<LocationCode>` is a structured `School` profile (DBN, name, address, phone, principal, grades, district, enrollment) — rendered client-side, not machine-readable on the domain.
2. **Off-domain it's extremely machine-readable.** NYC Open Data has **638 DOE assets** — including **462-column** High School Directories, School Locations, and Demographic Snapshots — plus InfoHub's Excel reports. The site doesn't consume them.
3. **Discovery is rented.** "Find a School" runs on **HawkSearch** (a vendor search API), so DOE owns neither a public school-search API nor the index behind it.
4. **A backend API already exists but is hidden** — `/CustomApi/*` drives the pages; it's robots-disallowed, undocumented, and not public.
5. **Enrollment is the net-new gap.** The MySchools application workflow (3K–12 admissions) is transactional with **no Open Data twin** — the flagship API opportunity, analogous to Parks permits.

> **Reframe (same as Parks):** integration + productization, not data liberation — but here with an extra twist: **capabilities (search, backend) are outsourced or hidden**, so part of modernization is *reclaiming* them into an owned, public, agent-native API.

## The fruit

| # | Name | Type | Entity | Scale | MR? | Open Data twin |
|---|---|---|---|---|---|---|
| 1 | School Directory | record-listing (JS) | `School` | 3,343 pages | ❌ | ✅ School Locations, HS/MS Directory, Demographics |
| 2 | Find a School (search) | search-form (vendor) | `School` | — | ❌ | ❌ (HawkSearch, not open) |
| 3 | School Year Calendar | faceted event listing | `CalendarEvent` | full year | ❌ | ❌ gap |
| 4 | Enrollment / MySchools | transactional workflow | `EnrollmentApplication` | 3K–12 | ❌ | ❌ **net-new** |
| 5 | School Quality Reports | per-school reports | `SchoolQualityReport` | per school | 🟡 InfoHub Excel | 🟡 Quality datasets |
| 6 | Demographics | reports | `SchoolDemographics` | per school/year | 🟡 | ✅ Demographic Snapshot (44c) |
| 7 | Test results (SAT/AP/Regents) | reports | `TestResult` | school-level | ✅ | ✅ SAT/AP/Specialized datasets |

## Backend APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **HawkSearch** — vendor search API behind Find-a-School.
- **`/CustomApi/*`** — internal Sitefinity REST driving school/page data (robots-blocked).
- **Azure Blob** (`pwsblobprd.schools.nyc`), **Esri ArcGIS** (maps), **Socrata SODA** (the only public API), **NYC Schools Account** (`nycenet.edu`) auth.
- Platform: **Progress Sitefinity** (.NET) CMS.

## Reverse-engineered entities

`School` · `SchoolDemographics` · `CalendarEvent` · `EnrollmentApplication` · `SchoolQualityReport` · `TestResult` (join key: **DBN** — District-Borough-Number, the school equivalent of Parks' gisPropNum)

## Next

1. **JSON Schema** per entity (School, SchoolDemographics, CalendarEvent, EnrollmentApplication, TestResult) reconciling school-page fields with Open Data columns.
2. **OpenAPI** unifying the read resources + the net-new **enrollment-application** write API.
3. **MCP** artifact exposing `find_schools`, `get_school`, `find_calendar_events`, `submit_enrollment_application`, `check_application_status`.
