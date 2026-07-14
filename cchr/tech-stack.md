# Technology & Vendor Inventory — CCHR

What the NYC Commission on Human Rights' public surface is built on and which third parties it depends on — fingerprinted from response headers and page markup during the crawl (2026-07-13). CCHR is a **single-surface, thin-data** domain: one informational/transactional site on the shared NYC.gov platform, whose most important feature — reporting discrimination — is a **plain server-rendered HTML form**, not an application with an API.

## One front door

| Surface | URL | What it does |
|---|---|---|
| Informational + intake site | `www.nyc.gov/site/cchr/` | About, the Human Rights Law, legal library, complaint process, trainings/workshops — and the **Report Discrimination** intake form |

There is no separate resident portal, no self-service account, no vendor case-management UI exposed to the public. The enforcement backend (Law Enforcement Bureau case management, Office of Mediation) is entirely opaque — nothing about it is observable from outside.

## The site (nyc.gov/site/cchr)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed`, `server-timing: cdn-cache; …`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| Load balancer | **AWS Application Load Balancer** | `set-cookie: AWSALB…`, `AWSALBCORS…` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme; `JSESSIONID` (Java app server) |
| Real-user monitoring | **Dynatrace** + **Akamai mPulse / Boomerang** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid`; `go-mpulse.net` / `BOOMR` snippet |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on (the same platform seen on the NYCHA informational site) — it is not a CCHR-specific stack.

## The Report Discrimination form — the important part

The Commission's core citizen transaction is the **Report Discrimination** page (`/about/report-discrimination.page`). It is a **native Livesite HTML form**, server-rendered, with typed-looking fields but **no machine-readable contract**:

| Property | Value | Evidence |
|---|---|---|
| Kind | Server-rendered HTML `<form>` on the Livesite platform | fields inlined in page markup (not a JS SPA, not a vendor iframe) |
| Fields | Your Name/Pronouns/Address/Email/Phone; Category of Discrimination; respondent name/location/phone; date of most recent incident; prior-complaint Yes/No; free-text problem; up to 3 attachments; "how did you hear about us" | visible form markup |
| Submission target | Opaque NYC.gov intake/case backend (Law Enforcement Bureau); a generic `apps.nyc.gov/nyc-mailform/validation` endpoint is referenced for validation | page markup |
| Contract | **None** — no OpenAPI, no JSON API, no documented POST schema; the form is the only interface | crawl |

Every field a person fills in is discarded as structured data the moment it leaves the browser: it posts into an opaque backend and, downstream, only re-surfaces as three aggregate counts on Open Data (inquiries, mediations, pre-complaint resolutions). The **category** choices on the form map one-to-one to the **columns** of the Inquiries Received dataset — evidence that structure exists internally but is never exposed.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data wide open, service layer locked in a vendor CRM (Siebel) → *unlock*.
- **CCHR** = almost **nothing is machine-readable** — the law is prose, the guidance is PDF, the intake is an untyped web form, and Open Data is three aggregate tallies → **structure the intake and the law into typed contracts**.

## Modernization implications

1. **The gap is structure, not vendor lock-in.** Unlike NYCHA, CCHR isn't trapped in a packaged CRM. Its core transaction runs on the city's own platform as a plain form. What's missing is a **typed contract** for that form and for the legal vocabulary behind it.
2. **Give the Report Discrimination form a real write API.** A modern CCHR API ([OpenAPI](openapi/cchr.yaml)) should turn "report discrimination" into a typed `POST /complaints` — capturing protected class(es), area, respondent, and incident as structured data from the first keystroke — instead of an HTML form whose data is only ever seen again as an annual tally.
3. **Publish the law as data.** Protected classes and legal guidance are the Commission's reference corpus; today they are prose and PDF. Turning them into resources ([schemas](schemas/)) makes "is X protected in housing?" answerable by an agent.
4. **An agent-native contract in front of it** ([MCP artifact](mcp/cchr-mcp.json)) is the low-hanging fruit — so a person (or their agent) can ask "am I protected?" and "help me report this" in one place.
