# Low-Hanging Fruit Index — City Clerk

**Agency:** New York City Office of the City Clerk (OCC)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt). Fingerprinted the informational site `cityclerk.nyc.gov` (AWS ALB + Akamai + nginx + Dynatrace; jQuery/Bootstrap; WebTrends), now driven by the NYC.gov **Content API** (`apps.nyc.gov/content-api/v1/content/cityclerk` + `/v2/nav/cityclerk`). Probed **Project Cupid** (`projectcupid.cityofnewyork.us/app/cupidceremony`), the online marriage-license/appointment system, identified as a no-code application on the rented **Unqork** platform (`polyfill.unqork.io`, `/fbu/` uapi, Angular SPA). Probed **e-Lobbyist** (`apps.nyc.gov/elobbyist`), a login-walled Java app (`JSESSIONID`, `.do`) behind **SAP CDC / Gigya** SSO, and the public **Lobbyist Search** (`lobbyistsearch.nyc.gov`). Verified the NYC Open Data agency label `Office of the City Clerk (OCC)` via the Socrata Discovery API and pulled all **2** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-cityclerk.md](opendata-cityclerk.md).

## Headline findings

1. **The City Clerk runs two bureaus on rented platforms.** The Marriage Bureau's **Project Cupid** is a no-code application on the rented **Unqork** platform; the Lobbying Bureau's **e-Lobbyist** is a login-walled Java app behind rented **SAP CDC / Gigya** SSO.
2. **The flagship transaction has no API and no data.** Applying for a **marriage license** — NYC's most personal civic transaction — lives only inside Project Cupid's Unqork screens. No API, no OpenAPI, **no Open Data twin**.
3. **The Lobbying Bureau is the more open half.** Registration and periodic filing happen inside e-Lobbyist, but the reported data *is* published — two NYC Open Data datasets (`fmf3-knd8`, `7arw-dbem`) plus a public Lobbyist Search.
4. **Marriage records aren't the City Clerk's on Open Data.** Only DORIS publishes historical vital-records indexes (`j62e-7maa`, `d8dr-nyhw`); the live marriage side is entirely closed.
5. **The content site got a modern JSON backend, quietly.** `apps.nyc.gov/content-api/v1` is a real, undocumented, read-only Content API.

> **Reframe (sixth distinct pattern):** Parks = *replatform*; DOE = *reclaim*; Council = *consolidate + own*; NYCHA = *unlock* a vendor CRM; CFB = *document* an undocumented API; **City Clerk = contract the rented machinery.** Here the two core citizen transactions run on rented platforms (Unqork no-code for marriage, Gigya SSO for lobbyist), and the flagship — applying for a marriage license — has no API and no data; the work is least about liberating datasets and most about putting an **owned API contract** in front of the rented transaction systems.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | **Apply for a marriage license** | `MarriageLicenseApplication` | Project Cupid (Unqork) | ❌ **net-new** |
| 2 | Book a ceremony / appointment | `Ceremony` | Project Cupid (Unqork) | ❌ gap (no API) |
| 3 | Marriage license (issued record) | `MarriageLicense` | Project Cupid (Unqork) | ❌ gap (DORIS historical only) |
| 4 | Marriage officiant registration | `MarriageLicenseApplication` | City Clerk Forms Online | ❌ gap (no API) |
| 5 | Lobbyist registration / Search | `LobbyistRegistration` | e-Lobbyist + Lobbyist Search | 🟡 eLobbyist Data (`fmf3-knd8`, 28c) |
| 6 | Lobbyist periodic filings | `LobbyistFiling` | e-Lobbyist | ✅ eLobbyist Data (`fmf3-knd8`, 28c) |
| 7 | Fundraising & political-consulting reports | `FundraisingReport` | e-Lobbyist | ✅ Fundraising Reports (`7arw-dbem`, 24c) |
| 8 | Commissioner of Deeds / Oath of Office | `LobbyistRegistration` | City Clerk Forms Online | ❌ gap (no API) |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Unqork** — Project Cupid, the marriage transaction system; rented no-code, no API, no Open Data.
- **SAP CDC / Gigya** — e-Lobbyist authentication; rented SSO.
- **Socrata SODA** — 2 City Clerk datasets (the one open, machine-readable API; lobbying only).
- **NYC.gov Content API** (`apps.nyc.gov/content-api/v1`) — the JSON backend behind the site; undocumented, read-only.
- Platform: informational site on the newer NYC.gov content-API chassis (AWS ALB, Akamai, nginx, Dynatrace, WebTrends) — distinct from Parks' Smarty/PHP, DOE's Sitefinity/.NET, Council's WordPress, NYCHA's Livesite/Siebel, and CFB's IIS/ASP.NET.

## Reverse-engineered entities

`MarriageLicenseApplication` (net-new write) · `MarriageLicense` · `Ceremony` (appointment) · `LobbyistRegistration` (Registrant) · `LobbyistFiling` (periodic report; `fmf3-knd8`) · `FundraisingReport` (`7arw-dbem`) — join keys: **REGISTRATION_ID**, **LOBBYIST_ID**, **CLIENT_ID**, and Project Cupid application/license ids.

## Next

1. **JSON Schema** per entity, reconciling the real Open Data column names (`LOBBYIST_ID`, `CLIENT_ID`, `PERIODIC_ID`, the fundraising `Report ID`) and the Project Cupid marriage shapes — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open lobbyist data as clean resources + the net-new `POST /marriage-license-applications` (apply for a marriage license) — done ([openapi/cityclerk.yaml](openapi/cityclerk.yaml)).
3. **MCP** artifact: `find_appointments`, `apply_for_marriage_license`, `get_marriage_license_application`, `get_marriage_license`, `find_lobbyist_registrations`, `get_lobbyist_registration`, `find_lobbyist_filings`, `find_fundraising_reports` — done ([mcp/cityclerk-mcp.json](mcp/cityclerk-mcp.json)).
