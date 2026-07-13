# Technology & Vendor Inventory — NYC Aging (DFTA)

What the NYC Department for the Aging's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). DFTA is a **connective agency**: it does not run a resident transaction system of its own, it funds a ~1,000-provider network and routes people to it through an information-and-referral contact center.

## Two front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/dfta/` | About, services, find-help, older-adult-center finder, benefits — content only |
| **Aging Connect** | **`212-AGING-NYC` / `212-244-6469`, `nyc.gov/site/dfta/services/find-help.page`** | The intake/referral layer: connect an older adult to case management, home-delivered meals, benefits, caregiver support, elder-abuse help, or center enrollment |

## Informational site (nyc.gov/site/dfta)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed`, `server-timing: cdn-cache; desc=HIT`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid` |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — it is not a DFTA-specific stack. Unlike NYCHA (which runs a packaged Oracle Siebel CRM behind its portal), DFTA has **no separate resident-facing application** at all: the service layer is a phone line.

## Aging Connect — the important part

The resident service layer is **not** a system with a machine-readable surface. It is an **information-and-referral (I&R) contact center**:

| Property | Value | Evidence |
|---|---|---|
| Name | **Aging Connect** | `nyc.gov/site/dfta/services/find-help.page` |
| Phone | `212-AGING-NYC` / `212-244-6469` | find-help page markup |
| Channel | Phone, walk-in to a center, or a web contact form | site content |
| Product | No packaged application exposed; internal case-management/CRM not public | no OpenAPI, no JSON endpoint |
| Requirement | Human-mediated | a caseworker takes the request by phone |

There is **no documented API, no OpenAPI, no JSON endpoint** — every resident transaction (find help, apply for meals, request case management, report elder abuse) is a phone call or a walk-in. The provider network the caseworker routes you into is, ironically, fully published on Open Data.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, resident service layer locked in an Oracle Siebel CRM → *unlock*.
- **DFTA** = provider-network reference data already **wide open** (11 datasets), but the **resident service layer is a phone-based referral center** with no system to expose → **connect the older adult to services with an owned, agent-native intake.**

## Modernization implications

1. **The gap is intake, not data.** DFTA already publishes its provider network, senior-center operations, activities, and contract spend generously. What has no machine-readable surface is what an older adult actually *does*: get connected to a service.
2. **Give Aging Connect a machine-readable front door.** A modern DFTA API ([OpenAPI](openapi/dfta.yaml)) should present providers/centers/activities/service-units as clean resources *and* expose the core write workflow — making a **service referral** — instead of leaving every older adult and caseworker to a phone queue.
3. **A referral is exactly the shape an agent should be able to fill.** An agent-native contract in front of Aging Connect ([MCP artifact](mcp/dfta-mcp.json)) — find the right provider, then submit the referral, with an urgent path to Adult Protective Services — is the low-hanging fruit.
