# Technology & Vendor Inventory — DYCD

What the NYC Department of Youth and Community Development's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). DYCD is a **split domain**: an informational site on the shared NYC.gov platform, and the **DYCD Connect** ecosystem — including the **DiscoverDYCD** program finder — built as a custom Angular application on Microsoft-IIS.

## Two front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/dycd/` | About, services, "how do I…", provider resources — content only |
| **DYCD Connect / DiscoverDYCD** | **`dycdconnect.nyc` · `discoverdycd.dycdconnect.nyc`** | The application layer: the public **program finder**, provider contract management, and program application/enrollment |

## Informational site (nyc.gov/site/dycd)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `server-timing: ak_p; desc=…`, `alt-svc: h3` |
| Load balancer | **AWS ALB** | `set-cookie: AWSALB`, `AWSALBCORS` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| Real-user monitoring | **Dynatrace** | `set-cookie: dtCookie`, `server-timing: dtSInfo/dtRpid` |
| App server hint | Java servlet container | `set-cookie: JSESSIONID` |

This is the **same NYC.gov chassis** every citywide agency site sits on — it is not DYCD-specific. DYCD's distinct technology is the DYCD Connect application ecosystem.

## DYCD Connect / DiscoverDYCD — the important part

The application layer is **not** on NYC.gov. It is a separate ecosystem on its own domain running a custom app:

| Property | Value | Evidence |
|---|---|---|
| Domains | `dycdconnect.nyc`, `discoverdycd.dycdconnect.nyc` | redirects from `dycdconnect.nyc` → `www.dycdconnect.nyc` |
| Web server | **Microsoft-IIS/10.0** | `server: Microsoft-IIS/10.0` |
| Hosting | AWS EC2 (internal EC2 hostnames on redirect) | `server: ip-10-123-…​.ec2.internal` |
| Front end | **Angular** single-page app | hashed bundles `runtime.*.js`, `polyfills.*.js`, `main.*.js`; `<title>discoverDYCD</title>` |
| Backend | Private internal **`/api/`** | `/api/*` referenced by the app; every public probe returns `404` |
| Maps | **Google Maps JS + Places** | `maps.googleapis.com/maps/api/js?...&libraries=places` |
| i18n | **Google Translate** widget | `translate.google.com/translate_a/element.js` |

DiscoverDYCD is a **real program finder that DYCD already built** — but its backend is a **private, undocumented `/api/`**: there is **no public API, no OpenAPI, no JSON surface** a developer or agent can call. The finder is reachable only by a human in the Angular UI. The provider/participant side of DYCD Connect is likewise login-walled with no public API, and **applying to a program** (e.g. SYEP) has no machine-readable contract.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data wide open, service layer locked in a vendor CRM → *unlock*.
- **DYCD** = supply-side data **wide open** on Open Data (15 datasets) **and** a program finder DYCD **already built** (DiscoverDYCD) — but the finder is an app with a private API, and there is no way to apply → **surface the finder (and add the apply write)**.

## Modernization implications

1. **The finder already exists — it just isn't an API.** DYCD invested in DiscoverDYCD to help the public find programs; the low-hanging fruit is exposing that same capability as an owned, documented, agent-callable API instead of an Angular-only screen.
2. **Publish the open supply data as one clean resource model.** Program sites, providers, contracts, and NDAs behind one owned DYCD contract ([OpenAPI](openapi/dycd.yaml)) — so consumers learn one model, not 15 Socrata IDs plus a private `/api/`.
3. **Add the one net-new write workflow** — applying to a program ([`POST /applications`](openapi/dycd.yaml)) — the transaction a young person actually needs, today trapped in a seasonal online form. An agent-native contract in front of it ([MCP artifact](mcp/dycd-mcp.json)) is the low-hanging fruit.
