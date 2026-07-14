# Technology & Vendor Inventory — MOCJ

What the NYC Mayor's Office of Criminal Justice's public surfaces are built on and which third parties they depend on — fingerprinted from response headers, page markup, and the WordPress REST API during the crawl (2026-07-13). MOCJ is a **split domain**: a thin informational stub on the shared NYC.gov platform, and the real office site running **WordPress on WP Engine behind Cloudflare**.

## Two front doors

| Surface | URL | What it does |
|---|---|---|
| Informational stub | `www.nyc.gov/site/criminaljustice/` | A near-empty shell on the NYC.gov chassis — most subpages 404 |
| **The real office site** | **`criminaljustice.cityofnewyork.us`** | Programs, System Data, Publications, Procurement (Contract with MOCJ), News, About — the actual content |

## Informational stub (nyc.gov/site/criminaljustice)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed`, `server-timing: cdn-cache; desc=HIT`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme |
| Real-user monitoring | **Dynatrace** + **Akamai mPulse (Boomerang)** | `x-oneagent-js-injection: true`, `BOOMR` snippet, `go-mpulse.net` |

This is the **same NYC.gov chassis** every citywide agency site sits on. But for MOCJ it is only a stub — the office's actual web presence lives elsewhere.

## The real site — criminaljustice.cityofnewyork.us (the important part)

MOCJ runs its real site on a **managed WordPress** stack, not on NYC.gov:

| Property | Value | Evidence |
|---|---|---|
| CDN / edge | **Cloudflare** | `server: cloudflare`, `cf-ray`, `__cf_bm` cookie |
| Managed host | **WP Engine** | `x-powered-by: WP Engine` |
| CMS | **WordPress** | `wp-json`, `wp-content`, `wp/v2` REST namespace |
| Page builder | **Kadence** blocks + **Advanced Custom Fields (ACF)** | `kadence_*` post types, `acf` fields on posts |
| Forms | **Contact Form 7** | `contact-form-7/v1` REST namespace |
| Events | **The Events Calendar** (Tribe) | `tribe/events/v1`, `tribe_events` post type |
| SEO / analytics | **Yoast**, **Site Kit by Google** | `yoast/v1`, `<meta name="generator" content="Site Kit by Google">` |

### The accidental API

WordPress ships a REST API by default, and MOCJ's is wide open and **exposes the office's entire content model as JSON** — without anyone intending it as a product. Enumerated custom post types (`/wp-json/wp/v2/types` + `x-wp-total` counts):

| Custom post type | `wp/v2` base | Count |
|---|---|--:|
| Programs | `programs` | 26 |
| Solicitations | `solicitation` | 25 |
| Notices | `notice` | 26 |
| Reports | `reports` | 26 |
| Data Reports | `data_reports` | 109 |
| Briefs & Fact Sheets | `briefs` | 54 |
| Data Stories | `data_stories` | 6 |
| Team | `team` | 92 |

There is **no documented API, no OpenAPI, no data product** — but the `wp/v2` endpoints return structured JSON for all of the above, and `contact-form-7/v1/.../feedback` is the only write path (a generic form-to-email).

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, resident service layer locked in a vendor CRM → *unlock*.
- **MOCJ** = a **coordination office that owns almost no data** — one stale dataset, jail numbers that belong to other agencies, and content reachable only through an *accidental* WordPress API → **route** its programs, publications, and referrals through one owned contract.

## Modernization implications

1. **The gap is ownership, not just format.** MOCJ analyzes and convenes; the numbers it is known for (jail population, re-arrest) are DOC's / NYPD's / DCJS's, published as PDF explainers with outbound links. An owned API can *aggregate and cite* those metrics rather than leave them in prose.
2. **Turn the accidental WordPress API into an intentional one.** Programs, publications, and solicitations already return JSON via `wp/v2` — an [OpenAPI](openapi/mocj.yaml) makes that a real, documented resource model instead of an undocumented plugin default.
3. **Give the coordination role a write surface.** The office's core function — routing a person or case to a program — has no API. The net-new `POST /program-referrals` ([schema](schemas/program-referral.json)) makes that machine-readable, with the caution that referral data is sensitive and must be authenticated, consented, and minimized.
4. **An agent-native contract** ([MCP artifact](mcp/mocj-mcp.json)) so an agent can answer "which reentry programs serve the Bronx at Intercept 5?" and — the point — "refer this client to a supervised-release program."
