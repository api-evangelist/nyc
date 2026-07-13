# Technology & Vendor Inventory — HRA / DSS

What the NYC Human Resources Administration / Department of Social Services' public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). HRA is a **three-surface benefits domain**: an informational NYC.gov site, the **ACCESS NYC** eligibility screener (open-source), and the **ACCESS HRA** application portal (a React SPA with no API).

## Three front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/hra/` | Help pages, program info, locations, forms — content only |
| **ACCESS NYC** (screener) | **`access.nyc.gov`** | Screen a household against ~30+ NYC benefits; program catalog. Open source |
| **ACCESS HRA** (portal) | **`a069-access.nyc.gov/accesshra`** | The transactional layer: apply for SNAP / Cash Assistance / Medicaid, upload documents, view case status |

## Informational site (nyc.gov/site/hra)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed`, `server-timing: cdn-cache; desc=HIT`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid` |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — it is not HRA-specific. HRA's distinct technology is the two benefits apps.

## ACCESS NYC — the open-source screener

| Property | Value | Evidence |
|---|---|---|
| Host | `access.nyc.gov` | crawl |
| CDN / edge | **Cloudflare** | `server: cloudflare`, `__cf_bm` cookie |
| Hosting / CMS | **WordPress on WP Engine** | `x-powered-by: WP Engine`; `wp-content/themes/access/…` markup |
| Eligibility logic | **Open source — Drools business rules** | `github.com/NYCOpportunity/ACCESS-NYC-Rules` — "The Drools Business Engine rules governing the ACCESS NYC eligibility screener at access.nyc.gov/eligibility"; companion `benefits-screening-api` (2025 replatform) |
| Program metadata | **NYC Benefits Platform** | published as Open Data `kvhd-5fmu` (Mayor's Office for Economic Opportunity) — the same catalog the screener renders |

This is the domain's most unusual asset: the **eligibility rules are public and city-owned**. What is missing is a *hosted* eligibility API — the screener returns HTML, not a machine-readable determination.

## ACCESS HRA — the application portal (the locked part)

The resident transaction layer is **not** on NYC.gov and **not** open. It is a separate host running a single-page app:

| Property | Value | Evidence |
|---|---|---|
| Host | `a069-access.nyc.gov` | `nyc.gov/accesshra` redirect target |
| Application path | `/accesshra/` | React app manifest at `/accesshra/manifest.json` |
| Product | **Custom React SPA** | `<title>React App</title>`, `<meta name="description">…apply for benefit programs, and view case information online`, `/accesshra/favicon.ico` |
| Edge / bot protection | **Akamai Bot Manager** | `_abck`, `bm_sz` cookies |
| Requirement | JavaScript-only, session-gated | SPA shell; login-walled |

There is **no documented API, no OpenAPI, no JSON endpoint** for applying or checking a case. Every resident transaction (apply, upload documents, check status) is trapped inside the React client or an in-person visit to a Benefits Access / SNAP Center.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data wide open, service layer locked in a vendor CRM → *unlock*.
- **HRA** = caseload data open **and** the eligibility engine open-sourced, but nothing binds the screener, the rules, and the closed application step together → **connect the benefits journey**.

## Modernization implications

1. **The gap is the connective API, not the data or the logic.** HRA already publishes caseloads and directories generously, and ACCESS NYC's eligibility rules are already open source. What has no machine-readable contract is the *journey*: screen → determine eligibility → apply → track a case.
2. **Expose the open rules as an endpoint.** The ACCESS NYC Drools rules are public; wrapping them as `POST /eligibility` ([OpenAPI](openapi/hra.yaml)) is low-hanging — the hard part (the rules) is done.
3. **Front the ACCESS HRA portal with an owned API.** A modern HRA API should present programs/centers/caseloads as clean resources *and* expose the core write workflow — submitting a **benefits application** — instead of leaving residents to a JavaScript-only React portal or a wait at a center.
4. **An agent-native contract** in front of all three surfaces ([MCP artifact](mcp/hra-mcp.json)) is the payoff: one place to ask "what do I qualify for, where do I apply, and what's the status of my case?"
