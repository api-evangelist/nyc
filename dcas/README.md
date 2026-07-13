# dcas — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Department of Citywide Administrative Services (DCAS)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (job postings, civil-service titles, eligible lists, exam schedule, buildings, fleet, and the locked transaction workflows).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace; the **aNNN app layer**: City Jobs on **ASP.NET Core/Azure**, Employee Self-Service on **PeopleSoft/NYCAPS**, the CityStore on **Shopify**).
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA over 32 datasets) vs. the **three vendor apps with no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (32 DCAS datasets) with coverage verdicts.
- [opendata-dcas.md](opendata-dcas.md) / [opendata-dcas.json](opendata-dcas.json) — all 32 DCAS Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `job-posting` · `civil-service-title` · `eligible-list` · `exam-schedule` · `city-building` · `fleet-vehicle` · `exam-registration` (+ shared `_common`).
- [openapi/dcas.yaml](openapi/dcas.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/dcas-mcp.json](mcp/dcas-mcp.json) — design-first MCP server definition (11 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

DCAS is a **fragmented domain**, and that fragmentation is the finding:

1. **Reference data is broadly open.** 32 NYC Open Data datasets publish the civil-service machine generously — the **Civil Service List (Active)** (`vx8i-nprf`, 3.5M lifetime views), **Certification** (`a9md-ynri`, 1.1M), **Civil Service Titles** (`nzjr-3966`), **Jobs NYC Postings** (`kpav-sd4t`, 30 columns), the **Annual Exam Schedule** (`4ptz-hmtc`), DCAS-managed buildings and energy, and the municipal fleet.
2. **The transaction layer is scattered and locked.** The careers front door has been replatformed onto modern **ASP.NET Core / Azure** (`cityjobs.nyc.gov`, where `a127-jobs` now redirects), but exam registration still runs through **OASys**, HR self-service is still on **PeopleSoft/NYCAPS** (`a127-ess`), and the CityStore is a **Shopify** tenant — three vendors, no shared API.

**The gap here is transactions, not data.** A citizen or agent asking "register me for the next open exam" or "apply me to this posting" has nothing to call.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **DCAS** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | NYC.gov + Oracle Siebel | **NYC.gov + aNNN apps: Azure/.NET, PeopleSoft, Shopify** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **data open, transactions scattered across rented apps** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **transact** |

## Reverse-engineered entities

`JobPosting` · `CivilServiceTitle` · `EligibleListEntry` · `ExamSchedule` · `CityBuilding` · `FleetVehicle` · `ExamRegistration` (net-new write) — join keys **Title Code**, **Exam Number**, **List No**, **Agency Code**, **BIN/BBL**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite, Dynatrace); the aNNN apps were identified from response headers and landing markup — City Jobs as ASP.NET Core/Azure (`Kestrel`, `AspNetCore.Antiforgery`, `x-ms-routing-name`), Employee Self-Service as PeopleSoft/NYCAPS (`psp/`, page title), the CityStore as Shopify (`_shopify_*` cookies) — without authenticating. Open Data agency label verified via the Socrata Discovery API; all 32 assets pulled with columns. A sample, not a full spider; the OASys/PeopleSoft internal workflows are inferred from DCAS's documented services, not scraped behind login.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (32 datasets) ✅ · JSON Schemas (7 + common) ✅ · OpenAPI 3.1 (13 paths/13 ops) ✅ · MCP artifact (11 tools) ✅.
- **Next:** an example implementation fronting OASys for `register_for_exam`; then the next domain from [../domains.md](../domains.md).
