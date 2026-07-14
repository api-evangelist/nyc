# Technology & Vendor Inventory — COIB

What the NYC Conflicts of Interest Board's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). COIB is a **transparency-out / attestation-in** agency: an informational site on the shared NYC.gov platform, and a separate **login-gated Annual Financial Disclosure filing website** where every senior public servant files their report.

## Two front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/coib/` | About, the Law, annual-disclosure guidance, public documents, contact — content only |
| **Annual Financial Disclosure filing website** | **login-gated e-filing (linked from `/annual-disclosure/`)** | The transactional layer: file/attest the annual disclosure report during the 4-week filing window |

## Informational site (nyc.gov/site/coib)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed`, `server-timing: cdn-cache; desc=REVALIDATE`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| Load balancer | **AWS ALB** | `AWSALB` / `AWSALBCORS` session cookies |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme; `JSESSIONID` (Java) |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `dtCookie`, `server-timing: dtSInfo/dtRpid` |
| RUM beacon | **Akamai mPulse** | `s.go-mpulse.net` / `s2.go-mpulse.net` |
| Maps | **Google Maps** | `maps.googleapis.com` embed |
| Security headers | CSP `frame-ancestors 'self' https://*.nyc.gov https://*.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on (identical to the NYCHA informational site) — it is not a COIB-specific stack. COIB's distinct technology is the filing website.

## Annual Financial Disclosure filing website — the important part

The compliance transaction layer is **not** browsable HTML. The Annual Disclosure pages state that filers file "**electronically through COIB's filing website**," a login-gated electronic system, with a small group of filers instead receiving a PDF fillable form by email:

| Property | Value | Evidence |
|---|---|---|
| Access | Login-gated electronic filing website | `/annual-disclosure/annual-disclosure.page` ("How Do They File: Electronically through COIB's filing website") |
| Filing window | 4 weeks each spring (deadline typically first Friday of May) | annual-disclosure page |
| Fallback | PDF fillable report by email (uncompensated board members, local public authorities, tax assessors, matching-funds candidates) | annual-disclosure page |
| Output | Elected officials' reports posted as **PDFs on request**; other filers' interests confidential | `/annual-disclosure/elected-officials-annual-disclosure-reports.page` |

There is **no documented API, no OpenAPI, no JSON endpoint** — the filing system is a closed web application. Every consequential COIB transaction (file annual disclosure, complete ethics training, request a waiver, get legal advice, report a violation) is reachable only by a human in a browser or a paper/email form.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data wide open, but the resident service layer locked in a vendor CRM → *unlock*.
- **COIB** = transparency **outputs** genuinely open on Open Data (8 datasets), but the core compliance **input** — the annual financial disclosure filing — locked in a login-only filing website with no API → **attest** (front the filing/attestation layer with an owned API).

## Modernization implications

1. **The gap is the attestation transaction, not the transparency data.** COIB already publishes enforcement, donations, and legal-defense-trust data generously. What has no machine-readable surface is the thing thousands of public servants actually *do* every spring: **file and attest an annual disclosure report**.
2. **Front the filing website with an owned API.** A modern COIB API ([OpenAPI](openapi/coib.yaml)) should present the open datasets as clean resources *and* expose the core write workflow — submitting a **FinancialDisclosureFiling** — instead of leaving filers to a login-only web form.
3. **A closed filing system for the City's entire ethics regime is a governance and continuity risk.** An agent-native contract in front of it ([MCP artifact](mcp/coib-mcp.json)) — that can also answer "which enforcement cases named my agency?" and "am I on the policymakers list, and is my disclosure filed?" — is the low-hanging fruit.
