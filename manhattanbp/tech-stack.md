# Technology & Vendor Inventory — Manhattan Borough President

What the Office of the Manhattan Borough President's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). The Manhattan BP runs a **single, generic WordPress site** (`manhattanbp.nyc.gov`) on managed hosting, with the office's real civic data sitting elsewhere on **NYC Open Data**.

## One front door

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.manhattanbp.nyc.gov/` | About BP Brad Hoylman-Sigal, community boards, land use, funding, policy, news, and forms — content + web forms |
| Open Data (offsite) | `data.cityofnewyork.us` (agency `Manhattan Borough President (MBPO)`) | 21 datasets — ULURP, appointments, funding awards, constituent services, community-board leadership |

## Informational site (manhattanbp.nyc.gov)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Cloudflare** | `server: cloudflare`, `cf-ray`, `cf-cache-status`, `__cf_bm` cookie, `alt-svc: h3` |
| Managed hosting | **WP Engine** | `x-powered-by: WP Engine`, `x-cache-group`, `wpe/cache-plugin` + `wpe_sign_on_plugin` REST namespaces |
| CMS | **WordPress** | `link: .../wp-json/`, `rel=shortlink`, `wp-content/...` asset paths |
| Theme | **Divi (Elegant Themes)** + `divi-child` | `wp-content/themes/Divi`, `wp-content/themes/divi-child`, `divi/v1` REST namespace, numerous `divi-*` plugins |
| Forms | **Forminator** (WPMU DEV) | `forminator/v1` REST namespace |
| Analytics / SEO | **Google Site Kit**, GTranslate | `generator: Site Kit by Google 1.168.0`, `gtranslate` plugin |
| Security headers | `x-frame-options: sameorigin`, `x-content-type-options: nosniff`, HSTS, permissions-policy | response headers |

This is an **off-the-shelf WordPress/Divi build** — a marketing theme plus a stack of Divi add-on plugins (`divi-machine`, `divi-modules-pro`, `dp-divi-filtergrid`, `supreme-modules-pro-for-divi`, `chi-divi-accordions`) and a form plugin. It is not a purpose-built civic platform, and it is **not** the shared NYC.gov "Livesite" chassis that agencies like NYCHA use — even though it lives under an `nyc.gov` hostname.

## The "API" is just default WordPress

The site does expose an API surface, but only the **generic WordPress REST API** (`/wp-json/wp/v2/…`) plus plugin namespaces (`forminator/v1`, `divi/v1`, `redirection/v1`, `google-site-kit/v1`, `wp-smush/v1`). That publishes pages/posts as JSON, but there is **no purpose-built API** for the office's actual work: ULURP recommendations, appointments, funding awards, or applying to serve on a community board. The community-board application is a **Forminator web form** (or a downloadable PDF), with no machine-readable contract.

## The five-borough finding

All five borough presidents run **near-identical thin sites** and publish the **same shapes of data** under parallel Socrata agency labels (`Manhattan Borough President (MBPO)`, `Brooklyn Borough President (BPBK)`, `Bronx Borough President (BPBX)`, `Queens Borough President (QBP)`, `Staten Island Borough President (BPSI)`). Each maintains its own WordPress-class site and its own scatter of per-year datasets. That is five parallel builds of the same civic office — a candidate for **one federated Borough President API standard**, deployed per office, rather than five one-off sites.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, service layer locked in a vendor CRM → *unlock*.
- **Manhattan BP** = data already open but fragmented into per-year datasets, site is a generic WordPress/Divi template, and the office is one of **five identical offices** → **federate** into one shared Borough President API.

## Modernization implications

1. **The gap is coherence and ownership, not raw openness.** The office publishes 21 datasets, but as one-off assets per program per fiscal year (Capital Grant Awards 2014, 2015, 2016, 2017, 2018 are five separate datasets). One owned API ([OpenAPI](openapi/manhattanbp.yaml)) should present a single `FundingAward` resource, not force a consumer to union five Socrata IDs.
2. **Give the flagship citizen action an API.** Applying to serve on a community board is the office's most public transaction; today it is a WordPress/Forminator form with no contract. That is the net-new write surface.
3. **Build once for five offices.** Because all five borough presidents are structurally the same, the API and MCP artifact here ([mcp/manhattanbp-mcp.json](mcp/manhattanbp-mcp.json)) are written to be federated across every BP office, not rebuilt five times.
