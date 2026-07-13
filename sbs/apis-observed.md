# APIs Observed While Crawling — SBS

Backend/service APIs the SBS surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is asymmetric: **SBS's program data has a real, open API (Socrata SODA over 28 datasets), but its guidance and *service* layer has none** — the MyCity Business portal (Step-by-Step wizard, certification, enrollment) is a stateful Spring/AEM application with no documented API. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 28 SBS datasets: certified businesses (M/WBE), Business Improvement Districts, Workforce1 recruitment events and job listings, service-center locations, training providers, and business-incentive rolls. Each has a SODA `/resource/<id>.json` endpoint. This is the one real, machine-readable SBS API. |
| **`nyc-business.nyc.gov/nycbusiness`** | Business service portal | NYC SBS/OTI (on **Spring + Adobe AEM**) | Session-walled UI; **no API** | MyCity Business — the transactional layer. Hosts the **Step-by-Step** licensing wizard (`/nycbusiness/wizard`), incentive/eligibility lookups, and the M/WBE **certification** and Workforce1 **enrollment** flows. Server-rendered, `SESSION` cookie, JavaScript-only, no JSON/OpenAPI surface. |
| `www.nyc.gov/site/sbs/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | Content only — programs, forms, news. No content API exposed. |
| `universal-editor-service.adobe.io` | CMS authoring API | Adobe (AEM Universal Editor) | Vendor | Loaded by MyCity Business for content authoring (`cors.js`). |
| Akamai edge / mPulse | CDN + RUM API | Akamai | Vendor | `x-akamai-transformed`; `go-mpulse.net` boomerang beacon on the portal. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` / `ruxitagentjs` real-user monitoring. |

## Takeaways

- **The API story is a mismatch, not an absence.** Program/directory data is generously open through Socrata SODA; the *guidance and service* layer that businesses actually use is a closed, stateful portal.
- **No API for the core transaction.** Applying for **M/WBE certification** — the flagship SBS business interaction — has no machine-readable contract; it is reachable only through the MyCity Business portal. Likewise the **Step-by-Step wizard** that tells a business which licenses it needs is pure session state with no callable surface.
- **The public certified list is the shadow of a private flow.** The open `SBS Certified Business List` (56 columns) is the *output* of a certification process that is entirely closed — you can read who got certified, but not apply through an API.
- **No agent-native surface.** The [OpenAPI](openapi/sbs.yaml) + [MCP artifact](mcp/sbs-mcp.json) here propose one owned contract that publishes the open program data cleanly *and* unlocks the net-new `apply_for_mwbe_certification` write workflow.
