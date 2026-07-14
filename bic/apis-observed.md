# APIs Observed While Crawling — BIC

Backend/service APIs the BIC surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is asymmetric: **BIC's regulatory registry has a real, open API (Socrata SODA over 9 datasets), but its business *service* layer has none** — it runs on a Salesforce Experience Cloud portal with no documented API. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 9 BIC datasets: trade waste hauler licensees, broker/self-hauler/construction-and-demolition registrants, public wholesale-market businesses, fleet vehicles, issued violations, complaints/inquiries, and denied companies. Each has a SODA `/resource/<id>.json` endpoint. This is the one real, machine-readable BIC API. |
| **`bicportal.nyc.gov`** | Licensing / payment portal | BIC (on **Salesforce Experience Cloud**) | Login-walled UI; **no API** | The transactional layer — apply for/renew a license or registration, and pay a violation fine (`/s/viopay`). Client-rendered Salesforce Lightning community (`server: sfdcedge`, `x-sfdc-request-id`), JavaScript-only, no JSON/OpenAPI surface. |
| `www.nyc.gov/site/bic/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | Content only — About, industries, laws & rules, forms. No content API exposed. |
| `portal.311.nyc.gov` | Complaint intake | NYC (311) | Web form | Complaints about trade waste hauling / wholesale markets route through 311; only closed records reach Open Data. |
| Akamai edge | CDN API | Akamai | Vendor | `x-akamai-transformed` on the informational site. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring. |

## Takeaways

- **The API story is a mismatch, not an absence.** The regulatory registry is generously open through Socrata SODA — in fact the most open of any NYC domain assessed so far — while the *service* layer that businesses transact in is a closed vendor SaaS.
- **No API for the core transaction.** Applying for and renewing a trade waste **license/registration**, and paying a violation fine, have no machine-readable contract at all; they are reachable only via the Salesforce portal.
- **Open data publishes outputs, not the workflow.** The registry publishes who *is* licensed and who was *denied* (`exsg-kpya`), but nothing about the apply → review → approve pipeline that produces those records.
- **No agent-native surface.** The [OpenAPI](openapi/bic.yaml) + [MCP artifact](mcp/bic-mcp.json) here propose one owned contract that publishes the open registry cleanly *and* unlocks the net-new `apply_for_license` write workflow.
