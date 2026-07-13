# Technology & Vendor Inventory — FDNY

What the Fire Department of the City of New York's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). FDNY is a **split domain**: an informational site on the shared NYC.gov platform, and a business **permitting portal running on a rented Accela Civic Platform** (FDNY Business).

## Two front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/fdny/` | About, firehouses, safety, business permitting how-to, news — content only |
| **FDNY Business** | **`fires.fdnycloud.org/CitizenAccess`** | The transactional layer: apply for fire permits, hold Certificates of Fitness/Operation, schedule inspections, answer violations, pay fees |

## Informational site (nyc.gov/site/fdny)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed`, `server-timing: cdn-cache; desc=HIT`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid` |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — it is not an FDNY-specific stack. FDNY's distinct technology is the FDNY Business portal.

## FDNY Business — the important part

The business service layer is **not** on NYC.gov. It is a separate host running a packaged, rented commercial platform:

| Property | Value | Evidence |
|---|---|---|
| Host | `fires.fdnycloud.org` | 301 → `/CitizenAccess/Default.aspx` |
| Application path | `/CitizenAccess/Default.aspx` | classic Accela Citizen Access (ACA) URL scheme; `.aspx` (ASP.NET) |
| Product | **Accela Civic Platform** (Citizen Access) | CSP `script-src`/`connect-src` allow-list of `*.accela.com` and `*.civicplatform.com.au`; ACA path convention |
| Edge / gateway | **Cloudflare** + **Azure Application Gateway** | `server: cloudflare`, `CF-RAY`; `ApplicationGatewayAffinity` / `ApplicationGatewayAffinityCORS` cookies |
| Monitoring | **Datadog RUM** | CSP `report-uri https://csp-report.browser-intake-datadoghq.com …`, `*.browser-intake-datadoghq.com` connect-src |
| Requirement | JavaScript-only, session-gated | ASP.NET server-rendered ACA; login-walled account registration |

There is **no documented API, no OpenAPI, no JSON endpoint** — the portal is a rented, server-rendered Accela Citizen Access application. Every business transaction (apply for a permit, hold a C of F, schedule an inspection, answer a violation) is trapped behind the ACA UI, reachable only by a human in a browser or on paper.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data wide open, resident service layer locked in an in-house vendor CRM (Oracle Siebel) → *unlock*.
- **FDNY** = reference and incident data already **wide open** (17 datasets), but the **business transaction layer rented out to a commercial SaaS** (Accela Civic Platform) with no API → **front the rented portal with an owned API**.

## Modernization implications

1. **The gap is transactions, not data.** FDNY already publishes its firehouses, dispatch, inspections, violations, and certificates generously. What has no machine-readable surface is what businesses actually *do*: apply for a permit, hold a certificate, schedule an inspection, answer a violation.
2. **Front the rented Accela portal with an owned API.** A modern FDNY API ([OpenAPI](openapi/fdny.yaml)) should present firehouses/incidents/inspections/violations/certificates as clean resources *and* expose the portal's core write workflow — submitting a **fire permit application** — instead of leaving applicants to a rented ACA screen.
3. **Depending on a commercial SaaS for the city's fire-safety permitting is a governance and continuity risk.** An agent-native contract in front of it ([MCP artifact](mcp/fdny-mcp.json)) is the low-hanging fruit.
