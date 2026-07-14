# cityclerk — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **New York City Office of the City Clerk (OCC)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (marriage-license application, ceremonies, lobbyist registration/filings, fundraising reports, and the locked Marriage Bureau transactions).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov Content API + Akamai/ALB/Dynatrace; **Project Cupid on the rented Unqork no-code platform**; e-Lobbyist Java app behind SAP CDC / Gigya SSO).
- [apis-observed.md](apis-observed.md) — the **open lobbying side** (Socrata SODA over 2 datasets + Lobbyist Search) vs. the **rented marriage side with no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (2 City Clerk datasets) with coverage verdicts.
- [opendata-cityclerk.md](opendata-cityclerk.md) / [opendata-cityclerk.json](opendata-cityclerk.json) — all 2 City Clerk Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `marriage-license` · `marriage-license-application` · `ceremony` · `lobbyist-registration` · `lobbyist-filing` · `fundraising-report` (+ shared `_common`).
- [openapi/cityclerk.yaml](openapi/cityclerk.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/cityclerk-mcp.json](mcp/cityclerk-mcp.json) — design-first MCP server definition (8 agent tools; artifact, not a deployment).

## What was found — the sixth distinct pattern

City Clerk is a **two-bureau domain running on rented platforms**, and that is the finding:

1. **The Marriage Bureau is fully outsourced.** **Project Cupid** (`projectcupid.cityofnewyork.us`) — where couples apply for a license, schedule appointments, and book ceremonies — is a **no-code application on the rented Unqork platform**. It has **no API and no Open Data twin**; NYC's most personal civic transaction runs entirely inside a vendor's screens.
2. **The Lobbying Bureau is the more open half.** **e-Lobbyist** (`apps.nyc.gov/elobbyist`) — a login-walled Java app behind rented **SAP CDC / Gigya** SSO — publishes its reported data to **2 NYC Open Data datasets** and a public **Lobbyist Search**.

**The gap here is ownership of the transaction, not the data.** A couple or agent asking "find us an appointment and apply for our marriage license" has nothing to call.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | CFB | **City Clerk** |
|---|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | Livesite + Siebel | IIS / ASP.NET | **Content API + Unqork + Gigya (rented)** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | service layer locked in a CRM | real API undocumented | **core transactions rented; marriage has no API or data** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **document** | **contract** |

## Reverse-engineered entities

`MarriageLicenseApplication` (net-new write) · `MarriageLicense` · `Ceremony` (appointment) · `LobbyistRegistration` (Registrant) · `LobbyistFiling` (periodic report) · `FundraisingReport` — join keys **REGISTRATION_ID**, **LOBBYIST_ID**, **CLIENT_ID**, and Project Cupid application/license ids.

## Method & caveats

Outside-in crawl (browser UA; robots-respecting). The informational site was fingerprinted from headers and its content-loader scripts (AWS ALB, Akamai, nginx, Dynatrace, WebTrends) and the shared NYC.gov Content API it fetches from. Project Cupid was identified as an Unqork no-code application from its landing markup (`polyfill.unqork.io`, `/fbu/` uapi, Angular SPA) without authenticating; e-Lobbyist as a Java app behind Gigya SSO from its `.do`/`JSESSIONID` markup and SAML form action. Open Data agency label verified via the Socrata Discovery API; both assets pulled with columns. A sample, not a full spider; the transaction systems' internal workflows are inferred from the City Clerk's documented services, not scraped behind login.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (2 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (8 paths/8 ops) ✅ · MCP artifact (8 tools) ✅.
- **Next:** an example implementation fronting Project Cupid for `apply_for_marriage_license`; then the next domain from [../domains.md](../domains.md).
