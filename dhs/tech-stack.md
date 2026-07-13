# Technology & Vendor Inventory — DHS

What the NYC Department of Homeless Services' public surface is built on and which third parties it depends on — fingerprinted from response headers and page markup during the crawl (2026-07-13). Unlike NYCHA, DHS has **no separate resident service portal**: it is an informational site on the shared NYC.gov platform, and every transaction routes through **NYC311** or an in-person intake center.

## One front door (plus a phone number)

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/dhs/` | About, shelter, outreach, "how do I…", statistics & reports — content only |
| **NYC311** | `portal.311.nyc.gov` / dial 311 | The transactional layer: report a homeless person for outreach ("Homeless Person Assistance"), find shelter — **not a DHS surface** |

## Informational site (nyc.gov/site/dhs)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed`, `server-timing: cdn-cache; desc=HIT`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid` |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — it is not a DHS-specific stack. DHS ships **no application of its own**: the header fingerprint is byte-for-byte the platform seen on NYCHA's informational site.

## The service layer — there isn't one (that DHS owns)

DHS's real transactions are not on a DHS system at all:

| Property | Value | Evidence |
|---|---|---|
| Street-outreach report | **NYC311 "Homeless Person Assistance"** | `nyc.gov/site/dhs/shelter/shelter.page` and outreach pages point to 311; routed to borough outreach providers |
| Apply for shelter | **In-person intake** (PATH for families with children, adult-intake centers) | Directory Of DHS Contacts (`cete-9g3v`) lists the intake sites |
| Emergency | **911** | life-safety cases |

There is **no documented API, no OpenAPI, no JSON endpoint, and no self-service portal** for any DHS transaction. Where NYCHA at least has a vendor CRM behind a login, DHS has only a phone tree and a front desk.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data wide open, service layer locked in a vendor CRM → *unlock*.
- **DHS** = observational data wide open (23 datasets led by the daily census), but **no service layer at all** — the human-services actions route through NYC311/phone/in-person → **connect** (give the action an owned, agent-native contract).

## Modernization implications

1. **The gap is the action, not the data.** DHS publishes the shelter census, directories, buildings, and street-count history generously. What has no machine-readable surface is what a New Yorker *does*: apply for shelter, or **report someone sleeping on the street so an outreach team responds**.
2. **Give the outreach request an owned API.** A modern DHS API ([OpenAPI](openapi/dhs.yaml)) should present the census/directories/facilities as clean resources *and* expose the core write workflow — creating an **outreach request** — instead of leaving New Yorkers to a 311 phone menu.
3. **Routing the city's most time-sensitive human-services action through a generic 311 call is a governance and outcomes risk.** An agent-native contract in front of it ([MCP artifact](mcp/dhs-mcp.json)) is the low-hanging fruit — so an assistant can file, and track, an outreach request on someone's behalf.
