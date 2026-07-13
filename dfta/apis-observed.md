# APIs Observed While Crawling — NYC Aging (DFTA)

Backend/service APIs the DFTA surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is asymmetric: **DFTA's provider-network data has a real, open API (Socrata SODA over 11 datasets), but its resident *service* layer has none** — intake and referral run through the Aging Connect contact center by phone, with no documented API. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 11 DFTA datasets: all contracted providers, publicly open sites, social adult day care, older adult center (senior center) Local Law 140 operations, activities, budgeted/reported service units, expenditures, and aggregate participation. Each has a SODA `/resource/<id>.json` endpoint. This is the one real, machine-readable DFTA API. |
| **Aging Connect (`212-AGING-NYC` / `212-244-6469`)** | Information & referral intake | NYC Aging (DFTA) | Phone / walk-in / web form; **no API** | The transactional layer — connect an older adult to case management, home-delivered meals, benefits, caregiver support, elder-abuse help, or center enrollment. No JSON/OpenAPI surface; a human contact center. |
| `www.nyc.gov/site/dfta/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | Content only — About, services, find-help, center finder. No content API exposed. |
| `nyc.gov/311` · `access.nyc.gov` | Citywide intake / benefits screening | NYC (OTI / HRA) | Public (HTML/app) | Alternate front doors New Yorkers use to reach aging services and screen for benefits. |
| Akamai edge | CDN API | Akamai | Vendor | `x-akamai-transformed` on the informational site. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring. |

## Takeaways

- **The API story is a mismatch, not an absence.** Provider/program/contract data is generously open through Socrata SODA; the *service* layer an older adult actually needs is a phone line.
- **No API for the core transaction.** Making a **service referral** — connecting an older adult to a service — the single most common DFTA interaction, has no machine-readable contract at all; it is reachable only via Aging Connect by phone or a 311 call.
- **No individual client data, by design.** Participation is published only in aggregate (unduplicated clients); per-person intake lives inside DFTA's case-management systems and Aging Connect.
- **No agent-native surface.** The [OpenAPI](openapi/dfta.yaml) + [MCP artifact](mcp/dfta-mcp.json) here propose one owned contract that publishes the open provider network cleanly *and* unlocks the net-new `make_referral` write workflow.
