# Technology & Vendor Inventory — NYC Tax Commission

What the New York City Tax Commission's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). The Tax Commission has **no distinct platform of its own**: an informational site on the shared NYC.gov chassis, plus a browser-only **online filing system** for the property-tax appeal.

## Two front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/taxcommission/` | About, how to appeal, forms, rules, guidelines, annual reports — content only |
| **Online filing system** | `www.nyc.gov/site/taxcommission/…` (online filing) | The transactional layer: file an **Application for Correction** of a tentative assessment and its income & expense statements; track the determination |

## Informational site (nyc.gov/site/taxcommission)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `server-timing: ak_p; …`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid`, `dtCookie` |
| Real-user monitoring | **Akamai mPulse / Boomerang** | `BOOMR` snippet + `go-mpulse.net` in page markup (`BOOMR_API_key`) |
| Load balancing | **AWS Application Load Balancer** | `AWSALB` / `AWSALBCORS` cookies |
| Security headers | CSP `frame-ancestors 'self' https://*.nyc.gov https://*.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — it is not a Tax-Commission-specific stack. The Commission's distinct surface is the online filing system, and even that is a browser-only flow with no API.

## The appeal — the important part

The Tax Commission is the City's **independent** body for reviewing property-tax assessments. The workflow, from the process pages and forms index:

| Step | What happens | Artifact |
|---|---|---|
| DOF sets value | The Department of Finance issues the tentative assessed value (Notice of Property Value) | DOF NOPV (separate agency) |
| Owner appeals | Owner (or representative) files an **Application for Correction** by the March 15/16 deadline | **TC101** (Class 2/4), **TC108** (Class 1), **TC109** (condo units), **TC106** (exemptions) |
| Income proof | Income-producing property must file an income & expense statement | **TC201** (rental), **TC203** (co-op), **TC208**, **TC214** |
| Certification | Assessed value of **$5.4M or more** requires an accountant's certification | **TC309** |
| Fee | A **$175 fee** applies when the assessed value is **$2M or more** (unless review is waived) | per NYC Admin Code §11-216 |
| Determination | The Commission reviews (with or without a hearing) and may **offer a reduction**, reclassify, or make no change | Determination / offer |
| Escalation | A dissatisfied owner may bring an **Article 7** petition in NY State Supreme Court | Open Article 7 Petitions dataset |

There is **no documented API, no OpenAPI, no JSON endpoint** for any of this. The application is a set of PDF forms and a browser-only online filing system; the determination is returned the same way.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, resident service layer locked in a vendor CRM → *unlock*.
- **Tax Commission** = a quasi-judicial appeals body whose intake is **PDF forms + a browser-only filing system**, publishing only a thin trail of **outcomes** → **digitize the appeal**.

## Modernization implications

1. **The gap is the transaction, and even the data is thin.** The two open datasets show only outcomes — the reductions granted and the court petitions that follow. The appeal itself (application → income & expense → determination → offer) has no machine-readable contract at all.
2. **Give the appeal an owned API.** A modern Tax Commission API ([OpenAPI](openapi/taxcommission.yaml)) should publish the open outcome datasets as clean resources *and* expose the core write workflow — **filing an assessment appeal** — instead of leaving owners and representatives to PDF forms and a browser-only screen.
3. **An independent adjudicative body on a shared CMS with no filing API is an accessibility and transparency risk.** An agent-native contract in front of it ([MCP artifact](mcp/taxcommission-mcp.json)) is the low-hanging fruit — and it keeps the DOF-sets / Tax-Commission-hears relationship explicit.
