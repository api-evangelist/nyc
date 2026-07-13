# Technology & Vendor Inventory — ACS

What the NYC Administration for Children's Services' public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). ACS is a **confidentiality-bound, delegated-intake** domain: an informational site on the shared NYC.gov platform, with **no owned transactional application** — the public actions it fronts are handed off to other systems.

## The front door and where actions go

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/acs/` | About, child welfare, youth justice, child care, for-families — content only |
| Report child abuse/neglect | → **NY State OCFS Statewide Central Register** (`ocfs.ny.gov`, 1-800-342-3720) | Statutory hotline; runs on the State **CONNECTIONS** case system — **not** an ACS surface |
| Complain about a child care provider / any city service | → **NYC 311** (`portal.311.nyc.gov`) | The citywide intake channel ACS defers to; ACS owns no equivalent |
| Find a program / locator | Google Maps JS embedded on `/early-care` and `/child-welfare` pages | Client-side map over the Community Partners directory |

## Informational site (nyc.gov/site/acs)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed`, `server-timing: cdn-cache; desc=HIT`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid` |
| Embedded maps | **Google Maps JavaScript API** | `maps.googleapis.com/maps/api/js` on child-care and child-welfare pages |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on (identical fingerprint to NYCHA's informational site). ACS adds **no distinct application of its own** — the notable thing is the *absence* of an owned transactional layer.

## The delegated / confidential service layer — the important part

Unlike domains that hide their transactions inside a vendor CRM, ACS mostly does not run the transactions at all:

| Property | Value | Evidence |
|---|---|---|
| Abuse/neglect intake | **NY State OCFS Statewide Central Register (SCR)** | `/child-welfare` page links `ocfs.ny.gov/main/cps/`; statutory 1-800-342-3720 hotline |
| SCR backing system | **CONNECTIONS** (NY State child-welfare case system) | State-operated; no public API |
| Provider / service complaints | **NYC 311** (`portal.311.nyc.gov`) | Linked citywide; ACS has no owned complaint API |
| Case & operational data | **CCWIS / internal ACS systems** | Confidential by statute (Social Services Law); published only as aggregates |

There is **no documented ACS API, no OpenAPI, no JSON endpoint**. The only machine-readable ACS surface is the Socrata SODA endpoint under one dataset (Community Partners); everything else is either a static report file on Open Data or a screen belonging to the State or 311.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, resident service layer locked in an Oracle Siebel CRM → *unlock*.
- **ACS** = data confidential or published as static files, and the two public actions **delegated to the State (SCR) and NYC 311** → **insource** an owned, agent-native contract for what ACS *can* publish and *should* own.

## Modernization implications

1. **The gap is ownership, not a hidden backend.** ACS doesn't have a secret API to expose — it has a provider directory worth publishing cleanly and a complaint intake it has handed to 311. The work is to *insource* an owned contract, not to unlock a CRM.
2. **Publish the one real dataset as a first-class resource.** The Community Partners directory ([OpenAPI](openapi/acs.yaml)) should be a clean `Provider` resource, and the aggregate reports queryable resources — not 16 downloadable spreadsheets.
3. **Own the child-care-provider complaint.** An owned `POST /child-care-complaints` ([schema](schemas/child-care-complaint.json)) gives ACS a machine-readable, agent-native intake for provider concerns instead of deferring to 311 — while **never** collecting a child's case data and always redirecting suspected abuse to the State Central Register.
4. **Confidentiality is a feature, not a limit.** An agent-native contract ([MCP artifact](mcp/acs-mcp.json)) can be explicit that only aggregates are exposed and that abuse reports route to 1-800-342-3720 — safer than a generic web form.
