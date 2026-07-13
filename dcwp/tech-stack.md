# Technology & Vendor Inventory — DCWP

What the NYC Department of Consumer and Worker Protection's (DCWP, formerly DCA) public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). DCWP is a **split domain**: an informational site on the shared NYC.gov platform, and a resident/business **transaction layer split across a Java licensing portal, CityPay, and 311**.

## Front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/dca/` | Licenses, consumer rights, workers' rights, "how do I…" — content only |
| **NYC Business portal** | **`nyc-business.nyc.gov/nycbusiness/`** | Apply for and manage DCWP business licenses |
| CityPay | `citypay.nyc.gov` | Pay DCWP fines and fees (CityBase checkout) |
| 311 | `portal.311.nyc.gov` | File a consumer complaint against a business |

## Informational site (nyc.gov/site/dca)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `server-timing: ak_p`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid` |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — not a DCWP-specific stack. DCWP's distinct technology is the licensing portal.

## NYC Business portal — the transaction layer

Business licensing is **not** served from an API. It runs as a separate Java web application:

| Property | Value | Evidence |
|---|---|---|
| Host | `nyc-business.nyc.gov` | redirect landing page |
| Application path | `/nycbusiness/` | app context root |
| Framework | **Java / Spring web app** | `SESSION` cookie (`Path=/nycbusiness; HttpOnly; SameSite=None`) — Spring Session, not an ASP.NET/PHP fingerprint |
| Edge / monitoring | Akamai + Dynatrace | `server-timing: ak_p`, `dtCookie`, `x-oneagent-js-injection` |
| Requirement | session-gated, browser-only | server-rendered; no JSON/OpenAPI surface |

There is **no documented API, no OpenAPI, no JSON endpoint** for applying for or managing a license. `citypay.nyc.gov` (CityBase) returns `403` to non-browser clients. Filing a consumer complaint routes through **311**, which has no public write API to DCWP.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, service layer locked in a vendor CRM → *unlock*.
- **DCWP** = the **entire regulatory lifecycle is already open** (37 datasets), but it is **spread across 37 Socrata IDs with no owned contract**, and the two citizen writes (apply, complain) live in a Java portal / 311 with no API → **bind the open lifecycle and add the writes**.

## Modernization implications

1. **The data problem is binding, not liberation.** DCWP already publishes applications, licenses, inspections, charges, complaints, and worker-protection matters — all joinable on `Business Unique ID` and `License Number`. What is missing is one owned contract ([OpenAPI](openapi/dcwp.yaml)) so consumers learn one model, not 37 dataset IDs.
2. **The gap is the two citizen writes.** Applying for a license and filing a consumer complaint — the things a person actually *does* — have no machine-readable surface; they live in a Java portal or a 311 form.
3. **An agent-native contract in front of it** ([MCP artifact](mcp/dcwp-mcp.json)) — `apply_for_license` and `file_complaint` alongside read access to the whole lifecycle — is the low-hanging fruit.
