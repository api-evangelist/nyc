# Technology & Vendor Inventory — SBS

What the NYC Department of Small Business Services' public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). SBS is a **split domain**: an informational site on the shared NYC.gov platform, and a business **service portal — MyCity Business** (`nyc-business.nyc.gov`) that hosts the Step-by-Step licensing wizard and the certification/enrollment flows.

## Two front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/sbs/` | About, programs, "how do I…", forms — content only |
| **MyCity Business** | **`nyc-business.nyc.gov/nycbusiness/`** | The transactional layer: the **Step-by-Step** licensing wizard, business/incentive lookups, and the M/WBE **certification** and Workforce1 **enrollment** flows |

## Informational site (nyc.gov/site/sbs)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed`, `server-timing: cdn-cache; desc=HIT`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid` |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — it is not an SBS-specific stack. SBS's distinct technology is the MyCity Business portal.

## MyCity Business — the important part

The business service layer is **not** on NYC.gov content pages. `www.nyc.gov/nycbusiness` 301-redirects to a separate application host running a stateful Java portal:

| Property | Value | Evidence |
|---|---|---|
| Host | `nyc-business.nyc.gov` | 301 from `nyc.gov/nycbusiness` → `/nycbusiness/` |
| Product | **MyCity Business** (NYC's rebrand of "NYC Business" / Business Express) | `<title>MyCity Business</title>` |
| Session framework | **Spring Session (Java)** | `Set-Cookie: SESSION=…; Path=/nycbusiness; HttpOnly; SameSite=None` (Base64 session id) |
| Content authoring | **Adobe Experience Manager** (Universal Editor) | `src="https://universal-editor-service.adobe.io/cors.js"` |
| Front-end | server-rendered + **jQuery 3.7.1**, **Handlebars**, Colorbox, Toastify | `/nycbusiness/static/js/libs/jquery-3.7.1.js`, `handlebars.js` |
| Monitoring | **Dynatrace RUM** + **Akamai mPulse / Boomerang** | `ruxitagentjs…`, `dtCookie`, `go-mpulse.net` boomerang snippet |
| **Step-by-Step wizard** | stateful licensing/permit questionnaire | `/nycbusiness/wizard` returns `<title>Step by Step</title>` |

There is **no documented API, no OpenAPI, no JSON endpoint** — MyCity Business is a session-gated, server-rendered Spring/AEM application. The **Step-by-Step wizard** (which licenses and permits does *my* business need?), the eligibility/incentive lookups, and the M/WBE **certification** and Workforce1 **enrollment** flows are all reachable only by a human in a browser.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data wide open, but the resident service layer locked in an Oracle Siebel CRM → *unlock*.
- **SBS** = program data reasonably open (28 datasets), but the agency's **guidance and eligibility engine** — the Step-by-Step wizard, certification, and enrollment — locked inside a stateful Spring/AEM portal with no API → **navigate**.

## Modernization implications

1. **The gap is guidance and transactions, not directory data.** SBS already publishes its certified businesses, BIDs, Workforce1 events, service centers, and incentive rolls generously. What has no machine-readable surface is what makes SBS SBS: *routing* a business to the right license, the right incentive, and through certification.
2. **Front MyCity Business with an owned API.** A modern SBS API ([OpenAPI](openapi/sbs.yaml)) should present the open program data as clean resources *and* expose the portal's core write workflow — submitting an M/WBE **certification application** — instead of leaving owners to a session-bound wizard.
3. **A stateful vendor-authored portal for the city's front door to small business is a governance and accessibility risk.** An agent-native contract in front of it ([MCP artifact](mcp/sbs-mcp.json)) is the low-hanging fruit.
