# APIs Observed While Crawling — SCA

Backend/service APIs the SCA surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is asymmetric: **SCA's capital-plan and procurement reference data has a real, open API (Socrata SODA over 43 datasets), but its vendor *transaction* layer has none** — bid documents and prequalification run through a SharePoint portal and PDF forms with no documented API. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 43 SCA datasets: active projects, schedules and budgets, capacity by school, upcoming CIP/CAP contracts, current/anticipated RFPs, change orders, prequalified & disqualified firms, enrollment/capacity, demographic projections, inspections. Each has a SODA `/resource/<id>.json` endpoint. This is the one real, machine-readable SCA API. |
| **`bidset.nycsca.org`** | Vendor bid-document portal | SCA (on **Microsoft SharePoint**) | Login-walled UI; **no API** | The transactional layer — obtaining bid sets and submitting on solicitations. `/_layouts/OnlineBidsetsLogin/CustomLogin.aspx` custom login; no JSON/OpenAPI surface. |
| `www.nycsca.org/WS/Reports/type/advbids` | "Web service" report (advertised bids) | SCA (**DotNetNuke**) | Public (HTML) | The path name suggests a web service, but it returns a **rendered DNN HTML page**, not JSON. No machine-readable contract. |
| `www.nycsca.org/` | Informational / vendor site | SCA (DotNetNuke on ASP.NET, obvio skin) | Public (HTML) | Content only — capital plan, vendor guidance, RFP notices. Fronted by AWS ALB. No content API. |
| `dnnhh5cc1.blob.core.windows.net` | Object storage (documents) | Microsoft Azure Blob Storage | SAS-signed URLs | PDFs (general conditions, safety manuals, press) served via `DNNFileManagerPolicy` SAS signatures. |

## Takeaways

- **The API story is a mismatch, not an absence.** Capital-plan and procurement *reference* data is generously open through Socrata SODA; the *transaction* layer a vendor lives in — getting prequalified, obtaining bid documents, bidding — is a closed SharePoint portal.
- **No API for the core vendor transaction.** Applying to become a **prequalified vendor** — the everyday onboarding step — has no machine-readable contract at all; it is reachable only via PDF forms and the bidset SharePoint login. SCA publishes the *resulting* Prequalified Firms roster (`szkz-syh6`) but never the act of applying.
- **A "WS" path that isn't a web service.** `/WS/Reports/…` returns DNN HTML — a reminder that a URL looking like an API is not one.
- **No agent-native surface.** The [OpenAPI](openapi/sca.yaml) + [MCP artifact](mcp/sca-mcp.json) here propose one owned contract that publishes the open reference data cleanly *and* unlocks the net-new `apply_for_prequalification` write workflow.
