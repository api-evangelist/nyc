# Technology & Vendor Inventory — Brooklyn Borough President

What the Office of the Brooklyn Borough President's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). The Brooklyn BP is a **thin content office** whose most striking technical fact is a governance one: it **let its former primary domain lapse**.

## Two front doors — and one that walked away

| Surface | URL | What it does |
|---|---|---|
| **Current site** | **`www.brooklynbp.nyc.gov`** | The live office site — about, initiatives, community boards, land use, newsroom, events, funding |
| Former domain | `brooklyn-usa.org` | **Gone.** Now 301-redirects offsite to `batman-news.com` |
| Open Data | `data.cityofnewyork.us` (agency `Brooklyn Borough President (BPBK)`) | 21 datasets — ULURP, appointments, awards, community boards |

## The lapsed domain (brooklyn-usa.org)

The assessment target, `brooklyn-usa.org`, no longer belongs to the office in any functional sense:

| Property | Value | Evidence |
|---|---|---|
| Behavior | `www` and apex both **301 → `https://batman-news.com/`** | `location: https://batman-news.com/`, `x-redirect-by: redirection` / `Permalink Manager` |
| Hosting | **WPX Cloud** (LiteSpeed) | `server: WPX CLOUD/ATL04`, `x-turbo-charged-by: LiteSpeed`, `wpx: 1` |
| Platform | WordPress with a **domain-flip toolkit** | `wp-json` namespaces `bm-bulker-api/v1`, `bm-geo-api/v1`, `bm-migration-api/v1`, `redirection/v1` |
| REST name | `brooklyn-usa.org` (no description) | `/wp-json/` root |

The `bm-*` (bulk-migration) namespaces plus the offsite redirect are the fingerprint of a **domain that was released and repurposed**. Whatever this domain was, it is no longer the Borough President's — a real ownership and continuity failure for a government office's public identity.

## The current site (www.brooklynbp.nyc.gov)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Cloudflare** | `server: cloudflare`, `cf-ray` |
| Hosting | **WP Engine** (managed WordPress) | `x-powered-by: WP Engine`, `x-cache`, `x-cache-group` |
| CMS | **WordPress** (headless) | `wp-json/wp/v2` live; `wp-content` refs; robots.txt disallows only `/wp-admin/` |
| Front end | **Next.js** | `_next/…` bundles in the rendered HTML |
| Events | **The Events Calendar** (Tribe) plugin | `wp-json/tribe/events/v1`, `tribe_events` / `tribe_venue` / `tribe_organizer` post types |
| Analytics / security | wp-statistics, **Wordfence**, MetaSlider | `wp-json` namespaces `wp-statistics/v2`, `wordfence/v1`, `metaslider/v1` |

This is a **modern but generic** stack — a commercially hosted headless WordPress with a Next.js skin. It is not a Borough-President-specific platform, and everything BP-specific (ULURP, appointments, funding) is authored as ordinary WordPress pages/posts, not as structured resources.

## APIs that fall out of the stack

Because it is WordPress, the site exposes machine-readable APIs **by accident of the platform**, not by design:

- **WordPress REST API** (`wp-json/wp/v2`) — 315 posts (press releases/news), 74+ pages. Public, read-only.
- **The Events Calendar REST API** (`wp-json/tribe/events/v1/events`) — the one live, purpose-shaped BP feed (hearings, borough board meetings); 6 upcoming at assessment.

Both are real and useful, but they are **CMS plumbing**, not an owned Borough President contract.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, service layer locked in a vendor CRM → *unlock*.
- **Brooklyn BP** = a thin office with real-but-scattered open data (21 Socrata IDs) + a generic CMS API + a **lapsed domain**, structurally identical to four other Borough Presidents → **template** one shared BP API across all five boroughs.

## Modernization implications

1. **The gap is ownership and shape, not raw availability.** The data exists (21 datasets, a live events feed) — but as 21 single-purpose Socrata IDs and generic WordPress objects, with no owned contract and a lapsed vanity domain.
2. **Template, don't rebuild five times.** All five Borough Presidents wield the same powers (ULURP advice, board appointments, discretionary funding, community-board coordination). One [OpenAPI](openapi/brooklynbp.yaml) contract + [MCP artifact](mcp/brooklynbp-mcp.json) should be defined once and instantiated per borough.
3. **Add the one missing write path.** The office's most consequential yearly constituent action — **applying to serve on a community board** — has no machine-readable surface at all; today it is an unstructured web form.
4. **Re-establishing and holding the office's own web identity** (rather than letting a `.org` lapse into a domain-flip) is itself part of the modernization.
