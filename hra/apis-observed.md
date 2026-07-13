# APIs Observed While Crawling — HRA / DSS

Backend/service APIs the HRA surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is asymmetric in a new way: **HRA's caseload data has a real, open API (Socrata SODA over 49 datasets) AND its eligibility logic is open source (a Drools rules engine) — yet neither the eligibility screener nor the application portal exposes a callable API.** Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 49 HRA datasets: SNAP/Cash Assistance/Medicaid caseloads, application-center directories, wait times, and 75-column case-action reports. Each has a SODA `/resource/<id>.json` endpoint. This is the one real, machine-readable HRA API — reference/caseload data only. |
| **`github.com/NYCOpportunity/ACCESS-NYC-Rules`** | Open-source rules engine | NYC Opportunity (Mayor's Office for Economic Opportunity) | **Open source (Drools)** | The Drools business rules governing the ACCESS NYC eligibility screener. The eligibility *logic* is public and city-owned — but there is no **hosted** API that returns a determination to a caller. A companion `benefits-screening-api` repo (2025 replatform) exists. |
| **`access.nyc.gov`** | Benefits screener + catalog | NYC Opportunity (WordPress / WP Engine) | HTML; **no result API** | The screener at `/eligibility` collects a household profile and renders eligible programs as HTML. Program metadata is published separately as Open Data (`kvhd-5fmu`). No JSON determination endpoint. |
| **`a069-access.nyc.gov/accesshra`** | Benefits application portal | HRA (React SPA behind Akamai) | Login-walled UI; **no API** | ACCESS HRA — apply for SNAP/Cash Assistance/Medicaid, upload documents, view case status. React client, Akamai Bot Manager (`_abck`/`bm_sz`), no JSON/OpenAPI surface. |
| `www.nyc.gov/site/hra/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | Content only — help pages, program info, locations. No content API exposed. |
| Akamai edge | CDN / bot-manager API | Akamai | Vendor | `x-akamai-transformed` on the informational site; `_abck`/`bm_sz` on ACCESS HRA. |
| Cloudflare edge | CDN API | Cloudflare | Vendor | `server: cloudflare`, `__cf_bm` on access.nyc.gov. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring on the informational site. |

## Takeaways

- **The API story is disconnection, not absence.** Caseload/reference data is generously open through Socrata SODA; the eligibility *logic* is even open-sourced. What is missing is any API that binds the journey — screen → determine → apply → track — together.
- **The open rules are unexploited low-hanging fruit.** ACCESS NYC's Drools rules already encode who qualifies for what; wrapping them as a hosted `POST /eligibility` returns a machine-readable determination the screener today only renders as HTML.
- **No API for the core transaction.** Applying for and tracking a benefits case — the single most important HRA resident interaction — has no machine-readable contract at all; it is reachable only via the ACCESS HRA React portal or an in-person visit.
- **No individual case data, by design.** Caseloads and case actions are published only in aggregate; per-resident applications live inside HRA's systems and the ACCESS HRA portal.
- **No agent-native surface.** The [OpenAPI](openapi/hra.yaml) + [MCP artifact](mcp/hra-mcp.json) here propose one owned contract that publishes the open reference data cleanly, exposes the open eligibility rules, *and* unlocks the net-new `apply_for_benefits` write workflow.
