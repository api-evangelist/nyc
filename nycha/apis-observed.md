# APIs Observed While Crawling — NYCHA

Backend/service APIs the NYCHA surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is asymmetric: **NYCHA's reference data has a real, open API (Socrata SODA over 24 datasets), but its resident *service* layer has none** — it runs on an Oracle Siebel CRM with no documented API. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 24 NYCHA datasets: developments, residential addresses, facilities, six utility consumption-and-cost streams, aggregate resident demographics, Local Law 163 / REES rollups. Each has a SODA `/resource/<id>.json` endpoint. This is the one real, machine-readable NYCHA API. |
| **`selfserve.nycha.info/nycha/app/eservice/enu`** | Resident service portal | NYCHA (on **Oracle Siebel**) | Login-walled UI; **no API** | The transactional layer — rent, recertification, application/waitlist status, and repair **work orders**. Server-rendered Siebel Open UI (`SWECmd`), JavaScript-only, no JSON/OpenAPI surface. |
| `www.nyc.gov/site/nycha/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | Content only — About, developments, forms, news. No content API exposed. |
| `on1.nyc.gov` | Citywide account / SSO host | NYC (OTI) | Login | NYC.gov ID / self-service SSO umbrella referenced for portal sign-in. |
| Akamai edge | CDN API | Akamai | Vendor | `x-akamai-transformed` on the informational site. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring. |

## Takeaways

- **The API story is a mismatch, not an absence.** Reference/asset data is generously open through Socrata SODA; the *service* layer that residents live in every day is a closed vendor CRM.
- **No API for the core transaction.** Reporting and tracking a **repair work order** — the single most common NYCHA resident interaction — has no machine-readable contract at all; it is reachable only via a Siebel screen or a phone call.
- **No individual household data, by design.** Resident demographics are published only in aggregate (Resident Data Book); per-household records live inside the Tenant Data System and Siebel.
- **No agent-native surface.** The [OpenAPI](openapi/nycha.yaml) + [MCP artifact](mcp/nycha-mcp.json) here propose one owned contract that publishes the open reference data cleanly *and* unlocks the net-new `report_repair` write workflow.
