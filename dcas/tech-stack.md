# Technology & Vendor Inventory — DCAS

What the NYC Department of Citywide Administrative Services' public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). DCAS is a **fragmented domain**: an informational site on the shared NYC.gov platform, plus a sprawl of separate **aNNN vendor applications** that each carry a different piece of the transaction layer.

## The front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/dcas/` | About, careers, exams, fleet, agency services — content only |
| **City Jobs portal** | **`cityjobs.nyc.gov`** (was `a127-jobs.nyc.gov`) | Careers search + the **exam application** Online Application System (OASys) |
| **Employee Self-Service** | **`a127-ess.nyc.gov`** | Pay stubs, benefits, W-2, direct deposit for city employees (NYCAPS) |
| **CityStore** | **`a856-citystore.nyc.gov`** | The official City of New York online store |

## Informational site (nyc.gov/site/dcas)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed`, `server-timing: cdn-cache; desc=HIT`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid`; `dtCookie` on app pages |
| App tier (some pages) | AWS load balancer | `AWSALB` / `AWSALBCORS` cookies on `/employees/...` pages |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — it is not a DCAS-specific stack. DCAS's distinct technology is the aNNN application layer below.

## The aNNN application layer — the important part

The transaction layer is **not** one system. It is several separate, differently-built vendor applications:

| App | Host | Product / stack | Evidence |
|---|---|---|---|
| **City Jobs / OASys** | `cityjobs.nyc.gov` (a127-jobs redirects here) | **ASP.NET Core on Azure App Service** | `server: Kestrel`, `.AspNetCore.Antiforgery.*` cookie, `x-ms-routing-name=self` + `TiPMix` (Azure App Service traffic routing), `COP-Personal` app cookie |
| **Employee Self-Service** | `a127-ess.nyc.gov` | **Oracle PeopleSoft (NYCAPS)** | page title "PeopleSoft", `psp/` PeopleSoft servlet path |
| **CityStore** | `a856-citystore.nyc.gov` | **Shopify** (behind Cloudflare) | `server: cloudflare`, `_shopify_y` / `_shopify_s` / `_shopify_essential` cookies, `cart_currency` |

The legacy `a127-jobs.nyc.gov` host now **301-redirects to `cityjobs.nyc.gov`** — evidence that DCAS has already replatformed the careers front door onto modern .NET/Azure, while Employee Self-Service is still on **PeopleSoft/NYCAPS** and the store is a **Shopify** tenant. Three different vendors, three different stacks, no shared API.

There is **no documented API, no OpenAPI, no JSON endpoint** for any of them. Every citizen transaction — registering for a civil-service exam, applying to a posting, buying a City map — is trapped inside a login-walled or vendor-tenant UI.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, the resident service layer locked in one vendor CRM → *unlock*.
- **DCAS** = reference data broadly **open** (32 datasets) and the careers front door already replatformed to .NET/Azure, but every **citizen transaction is scattered across separate rented apps** (Azure, PeopleSoft, Shopify) with no API → **transact** — give the civil-service pipeline one owned transaction API.

## Modernization implications

1. **The gap is transactions, not data.** DCAS already publishes its civil-service lists, titles, exam schedule, buildings, and fleet generously. What has no machine-readable surface is what a citizen actually *does*: **register for an exam**, apply to a job, or buy from the CityStore.
2. **Front the aNNN apps with one owned API.** A modern DCAS API ([OpenAPI](openapi/dcas.yaml)) should present postings, titles, eligible lists, exam schedule, buildings, and fleet as clean resources *and* expose the core write workflow — **registering for a civil-service exam** — instead of leaving candidates to OASys screens.
3. **Depending on three separate vendor tenants for the city's HR, hiring, and retail transactions is a governance and continuity risk.** An agent-native contract in front of them ([MCP artifact](mcp/dcas-mcp.json)) is the low-hanging fruit.
