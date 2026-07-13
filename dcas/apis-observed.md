# APIs Observed While Crawling — DCAS

Backend/service APIs the DCAS surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is asymmetric: **DCAS's reference data has a real, open API (Socrata SODA over 32 datasets), but its citizen *transaction* layer has none** — it is spread across three separate vendor applications (Azure/.NET, PeopleSoft, Shopify), none exposing a DCAS-owned API. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 32 DCAS datasets: civil-service lists & titles, job postings, exam schedule, procurement/City Record, DCAS-managed buildings & energy, and the municipal fleet. Each has a SODA `/resource/<id>.json` endpoint. This is the one real, machine-readable DCAS API. |
| **`cityjobs.nyc.gov`** (was `a127-jobs.nyc.gov`) | Careers + exam application portal | DCAS (ASP.NET Core / Azure) | Login-walled UI; **no API** | The City Jobs external portal and the OASys Online Application System — where job applications and **exam registrations** happen. `Kestrel` server, Azure App Service routing, `AspNetCore.Antiforgery`. No JSON/OpenAPI surface. |
| **`a127-ess.nyc.gov`** | Employee self-service (HR) | DCAS/OPA (Oracle PeopleSoft / NYCAPS) | Login-walled UI; **no API** | NYC Automated Personnel System — pay, benefits, W-2. PeopleSoft (`psp/` path, page title). Legacy vendor HR app, no public API. |
| **`a856-citystore.nyc.gov`** | E-commerce store | DCAS (Shopify) | Public UI; Shopify API is vendor-tenant | The official CityStore runs on **Shopify** (`_shopify_*` cookies, Cloudflare edge). Storefront/Admin APIs exist but belong to the Shopify tenant, not a DCAS contract. |
| `www.nyc.gov/site/dcas/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | Content only — careers, exams, fleet, agency services. No content API exposed. |
| Akamai edge | CDN API | Akamai | Vendor | `x-akamai-transformed` on the informational site. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring. |

## Takeaways

- **The API story is a mismatch, not an absence.** Reference/asset data is generously open through Socrata SODA; the *transaction* layer that citizens and employees live in is a set of closed, differently-built vendor apps.
- **No API for the core transaction.** Registering for a **civil-service exam** — the DCAS-signature citizen interaction — has no machine-readable contract at all; it is reachable only via the OASys / City Jobs UI. The exam *schedule* is open data, but you cannot *apply* through any API.
- **Three vendors, no shared contract.** Even though the careers front door has been replatformed to modern .NET/Azure, hiring (Azure), HR self-service (PeopleSoft), and retail (Shopify) each stand alone; there is no unifying DCAS API across them.
- **No agent-native surface.** The [OpenAPI](openapi/dcas.yaml) + [MCP artifact](mcp/dcas-mcp.json) here propose one owned contract that publishes the open reference data cleanly *and* adds the net-new `register_for_exam` write workflow.
