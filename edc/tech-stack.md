# Technology & Vendor Inventory — EDC

What the New York City Economic Development Corporation's public surfaces are built on and which third parties they depend on — fingerprinted from response headers, robots.txt, and the Socrata catalog during the crawl (2026-07-13). EDC is a **public benefit corporation**, and its stack looks the part: a **Drupal** marketing site sealed behind a **Cloudflare bot challenge**, a contractor-run ferry site, and almost nothing published as data.

## Front doors

| Surface | URL | What it does |
|---|---|---|
| Primary site | `edc.nyc` | Projects, real estate, RFPs, programs, about — content only |
| Alias domain | `nycedc.com` | Legacy/marketing alias of edc.nyc |
| **NYC Ferry** | **`www.ferry.nyc`** | Rider-facing schedules and booking for the ferry EDC operates |

## edc.nyc / nycedc.com

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge / bot mgmt | **Cloudflare** | `server: cloudflare`, `cf-ray`, `cf-mitigated: challenge`, `server-timing: chlray` |
| Bot challenge | **Cloudflare Challenge (Turnstile)** | HTTP **403** to non-browser clients; CSP allows `challenges.cloudflare.com`; `accept-ch` / `critical-ch` UA client-hint negotiation |
| CMS platform | **Drupal** | `robots.txt` disallow/allow rules for `/core/…`, `/profiles/…`, `/modules/`, `/themes/` — the Drupal fingerprint |
| Security headers | HSTS, `x-frame-options: SAMEORIGIN`, `x-content-type-options: nosniff`, COEP/COOP/CORP | response headers |

The consequence matters for this assessment: **the site is not machine-accessible**. A non-browser client (curl, a crawler, an agent) is met with a Cloudflare challenge and a 403, so even the human-readable project, asset, and RFP listings can't be reliably fetched, let alone parsed. There is **no API, no OpenAPI, no JSON endpoint**.

## NYC Ferry (ferry.nyc)

| Property | Value | Evidence |
|---|---|---|
| Edge | **Cloudflare + Amazon CloudFront** | `server: cloudflare`, `via: … .cloudfront.net (CloudFront)` |
| Operator | Ferry operated **on behalf of EDC** by a contractor | EDC owns the system; day-to-day operations are contracted out |
| API | No documented public EDC ferry API | rider site only; ridership is published to Open Data (`t5n6-gx8c`) |

## Open Data footprint

| Source | Scope | Note |
|---|---|---|
| **`data.cityofnewyork.us` (Socrata SODA)** | **5** EDC-labeled datasets | Mapped In NY, NYC Ferry Ridership, 3× WiredNYC — all peripheral to EDC's mission |
| **PASSPort** (`passport.cityofnewyork.us`) | Citywide procurement | Where formal solicitation responses are processed citywide; not an EDC-native API |

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy Smarty/PHP platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data wide open, service layer locked in a vendor CRM → *unlock*.
- **EDC** = a public benefit corp whose **core business (real estate, projects, RFPs) is not published at all**, while only peripheral programs reach Open Data, and the site itself is bot-walled → **surface the portfolio**.

## Modernization implications

1. **The gap is coverage, not format.** Unlike NYCHA (where the data is open but the service is locked), EDC barely publishes its core at all. Its real estate, projects, and solicitations have no machine-readable existence.
2. **A bot-challenged Drupal site is not a data strategy.** Sealing edc.nyc behind Cloudflare protects the marketing site but leaves EDC with no way for partners, developers, or agents to consume its portfolio — an owned API ([OpenAPI](openapi/edc.yaml)) would.
3. **Open the solicitation pipeline.** EDC's signature transaction — responding to an RFP/RFEI — has no machine-readable front door. The net-new write workflow (`submit_rfp_response`) and an agent-native contract ([MCP artifact](mcp/edc-mcp.json)) are the low-hanging fruit.
