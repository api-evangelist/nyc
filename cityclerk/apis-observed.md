# APIs Observed While Crawling — City Clerk

Backend/service APIs the City Clerk surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is asymmetric across the two bureaus: **the Lobbying Bureau's reported data is open (SODA over 2 datasets + a public Lobbyist Search), but the Marriage Bureau's transaction system has no machine-readable surface at all** — it runs on the rented Unqork no-code platform. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`apps.nyc.gov/content-api/v1/content/cityclerk`** + **`/v2/nav/cityclerk`** | Content API | NYC (OTI) shared platform | **JSON, undocumented** | Real JSON backend that drives `cityclerk.nyc.gov` (page content + navigation tree). Read-only, shared across NYC.gov agency sites, no OpenAPI. Content only — no transactions. |
| **`projectcupid.cityofnewyork.us/app/cupidceremony`** | Marriage-license / appointment system | NYC City Clerk (on **Unqork**) | Login-walled SPA; **no API** | Apply for a marriage license, schedule appointments, book ceremonies. Built on the rented Unqork no-code platform (`polyfill.unqork.io`, `/fbu/` uapi, Angular SPA). No JSON/OpenAPI surface; **no Open Data twin either**. The net-new write surface. |
| **`apps.nyc.gov/elobbyist`** | Lobbyist filing application | NYC City Clerk (Java) | Login-walled; **no API** | Lobbyist registration and periodic filing. Java servlet (`.do`, `JSESSIONID`) behind **SAP CDC / Gigya** SAML SSO. Reported data is published to Open Data. |
| **`lobbyistsearch.nyc.gov`** | Public lobbyist search database | NYC City Clerk | Public SPA; **no documented API** | Lobbyist Search — JS SPA (webpack) over a `.do` Java backend. Public but contract-less. |
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 2 City Clerk datasets (eLobbyist Data `fmf3-knd8`; Fundraising & Political Consulting Reports `7arw-dbem`), each a SODA `/resource/<id>.json` endpoint. The one open, machine-readable City Clerk API — lobbying only. |
| `cityclerkforms.nyc.gov/cityclerkformsonline` | Forms application | NYC City Clerk (Java) | HTML forms; no API | Officiant registration, records requests. Server-rendered Java forms app. |
| Akamai edge / mPulse | CDN + RUM API | Akamai | Vendor | `AkamaiGHost`, `boomerang` beacon on Project Cupid. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `ruxitagentjs` / `x-oneagent-js-injection` on the informational site and e-Lobbyist. |

## Takeaways

- **The API story splits by bureau.** The Lobbying Bureau publishes its reported data (SODA + Lobbyist Search); the Marriage Bureau publishes nothing and runs on a rented no-code platform.
- **No API for the flagship transaction.** Applying for a **marriage license** — the single most common Marriage Bureau interaction — has no machine-readable contract at all; it is reachable only through Project Cupid's Unqork SPA.
- **The content site got a modern JSON backend, quietly.** `apps.nyc.gov/content-api/v1` is a real Content API, but it is undocumented, shared, and read-only.
- **Even the open side is contract-less.** e-Lobbyist and Lobbyist Search run on JSON/Java backends, but neither exposes a documented API or OpenAPI.
- **No agent-native surface.** The [OpenAPI](openapi/cityclerk.yaml) + [MCP artifact](mcp/cityclerk-mcp.json) here propose one owned contract that publishes the open lobbyist data cleanly *and* unlocks the net-new `apply_for_marriage_license` write workflow.
