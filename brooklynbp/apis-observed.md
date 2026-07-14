# APIs Observed While Crawling — Brooklyn Borough President

Backend/service APIs the Brooklyn BP surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is one of **shape, not absence**: the office has more machine-readable surface than expected — 21 NYC Open Data datasets *and* a live WordPress/Events-Calendar API — but **none of it is an owned, purpose-built Borough President API**, and the office no longer controls its former primary domain. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 21 datasets under agency `Brooklyn Borough President (BPBK)`: ULURP recommendations, community-board contacts, a dozen 'BP Appointments' tables, capital/discretionary/tourism awards, passed legislation. Each has a SODA `/resource/<id>.json` endpoint. Real and open — but scattered across single-purpose IDs, several thin/stale. |
| **`www.brooklynbp.nyc.gov/wp-json/tribe/events/v1`** | Events API (The Events Calendar plugin) | Brooklyn BP (WP Engine) | **Yes — open** | The one live, purpose-shaped read API — events, ULURP public hearings, borough board meetings (6 upcoming at assessment). Provided by the generic Tribe Events plugin. |
| **`www.brooklynbp.nyc.gov/wp-json/wp/v2`** | WordPress REST API | Brooklyn BP (WP Engine) | **Yes — open** | Generic CMS content API — 315 posts (press releases/news), 74+ pages, categories, media. Machine-readable but not a BP contract; robots.txt disallows only `/wp-admin/`. |
| `www.brooklynbp.nyc.gov` | Site (headless WordPress + Next.js) | Brooklyn BP (WP Engine, Cloudflare) | Public (HTML) | `x-powered-by: WP Engine`; `_next` front end; Wordfence, wp-statistics, MetaSlider plugins. |
| `brooklyn-usa.org` | **Lapsed / repurposed domain** | Third party (WPX Cloud) | Redirects offsite | `www` + apex 301 → `batman-news.com`; `bm-bulker-api` / `bm-migration-api` domain-flip namespaces. The office no longer controls its former primary domain. |
| Cloudflare edge | CDN | Cloudflare | Vendor | `cf-ray` on the current site. |

## Takeaways

- **The API story is fragmentation, not scarcity.** Between 21 Socrata datasets and a live WordPress/Events-Calendar API, the raw material is unusually plentiful for a Borough President — but there is **no owned, purpose-built BP API**, and consumers must learn 21 dataset IDs plus generic CMS endpoints.
- **The one BP-shaped live API is a plugin.** The Events Calendar feed is genuinely useful (hearings, board meetings), but it exists because WordPress does — not because the office designed a contract.
- **No write surface for the core constituent action.** Applying to serve on a **community board** — the office's most consequential yearly interaction with residents — has no machine-readable contract at all; it is an unstructured web form. Meeting requests and requests-for-assistance survive only as form dumps / aggregate call counts.
- **Ownership is the weak link.** The office let `brooklyn-usa.org` lapse into an offsite domain-flip; its content sits on a commercial host; its data sits under 21 city-owned Socrata IDs. Nothing ties this together as *the Brooklyn BP's own API*.
- **No agent-native surface.** The [OpenAPI](openapi/brooklynbp.yaml) + [MCP artifact](mcp/brooklynbp-mcp.json) here propose one owned contract that publishes the open reference data cleanly, wraps the events feed, and adds the net-new `apply_to_community_board` write workflow — designed to be **templated across all five Borough Presidents**.
