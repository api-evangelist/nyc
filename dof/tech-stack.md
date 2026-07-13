# Technology & Vendor Inventory — DOF

What the NYC Department of Finance's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). DOF is an **app-layer legacy** domain: an informational site on the shared NYC.gov platform, and a **fleet of aging, siloed `a836-*.nyc.gov` applications** that carry the real transactions.

## Front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/finance/` | Property, benefits, parking, business tax, "how do I…" — content only |
| **ACRIS** | **`a836-acris.nyc.gov`** | Automated City Register Information System — search/record deeds, mortgages, and other real-property documents |
| **CityPay** | **`a836-citypay.nyc.gov`** | Pay parking/camera tickets, property taxes, and other city charges |
| **Property Tax System** | **`a836-pts-access.nyc.gov`** | Property tax account access and payment (PTS) |

## Informational site (nyc.gov/site/finance)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `server-timing: ak_p`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid` |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — it is not a DOF-specific stack. DOF's distinct technology is the `a836` app fleet.

## The a836 legacy application layer — the important part

DOF's transactions are **not** on NYC.gov. They run on a set of standalone, packaged/legacy web apps under the `a836-*.nyc.gov` naming convention:

| App | Host | Product / evidence | State |
|---|---|---|---|
| **ACRIS** | `a836-acris.nyc.gov` | **ASP.NET / IIS** — `X-Powered-By: ASP.NET`, `iso-8859-1`, meta-refresh into a `/CP/` frameset, `Last-Modified: Wed, 15 May 2013`. `<title>ACRIS Main Options</title>` | Legacy, server-rendered, no API |
| **CityPay** | `a836-citypay.nyc.gov` | Payment form; CSP allowlists `js.braintreegateway.com` and `*.paypal.com` / `www.paypalobjects.com` — **PayPal / Braintree**-backed | Modern-ish UI, no API |
| **Property Tax System** | `a836-pts-access.nyc.gov` | Akamai-fronted, **session-cookie gated** (`mspwvw-*` cookie), `no-cache/no-store` | Legacy, session app, no API |

None of these exposes a **documented API, OpenAPI, or JSON endpoint**. ACRIS in particular is a **2013-era ASP.NET frameset application** — the register of every deed and mortgage in the city runs on markup a decade old. Every DOF transaction (record a document, pay a ticket, pay a tax bill) is trapped inside one of these screens, reachable only by a human in a browser.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, service layer locked in one vendor CRM (Siebel) → *unlock*.
- **DOF** = reference data **wildly open** (145 datasets), but transactions spread across a **fleet of aging in-house `a836` legacy apps** (ACRIS, CityPay, PTS), none with an API → **modernize the app layer**.

## Modernization implications

1. **The gap is transactions, not data.** DOF already publishes valuation, exemptions, tax charges, the ACRIS register, and every parking summons. What has no machine-readable surface is what residents actually *do*: pay a ticket, pay a tax bill, record a document.
2. **Front the a836 fleet with one owned API.** A modern DOF API ([OpenAPI](openapi/dof.yaml)) should present valuation/exemptions/tax-bills/ACRIS/violations as clean resources keyed on the **BBL** *and* expose the core write workflow — **paying a parking ticket** — instead of leaving people to CityPay's form or a 2013 ASP.NET screen.
3. **A decade-old ASP.NET app fronting the city's property-document register is a governance and continuity risk.** An agent-native contract in front of it ([MCP artifact](mcp/dof-mcp.json)) is the low-hanging fruit.
