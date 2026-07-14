# Technology & Vendor Inventory — Staten Island DA

What the Office of the District Attorney, Richmond County's public surface is built on and which third parties it depends on — fingerprinted from response headers and a Wayback snapshot during the crawl (2026-07-13). The Staten Island DA is an **off-platform, data-dark** domain: a self-hosted WordPress marketing site on a commercial host, with no Open Data and no API.

## First, the address

The prompt's `rcda.nyc.gov` **does not resolve** — it is a dead legacy NYC.gov address (last live on the Wayback Machine around 2007). The office's real, current site is **`statenislandda.org`** (`rcda.org` is the Roman Catholic Diocese of Albany — a false friend). Everything below is that site.

## One front door

| Surface | URL | What it does |
|---|---|---|
| Marketing / comms site | `www.statenislandda.org` | About the DA and staff, "Our Efforts" programs, victim services, scam/safety info, press releases, careers, contact, and two tip forms — content and intake only |

## The stack (fingerprinted)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| Hosting / CDN | **SiteGround** (on Google Cloud) | `x-sg-cdn: 1`, `set-cookie: nevercache-…` (SG Optimizer), `x-ce: us-east4-…`, `x-proxy-cache-info` |
| Web server | **nginx** | `server: nginx` |
| **Bot protection** | **SiteGround captcha** | every request 202s and redirects to `/.well-known/sgcaptcha/?r=…` — including `robots.txt`, `sitemap.xml`, and `/wp-json` |
| CMS | **WordPress** | `wp-content/…`, `/wp-json`, `xmlrpc.php`, `wp-sitemap.xml` |
| Theme | **Themeco "Pro"** (+ `pro-child`) | `wp-content/themes/pro`, `wp-content/themes/pro-child` |
| Forms | **Contact Form 7** | `wpcf7` markup on `/drug-tip-form/`, `/scam-tip-form/`, `/contact/` |
| Sliders / grids | **Slider Revolution 7.0.14**, **Essential Grid** | `generator … Slider Revolution 7.0.14`, `wp-content/plugins/revslider`, `…/essential-grid` |
| Social feed | **Custom Twitter Feeds Pro** | `wp-content/plugins/custom-twitter-feeds-pro` |
| Accessibility | **WP Accessibility** plugin | `wp-content/plugins/wp-accessibility` |
| Translation | **Google Language Translator** | `wp-content/plugins/google-language-translator` |
| Performance | **Perfmatters** | `wp-content/plugins/perfmatters` |

This is a **commercial, self-hosted WordPress** stack — not the NYC.gov shared "Livesite" platform every citywide agency site sits on, and not on any NYC-managed infrastructure. The DA's office bought its own domain and hosting and stood up a marketing site.

## What has no machine-readable surface

- **No Open Data.** Zero Socrata datasets under any Richmond County / Staten Island DA agency label (verified via the Discovery API). See [opendata-statenislandda.md](opendata-statenislandda.md).
- **No usable API.** WordPress ships a REST API at `/wp-json`, but it is (a) undocumented, (b) not intended as a public product, and (c) unreachable behind the SiteGround captcha. There is no OpenAPI, no JSON contract.
- **Dark core data.** The office's actual work — cases prosecuted, dispositions, declinations, diversions — has no dataset, no API, and no structured public record. It lives inside an internal case-management system and reaches the public only as prose in a press release.
- **Write path without an API.** The two tip forms (`/drug-tip-form/`, `/scam-tip-form/`) are Contact Form 7 forms that email the office. No API, no confirmation number, no way to check status.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data wide open, service layer locked in a vendor CRM → *unlock*.
- **Staten Island DA** = **no data, no API, off the city platform, bot-walled** → **surface** it (and its dark case data), then share the model across all five borough DAs.

## Modernization implications

1. **The gap is everything upstream of a press release.** There is no data to consume and no contract to call. The first win is simply *publishing* — press releases, programs, victim services, and advisories as clean resources ([OpenAPI](openapi/statenislandda.yaml)).
2. **Surface the dark data — as aggregate.** Prosecutorial-transparency counts (caseloads, dispositions, diversions) are exactly what a DA should publish; propose an [aggregate, never-per-defendant schema](schemas/prosecution-statistics.json).
3. **Give the tip line an API.** Replace the Contact Form 7 email forms with a real `POST /tips` that supports anonymity and returns a trackable reference.
4. **Un-wall the content.** The SiteGround captcha makes the site inaccessible to agents and crawlers — an accessibility and discoverability problem for a public office.
5. **Build it once for five boroughs.** Every NYC DA office has the same shape; this model is deliberately generic so one shared DA API can serve all five. See [README.md](README.md).
