# Technology & Vendor Inventory — nycgovparks.org

What the NYC Parks & Recreation website is built on and which third parties it depends on — fingerprinted from response headers and page markup during the crawl (2026-07-13; backfilled for consistency with the [schools.nyc.gov](../schools.nyc.gov/tech-stack.md) inventory). Vendor lock-in and legacy platforms are as much a modernization constraint as the data itself.

## Platform & hosting

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| Web server | **nginx/1.31.1** | `server` header |
| CDN / edge | **AWS CloudFront** | `x-cache: Hit from cloudfront`, `via ... cloudfront.net` |
| Templating / CMS | **Smarty 2.6.2** (legacy PHP template engine) | `/common_files/Smarty-2.6.2/libs/templates/...`; `.php` endpoints; one `.aspx` reference |
| Front-end libs | **jQuery** (+ jquery-migrate, jquery-cookie, hoverIntent), **Select2**, **Chosen**, **Fancybox**, **Typeahead.js** | `/assets/*` script srcs — a classic jQuery-era stack |
| Image delivery | **Cloudinary** (`res.cloudinary.com`) | 5 refs |
| Icons | **Font Awesome** (`kit.fontawesome.com`) | kit script |
| Translation | **Google Translate** website widget | `translate.google.com/translate_a/element.js` |

## The Tree Map is a separate modern island

The interactive [NYC Tree Map](https://tree-map.nycgovparks.org/) is a **Next.js / React** application (served under `www.nycgovparks.org/cdn/tree/_next/static/...`) — a modern SPA bolted onto the legacy site, with its **own** Google Tag Manager container (`G-Z50SRPG57K`) and **Loggly** logging (`cloudfront.loggly.com`). It's the one place NYC Parks already built an app-grade, API-backed experience — but the API is private to the app.

## Analytics & integrations

| Capability | Vendor / Service | Notes |
|---|---|---|
| Tag management | **Google Tag Manager** | site + separate Tree Map container |
| Web analytics | **Google Analytics** (legacy `ssl.google-analytics.com`) | |
| Logging (Tree Map) | **Loggly** | SPA telemetry |
| Emergency notifications | **Notify NYC** (`a858-nycnotify.nyc.gov`) | citywide alert integration (an `aNNN-*.nyc.gov` app host) |
| Voter registration link | **NYC Votes / CFB** (`nycvotes.org`) | civic cross-link |
| Social | Instagram, YouTube, Twitter/X, LinkedIn, Facebook | |

## Contrast with schools.nyc.gov

- **Search is self-hosted here.** The site search posts to an internal `/search` endpoint — NYC Parks owns its search, unlike DOE which rents discovery from HawkSearch. (Good: less to reclaim.)
- **But the platform is older.** A Smarty/PHP + jQuery stack (with `.php` data endpoints leaking into URLs) vs. DOE's Progress Sitefinity (.NET). Modernization here is more about **replatforming the delivery layer** than untangling vendors.
- **One modern island already exists** (the Next.js Tree Map) — a proof NYC Parks can build API-backed apps; the opportunity is to generalize that pattern behind a real public API.

## Modernization implications

1. **Legacy delivery layer.** Smarty 2.6.2 (released ~2005) + jQuery renders data server-side into HTML; there's no component/API separation. A resource API (this project's [OpenAPI](openapi/nyc-parks.yaml)) is the precondition for replatforming the front end.
2. **The Tree Map shows the target state** — a modern SPA over an API. Generalize it: one Parks API, many app islands (facilities finder, events, permits), plus the MCP surface.
3. **`.php` endpoints in public URLs** (e.g. Historical Signs) are the visible edge of the legacy backend — first candidates to hide behind clean API routes.
