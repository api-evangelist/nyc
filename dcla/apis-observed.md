# APIs Observed While Crawling — DCLA

Backend/service APIs the DCLA surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is asymmetric: **DCLA's funding-outcome and directory data has a real, open API (Socrata SODA over 9 datasets), but its grant *application* layer has none** — it runs on a Salesforce Experience Cloud portal with no documented public API. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 9 DCLA datasets: cultural-organization directory, program & capital grant awards, Cultural Institutions Group support, completed Percent for Art commissions, Materials for the Arts summaries. Each has a SODA `/resource/<id>.json` endpoint. This is the one real, machine-readable DCLA API — and it publishes outcomes only. |
| **`dclagms.nyc.gov/grants/s/`** | Grants Management System | DCLA (on **Salesforce Experience Cloud**) | Login-walled UI; **no public API** | The transactional layer — register an organization, create and submit a **Cultural Development Fund grant application**, and track status. Salesforce Lightning Community (`LSKey-c$` cookies, `/grants/s/` path), backed by `culturalaffairsnyc.my.salesforce.com` with SAML SSO. No documented public JSON/OpenAPI surface. |
| `www.nyc.gov/site/dcla/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | Content only — About, cultural funding, MFTA, Public Art, resources. No content API exposed. |
| Akamai edge | CDN API | Akamai | Vendor | `x-akamai-transformed` on the informational site. |
| Dynatrace RUM / mPulse | Monitoring beacons | Dynatrace / Akamai | Vendor | `x-oneagent-js-injection`, `ruxitagentjs`, `go-mpulse.net` real-user monitoring. |
| Google Maps JS | Mapping API | Google | Vendor | `maps.googleapis.com` embedded on location pages. |

## Takeaways

- **The API story is a mismatch, not an absence.** Funding-outcome and directory data is generously open through Socrata SODA; the *application* pipeline that produces those outcomes is a closed vendor CRM.
- **No API for the core transaction.** Applying for and tracking a **Cultural Development Fund grant** — the single most important interaction between DCLA and its constituency — has no machine-readable contract at all; it is reachable only via the Salesforce portal after login.
- **Outcomes published, requests hidden.** Open Data shows who was funded and for how much, but never the application, the requested amount, or the panel-review process.
- **No agent-native surface.** The [OpenAPI](openapi/dcla.yaml) + [MCP artifact](mcp/dcla-mcp.json) here propose one owned contract that publishes the open funding/organization data cleanly *and* opens the net-new `apply_for_grant` write workflow.
