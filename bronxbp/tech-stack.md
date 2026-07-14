# Technology & Vendor Inventory — Bronx Borough President

What the Office of the Bronx Borough President's public surface is built on and which third parties it depends on — fingerprinted from response headers and page markup during the crawl (2026-07-13). Unlike the citywide agencies, this office is **not** on the shared NYC.gov "Livesite" platform: it runs a **Revize government SaaS CMS** on its own host.

## One front door

| Surface | URL | What it does |
|---|---|---|
| Informational site | `bronxboropres.nyc.gov` | About, newsroom, services (ULURP, budget, constituent services), community boards, events, contact — content only |

There is no separate transactional portal. `nyc.gov/site/bronxbp` returns **404** — the office is not on the shared city chassis.

## The stack

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| Hosting | **Oracle Cloud Infrastructure** | `bronxboropres.nyc.gov` resolves to `129.153.208.86` (OCI range); `Server: nginx`, `X-Request-Id`, AWSALB cookies on some responses |
| CMS platform | **Revize** (government SaaS CMS) | `og:image` → `cms2.revize.com/revize/officeofthebronxboroughpresident/...`; `/revize/plugins/...`; `RZ.*` JS globals; `RZ.revizeserverurl = https://cms2.revize.com/revize/officeofthebronxboroughpresident` |
| Front end | **PHP** page templates | `index.php`, `news_detail_T4_R<n>.php`, `calendar.php`, `newslist.php`; Revize `document_center` template (`RZ.pagetemplatename='document_center'`) |
| CMS admin | **Revize JSP back end** | login at `cms2.revize.com/revize/security/index.jsp?webspace=officeofthebronxboroughpresident` |
| UI framework | **Bootstrap 4.6** + **jQuery 3.7.1** | `cdn.jsdelivr.net/npm/bootstrap@4.6.0`, `code.jquery.com/jquery-3.7.1.js` |
| Calendar | **Revize calendar plugin over Google Calendar** | `/revize/plugins/revize_calendar/google-calendar/main.min.js`; `ImportCals = ["1","2"]` → calendars named `Events` and `Meetings` |
| Documents | **Revize document center** | ULURP page carries 315 `document_center` references and 40+ `.pdf` links |
| Social wall | **Curator.io** | `cdn.curator.io/published/....js` |
| Newsletter | **Constant Contact** | `visitor.r20.constantcontact.com` (the "Subscribe for eNotifications" / `enotify` flow) |
| Accessibility | **UserWay** | `cdn.userway.org`, `userway.org` overlay widget |
| Analytics | **Google Tag Manager / GA4** | `googletagmanager.com`, GA4 measurement id `G-DMD6JC0H5S` |
| Security headers | `Content-Security-Policy: frame-ancestors 'self'`, `X-Frame-Options: SAMEORIGIN`, `X-Content-Type-Options: nosniff` | response headers |

There is **no documented API, no OpenAPI, no JSON endpoint**. Every page is server-rendered by Revize; the two structured things the office publishes live off-site on **NYC Open Data**, and events live in **Google Calendar**.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy Smarty/PHP platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, resident service layer locked in a vendor CRM → *unlock*.
- **Bronx BP** = a **thin brochure site on a vendor SaaS CMS** (Revize) where almost nothing is machine-readable — and where the office is **structurally identical to four other Borough Presidents** → **templatize into one shared Borough President API.**

## Modernization implications

1. **The office produces charter work, not data.** Its outputs — ULURP recommendations, community-board appointments, discretionary funding, testimony — are real and consequential, but only two of them (funding, appointments) are machine-readable, and those only because someone published them to Socrata by hand.
2. **The CMS is the ceiling.** Recommendations are PDFs in a document center, the newsroom is PHP pages, events are a borrowed Google Calendar. A modern [OpenAPI](openapi/bronxbp.yaml) would give each of these an owned, machine-readable shape and add the one inbound workflow that is missing entirely: **applying to serve on a community board**.
3. **Do not build this five times.** All five Borough President offices share the same NYC Charter duties and run near-identical thin sites on assorted vendor CMSes. The low-hanging fruit is **one shared, templatable Borough President API** ([MCP artifact](mcp/bronxbp-mcp.json)) instantiated per borough — not five bespoke modernizations.
