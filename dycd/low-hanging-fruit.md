# Low-Hanging Fruit Index — DYCD

**Agency:** NYC Department of Youth and Community Development (DYCD)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/dycd` (Akamai + nginx + NYC.gov "Livesite" v22 + Dynatrace + AWS ALB) and the **DYCD Connect** ecosystem — `dycdconnect.nyc` and the **DiscoverDYCD** program finder `discoverdycd.dycdconnect.nyc`, identified as an **Angular SPA on Microsoft-IIS/10.0** with a private internal `/api/` backend (Google Maps + Places). Verified the NYC Open Data agency label `Department of Youth and Community Development (DYCD)` via the Socrata Discovery API and pulled all **15** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-dycd.md](opendata-dycd.md).

## Headline findings

1. **DYCD is a split domain.** An informational site on the shared NYC.gov chassis, and the **DYCD Connect** ecosystem — including the **DiscoverDYCD** program finder — a custom Angular app on Microsoft-IIS with a **private, undocumented `/api/`** backend.
2. **DYCD is a funder/intermediary.** It doesn't deliver services directly; it contracts hundreds of community-based organizations (providers) to run programs (SYEP, COMPASS/SONYC, Beacon, Cornerstone) at physical **program sites**. The open data documents that supply chain.
3. **The supply-side data is well published.** **15 NYC Open Data datasets** cover program sites (`ebkm-iyma`, 34 columns with a full geography spine, slots, and participants), contracts, contractors/providers, Neighborhood Development Areas, and aggregate participant demographics (`k9kq-67vm`, 52 columns).
4. **But the finder is an app, not an API.** DYCD already built DiscoverDYCD to help the public find programs — yet its backend is private, there is no clean Open Data catalog of the offerings, and there is **no public API to apply** to a program.
5. **Participants stay private by design.** Demographics are published only in aggregate; no individual participant record is ever exposed.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a service layer locked in a vendor CRM; **DYCD = surface the finder.** Here the supply data is already open **and** DYCD already built a program finder — the work is least about liberating datasets and most about exposing the finder DYCD already owns as an agent-native API, and giving the one transaction that has none — **applying to a program** — an owned contract instead of a seasonal web form.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Program offerings (SYEP, COMPASS, Beacon…) | `Program` | DiscoverDYCD finder (app) | 🟡 taxonomy only; no catalog dataset |
| 2 | Program Sites | `ProgramSite` | SODA + map | ✅ DYCD Program Sites (`ebkm-iyma`, 34c) |
| 3 | Providers (contracted CBOs) | `Provider` | SODA | ✅ DYCD Contractors (`75e9-fg2t`) |
| 4 | Contracts | `Contract` | SODA | ✅ DYCD Contracts (`graj-69em`, 15c) |
| 5 | Neighborhood Development Areas | `ServiceArea` | SODA + map | ✅ NDAs (`vd7c-qjsx`) + map (`p57r-4v4f`) |
| 6 | Participant Demographics | `ParticipantDemographics` | SODA | 🟡 Participant Demographics (`k9kq-67vm`, 52c) — aggregate only |
| 7 | SYEP for NYCHA residents (LL163) | `ParticipantDemographics` | SODA | ✅ by borough/development/council (`x4x8-m3ds`…) |
| 8 | RHY reporting (LL79/81/86) | `ParticipantDemographics` | SODA | ✅ Daily Census (`5rw7-99k7`) + demographics/access/referrals |
| 9 | **Apply to a program (SYEP application)** | `ProgramApplication` | DYCD Connect / seasonal form | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 15 DYCD datasets (the one real, open API; supply-side data only).
- **DiscoverDYCD** — the program finder; Angular SPA on Microsoft-IIS with a **private, undocumented `/api/`**; Google Maps + Places.
- **DYCD Connect** — the provider/participant portal; login-walled, no public API.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, Dynatrace RUM, AWS ALB) — the same chassis as NYCHA, distinct from Parks' Smarty/PHP, DOE's Sitefinity/.NET, and Council's WordPress.

## Reverse-engineered entities

`Program` (offering; finder-only) · `ProgramSite` (core supply unit) · `Provider` (contracted CBO) · `Contract` · `ServiceArea` (Neighborhood Development Area) · `ParticipantDemographics` (aggregate Enrollment; never individual) · `ProgramApplication` (net-new write; apply to a program) — join keys: **PortfolioID**, **Contract Number**, **Provider**, **NDA**, and the NYC geography spine (**BBL/BIN**, council/community district, NTA).

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (PortfolioID, Contract Number, the geography spine, the program taxonomy) — done ([schemas/](schemas/)).
2. **OpenAPI** surfacing the finder + open supply data as clean resources + the net-new `POST /applications` (apply to a program) — done ([openapi/dycd.yaml](openapi/dycd.yaml)).
3. **MCP** artifact: `find_programs`, `get_program`, `find_program_sites`, `get_program_site`, `find_providers`, `find_contracts`, `find_service_areas`, `find_participant_demographics`, `list_my_applications`, `apply_to_program` — done ([mcp/dycd-mcp.json](mcp/dycd-mcp.json)).
