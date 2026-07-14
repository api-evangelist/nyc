# APIs Observed While Crawling — CFB

Backend/service APIs the CFB surfaces call or expose, surfaced during the crawl (2026-07-13). The finding here is the opposite of most domains: **CFB already has a real, working campaign-finance JSON API** (`nyccfb.info/FTMSearchWebAPI`) plus 16 open datasets and a bulk CSV library — it just never documented or owned the API as a product, and the one **write** it owns (filing a disclosure) has no API at all. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`www.nyccfb.info/FTMSearchWebAPI`** | Backend JSON Web API (ASP.NET Web API) | CFB | **Reachable, undocumented** | The API behind the Follow the Money AngularJS search. Confirmed live JSON from `/api/Common/GetElectionCycle`. Reference lists (`GetOfficeList`, `GetStatementList`, `GetTransactionTypeList`, `GetExpenditurePurposeList`, …) and autocomplete (`GetCandidates`, `GetContributors`, `GetPayees`, `GetIntermediaries`, `GetIndependentSpenders`). Real API, no OpenAPI/docs. **The core finding.** |
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 16 CFB datasets: contributions, expenditures, intermediaries, public funds, financial analysis, enforcement, late/missing filings, voter analysis. Each has a SODA `/resource/<id>.json` endpoint. |
| **`www.nyccfb.info/DataLibrary/*.csv`** | Bulk file downloads | CFB | **Yes — open** | 56 flat CSVs (contribution / expenditure / payment / intermediary / analysis) per election cycle, 2001–2025. The bulk twin of the Open Data + FTM data. |
| **C-SMART** (`/candidate-services/c-smart-help`) | Disclosure filing application | CFB | **Login-walled; no API** | The web application campaigns use to **submit** (file) disclosure statements. Server-rendered, login-gated; no JSON/OpenAPI. The net-new write surface. |
| **IEDS** (`ieds.nyccfb.info/Public/Login.aspx`) | Independent-expenditure filing | CFB | Login (ASP.NET WebForms) | Independent Expenditure Disclosure System — a separate filing app for outside spenders. No API. |
| `caccess.nyccfb.info` (C-Access) | Access portal | CFB | Login | Candidate/public access portal referenced from the FTM header. |
| `www.nycvotes.org` | Voter-engagement site | CFB / NYC Votes (Umbraco on Azure) | Public (HTML) | Umbraco CMS / ASP.NET on Azure App Service. `contribute.nycvotes.org`, `nycvotes.turbovote.org` are separate services. No public content API observed. |
| Azure Application Insights | Monitoring beacon | Microsoft Azure | Vendor | `appInsights` telemetry on the FTM search page. |

## Takeaways

- **The API already exists — it's just undocumented.** Unlike DOE (search *rented* to a vendor) or NYCHA (no service API at all), CFB built its own JSON Web API for Follow the Money. The work is to **document and own** it (OpenAPI, docs, stable contract), not to build it.
- **Data is published every way but the owned one.** Same campaign-finance facts appear as Socrata datasets, bulk CSVs, and live API responses — three uncoordinated copies, none presented as one clean, versioned product.
- **No API for the core write.** Submitting a **disclosure statement** — the transaction the CFB uniquely owns — has no machine-readable contract; it happens only inside C-SMART (or IEDS). Only *filing status* leaks out, via the Late/Missing Disclosure Statements dataset.
- **No agent-native surface.** The [OpenAPI](openapi/cfb.yaml) + [MCP artifact](mcp/cfb-mcp.json) here propose one owned contract that documents the open data + FTM search cleanly *and* adds the net-new `file_disclosure` write workflow.
