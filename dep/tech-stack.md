# Technology & Vendor Inventory — DEP

What the New York City Department of Environmental Protection's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). DEP is a **split domain**: an informational site on the shared NYC.gov platform, and a customer **billing/account portal running a packaged utility CIS (uMAX) on ASP.NET + Azure AD B2C**.

## Two front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/dep/` | Drinking water, wastewater, green infrastructure, permits, "how do I…" — content only |
| **My DEP Account portal** | **`a826-umax.dep.nyc.gov`** | The transactional layer: water/sewer **bill payment**, account management, service requests |

## Informational site (nyc.gov/site/dep)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed`, `server-timing: cdn-cache; desc=HIT`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid`, `dtCookie` |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on (identical to Parks, DOE, Council, NYCHA's informational surfaces) — it is not a DEP-specific stack. DEP's distinct technology is the customer portal.

## My DEP Account portal — the important part

The customer service layer is **not** on NYC.gov. It is a separate host running a packaged water-utility Customer Information System (CIS):

| Property | Value | Evidence |
|---|---|---|
| Host | `a826-umax.dep.nyc.gov` | linked from the DEP homepage (`/`, `/quickpay`) |
| Product | **uMAX** — utility CIS / billing platform (Advanced Utility Systems, a Harris company) | host name `umax`, portal title `My DEP Account`, quickpay flow |
| App framework | **ASP.NET / ASP.NET Core** | `x-powered-by: ASP.NET`, `.AspNetCore.OpenIdConnect.*` and `.AspNetCore.Correlation.*` cookies |
| Identity | **Azure AD B2C** (OIDC, MFA) | redirect to `umaxazprodb2c.b2clogin.com/.../b2c_1a_prod_signup_signin_mfa/oauth2/v2.0/authorize` |
| Hosting | **Microsoft Azure App Service** | `ARRAffinity` / `ARRAffinitySameSite` (Azure ARR) + `ASLBSA` load-balancer cookies |
| UI | JavaScript SPA, session-gated | landing `<title>Loading…</title>`, sign-in wall at `/session/signin` |

There is **no documented API, no OpenAPI, no JSON endpoint** for the account/billing workflows — the portal is a login-walled SPA behind Azure AD B2C. Paying a water bill, managing an account, and account-tied service requests are reachable only by a human in a browser (a public `/quickpay` page exists for one-off payments, but exposes no machine contract).

## The other half of the transaction layer: NYC311

Unlike NYCHA (one Siebel CRM), DEP's **service requests are split**. Street conditions — a **water-main break, no water, sewer backup, clogged catch basin, hydrant problem, or discolored water** — are funneled from the DEP site into **generic NYC311** (`portal.311.nyc.gov`), not a DEP-owned intake. DEP's own *completed* tickets surface, after the fact, as the read-only **Work Order Management Module** Open Data dataset (`4fvw-nn9c`). So there is no single place — and certainly no single API — where a resident both reports a DEP problem and tracks it.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data wide open, resident service layer locked in one vendor CRM (Oracle Siebel) → *unlock*.
- **DEP** = reference data **very** open but **sprawling and inconsistently typed** (57 datasets), and the customer transaction layer **split** between a uMAX billing portal and generic NYC311 → **transact** (give the service layer one owned, well-typed, agent-native contract).

## Modernization implications

1. **The gap is transactions, not data.** DEP publishes reservoirs, water quality, consumption, green infrastructure, hydrants, and permits generously. What has no machine-readable surface is what customers *do*: pay a bill, manage an account, and — most urgently — **report a water-main break or sewer backup**.
2. **Front uMAX and NYC311 with one owned API.** A modern DEP API ([OpenAPI](openapi/dep.yaml)) should present the open reference data as clean, well-typed resources *and* expose the net-new **water service request** write workflow, instead of leaving residents to a JavaScript-only Azure B2C portal or a generic 311 form.
3. **The data itself needs a typed contract.** With Harbor Water Quality at 100 free-text columns and reservoir levels as cryptic SCADA tags, even the *open* data is hard to consume. An agent-native contract in front of it ([MCP artifact](mcp/dep-mcp.json)) is the low-hanging fruit.
