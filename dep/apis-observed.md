# APIs Observed While Crawling — DEP

Backend/service APIs the DEP surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is asymmetric: **DEP's reference and telemetry data has a real, open API (Socrata SODA over 57 datasets), but its customer *service* layer has none** — bill payment and account management run on a uMAX Customer Information System behind Azure AD B2C with no documented API, and street-condition service requests are funneled into generic NYC311. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 57 DEP datasets: water consumption, reservoir levels, harbor/drinking/watershed/lead-copper water quality, green infrastructure, hydrants & catch basins, water/air/asbestos permits, FloodNet, wastewater performance. Each has a SODA `/resource/<id>.json` endpoint. This is the real, machine-readable DEP API — reference/telemetry data only, and sprawling/inconsistently typed. |
| **`a826-umax.dep.nyc.gov`** | Customer billing/account portal (CIS) | NYC DEP (on **uMAX** / Advanced Utility Systems) | Login-walled UI; **no API** | The transactional layer — water/sewer bill payment, account management. ASP.NET / ASP.NET Core SPA behind **Azure AD B2C** (`umaxazprodb2c.b2clogin.com`), on Azure App Service. A public `/quickpay` page exists but exposes no JSON/OpenAPI. |
| **`portal.311.nyc.gov`** | Citywide service-request intake | NYC (311 / OTI) | Public UI | Where DEP street conditions (water-main break, no water, sewer backup, catch basin, hydrant, water quality) are actually reported — generic 311, not a DEP-owned intake. |
| `data.cityofnewyork.us/d/4fvw-nn9c` | Open Data (Work Order Management Module) | NYC DEP via Socrata | Open | DEP's *completed* work orders / service requests — the closest open twin to the locked service layer, but read-only and after the fact. |
| `www.nyc.gov/site/dep/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | Content only — drinking water, wastewater, green infrastructure, permits. No content API exposed. |
| Akamai edge | CDN API | Akamai | Vendor | `x-akamai-transformed` on the informational site. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring. |

## Takeaways

- **The API story is a mismatch, not an absence.** Reference/telemetry data is generously open through Socrata SODA (57 datasets); the *service* layer customers live in — paying a bill, reporting a leak or backup — is closed or fragmented.
- **No API for the core transactions.** Water-bill/account management is a login-walled uMAX portal behind Azure AD B2C; reporting a **water-main break or sewer backup** has no DEP-owned API at all — it is handed to generic NYC311 or a phone call.
- **Even the open data is hard to consume.** Harbor Water Quality is 100 free-text columns; reservoir levels are cryptic SCADA tags; there are ~a dozen near-duplicate Watershed tables. Open ≠ usable.
- **No agent-native surface.** The [OpenAPI](openapi/dep.yaml) + [MCP artifact](mcp/dep-mcp.json) here propose one owned contract that publishes the open reference data as clean, well-typed resources *and* unlocks the net-new `report_water_problem` write workflow.
