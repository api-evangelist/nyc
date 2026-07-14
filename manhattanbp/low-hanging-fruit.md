# Low-Hanging Fruit Index — Manhattan Borough President

**Agency:** Office of the Manhattan Borough President (MBPO) — Borough President Brad Hoylman-Sigal
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `manhattanbp.nyc.gov/robots.txt` disallows nothing). Fingerprinted the site `manhattanbp.nyc.gov` (Cloudflare + WP Engine + **WordPress / Divi theme** + Forminator forms + Google Site Kit) from response headers and page markup. Verified the NYC Open Data agency label `Manhattan Borough President (MBPO)` via the Socrata Discovery API and pulled all **21** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-manhattanbp.md](opendata-manhattanbp.md).

## Headline findings

1. **The data is open — but fragmented.** Contrary to the "borough presidents publish only PDFs" hypothesis, the office maintains **21 NYC Open Data datasets** (ULURP recommendations, appointments, community-board leadership, constituent services, and years of funding awards). The catch: it publishes **one dataset per program per fiscal year** — `Capital Grant Awards` alone is **five** separate datasets (2014–2018).
2. **The site is a generic WordPress/Divi template.** `manhattanbp.nyc.gov` is an off-the-shelf WordPress build (Divi theme, a stack of Divi add-on plugins, Forminator forms) on WP Engine behind Cloudflare. Its only API is the **default WordPress REST API** — nothing purpose-built for the office's civic work.
3. **The flagship citizen action has no API.** Applying to serve on a **community board** — the office's most public transaction — is a WordPress/Forminator web form (or a downloadable PDF), with no machine-readable contract and no Open Data twin.
4. **Five identical offices.** All five borough presidents run near-identical thin sites and publish the same shapes of data under parallel Socrata labels — the case for building the API once.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a vendor-CRM service layer; **Manhattan BP = federate.** Here the data is already open but scattered across per-year datasets, the site is a generic WordPress template, and the office is one of five structurally identical borough presidents — so the work is least about liberating data and most about giving these thin, duplicated offices **one owned, shared Borough President API** (and a real write surface for community-board applications).

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Community Boards (12) | `CommunityBoard` | SODA + site | ✅ Community Board Leadership (`3gkd-ddzn`, 26c) |
| 2 | ULURP Recommendations | `LandUseRecommendation` | SODA (PDF-linked) | 🟡 ULURP Recommendations (`gt5i-dmde`) — body is a PDF |
| 3 | BP Appointments | `BoardAppointment` | SODA | ✅ BP Appointments (`nr9n-yqxr`) |
| 4 | Funding Awards (capital/tourism/community/MCAP) | `FundingAward` | SODA (×9) | ✅ but fragmented — Capital 2014–2018 + Tourism + Community + MCAP + Police-Community |
| 5 | Legislation / policy | `Legislation` | SODA (link-out) | 🟡 Legislation (`uf8p-ervp`) — external URLs |
| 6 | Constituent Services | `ConstituentCase` | SODA | 🟡 Constituent Services (`39qw-754y`) — de-identified |
| 7 | **Apply to serve on a community board** | `CommunityBoardApplication` | Forminator form + PDF | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 21 MBPO datasets (the one real, open data API; fragmented by year/program).
- **WordPress REST API** — the site's only API; generic CMS content, nothing purpose-built.
- **Forminator** — the community-board application and intake forms; HTML forms, no contract.
- Platform: **WordPress + Divi theme on WP Engine, behind Cloudflare** (Google Site Kit, GTranslate) — the fifth distinct platform after Parks' Smarty/PHP, DOE's Sitefinity/.NET, Council's WordPress, and NYCHA's NYC.gov Livesite + Oracle Siebel.

## Reverse-engineered entities

`CommunityBoard` · `LandUseRecommendation` (ULURP; body is a PDF) · `BoardAppointment` · `FundingAward` (unifies five per-year capital datasets + tourism/community/MCAP/police-community) · `Legislation` (links out) · `ConstituentCase` (de-identified) · `CommunityBoardApplication` (net-new write) — join keys: **community board (1–12)**, **council district**, **BBL/BIN**, **fiscal year**.

## Next

1. **JSON Schema** per entity, unifying the fragmented per-year funding datasets and the geography spine — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open data as clean resources + the net-new `POST /community-board-applications` — done ([openapi/manhattanbp.yaml](openapi/manhattanbp.yaml)).
3. **MCP** artifact: `find_community_boards`, `find_land_use_recommendations`, `find_board_appointments`, `find_funding_awards`, `find_legislation`, `find_constituent_cases`, `list_my_applications`, `apply_to_community_board` — done ([mcp/manhattanbp-mcp.json](mcp/manhattanbp-mcp.json)).
4. **Federate:** template this contract across the other four borough presidents (Brooklyn, Bronx, Queens, Staten Island) as one shared Borough President API.
