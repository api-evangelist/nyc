# Technology & Vendor Inventory — NYCHA

What the New York City Housing Authority's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). NYCHA is a **split domain**: an informational site on the shared NYC.gov platform, and a resident **service portal running Oracle Siebel CRM**.

## Two front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/nycha/` | About, developments, news, forms, "how do I…" — content only |
| **Self Service Portal** | **`selfserve.nycha.info/nycha/app/eservice/enu`** | The transactional layer: rent payment, annual recertification, application/waitlist status, and repair **work orders** |

## Informational site (nyc.gov/site/nycha)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed`, `server-timing: cdn-cache; desc=HIT`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid` |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — it is not a NYCHA-specific stack. NYCHA's distinct technology is the portal.

## Self Service Portal — the important part

The resident service layer is **not** on NYC.gov. It is a separate host running a packaged CRM:

| Property | Value | Evidence |
|---|---|---|
| Host | `selfserve.nycha.info` | redirect landing page |
| Application path | `/nycha/app/eservice/enu` | `enu` = English-US locale segment |
| Product | **Oracle Siebel Customer Relationship Management** | `<title>Oracle - Siebel Customer Relationship Management</title>`, `OracleSiebel_logo.gif`, `SWECmd=Start`, `SWEHo` host param |
| UI framework | Siebel Open UI (SWE — Siebel Web Engine) | `SWECmd`, `start.swe` command routing |
| Requirement | JavaScript-only, session-gated | `<noscript>` "requires JavaScript"; login-walled |

There is **no documented API, no OpenAPI, no JSON endpoint** — the portal is a server-rendered Siebel Open UI application. Every resident transaction (pay rent, recertify, check application status, report a repair) is trapped behind SWE commands, reachable only by a human in a browser or a phone call to the Customer Contact Center.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data already **wide open** on Open Data (24 datasets), but the **resident service layer locked inside a vendor CRM** (Oracle Siebel) with no API → **unlock the transaction layer**.

## Modernization implications

1. **The gap is transactions, not data.** NYCHA already publishes its physical stock, utilities, and demographics generously. What has no machine-readable surface is what residents actually *do*: pay, recertify, apply, and — most of all — **report repairs**.
2. **Front the Siebel portal with an owned API.** A modern NYCHA API ([OpenAPI](openapi/nycha.yaml)) should present developments/addresses/facilities/utilities as clean resources *and* expose the portal's core write workflow — creating a **work order** — instead of leaving residents to a JavaScript-only Siebel screen or a phone queue.
3. **Depending on a packaged CRM for the city's largest landlord–tenant relationship is a governance and accessibility risk.** An agent-native contract in front of it ([MCP artifact](mcp/nycha-mcp.json)) is the low-hanging fruit.
