# Technology & Vendor Inventory — Bronx District Attorney

What the Office of the Bronx District Attorney's public surface is built on and which third parties it depends on — fingerprinted from response headers and page markup during the crawl (2026-07-13). The short version: it is a **legacy NYC.gov `/html/` SHTML site** — not the modern shared "Livesite" platform — and its only quantitative data lives inside **Microsoft Power BI (Gov)** iframes.

## One front door

| Surface | URL | What it does |
|---|---|---|
| Public site | `www.bronxda.nyc.gov` → `/html/home/home.shtml` | Everything: about, bureaus, careers, newsroom/press releases, outreach, data dashboards, contact, FOIL |

The bare domain (`/`) is a 5 KB **meta-refresh** stub that redirects to `/html/home/home.shtml` — the tell-tale signature of the old hand-built NYC.gov `/html/` sites (the same family as NYC Parks), not the newer `/site/<agency>/…page` Livesite chassis.

## Public site (bronxda.nyc.gov)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `server-timing: ak_p; desc=...`, `x-akamai`-style RUM (`ak.*` BOOMR vars), `alt-svc: h3` |
| Origin load balancer | **AWS Application Load Balancer** | `set-cookie: AWSALB=…`, `AWSALBCORS=…` |
| Page technology | **Server-Side Includes (.shtml)** + JavaScript-built nav | `.shtml` extension throughout; `SSI` markers; `js/nav-nodes.js`, `js/top-nav.js` build the menu; `jquery.min.js`, `bootstrap.min.js`, `tether.min.js` |
| Real-user monitoring | **Dynatrace** (`ruxit`) + **Akamai mPulse / Boomerang** | `x-oneagent-js-injection: true`, `x-ruxit-js-agent: true`, `ruxitagentjs_…js`; `s.go-mpulse.net` BOOMR snippet |
| Analytics / translate | **Google Analytics** + **Google Website Translator** | CSP allows `www.google-analytics.com`, `translate.google.com`, `googletagmanager.com` |
| Embedded data | **Microsoft Power BI (Government cloud)** | CSP `frame-src … https://app.powerbigov.us`; `<iframe title="Public Dash Case v9a" src="https://app.powerbigov.us/view?r=…">` on the `/html/data/` dashboards |
| Social | Twitter/X (`@BronxDAClark`), Facebook, Instagram (`@bronxdaclark`) | homepage links |
| Security headers | `x-content-type-options: nosniff`, `x-frame-options: SAMEORIGIN`, HSTS, CSP | response headers |

There is **no CMS API, no JSON, no OpenAPI, and no Open Data**. The nav is the only structured artifact: `nav-nodes.js` is a static JavaScript sitemap of every `.shtml` page.

## The Power BI trap

The office's `/html/data/` section — Dashboards, Case Decision Points / Case Outcomes, Arrests, Defendant Demographics, a Data & Legal Glossary, plus "Data, Facts & Insights" and "Data Stories" narrative pages — is the **only** place it publishes numbers. Every one is a **Power BI (Gov)** report embedded in an `<iframe>` (report label "Public Dash Case v9a"). That means:

- the figures are **rendered pixels**, not data — no CSV/JSON download, no query URL, no Open Data twin;
- they cannot be diffed, charted, or reconciled by anyone outside the office;
- the office's most valuable public asset (aggregate prosecution outcomes) depends wholly on a **Microsoft vendor SaaS** with no owned data layer beneath it.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **NYCHA** = reference data open, service layer locked in Oracle Siebel → *unlock*.
- **Bronx Borough President** = thin brochure site on a Revize vendor CMS, two datasets → *templatize*.
- **Bronx DA** = a **legacy .shtml site with no API and zero Open Data**, whose only data is trapped in **Power BI iframes**, and which is **one of five structurally identical borough DA offices** → **standardize**: publish a first data + API layer once, as a shared District Attorney API.

## Modernization implications

1. **There is no data layer to speak of — build one.** The first move is not "publish more datasets," it is publishing *anything* machine-readable: press releases as a feed, the Power BI figures as `CaseStatistic` records, bureaus/programs/resources as directories.
2. **Get the numbers out of the iframe.** The aggregate prosecution data already exists in a form the office maintains (Power BI); exposing it as `/case-statistics` ([OpenAPI](openapi/bronxda.yaml)) is low-hanging fruit and a transparency win.
3. **Add the one net-new write workflow** — `submit_tip` for tips, Civilian Complaint Unit complaints, and FOIL requests, replacing a phone number and a shared mailbox with a trackable intake.
4. **Do it once for five offices.** Manhattan, Brooklyn (Kings), Queens, and Staten Island (Richmond) DAs run the same functions; a shared, agent-native contract ([MCP artifact](mcp/bronxda-mcp.json)) is the real low-hanging fruit, not a bespoke Bronx build.
