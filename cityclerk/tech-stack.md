# Technology & Vendor Inventory — City Clerk

What the New York City Office of the City Clerk's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). The City Clerk is a **multi-front domain**: a content-API-driven informational site, plus **two rented transaction platforms** — the Marriage Bureau's Project Cupid on the no-code **Unqork** platform, and the Lobbying Bureau's e-Lobbyist Java app behind rented **SAP CDC / Gigya** SSO.

## The front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.cityclerk.nyc.gov/content/` | Marriage Bureau + Lobbying Bureau + Additional Services content — read only |
| **Project Cupid** | **`projectcupid.cityofnewyork.us/app/cupidceremony`** | The Marriage Bureau transaction layer: **apply for a marriage license**, schedule appointments, book ceremonies |
| **e-Lobbyist** | **`apps.nyc.gov/elobbyist/`** | The Lobbying Bureau filing layer: lobbyist registration and periodic reports |
| Lobbyist Search | `lobbyistsearch.nyc.gov` | Public database of registered lobbyists and their filings |
| City Clerk Forms Online | `cityclerkforms.nyc.gov/cityclerkformsonline` | Officiant registration, records requests — Java forms app |

## Informational site (cityclerk.nyc.gov)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `AkamaiGHost` on nyc.gov redirects, `alt-svc: h3`, `server-timing: ak_p` |
| Load balancer | **AWS ALB** | `AWSALB` / `AWSALBCORS` cookies, `server: awselb/2.0` |
| Web server | **nginx** | `server: nginx` |
| Content platform | **NYC.gov Content API** | site is a JS shell (`content-loader.js`, `content-config.js`, `nav-template.js`) that fetches from `apps.nyc.gov/content-api/v1/content/cityclerk` and `/content-api/v2/nav/cityclerk` (JSON) |
| Front-end libs | jQuery 1.9.1, Bootstrap, Popper, Colorbox | `src=".../jquery-1.9.1.js"`, `bootstrap.min.js` |
| Analytics | **WebTrends** | `webtrends_v10.js`, `agency-wt.js` |
| Real-user monitoring | **Dynatrace** | `ruxitagentjs`, `x-oneagent-js-injection: true`, `dtCookie` |

This is the **newer NYC.gov chassis** — a thin JavaScript site over a shared, undocumented JSON **Content API**. It is content only; every real transaction lives on a separate platform below.

## Project Cupid — the marriage transaction layer

The Marriage Bureau's flagship transaction system is **not** a City Clerk-built app. It is a no-code application on a rented platform:

| Property | Value | Evidence |
|---|---|---|
| Host | `projectcupid.cityofnewyork.us` (reached via `nyc.gov/cupid`) | redirect chain through `AkamaiGHost` → nginx |
| Application | Online marriage-license application, appointment scheduling, ceremony booking | `/app/cupidceremony#/display/...` hash-routed SPA |
| Platform | **Unqork (no-code)** | `polyfill.unqork.io`, `/fbu/` + `uapi` Unqork API routes, `UNQORK`/`moduleId` markers |
| UI framework | Angular SPA | Angular runtime markers, `ENVIRONMENT` config block |
| RUM | Akamai mPulse (`boomerang`) + Google Tag Manager | `s.go-mpulse.net/boomerang`, `GTM-K3TFGXF` |
| Requirement | JavaScript-only, session-gated | SPA; login-walled |

There is **no documented API, no OpenAPI, no public JSON contract**. The city's single most personal civic transaction — getting married — runs entirely inside a **rented no-code vendor's** screens, and (unlike the lobbying side) emits **no Open Data at all**.

## e-Lobbyist & Lobbyist Search — the lobbying layer

| Property | Value | Evidence |
|---|---|---|
| e-Lobbyist host | `apps.nyc.gov/elobbyist/` | redirect from `www1.nyc.gov/elobbyist/` |
| e-Lobbyist app | **Java servlet** (Struts/Spring `.do`) | `JSESSIONID`, `.do` actions, `Path=/elobbyist` |
| Authentication | **SAP Customer Data Cloud / Gigya** SAML SSO | form action to `fidm.us1.gigya.com/saml/v2.0/.../idp/sso` |
| Lobbyist Search host | `lobbyistsearch.nyc.gov` | `<title>Elobbyist Search</title>` |
| Lobbyist Search app | JS SPA (webpack) over a `.do` Java backend | `main.<hash>.js` bundle, `.do` |

The lobbying side is the **more open half**: filing is login-walled, but the reported data is published to two NYC Open Data datasets and browsable through the public Lobbyist Search. Even so, neither Search nor e-Lobbyist exposes a **documented** API.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, service layer locked in a vendor CRM → *unlock*.
- **CFB** = real undocumented search API, the one write locked in a filing app → *document*.
- **City Clerk** = the two core citizen transactions run on **rented platforms** (Unqork no-code for marriage, SAP CDC/Gigya for lobbyist), and the flagship (marriage) has **no API and no data** → **contract** — put an owned API contract in front of the rented transaction machinery.

## Modernization implications

1. **The gap is ownership of the transaction, not the data.** The lobbying side already publishes; the marriage side publishes nothing and is fully outsourced to a no-code vendor.
2. **Front the rented platforms with an owned API.** A modern City Clerk API ([OpenAPI](openapi/cityclerk.yaml)) should present the open lobbyist data as clean resources *and* expose the marriage side's core write workflow — submitting a **marriage-license application** — instead of leaving couples to an Unqork SPA.
3. **Renting the machinery of the city's most personal transaction is a governance and continuity risk.** An agent-native contract in front of it ([MCP artifact](mcp/cityclerk-mcp.json)) is the low-hanging fruit.
