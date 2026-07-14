# APIs Observed While Crawling — CUNY

Backend/service APIs the CUNY surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is an **absence**: CUNY has **no public reference API and no open-data presence** — its content sits on WordPress Multisite, and its transactional system of record (CUNYfirst) is an Oracle PeopleSoft ERP with no documented API. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`cssa.cunyfirst.cuny.edu/psc/…GBL`** | Student information system (ERP) | CUNY (on **Oracle PeopleSoft Campus Solutions**) | Guest/login UI; **no API** | The transactional layer — admissions (`CU_E1385_CNSLR_FL`), course catalog browse (`SSS_BROWSE_CATLG`), enrollment, financial aid. Server-rendered PeopleSoft Fluid PIA (`/psc/`, `.GBL`, `PT_LANDINGPAGE`), JavaScript-only, behind an F5 BIG-IP. No JSON/OpenAPI. |
| **`www.cuny.edu` (`wp-json`)** | CMS / content | CUNY (WordPress Multisite, nginx) | Public (HTML) + `wp-json` | Central site + ~25 federated college subsites (WPBakery, Slider Revolution). `wp-json` responds `200` but is content-only — no reference/product API. |
| `www.cuny.edu/academics/programs/` | Program search tool | CUNY | HTML / client-rendered | 'Explore Programs' degree-program finder; no documented backing API exposed to consumers. |
| `academicworks.cuny.edu` | Institutional repository | CUNY (bepress Digital Commons) | HTML + **OAI-PMH** | CUNY Academic Works — faculty/research output; harvestable via OAI-PMH per college, but no unified REST API. |
| `data.cityofnewyork.us` (SODA) | Open Data API | NYC (Socrata / Tyler) | Yes — open | **Effectively zero CUNY presence**: the CUNY agency label returns one external-link (`href`) asset; the one CUNY-subject dataset (`wusu-mzmq`, community-college expenditures) is tagged to **OMB**, not CUNY. |
| `data.ny.gov` | Open Data API | NY State (Socrata) | Yes — open | State-level SUNY/CUNY enrollment tables live on the **state** portal — reflecting CUNY's status as a state public benefit corporation, not a NYC agency. |

## Takeaways

- **The API story is an absence, plus a federation problem.** There is no public reference API for campuses, programs, courses, enrollment, or research; the data is scattered across 25 college sites, a client-rendered finder, and PDF/Excel data books.
- **No API for the core transaction.** Submitting and tracking a **CUNY admissions application** — the single most common prospective-student interaction — has no machine-readable contract; it is reachable only via CUNYfirst PeopleSoft screens.
- **No NYC Open Data twin.** As a state public benefit corporation, CUNY publishes nothing under a CUNY agency label on NYC Open Data; every entity here is reverse-engineered from HTML and PeopleSoft, not Socrata.
- **No individual student data, by design.** Enrollment is published only in aggregate (OIRA data books); per-student records live inside CUNYfirst (FERPA-protected).
- **No agent-native surface.** The [OpenAPI](openapi/cuny.yaml) + [MCP artifact](mcp/cuny-mcp.json) here propose one owned contract that federates the reference data cleanly *and* unlocks the net-new `submit_application` write workflow.
