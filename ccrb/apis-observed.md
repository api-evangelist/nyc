# APIs Observed While Crawling — CCRB

Backend/service APIs the CCRB surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is a mismatch: **CCRB's accountability data has a real, open API (Socrata SODA over 4 daily-updated datasets), but the two things a member of the public actually *does* — file a complaint and check its status — have none.** Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 4 CCRB datasets: police officers (`2fir-qns4`), allegations (`6xgr-kwjq`), complaints (`2mby-ccnw`), penalties (`keep-pkmh`). Each has a SODA `/resource/<id>.json` endpoint, updated **daily** and automated. This is the one real, machine-readable CCRB API — the read side of the CCRB Complaints Database. |
| **`www.nyc.gov/site/ccrb/.../file-online.page`** | Complaint intake form | CCRB (on NYC.gov Livesite) | Public UI; **no API** | The online complaint form — file a misconduct complaint. Server-rendered JavaScript page, no JSON/OpenAPI surface. The net-new write gap. |
| **`apps.nyc.gov/ccrb-status-lookup/`** | Complaint status lookup | CCRB (citywide `apps.nyc.gov`) | Public UI; **no API** | Check the status of a filed complaint. A standalone screen disconnected from intake; no machine-readable contract. |
| `www.nyc.gov/site/ccrb/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | About, complaint process, policy, Data Transparency Initiative dashboards. No content API exposed. |
| Data Transparency Initiative dashboards | Interactive data viz | CCRB | Public (HTML/JS) | Complaints, allegations, members of service, victims/alleged, feedback — rendered from the CCRB Complaints Database; dashboards, not an API. |
| `portal.311.nyc.gov` | Citywide 311 intake | NYC (OTI) | Public | Alternate complaint channel referenced from CCRB's file-a-complaint pages. |
| Akamai edge | CDN API | Akamai | Vendor | `x-akamai-transformed` on the informational and app hosts. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring. |

## Takeaways

- **The API story is a mismatch, not an absence.** The accountability *record* is generously open through Socrata SODA and refreshed daily; the *intake* that produces those records has no machine-readable contract.
- **No API for the core civic act.** Filing a complaint of NYPD misconduct — the reason the agency exists — is reachable only via a web form, a 311 call, mail, or in person. Status is a second, disconnected screen.
- **Delivery, not openness, is the constraint.** CCRB is already a transparency model; the gap is that its data is dashboards-and-CSV rather than a queryable, agent-native API.
- **No agent-native surface.** The [OpenAPI](openapi/ccrb.yaml) + [MCP artifact](mcp/ccrb-mcp.json) here propose one owned contract that exposes the open accountability data cleanly *and* adds the net-new `file_misconduct_complaint` write workflow with a tracked status.
