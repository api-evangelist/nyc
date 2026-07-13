# APIs Observed While Crawling — DVS

Backend/service APIs the DVS surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is asymmetric: **DVS's reference and de-identified service data have a real, open API (Socrata SODA over 7 datasets), but the live care-coordination *referral* has none** — it runs on a third-party vendor platform, **Combined Arms** (VetConnectNYC), with no documented API. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 7 DVS datasets: DVS Resource Map, NYC Veteran Owned Businesses, DVS Assistance Requests, DVS Cases, DVS Clients (aggregate), plus two historical request/VPC-move datasets. Each has a SODA `/resource/<id>.json` endpoint. This is the one real, machine-readable DVS API — and unusually, it reaches into the (de-identified) service layer. |
| **`nyc.veteranportal.combinedarms.us`** (VetConnectNYC) | Care-coordination intake portal | **Combined Arms** (vendor); DVS Care Coordinators work the queue | Registration-gated web form; **no API** | The transactional layer — a veteran submits the VetConnectNYC Request Form to be connected to services (housing, benefits, VA claims, health, employment, food, legal). Next.js app on CloudFront (`x-powered-by: Next.js`, `via: cloudfront`), "CA - Military Resource Portal". No JSON/OpenAPI surface; DVS processes requests manually within 3–5 business days. |
| `www.nyc.gov/site/veterans/` | Informational site | NYC.gov shared platform ("Livesite" v22) | Public (HTML) | Content only — About, services, initiatives, resource lists. No content API exposed. |
| `nyc.veterranportal…` / `combinedarms.us` | Vendor platform root | Combined Arms | Public (HTML) | Redirects to `www.combinedarms.us`; the coordinated-care network behind VetConnectNYC. |
| Akamai edge | CDN API | Akamai | Vendor | `x-akamai-transformed` on the informational site. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring. |

## Takeaways

- **The API story is a mismatch, not an absence.** Reference data *and* de-identified service analytics are generously open through Socrata SODA; the *live referral* that a veteran files is a closed, out-of-city vendor web form.
- **No API for the core transaction.** Making and tracking a **VetConnectNYC referral** — the single most important DVS interaction — has no machine-readable contract at all; it is reachable only through the Combined Arms portal and a 3–5 day manual queue.
- **No individual veteran data, by design.** Client demographics are published only de-identified/aggregate (DVS Clients); per-veteran records live inside DVS's case system and the vendor portal.
- **No agent-native surface.** The [OpenAPI](openapi/dvs.yaml) + [MCP artifact](mcp/dvs-mcp.json) here propose one owned contract that publishes the open reference and service data cleanly *and* unlocks the net-new `make_referral` write workflow.
- **Vendor correction.** VetConnectNYC is **Combined Arms**, not Unite Us (the assignment's tentative guess) — see [tech-stack.md](tech-stack.md).
