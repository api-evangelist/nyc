# Technology & Vendor Inventory — DCLA

What the NYC Department of Cultural Affairs' public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). DCLA is a **split domain**: an informational site on the shared NYC.gov platform, and a grants **application portal running Salesforce Experience Cloud**.

## Two front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/dcla/` | About, cultural funding, MFTA, Public Art, resources — content only |
| **Grants Management System** | **`dclagms.nyc.gov/grants/s/`** | The transactional layer: register an organization, create and submit a **Cultural Development Fund grant application**, and track its status |

## Informational site (nyc.gov/site/dcla)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed`, `server-timing: ak_p`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| App tier | Java (session) | `JSESSIONID` cookie; `AWSALB`/`AWSALBCORS` load-balancer cookies |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `ruxitagentjs` script, `dtCookie`; mPulse (`go-mpulse.net`) |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — it is not a DCLA-specific stack. DCLA's distinct technology is the grants portal.

## Grants Management System — the important part

The grant application layer is **not** on NYC.gov. It is a separate host running a packaged CRM platform:

| Property | Value | Evidence |
|---|---|---|
| Host | `dclagms.nyc.gov` | linked from the CDF application page on nyc.gov/site/dcla |
| Community path | `/grants/s/` | Salesforce Experience Cloud (Community) site path |
| Product | **Salesforce Experience Cloud** (Lightning Communities) | `LSKey-c$CookieConsentPolicy` cookies, `CookieConsentPolicy`, `301` chain to `/grants/s/`, references to `salesforce.com` |
| Backing org | `culturalaffairsnyc.my.salesforce.com` | SAML SSO issuer embedded in the login markup (`...culturalaffairsnyc.my.salesforce.com&samlSsoConfig=...`) |
| Requirement | Login-gated; register a new account or sign in as the organization's Primary User | "Register New Account" / "Account Log In" on the CDF application page |

There is **no documented API, no OpenAPI, no public JSON** — the portal is a Salesforce Experience Cloud community. Every grant transaction (register, apply, submit, track) is reachable only by a human in a browser after login. (Salesforce has REST/SOAP APIs internally, but none is published or documented for public/consumer use here.)

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, resident service layer locked in an Oracle Siebel CRM → *unlock*.
- **DCWP** = whole lifecycle open across 37 datasets, no owned contract, two citizen writes locked → *bind + add the writes*.
- **DCLA** = funding **outcomes** published openly (9 datasets), but the grant **application** locked inside a Salesforce Experience Cloud portal, and no owned API binds organizations to their funding → **open the grant pipeline**.

## Modernization implications

1. **The gap is the application, not the outcome.** DCLA already publishes who it funded, its cultural-organization directory, its public art, and MFTA donations. What has no machine-readable surface is what an organization actually *does*: **apply for a grant**.
2. **Front the Salesforce portal with an owned API.** A modern DCLA API ([OpenAPI](openapi/dcla.yaml)) should present organizations, program/capital funding, CIG support, public artworks, and MFTA as clean resources *and* expose the portal's core write workflow — creating a **grant application** — instead of leaving applicants to a login-only Salesforce community.
3. **Depending on a packaged CRM for the nation's largest municipal cultural-grant pipeline is a governance and accessibility risk.** An agent-native contract in front of it ([MCP artifact](mcp/dcla-mcp.json)) is the low-hanging fruit.
