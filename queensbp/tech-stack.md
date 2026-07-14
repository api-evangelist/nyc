# Technology & Vendor Inventory — Queens Borough President

What the Office of the Queens Borough President's (QBP) public surface is built on and which third parties it depends on — fingerprinted from response headers, `wp-json` namespaces, and page markup during the crawl (2026-07-13). The short version: **`queensbp.org` 301-redirects to `www.queensbp.nyc.gov`, a WordPress/Divi brochure on WP Engine behind Cloudflare** — a thin site whose one machine-readable surface (the WordPress REST API) is switched on but empty.

## One front door (with a redirect)

| Surface | URL | What it does |
|---|---|---|
| Legacy domain | `queensbp.org` | **301-redirects** (Cloudflare) to the nyc.gov host — the office has migrated onto nyc.gov |
| Informational site | **`www.queensbp.nyc.gov`** | About, land use, community boards, budget/major allocations, constituent services, newsroom — content only |
| WordPress REST API | `www.queensbp.nyc.gov/wp-json/wp/v2` | Enabled and public, but **empty** — `X-WP-Total: 0` for posts and the `project` custom post type |

## Informational site (www.queensbp.nyc.gov)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Cloudflare** | `server: cloudflare`, `cf-ray`, `cf-cache-status`, `alt-svc: h3` |
| Managed hosting | **WP Engine** | `x-powered-by: WP Engine`, `x-cache-group`, `wpe/cache-plugin/v1` and `wpe_sign_on_plugin/v1` REST namespaces |
| CMS platform | **WordPress** | `link: <…/wp-json/>; rel="https://api.w.org/"`, `wp-json/wp/v2` |
| Theme / page builder | **Divi** (Elegant Themes) + **Elementor** markup | `/wp-content/themes/Divi`, `divi/v1` REST namespace, `elementor` in markup |
| SEO | **Yoast SEO** | `yoast/v1` namespace; Yoast block in `robots.txt`; `sitemap_index.xml` |
| Security | **Wordfence** | `wordfence/v1` REST namespace |
| Translation | **Google Language Translator** plugin | `/wp-content/plugins/google-language-translator` |

This is a **commodity managed-WordPress stack** — the same shape a mid-size nonprofit or campaign site runs. It is a fifth distinct platform in the NYC Modernization survey, after Parks' Smarty/PHP, DOE's Sitefinity/.NET, Council's WordPress, and NYCHA's NYC.gov Livesite + Oracle Siebel.

## The REST API is on, but empty — the important part

WordPress ships a real REST API, and QBP's is reachable and returns valid JSON for pages. But the content that matters isn't in it:

| Endpoint | Result |
|---|---|
| `/wp-json/` | 10 namespaces (`wp/v2`, `oembed`, `yoast/v1`, `divi/v1`, `wpe/cache-plugin/v1`, `wordfence/v1`, …) |
| `/wp-json/wp/v2/posts` | **`X-WP-Total: 0`** — no posts |
| `/wp-json/wp/v2/project` (custom post type) | **`X-WP-Total: 0`** — no entries |
| `/wp-json/wp/v2/pages` | The whole site — press releases, land use, budget — is authored here as **Divi page-builder Pages** |

Press releases, events, and everything in the Newsroom are laid out as Divi Pages, so the platform's own machine-readable surface carries almost none of the office's actual content. The fix isn't to buy an API — it's to **author content as structured posts/CPTs the existing REST API would expose**.

## Open Data footprint

Verified via the Socrata Discovery API: `Dataset-Information_Agency = "Queens Borough President (QBP)"` returns exactly **two** datasets, both about community boards:

- **Queens Community Board Members** (`rps4-dwwk`, 4 columns)
- **Queens Community Board District Managers and Chairs** (`8z5h-tzdr`, 20 columns)

Nothing on land use, discretionary funding, events, or applications.

## Modernization implications

1. **The one API is dormant, not absent.** WordPress REST is enabled but empty — the cheapest win is to move Newsroom and events into posts/CPTs so `wp/v2` actually serves them.
2. **The core functions have no contract.** Land-use (ULURP) recommendations, discretionary funding, and community-board applications — the things a borough president uniquely does — are HTML/PDF only. An owned [OpenAPI](openapi/queensbp.yaml) should publish them as clean resources and add the net-new **community board application** write.
3. **Five near-identical offices.** All five borough presidents run thin sites of this shape. Building a fifth one-off API is waste; the leverage is **one standardized Borough President API** every borough implements — with an agent-native contract ([MCP artifact](mcp/queensbp-mcp.json)) on top.
