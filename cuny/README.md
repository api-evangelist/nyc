# cuny — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **City University of New York (CUNY)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (campuses, programs, courses, enrollment, faculty/research, and the CUNYfirst-locked transactions).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (**WordPress Multisite** on nginx; the **Oracle PeopleSoft** CUNYfirst SIS).
- [apis-observed.md](apis-observed.md) — the **absence** of any public reference API vs. the **PeopleSoft ERP with no API** and an empty NYC Open Data corpus.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (essentially empty for CUNY) with coverage verdicts.
- [opendata-cuny.md](opendata-cuny.md) / [opendata-cuny.json](opendata-cuny.json) — the one CUNY-labeled asset (an external link) + the one CUNY-subject dataset (tagged to OMB), and why the corpus is empty.
- [schemas/](schemas/) — individual JSON Schema per object: `campus` · `degree-program` · `course` · `enrollment-statistics` · `faculty-research` · `admissions-application` (+ shared `_common`).
- [openapi/cuny.yaml](openapi/cuny.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/cuny-mcp.json](mcp/cuny-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

CUNY is a **federated system**, and that federation is the finding:

1. **~25 campuses, one WordPress, one ERP.** The colleges each have their own website on a shared **WordPress Multisite** (`cuny.edu`, nginx), and all share a single **Oracle PeopleSoft Campus Solutions** SIS branded **CUNYfirst**.
2. **A state entity, not a city publisher.** As a New York **State** public benefit corporation, CUNY publishes **nothing** under a CUNY agency label on NYC Open Data — the label returns one external link, not a dataset.
3. **Reference data scattered; transactions locked.** Campuses and programs are HTML; enrollment is PDF/Excel data books; the catalog, applications, enrollment, and aid live only inside CUNYfirst PeopleSoft screens.

**The gap here is federation *and* transactions.** A student or agent asking "which CUNY colleges offer a BS in Nursing, and how do I apply?" has nothing to call.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **CUNY** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | Livesite + Oracle Siebel | **WordPress Multisite + Oracle PeopleSoft (CUNYfirst)** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **~25 campuses, no open data, transactions locked in an ERP** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **federate** |

## Reverse-engineered entities

`Campus` (~25 colleges/schools) · `DegreeProgram` · `Course` · `EnrollmentStatistics` (aggregate only) · `FacultyResearch` · `AdmissionsApplication` (net-new write) — federation keys **institution code**, **program code / CIP / HEGIS**, **term**.

## Method & caveats

Outside-in crawl (browser UA; `cuny.edu/robots.txt` sets a 30s crawl-delay). The informational site was fingerprinted from headers and markup (nginx, `wp-json`, `wp-content/uploads/sites/`, WPBakery, Slider Revolution); CUNYfirst was identified as Oracle PeopleSoft Campus Solutions from its PIA URLs (`/psc/…GBL`, `PT_LANDINGPAGE`, `SSS_BROWSE_CATLG`, `CU_E1385_CNSLR_FL`) without authenticating. The NYC Open Data agency label was verified via the Socrata Discovery API; it returns one non-dataset asset. A sample, not a full spider; CUNYfirst's internal workflows are inferred from CUNY's documented admissions/enrollment services, not scraped behind login.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (empty corpus documented) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (10 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** an example implementation fronting CUNYfirst for `submit_application`; then the next domain from [../domains.md](../domains.md).
