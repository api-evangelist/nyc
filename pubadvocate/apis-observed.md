# APIs Observed While Crawling — NYC Public Advocate

Backend/service APIs the Public Advocate's surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is stark: **the city's ombudsman has almost no machine-readable surface**. There is exactly one real API — the **undocumented** `/api/landlords` route behind the Worst Landlord Watchlist — while the main site was **down (502)**, the office publishes **zero** Open Data, and its core intake function has **no API at all**. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`landlordwatchlist.com/api/landlords`** | Undocumented JSON API | NYC Public Advocate (app on Vercel) | **Reachable, undocumented** | The one real API. Returns `{ results: [ { landlordid, org, officer, buildings, UNIT, dob, tax_lien, evictions, num_avg, rank } × 99 ] }` — the Top 100 Worst Landlords. No docs, no OpenAPI, no versioning; a Next.js data route, not a governed contract. |
| **`advocate.nyc.gov`** | Informational site | NYC Public Advocate (self-hosted) | HTML — **502 during crawl** | Self-run `nginx/1.18.0 (Ubuntu)`, not the shared NYC.gov platform. Reports, "help with a city agency", and public interest content are HTML/PDF; no content API. Returned **502 Bad Gateway** on every path. |
| `legistar.council.nyc.gov` | Legislative system (Legistar Web API) | **City Council (NYCC)** / Granicus | Web + API | Where the PA's sponsored bills actually live. Owned by the Council — the Public Advocate is a *sponsor*, not the system of record. |
| `data.cityofnewyork.us` (SODA) | Open Data API | NYC (Socrata / Tyler) | Yes — open | Hosts the underlying HPD Housing Maintenance Code violations / DOB / registration data the Watchlist is derived from — but **nothing under a Public Advocate label**. The PA contributes zero assets. |
| Vercel edge | Hosting / CDN | Vercel | Vendor | `server: Vercel`, `x-vercel-cache`, `x-vercel-id` on the Watchlist — the flagship product runs off-platform on a commercial PaaS. |

## Takeaways

- **One undocumented API is the whole story.** The Worst Landlord Watchlist proves the office *can* stand up a real, data-backed product — but it did so as an orphan Next.js/Vercel app with an unversioned, undocumented `/api/landlords` route, disconnected from advocate.nyc.gov and from any governance.
- **The main site was down.** Every request to `advocate.nyc.gov` returned 502 from a self-hosted nginx/Ubuntu origin. The city's watchdog cannot be relied on to even serve its own HTML, let alone an API.
- **Zero Open Data.** Unlike NYCHA's 24 datasets, the Public Advocate publishes nothing machine-readable to NYC Open Data (verified across four agency-label variants).
- **No intake API.** The office's constitutional job — helping residents with a city agency — is a web form, phone call, or email. There is no way to file or track an `OmbudsmanComplaint` by machine.
- **No agent-native surface.** The [OpenAPI](openapi/pubadvocate.yaml) + [MCP artifact](mcp/pubadvocate-mcp.json) here propose one owned contract that documents the Watchlist, consolidates legislation/reports/public-interest output, and adds the net-new `file_complaint` write workflow.
