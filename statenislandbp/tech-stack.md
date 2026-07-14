# Technology & Vendor Inventory — Staten Island Borough President

What the Office of the Staten Island Borough President's public surface is built on — fingerprinted from response headers and page markup during the crawl (2026-07-13). The finding is short because the stack is short: this is a **Weebly brochure site behind Cloudflare**, with no application, no API, and no owned platform.

## One front door

| Surface | URL | What it does |
|---|---|---|
| Public site | `www.statenislandusa.com` | Everything — About/BP Office, news, resources, community board application, BP Assist, budget page, borough board archive, events, concerts. Content and a few embedded forms only. |

## Fingerprint

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Cloudflare** | `server: cloudflare`, `cf-ray`, `cf-cache-status`, `__cf_bm` cookie |
| Site builder / host | **Weebly** (Square) | `x-host: blu123.sf2p.intern.weebly.net`; `weebly.com/weebly/apps/anchor/weebly-anchor.js`; `weeblylink_*` classes; `/apps/search` and `/ajax/` paths in robots.txt |
| Form handling | **Weebly Forms** | Community Board application posts to `//www.weebly.com/weebly/apps/formSubmit.php` with opaque `_u…` field names and `wsite_subject` / `form_version` hidden fields |
| Email capture | **Constant Contact** | newsletter sign-up links to `lp.constantcontactpages.com/su/wWLrBxD/sibp` |
| Compatibility | `x-ua-compatible: IE=edge,chrome=1` | response header |

That is the entire stack. There is **no CMS of record, no application server, no API gateway, no JSON endpoint, no OpenAPI** — a DIY website builder rendering static pages and relaying a couple of forms to Weebly's and Constant Contact's servers.

## What the office actually does vs. what it publishes

The Borough President holds real NYC Charter powers — **advisory review of every land-use (ULURP) application, appointment of all community board members, a share of the capital and expense budget to allocate, and a monthly Borough Board**. None of that has a machine-readable home:

- **Land use** lives as PDFs/notices on the site and inside *City Planning's* ZAP system (another agency).
- **Community board appointments** are recruited through a Weebly form; there is no published roster dataset.
- **Discretionary funding** is requested "via mail or email" and surfaces only inside the adopted citywide budget (Schedule C).
- **Borough Board resolutions** are monthly PDFs on `borough-board.html`.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy Smarty/PHP platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data wide open, service layer locked in an Oracle Siebel CRM → *unlock*.
- **Staten Island BP** = a **Weebly brochure site with two trivial datasets and no API at all** — and four other borough-president offices that look exactly the same → **federate**.

## Modernization implications

1. **There is nothing to reclaim or unlock here — there is nothing built.** The work is to give the office's charter functions a first-ever data model and contract.
2. **Do not build five bespoke BP APIs.** Manhattan, Bronx, Brooklyn, Queens, and Staten Island run near-identical thin sites with identical charter roles. The right move is **one shared Borough President API** ([OpenAPI](openapi/statenislandbp.yaml)) whose `borough` field selects the office — this assessment instantiates it for Staten Island.
3. **The two things residents actually *do* deserve a contract first:** report a quality-of-life issue (BP Assist) and apply to a community board — today an opaque Weebly form. An agent-native front ([MCP artifact](mcp/statenislandbp-mcp.json)) is the low-hanging fruit.
