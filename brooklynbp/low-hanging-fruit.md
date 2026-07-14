# Low-Hanging Fruit Index — Brooklyn Borough President

**Agency:** Office of the Brooklyn Borough President (BPBK) — Antonio Reynoso
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt). The brief's target `brooklyn-usa.org` has been **let go** — its `www` and apex both 301-redirect offsite to `batman-news.com` via WordPress domain-flip plugins on WPX Cloud (`bm-bulker-api` / `bm-migration-api` namespaces). The live office site is **`www.brooklynbp.nyc.gov`**, fingerprinted as **headless WordPress on WP Engine + Next.js behind Cloudflare**, exposing a live WordPress REST API and The Events Calendar plugin API. Verified the NYC Open Data agency label **`Brooklyn Borough President (BPBK)`** via the Socrata Discovery API and pulled all **21** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-brooklynbp.md](opendata-brooklynbp.md).

## Headline findings

1. **The office let its own domain go.** `brooklyn-usa.org` now redirects offsite to `batman-news.com` (a domain-flip WordPress on WPX Cloud). The live site is `www.brooklynbp.nyc.gov` — headless WordPress on WP Engine with a Next.js front end, behind Cloudflare.
2. **There are 21 open datasets, not zero.** Contrary to the brief's guess, `Brooklyn Borough President (BPBK)` publishes 21 NYC Open Data assets: ULURP recommendations, a community-board contact list, a dozen 'BP Appointments' tables, and capital/discretionary/tourism awards.
3. **But it is fragmented and unowned.** 21 single-purpose Socrata IDs, many thin (3-6 columns), several stale snapshots (Cornerstone Awards 2015-2017, Discretionary Contract Awards 2017-2018). The one live, purpose-shaped API is generic CMS plumbing — the WordPress REST API (315 posts) and The Events Calendar (`tribe/events/v1`).
4. **No write surface for the core constituent action.** Applying to serve on a **community board** — the office's most consequential yearly interaction with residents — is only an unstructured web form.

> **Reframe (fifth distinct pattern):** Parks = *replatform*; DOE = *reclaim*; Council = *consolidate + own*; NYCHA = *unlock*; **Brooklyn BP = template.** The raw material is plentiful but scattered across 21 datasets and a CMS API, owned by no one as *the BP's API*, on an office that even let its `.org` lapse. And because all five Borough Presidents run near-identical thin offices with the same powers, the highest-leverage move is to define **one shared, templated Borough President API** and instantiate it per borough — not to rebuild it five times.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | ULURP Land Use Recommendations | `LandUseRecommendation` | SODA | ✅ ULURP Recommendations (`4j6i-9rmr`, 6c) |
| 2 | Community Boards | `CommunityBoard` | SODA | ✅ Community Board Contact List (`dy27-rrad`, 16c) |
| 3 | BP Board Appointments | `BoardAppointment` | SODA (×7) | 🟡 BIDS (`pvxf-9irb`) + CEC/HHC/BPL/DYCD/SWAB/Misc |
| 4 | Funding Awards (capital/discretionary/tourism) | `FundingAward` | SODA (×4) | 🟡 Tourism Grants (`rma9-fm39`) + capital/discretionary |
| 5 | Publications (legislation/reports/testimony/press) | `Report` | SODA + WP REST | 🟡 Legislation - Passed (`e6ph-9uv7`) + CMS posts |
| 6 | Events & Hearings | `Event` | **The Events Calendar REST (live)** | ✅ live API (no Socrata twin) |
| 7 | Meeting requests / assistance | `CommunityBoardApplication` | Web form | ❌ form dump (`gqzy-vhwd`, `y6ds-67d5`) |
| 8 | **Apply to a community board** | `CommunityBoardApplication` | Web form | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 21 BPBK datasets (real, open; fragmented and partly stale).
- **The Events Calendar REST API** — the one live, BP-shaped read feed (hearings, board meetings).
- **WordPress REST API** — generic CMS content (315 posts, 74+ pages).
- Platform: headless **WordPress on WP Engine** + **Next.js**, behind **Cloudflare** — the fifth distinct platform after Parks' Smarty/PHP, DOE's Sitefinity/.NET, Council's WordPress, and NYCHA's Livesite + Oracle Siebel.
- **Lapsed domain:** `brooklyn-usa.org` → `batman-news.com` (WPX Cloud domain-flip).

## Reverse-engineered entities

`LandUseRecommendation` (ULURP) · `CommunityBoard` · `BoardAppointment` (consolidating a dozen board tables) · `FundingAward` (capital/discretionary/tourism) · `Report` (legislation/testimony/press) · `Event` (live Events Calendar) · `CommunityBoardApplication` (net-new write) — join keys: **ULURP Number**, **Community Board number (1-18)**, **Council District**, **Fiscal Year**, **BBL/BIN**.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (ULURP Number(s), Board Number, Funded Amount, appointee/term fields, the geography spine) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open data + events feed as clean resources + the net-new `POST /community-board-applications` (apply to a board) — done ([openapi/brooklynbp.yaml](openapi/brooklynbp.yaml)).
3. **MCP** artifact: `find_land_use_recommendations`, `get_land_use_recommendation`, `find_community_boards`, `find_appointments`, `find_funding_awards`, `find_reports`, `find_events`, `apply_to_community_board`, `get_application_status` — done ([mcp/brooklynbp-mcp.json](mcp/brooklynbp-mcp.json)).
4. **Template across all five Borough Presidents** — the distinguishing move for this domain.
