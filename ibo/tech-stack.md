# Technology & Vendor Inventory — IBO

What the New York City Independent Budget Office's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). IBO is a **reference / analysis agency** (NYC's nonpartisan budget watchdog), and its site is a **client-side SPA on the NYC.gov "Content API v2" platform** — a different NYC.gov chassis than NYCHA's "Livesite".

## The domain move — a finding in itself

| Surface | URL | What happens |
|---|---|---|
| Legacy own domain | `www.ibo.nyc.ny.us` | **301 → `https://www.ibo.nyc.gov/`** |
| Current site | `www.ibo.nyc.gov/content/` | The SPA (Apache 301 from `/` → `/content/`) |

IBO once had its **own `.ny.us` domain**. It now permanently redirects onto `nyc.gov`. The "Independent" Budget Office has folded its public identity into the shared city chassis — worth noting for an agency whose entire brand is independence from the administration it analyzes.

## The site is a Single-Page Application

Every path — `/content/publications`, `/content/ask-ibo`, `/content/budget-101`, anything — returns the **same 36 KB HTML shell**. There is no server-rendered content. A jQuery/Bootstrap "content-loader" fetches the real content client-side from a JSON API.

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `server-timing: ak_p; desc=...`, `server-timing: edge; dur=...`, `alt-svc` |
| Web server | **nginx** (origin), Apache (legacy redirect host) | `server: nginx` on 404s; `Server: Apache` on the `.ny.us` 301 |
| Front-end platform | **NYC.gov "Content API v2"** SPA | `content-loader.js`, `content-config.js`, `nav-template.js`, `publications-filter.js` under `/assets/*/js/content-api/` |
| UI libraries | **jQuery 3.3.1 + Bootstrap 4.3.1** (+ jQuery UI, Popper, Colorbox) | `<script src=".../libs/jquery-3.3.1.min.js">` etc. |
| Real-user monitoring | **Dynatrace** (ruxit) | `x-oneagent-js-injection: true`, `x-ruxit-js-agent: true`, `ruxitagentjs_*.js` |
| Web analytics | **WebTrends** | `webtrends_v10.js` |
| On-site search | **Google Custom Search / AdSense CSE** | CSP `frame-src https://www.adsensecustomsearchads.com`, `cse.google.com` |
| Translation | **Google Translate** widget | `translate.google.com/translate_a/element.js` |
| Security headers | `x-frame-options: SAMEORIGIN`, `x-content-type-options: nosniff`, HSTS preload, detailed CSP | response headers |

## The content backend — the important part

The SPA is fed by a **real, public JSON API** on the shared NYC.gov application host:

| Property | Value | Evidence |
|---|---|---|
| Host | `apps.nyc.gov` | referenced in `publications-filter.js` |
| Content endpoint | `/content-api/v2/custom-contents/{site}/{path}` | e.g. `/custom-contents/ibo/IBO-Publications/1` |
| Nav endpoint | `/content-api/v2/nav/{site}` | e.g. `/nav/ibo` returns the site tree |
| Payload | `application/json;charset=utf-8` | ~1,145 publications with structured `values[]` metadata |
| Contract | **none** | no OpenAPI, no versioned consumer docs, undocumented; a page-rendering backend, not a published API |

The publication records carry real structure: `Title`, `Publication Date`, `Description`, `Topics`, `Publication Type` (Report / Interactive / Testimony / Letter / Press Release / Budget Options / Explainer / Dataset), `Fiscal Year`, `Author`, and `Content Link`. This is a genuine machine-readable API hiding behind a client-side site.

## Data & visualization vendors

IBO's interactives and maps are **outsourced**, embedded via the CSP `frame-src` allow-list:

- **ArcGIS Online** — `ibomap.maps.arcgis.com` (map interactives)
- **Airtable** — `airtable.com` (interactive data tables)
- **Infogram** — `e.infogram.com` (charts/infographics)

Its bulk data lives on **NYC Open Data / Socrata** (20 datasets) — see [opendata-ibo.md](opendata-ibo.md).

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, service layer locked in a vendor CRM → *unlock*.
- **IBO** = the content API and the datasets **already exist**, but neither is documented, versioned, or agent-native, and the wide fiscal tables are Excel-shaped → **formalize**.

## Modernization implications

1. **There is already an API — publish a contract over it.** `apps.nyc.gov/content-api/v2` returns IBO's ~1,145 publications as JSON today. The work is a documented, versioned, filterable [OpenAPI](openapi/ibo.yaml) surface (by topic, type, fiscal year), not building a backend from scratch.
2. **Pivot the wide tables.** IBO's Socrata datasets are one-column-per-fiscal-year. Republish them as long-form `(series, lineItem, fiscalYear, value)` observations so a consumer or agent can ask "capital expenditures by purpose for FY 2015" without reshaping a spreadsheet.
3. **Give the one citizen transaction an API.** IBO has no payments/permits/applications; its single interactive input is **Ask IBO**, today a form/email. An owned `POST /data-requests` — plus an [MCP artifact](mcp/ibo-mcp.json) so an agent can ask IBO a fiscal question — is the net-new write surface.
