# APIs Observed While Crawling — DOI

Backend/service APIs the DOI surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is asymmetric: **DOI's oversight data has a real, open API (Socrata SODA over 4 datasets), but its investigative outputs and its complaint intake have none** — the reports are PDFs and the corruption complaint runs on a third-party Kaseware case-management SaaS with no documented API. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 4 DOI datasets: Evictions (`6z8x-wfk4`, ~237k views), City Marshals Revenue (`7ewi-9cdf`), Policy & Procedure Recommendations (`jstn-jaut`), Monthly Performance Management Reports (`i8ua-bnkj`). Each has a SODA `/resource/<id>.json` endpoint. This is the one real, machine-readable DOI API — mostly City Marshal oversight, not investigations. |
| **`app.kaseware.us/public/#NYCDOI/…`** | Complaint intake portal | DOI (on **Kaseware**, Cloudflare-fronted) | Public web form; **no API** | The "Submit Report Online" corruption-complaint form. Client-rendered Kaseware Portal SPA, hash-routed, JavaScript-only, no JSON/OpenAPI surface. |
| `www.nyc.gov/site/doi/` + `/assets/doi/reports/pdf/` | Informational site + PDF report library | NYC.gov shared platform ("Livesite") | Public (HTML + static PDF) | Content only — About, units, news, Reports index. Public reports are static PDFs; no content or report API. |
| `portal.311.nyc.gov` | Citywide service request | NYC (OTI / 311) | Public (web/app) | Referenced as an alternate reporting channel for certain complaint types. |
| Akamai edge | CDN API | Akamai | Vendor | `x-akamai-transformed` on the informational site. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring. |

## Takeaways

- **The API story is a mismatch, not an absence.** Oversight data (evictions, marshal revenue, recommendations, performance) is open through Socrata SODA; the *investigations* and the *complaint intake* that define DOI are closed — one as PDFs, the other as a vendor SaaS.
- **No API for the core output.** DOI's public investigation reports have no machine-readable contract at all — they are PDFs served from `/assets/doi/reports/pdf/`. The PPR dataset proves DOI *can* publish structured recommendations.
- **No API for the core transaction.** Reporting fraud, waste, or corruption — the tip that starts every investigation — runs through a third-party Kaseware form or a phone call; there is no structured, ownable intake.
- **No agent-native surface.** The [OpenAPI](openapi/doi.yaml) + [MCP artifact](mcp/doi-mcp.json) here propose one owned contract that publishes the open oversight data cleanly, indexes the PDF reports, *and* unlocks the net-new `file_complaint` write workflow.
