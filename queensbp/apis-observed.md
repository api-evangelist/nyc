# APIs Observed While Crawling — Queens Borough President

Backend/service APIs the QBP surface calls or exposes, surfaced during the crawl (2026-07-13). The finding is a twist on the others: **QBP's platform ships a real API (the WordPress REST API), but it is switched on and empty**, and Open Data offers only two community-board datasets. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`www.queensbp.nyc.gov/wp-json/wp/v2`** | WordPress REST API | QBP (WordPress/Divi on WP Engine) | **Yes — but empty** | Enabled and reachable; returns valid JSON for pages. But `X-WP-Total: 0` for both posts and the `project` custom post type — content is authored as Divi Pages, so the office's actual content (press releases, events) never flows through it. Namespaces: `wp/v2`, `oembed`, `yoast/v1`, `divi/v1`, `wpe/cache-plugin/v1`, `wordfence/v1`. |
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata/Tyler) | **Yes — open** | Exactly **two** QBP-attributed datasets: Queens Community Board Members (`rps4-dwwk`, 4c) and Queens Community Board District Managers and Chairs (`8z5h-tzdr`, 20c). Each has a SODA `/resource/<id>.json` endpoint. The only substantive machine-readable QBP data — and it is entirely about community boards. |
| `www.queensbp.nyc.gov` | Informational site | QBP (WordPress/Divi, WP Engine, Cloudflare) | Public (HTML) | Land use, community boards, budget, constituent services, newsroom — Divi page-builder Pages. No content API in practice. |
| `queensbp.org` | Legacy domain | QBP | 301 redirect | Redirects (Cloudflare) to `www.queensbp.nyc.gov`; the office has moved onto the nyc.gov domain. |
| Cloudflare edge | CDN | Cloudflare | Vendor | `server: cloudflare`, `cf-ray`, `cf-cache-status`. |

## Takeaways

- **The API is dormant, not missing.** WordPress REST is on but empty — the office already owns a machine-readable surface and simply doesn't publish through it. Authoring Newsroom/events as posts or a custom post type would light it up for free.
- **Open Data is thin and one-note.** Only community boards are published; the borough president's other core acts — **land-use (ULURP) recommendations**, **discretionary funding**, events, and press — have no machine-readable contract at all.
- **No write surface.** The QBP's flagship participatory act, **applying to serve on a community board**, is an HTML/PDF form. So is a constituent-services request. Neither is callable.
- **No agent-native surface.** The [OpenAPI](openapi/queensbp.yaml) + [MCP artifact](mcp/queensbp-mcp.json) here propose one owned contract that publishes the community-board data cleanly, gives the ULURP/funding/newsroom functions a structured home, and unlocks the net-new `apply_to_community_board` write.
- **This is a five-office pattern.** Every borough president runs a thin site like this. The observation argues for **one shared Borough President API**, not five.
