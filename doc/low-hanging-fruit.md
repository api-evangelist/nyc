# Low-Hanging Fruit Index — DOC

**Agency:** New York City Department of Correction (DOC)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/doc` (Akamai + nginx + NYC.gov "Livesite" platform v22 + Dynatrace) and the **Inmate Lookup Service** linked from it, identified as the **"P.I.C. Lookup"** at `a073-ils-web.nyc.gov/inmatelookup` — a legacy **Apache MyFaces (JavaServer Faces)** web app (`javax.faces.ViewState`, `myfaces`, WebSphere-style `JSESSIONID`) with no API. Verified the NYC Open Data agency label `Department of Correction (DOC)` via the Socrata Discovery API and pulled all **15** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-doc.md](opendata-doc.md).

## Headline findings

1. **DOC is transparency-heavy but transaction-poor.** **15 NYC Open Data datasets** publish the daily in-custody population, admissions/discharges, deaths, and five more parallel safety/security incident streams, plus Local Law 33/85 security and visitation indicators.
2. **It also runs a live custody lookup — with no API.** The **Inmate Lookup Service / "P.I.C. Lookup"** (`a073-ils-web.nyc.gov`) is a real-time person-in-custody search, but it is a legacy **JavaServer Faces** application: postback/view-state, JavaScript-only, no OpenAPI, no JSON.
3. **The public transactions have no surface at all.** **Scheduling a visit** and **filing a complaint / records request** — the things the public needs to *do* — are phone/mail/in-person or vendor/OpenRecords portals, with no API and no status contract.
4. **Two disconnected views of the same person.** Open Data publishes an anonymized daily snapshot (`INMATEID` only); the live lookup returns a named record keyed on NYSID / Book & Case number. Neither is an API, and nothing joins them.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a service layer in a vendor CRM; **DOC = expose the live lookup and the missing writes.** Here the accountability data is already open and a real-time lookup already runs — the work is to give that lookup an owned, agent-native API and to add the **visit** and **complaint/records-request** transactions that today live only offline.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Daily Inmates In Custody | `PersonInCustody` | SODA | ✅ Daily Inmates In Custody (`7479-ugqb`, 13c) |
| 2 | Inmate Lookup ("P.I.C. Lookup") | `PersonInCustody` | Live JSF app | ❌ no API (live, but JSF only) |
| 3 | DOC Facilities (jails) | `Facility` | site + derived | 🟡 derived from `FACILITY` dimension |
| 4 | Safety & Security Incidents | `IncidentReport` | SODA (×6) | ✅ Deaths/Slashing/Fights/Assault/Injuries/Lock-In |
| 5 | Daily Population & Security Indicators | `DailyPopulation` | SODA | ✅ Local Law 33 (`2wuc-x56b`) + waitlist/medical/LL85 |
| 6 | **Schedule a visit** | `Visit` | Vendor / offline | ❌ **net-new** (LL85 aggregate only) |
| 7 | **File a complaint / records request** | `Complaint` | OpenRecords / offline | ❌ **net-new** |
| 8 | Hart Island Burial Records | `PersonInCustody` | SODA | ✅ Hart Island Burial Records (`f5mc-f3zp`) |
| 9 | Aggregate Employee Statistics | `DailyPopulation` | SODA | ✅ Aggregate Employee Statistics (`eddp-3v5g`) |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 15 DOC datasets (the one real, open API; accountability data only).
- **Apache MyFaces (JSF)** — the Inmate Lookup Service / "P.I.C. Lookup"; live, but browser-only, no API.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, Dynatrace RUM) — the same chassis as the earlier domains; DOC's distinct technology is the legacy JSF lookup.

## Reverse-engineered entities

`PersonInCustody` (INMATEID; live keys NYSID / Book & Case) · `Facility` (derived; mostly Rikers Island) · `DailyPopulation` (security indicators, ADP) · `IncidentReport` (six unified incident streams) · `Visit` (net-new write) · `Complaint` (net-new write; complaint / records / FOIL) — join keys: **INMATEID**, **NYSID**, **Book & Case number**, **INCIDENT_ID**, **FACILITY**.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (INMATEID, INCIDENT_ID, the FACILITY dimension) and the live lookup keys (NYSID, Book & Case) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open accountability data and the live lookup as clean resources + the net-new `POST /visits` (schedule a visit) and `POST /complaints` (file a complaint / records request) — done ([openapi/doc.yaml](openapi/doc.yaml)).
3. **MCP** artifact: `find_people_in_custody`, `get_person_in_custody`, `find_facilities`, `find_daily_population`, `find_incidents`, `list_my_visits`, `schedule_visit`, `file_complaint` — done ([mcp/doc-mcp.json](mcp/doc-mcp.json)).
