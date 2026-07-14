# Low-Hanging Fruit Index — NYC Law Department

**Agency:** New York City Law Department (Office of the Corporation Counsel)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/law` (Akamai + nginx + NYC.gov "Livesite" v22 + Dynatrace) — the shared citywide chassis, with no Law-specific portal or application system. Verified the NYC Open Data agency label `Law Department (LAW)` via the Socrata Discovery API and pulled all **7** assets with column schemas. Separately confirmed the claims/settlement ledger is published by the **Office of the Comptroller** (`ex6k-ym48`), not by Law.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-law.md](opendata-law.md).

## Headline findings

1. **The Law Department is agency-facing.** It is the City's in-house law firm, with almost **no citizen-facing transactions**. Its public site runs the same shared NYC.gov "Livesite" chassis as every other agency — there is no Law-specific portal, search vendor, or application system.
2. **Its Open Data is thin and stale.** Only **7 datasets** under `Law Department (LAW)`, every one flagged **'No' automation / 'Annually'** updated: a civil-litigation case index, a divisions list, three publication feeds (press releases / speeches / columns), M/WBE statistics, and a pro bono program list.
3. **The core data belongs to another agency.** The ledger of **claims filed and settlement dollars** is the **Comptroller's** (`ex6k-ym48`), not Law's. Law's own litigation dataset (`pjgc-h7uv`) is a case **index**, not the claims record.
4. **No service layer, no write surface.** Nothing a resident *does* with the Law Department has a machine-readable contract; the one citizen-initiated transaction — applying for a legal internship — is handled by email/PDF.

> **Reframe (fifth distinct pattern):** Parks = *replatform*; DOE = *reclaim*; Council = *consolidate + own*; NYCHA = *unlock*; **Law = catalog.** Here there is little to liberate and no service layer to unlock — the work is to *catalog* the seven thin datasets into one owned contract, route claims questions to the Comptroller, and give the one public-initiated transaction (applying to work there) an owned, agent-native API.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Civil Litigation Case Index | `LegalCase` | SODA | 🟡 Civil Litigation (`pjgc-h7uv`, 17c) — index only |
| 2 | Claims & Settlements | `LegalCase` | SODA (Comptroller) | ↪ `ex6k-ym48` — **Comptroller, not Law** |
| 3 | Legal Divisions | `LegalDivision` | SODA | ✅ LAW Divisions (`4se9-mk53`, 2c) |
| 4 | Publications (releases/speeches/columns) | `Publication` | SODA (×3) | ✅ `kewa-q4dq` / `g7ir-4pf8` / `d84z-5kap` |
| 5 | M/WBE Statistics | `MwbeStatistic` | SODA | ✅ M/WBE Statistics (`svyi-maaj`, 7c) |
| 6 | Public Service Program (pro bono) | `PublicServiceProgram` | SODA | ✅ Public Service Program (`yk6f-pa7p`, 1c) |
| 7 | **Apply for a legal internship** | `LawInternshipApplication` | email / PDF | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 7 Law datasets (the only open API; thin, annual reference data).
- **Office of the Comptroller** — publishes the real claims/settlement ledger (`ex6k-ym48`) — a *different* agency.
- Platform: the informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, AWS ALB, Dynatrace RUM) — the same shared chassis as NYCHA's informational side; no Law-specific technology.

## Reverse-engineered entities

`LegalCase` (litigation index; claims dollars owned by the Comptroller) · `LegalDivision` · `Publication` (press release / speech / column) · `MwbeStatistic` · `PublicServiceProgram` · `LawInternshipApplication` (net-new write) — join keys: **docket/index**, **division name**, **Lead BBL** (litigation only).

## Next

1. **JSON Schema** per entity, reconciling the real Open Data column names — done ([schemas/](schemas/)).
2. **OpenAPI** cataloging the seven datasets as clean resources + the net-new `POST /internship-applications` — done ([openapi/law.yaml](openapi/law.yaml)).
3. **MCP** artifact: `find_cases`, `get_case`, `find_divisions`, `find_publications`, `find_mwbe_statistics`, `find_public_service_program`, `list_my_internship_applications`, `submit_internship_application` — done ([mcp/law-mcp.json](mcp/law-mcp.json)).
