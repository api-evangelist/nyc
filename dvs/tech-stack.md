# Technology & Vendor Inventory — DVS

What the NYC Department of Veterans' Services' public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). DVS is a **connective agency with a vendor service layer**: an informational site on the shared NYC.gov platform, and a resident **care-coordination intake (VetConnectNYC) that runs on a third-party platform, Combined Arms**.

## Two front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/veterans/` | About, services (housing, benefits, VA claims, health, employment, food, legal, women/senior veterans), initiatives, resource directory — content only |
| **VetConnectNYC intake** | **`nyc.veteranportal.combinedarms.us`** | The transactional layer: a veteran fills out the **VetConnectNYC Request Form** to be connected to services; **DVS Care Coordinators** receive all requests and process them within **3–5 business days** |

## Informational site (nyc.gov/site/veterans)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed: 9 …pmb=mRUM`, `server-timing: cdn-cache; desc=HIT`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid` |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — it is not a DVS-specific stack. DVS's distinct technology is what it points veterans to: VetConnectNYC.

## VetConnectNYC — the important part

The care-coordination service layer is **not** on NYC.gov and is **not** DVS-built. It is a separate host running a packaged veteran-services platform:

| Property | Value | Evidence |
|---|---|---|
| Host | `nyc.veteranportal.combinedarms.us` | link target on `nyc.gov/site/veterans/services/services.page` |
| Product | **Combined Arms "Military Resource Portal"** | `<title>CA - Military Resource Portal</title>` |
| Vendor | **Combined Arms** (`combinedarms.us`) — a veteran-services network platform | title + host domain |
| Framework | **Next.js** on **AWS CloudFront** | `x-powered-by: Next.js`, `via: … cloudfront.net`, `x-amz-cf-id`, `__next`/`react` markup |
| Requirement | JavaScript app, login/registration | React SPA; account-gated request form |

> **Verification note / honest correction.** The assignment hinted VetConnectNYC was "likely the Unite Us platform." It is **not** — the crawl resolves VetConnectNYC to **Combined Arms**, a different veteran-focused coordinated-care vendor. The intake is a **vendor web form**, not an integration DVS operates: there is **no documented API, no OpenAPI, no JSON endpoint** exposed, and the hand-off to DVS Care Coordinators is a manual 3–5 business-day queue.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data wide open, service layer locked in a vendor CRM (Oracle Siebel) → *unlock*.
- **DFTA** = provider network open, service layer is a phone contact center (Aging Connect) → *connect*.
- **DVS** = reference **and de-identified service data** open, but the live care-coordination referral runs on a **third-party vendor portal** (Combined Arms / VetConnectNYC) with no API → **coordinate** (own the referral).

## Modernization implications

1. **The gap is the live referral, not the data.** DVS is remarkably open — it publishes not only its resource directory but de-identified assistance requests, cases, and client demographics. What has no machine-readable surface is what a veteran actually *does*: submit a VetConnectNYC request and get connected to care.
2. **Own the coordination.** A modern DVS API ([OpenAPI](openapi/dvs.yaml)) should present the Resource Map, Veteran Owned Businesses, assistance requests, cases, and aggregate client stats as clean resources *and* expose the one net-new **write** workflow — creating a **ServiceReferral** — instead of routing veterans into a third-party form and a multi-day manual queue.
3. **Depending on an out-of-city vendor for the veteran's first point of contact is a governance and continuity risk.** An agent-native contract in front of it ([MCP artifact](mcp/dvs-mcp.json)) is the low-hanging fruit — so an agent can make and track a referral on a veteran's behalf.
