# APIs Observed While Crawling — FDNY

Backend/service APIs the FDNY surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is asymmetric: **FDNY's reference and operational data has a real, open API (Socrata SODA over 17 datasets), but its business *service* layer has none** — it runs on a rented Accela Civic Platform with no documented API. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 17 FDNY datasets: firehouses, Fire and EMS incident dispatch, Bureau of Fire Prevention inspections, active violation orders, certificates of fitness, building vacate list, fire causes. Each has a SODA `/resource/<id>.json` endpoint. This is the one real, machine-readable FDNY API. |
| **`fires.fdnycloud.org/CitizenAccess`** | Business permitting portal | FDNY (on **Accela Civic Platform**) | Login-walled UI; **no API** | FDNY Business — the transactional layer: fire permits, Certificates of Fitness/Operation, inspection scheduling, violation response, fee payment. Server-rendered Accela Citizen Access (`.aspx`), JavaScript-only, no JSON/OpenAPI surface. |
| `www.nyc.gov/site/fdny/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | Content only — About, firehouses, safety, business how-to, news. No content API exposed. |
| Cloudflare + Azure App Gateway | Edge / gateway | Cloudflare, Microsoft Azure | Vendor | `CF-RAY`, `ApplicationGatewayAffinity` cookies front the Accela portal. |
| Akamai edge | CDN API | Akamai | Vendor | `x-akamai-transformed` on the informational site. |
| Datadog RUM | Monitoring beacon | Datadog | Vendor | Accela portal CSP ships a Datadog browser-agent `report-uri`. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` on the informational site. |

## Takeaways

- **The API story is a mismatch, not an absence.** Reference/operational data is generously open through Socrata SODA; the *business* layer that permit-holders live in is a rented, closed vendor SaaS.
- **No API for the core transaction.** Applying for and tracking a **fire permit** — the central FDNY Business interaction — has no machine-readable contract at all; it is reachable only via an Accela screen or on paper.
- **The open data is a rear-view mirror.** Inspections, violations, certificates, and building summaries are all published as **historical snapshots**; the live regulatory state lives inside Accela.
- **No agent-native surface.** The [OpenAPI](openapi/fdny.yaml) + [MCP artifact](mcp/fdny-mcp.json) here propose one owned contract that publishes the open reference/operational data cleanly *and* unlocks the net-new `apply_for_permit` write workflow.
