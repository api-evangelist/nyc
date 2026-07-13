# Technology & Vendor Inventory — DDC

What the NYC Department of Design and Construction's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). DDC is a **vendor-facing, business-to-government agency**: an informational site on the shared NYC.gov platform, and a set of **transaction systems that DDC does not own** — they belong to the Mayor's Office of Contract Services (MOCS) and the Comptroller.

## Two front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/ddc/` | About, Work With DDC, Projects, MWBE, Resources, Careers — content only |
| **Vendor / procurement systems** | **citywide, not DDC-owned** | Where the transactions actually happen: solicitations (PASSPort), notices (City Record), contract records (Checkbook NYC), and the contract-process portal (DDC Anywhere) |

## Informational site (nyc.gov/site/ddc)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed: 9 …`, `server-timing: cdn-cache`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| App tier / load balancing | **AWS ALB** | `set-cookie: AWSALB / AWSALBCORS`; `JSESSIONID` (Java) |
| Real-user monitoring | **Dynatrace** + **Akamai mPulse** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid`; `s.go-mpulse.net` beacon |
| Maps | **Google Maps JS** | `maps.googleapis.com` referenced on content pages |
| Security headers | CSP `frame-ancestors 'self' https://*.nyc.gov https://*.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — it is not a DDC-specific stack. DDC exposes **no content API, no OpenAPI, no JSON endpoint** on its informational site.

## The transaction systems — the important part (and none are DDC's)

DDC's "Work With DDC" page is explicit: *"All solicitations are conducted via a centralized, Citywide system managed by the Mayor's Office of Contract Services (MOCS)."* The systems a vendor must use are all owned elsewhere:

| System | Host | Owner | What it does |
|---|---|---|---|
| **PASSPort** | `nyc.gov/site/mocs/passport` | **MOCS** | Procurement and Sourcing Solutions Portal — registration required to search and respond to **all** DDC solicitations; the real vendor onboarding + prequalification system. No public API. |
| **City Record** | `a856-cityrecord.nyc.gov` | DCAS / citywide | Publishes solicitations and award notices; vendors register for email alerts. |
| **Checkbook NYC** | `checkbooknyc.com` | **Comptroller** | Public record of existing DDC and City contracts. Has its own API, but it is the Comptroller's, not DDC's. |
| **DDC Anywhere** | `ddcanywhere.nyc` | DDC | The one DDC-owned vendor system — a login-walled portal for current/anticipated contract holders to manage the design/construction process. No documented API observed. |

So the transactional layer for DDC's core relationship — vendors and client agencies delivering $34B+ of capital work — is **almost entirely outsourced to citywide systems**, and the one piece DDC does own (DDC Anywhere) has no machine-readable surface.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, resident service layer locked in a vendor CRM → *unlock*.
- **DFTA** = provider network open, the connecting transaction is a phone call → *connect*.
- **DDC** = a **vendor-facing agency** whose own data is thin and **historical**, and whose transactions all run on **citywide systems it doesn't own** (PASSPort/MOCS, City Record, Checkbook) → **surface** the live portfolio and front the citywide vendor flow with an owned contract.

## Modernization implications

1. **DDC owns almost none of its surface.** Its published data is four Open Data datasets — three of them `(Historical)` snapshots — and every transaction is on a citywide system. There is no live project API and no DDC-owned write surface at all.
2. **Surface the live portfolio.** A modern DDC API ([OpenAPI](openapi/ddc.yaml)) should present 550+ active projects and awarded contracts as clean, **live** resources instead of stale snapshots, keyed on Project ID and PIN.
3. **There is no citizen write here — the honest net-new write is B2G.** The one write surface DDC could own is **vendor prequalification / expression of interest**, fronting the citywide PASSPort flow, plus an optional City Record notification subscription. An agent-native contract ([MCP artifact](mcp/ddc-mcp.json)) over that is the low-hanging fruit.
