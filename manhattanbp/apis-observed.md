# APIs Observed While Crawling — Manhattan Borough President

Backend/service APIs the Manhattan Borough President surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is a mismatch: **the office's civic data has a real, open API (Socrata SODA over 21 datasets), and the website exposes only the generic WordPress REST API** — but neither is a purpose-built contract for the office's actual work, and the flagship citizen action (applying to serve on a community board) has no API at all. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 21 MBPO datasets: ULURP recommendations, BP appointments, community-board leadership, constituent services, and years of capital/tourism/community funding awards. Each has a SODA `/resource/<id>.json` endpoint. This is the one real, machine-readable MBPO data API — but the data is fragmented into one dataset per program per fiscal year. |
| **`manhattanbp.nyc.gov/wp-json/`** | WordPress REST API | MBPO (on WordPress / WP Engine) | Public (generic) | Default WP REST surface (`wp/v2` pages/posts) plus plugin namespaces (`forminator/v1`, `divi/v1`, `redirection/v1`, `google-site-kit/v1`, `wpe/cache-plugin`). Publishes site content as JSON; **no purpose-built endpoint** for ULURP, appointments, funding, or community-board applications. |
| **Forminator forms** | Web form plugin | MBPO (WPMU DEV Forminator) | Public UI; **no API** | The community-board application and other intake live as Forminator forms (`forminator/v1`) or downloadable PDFs — HTML forms, not a machine-readable write contract. |
| `manhattanbp.nyc.gov/` | Informational site | MBPO (WordPress + Divi theme) | Public (HTML) | About, community boards, land use, funding, policy, news. Content only. |
| Cloudflare edge | CDN | Cloudflare | Vendor | `cf-ray`, `cf-cache-status`, `__cf_bm`. |
| Google Site Kit | Analytics/SEO beacon | Google | Vendor | `generator: Site Kit by Google`. |

## Takeaways

- **The API story is fragmentation, not absence.** The civic data is open through Socrata SODA, but as 21 one-off assets (five separate Capital Grant Awards datasets, one per year); the website's only API is generic WordPress. Neither is an owned, purpose-built contract for the office.
- **No API for the flagship action.** Applying to serve on a **community board** — the office's most public citizen transaction — has no machine-readable contract; it is a WordPress/Forminator form or a PDF.
- **Constituent data is de-identified by design.** Constituent-service cases are published only as case type/subject/status/geography; no individual constituent identity is exposed.
- **Five identical offices.** The same shapes of data appear under all five borough-president Socrata labels, each behind its own thin WordPress site — the argument for a single federated Borough President API.
- **No agent-native surface.** The [OpenAPI](openapi/manhattanbp.yaml) + [MCP artifact](mcp/manhattanbp-mcp.json) here propose one owned contract that unifies the open data cleanly *and* adds the net-new `apply_to_community_board` write workflow.
