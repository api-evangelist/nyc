# Technology & Vendor Inventory — NYC Law Department

What the New York City Law Department's (Office of the Corporation Counsel) public surface is built on and which third parties it depends on — fingerprinted from response headers and page markup during the crawl (2026-07-13). Unlike the citizen-service agencies elsewhere in this project, Law is an **agency-facing legal office** with a single, content-only front door on the shared NYC.gov platform and **no application, portal, or service system of its own**.

## One front door

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/law/` | About, Corporation Counsel's message, Legal Divisions, Careers, Public Resources (laws of the City, tax certiorari, False Claims Act, M/WBE, procurement), News — content only |

There is no `selfserve.*` host, no login-walled portal, and no online application system — the Careers page directs applicants to email/PDF instructions.

## Informational site (nyc.gov/site/law)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `server-timing: ak_p; desc=...`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| App/load balancer | **AWS ALB** | `set-cookie: AWSALB`, `AWSALBCORS` |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid`, `dtCookie` |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — it is not a Law-specific stack. Law has **no distinct technology to point at**; that itself is the finding.

## Where the important data actually lives

The Law Department publishes only seven thin, manually-updated annual datasets on NYC Open Data (Socrata/Tyler). The data most people want from "the City's lawyers" — the ledger of **claims filed against the City and settlement dollars paid** — is **not the Law Department's** to publish. It is published by the **Office of the Comptroller** (`ex6k-ym48`, "Claims Report — Underlying Settlements and Claims Filed"). Law's own litigation dataset (`pjgc-h7uv`) is a **case index**, not the claims ledger.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data wide open, service layer locked in a vendor CRM → *unlock*.
- **Law** = an **agency-facing legal office** with almost no citizen transactions, a handful of stale annual datasets, and the core claims data owned by *another* agency → **catalog** what little exists into one owned contract and route claims questions to the Comptroller.

## Modernization implications

1. **There is little to liberate and no service layer to unlock.** Law's public data is seven small annual snapshots; the crawl found no hidden backend, portal, or search vendor.
2. **Catalog the scattered publications and the case index** ([OpenAPI](openapi/law.yaml)) so consumers learn one model — cases, divisions, publications, M/WBE, pro bono program — instead of seven Socrata IDs, and so the contract can point explicitly at the Comptroller for claims/settlement dollars.
3. **The one net-new write surface is inward-facing recruitment, not a citizen service.** The single transaction the public initiates with Law is applying to work there; giving that an owned API + an [MCP artifact](mcp/law-mcp.json) is the low-hanging fruit here.
