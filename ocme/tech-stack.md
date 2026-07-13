# Technology & Vendor Inventory — OCME

What the NYC Office of Chief Medical Examiner's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). OCME has **almost no digital surface of its own**: an informational site on the shared NYC.gov platform, and a service layer that is not an application at all but **paper forms plus NYC 311**.

## One front door, and it is only informational

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/ocme/` | About, forensic services, reporting-a-case guidance, records-request instructions, family services centers, FAQ, NamUs — **content only** |
| Records / service channel | `portal.311.nyc.gov` + paper (notarized) forms | The transactional layer: requesting a decedent's casefile record. **Not an OCME system** — the citywide 311 request portal and mailed forms |

Unlike NYCHA — which at least ran a dedicated resident CRM (Oracle Siebel) — OCME has **no agency-specific application at all**. There is no portal, no login, no CRM to fingerprint. The "system" behind a records request is a PDF, a notary, and a 311 case.

## Informational site (nyc.gov/site/ocme)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed`, `alt-svc: h3`, `server-timing: ak_p` |
| Web server | **nginx** | `server: nginx` |
| App tier / load balancing | **AWS ALB** | `set-cookie: AWSALB`, `AWSALBCORS` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `dtCookie`, `server-timing: dtSInfo/dtRpid` |
| Session | Java servlet container | `JSESSIONID` cookie |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on (identical to what NYCHA's informational site runs on) — it is not an OCME-specific stack. OCME's distinguishing technology fact is the *absence* of anything else.

## The service layer — paper and 311

The things a bereaved family or an authorized agency actually needs to *do* have **no application** behind them:

| Property | Value | Evidence |
|---|---|---|
| Records-request channel | Paper form → notarization (for third-party delivery) → mail; NYC **311** for questions/tracking | `records-requests.page` instructions; every service page links to `portal.311.nyc.gov` |
| Turnaround | **Three to six months or more**, pending case finalization | stated on the records-requests page |
| Missing persons / identification | Federal **NamUs** (`namus.nij.ojp.gov`) + OCME Identification Unit (phone `212-447-2030`) | `for-families/namus.page`, `family-services-centers.page` |
| Death **certificates** (distinct) | Issued by **DOHMH** (Health), not OCME | out of scope for OCME; a common point of confusion |

There is **no documented API, no OpenAPI, no JSON endpoint, and no portal** — because there is no application to expose one. The core object, a **death investigation**, is confidential and is never published, even in aggregate.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, resident service layer locked in a vendor CRM → *unlock*.
- **OCME** = essentially **no published data and no application at all**, over a domain that is also the most privacy-constrained → **instrument** it — carefully.

## Modernization implications

1. **The gap is almost total, and that is the point.** OCME publishes one stale MMR dataset and runs zero owned applications. It is the least-instrumented agency assessed.
2. **Instrument respectfully, not maximally.** The move is *not* to publish casework. It is to (a) publish the small set of things that can responsibly be public — performance indicators, AGGREGATE case statistics, the service catalog, family services centers, NamUs listings — as one clean [OpenAPI](openapi/ocme.yaml), and (b) give families **one dignified write path**: request a decedent's casefile record ([DeathRecordRequest](schemas/death-record-request.json)) instead of a notarized PDF and a six-month wait.
3. **Privacy is a first-class design constraint.** No per-decedent record, no cause-of-death against an individual, ever. The [MCP artifact](mcp/ocme-mcp.json)'s instructions encode that as agent guidance.
