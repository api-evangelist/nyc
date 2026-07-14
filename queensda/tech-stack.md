# Technology & Vendor Inventory — Queens District Attorney

What the Queens County District Attorney's public surface (`queensda.org`) is built on and which third parties it depends on — fingerprinted from response headers and page markup during the crawl (2026-07-13). Unlike the geographic agencies, Queens DA is a **single WordPress site**: prolific, multilingual, and — by accident — already serving a machine-readable API.

## One front door

| Surface | URL | What it does |
|---|---|---|
| Public site | `queensda.org` | Everything: press releases, cases, cold cases, programs, resources, victim services, careers, contact |

There is no separate portal, no login area, no transactional system. The whole office is a content site.

## Stack

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Cloudflare** | `server: cloudflare`, `cf-ray`, `cf-cache-status`, `alt-svc: h3` |
| Managed host | **Kinsta** (managed WordPress) | `x-kinsta-cache: HIT`, `ki-edge: v=28.4.4`, `ki-cf-cache-status`, `ki-origin: g1p` |
| CMS | **WordPress 7.0.1** | `<meta name="generator" content="WordPress 7.0.1">`, `x-redirect-by: WordPress`, `/wp-content/`, `/wp-json/` |
| Theme | **Divi** + a `queensdistrictattorney` child theme | `wp-content/themes/queensdistrictattorney`, `Divi` asset handles |
| Page builder | **Beaver Builder** (+ PowerPack) | `wp-content/plugins/bb-plugin`, `wp-content/themes/bb-theme`, `bbpowerpack`, `fl-builder-template`, `fl-controls/v1` REST namespace |
| Multilingual | **WPML** | `<meta name="generator" content="WPML ver:4.9.5 …">`, `sitepress-multilingual-cms`, `wpml/v1` REST namespace |
| Faceted search | **FacetWP** | `facetwp/v1/refresh`, `facetwp/v1/fetch` REST endpoints |
| Analytics (first-party) | **Matomo** (self-hosted) | `matomo/v1` REST namespace |
| Analytics/SEO (third-party) | **Google Site Kit**, **Yoast SEO** | `Site Kit by Google 1.182.0` generator, `google-site-kit/v1` + `yoast/v1` namespaces |
| Content type registry | **Toolset Types** | `wp-content/plugins/types` |
| Spam / utility | Akismet, Redirection, Simple Sitemap | `akismet/v1`, `redirection/v1`, `simple-sitemap/v1` namespaces |

`robots.txt` disallows nothing (`Disallow:` empty).

## The important part — the accidental API

The finding that separates Queens DA from the earlier domains: **the data is already machine-readable, but by accident.** WordPress ships a REST API at `/wp-json/`, and on this site it is **fully open**:

- `wp-json/wp/v2/posts` → **1,557 posts** (X-WP-Total header), paginated as JSON.
- `wp-json/wp/v2/categories` → the full prosecution/press taxonomy with counts (press-releases 1,216; court-cases 378; arraignments 131; charges 127; indictments 119; cold-cases 67; unidentified 19; identified 47; …).
- `wp-json/wp/v2/pages` → **60 pages** (programs, resources, access plans).
- `wp-json/facetwp/v1/fetch` → the site's own faceted search.

This is a real, queryable API — but it is **undesigned and uncontracted**. It exposes WordPress's internal shape (post objects, `content.rendered` HTML), not a District Attorney's domain model. There is no OpenAPI, no stable resource contract, and no guarantee it stays open; it is a side effect of the CMS, not a decision.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy Smarty/PHP platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data wide open on Open Data, service layer locked in Oracle Siebel → *unlock*.
- **Queens DA** = prolific narrative on modern WordPress, **already machine-readable by accident** (WordPress REST), **zero open data**, prosecution data only as prose → **structure it into a designed, shared contract.**

## Modernization implications

1. **The gap is structure, not access.** The bytes are reachable; the *model* is not. Cases, charges, dispositions, and cold-case facts live as HTML prose and post titles, so no one can query "unidentified males found in Flushing" or "indictments this quarter."
2. **Design a contract over the accidental API.** Put an owned OpenAPI ([openapi/queensda.yaml](openapi/queensda.yaml)) in front of the WordPress REST surface, mapping posts→`PressRelease`, lifecycle categories→`Case`, cold-case posts→`ColdCase`, and add the missing inbound **`TipSubmission`** write path.
3. **Share it across all five DAs.** Manhattan, Brooklyn, Bronx, and Staten Island DA offices run the same functions on similar stacks. The low-hanging fruit is not five accidental REST APIs — it is **one shared five-borough DA API** and an agent-native MCP layer ([mcp/queensda-mcp.json](mcp/queensda-mcp.json)).
