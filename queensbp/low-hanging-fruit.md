# Low-Hanging Fruit Index — Queens Borough President

**Agency:** Office of the Queens Borough President (QBP)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `queensbp.nyc.gov/robots.txt` is a Yoast block that disallows nothing, `Crawl-delay: 10`). `queensbp.org` **301-redirects to `www.queensbp.nyc.gov`**, fingerprinted as **WordPress (Divi + Elementor) on WP Engine behind Cloudflare** (Yoast, Wordfence, Google Language Translator) from headers, `wp-json` namespaces, theme markup, and `sitemap_index.xml`. Confirmed the WordPress REST API (`/wp-json/wp/v2`) is enabled but **empty** (`X-WP-Total: 0` for posts and the `project` custom post type). Verified the NYC Open Data agency label `Queens Borough President (QBP)` via the Socrata Discovery API and pulled all **2** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-queensbp.md](opendata-queensbp.md).

## Headline findings

1. **A thin WordPress/Divi brochure on nyc.gov.** `queensbp.org` redirects to `www.queensbp.nyc.gov`, a Divi page-builder site on WP Engine behind Cloudflare — a fifth distinct platform after Parks, DOE, Council, and NYCHA.
2. **The REST API is switched on but empty.** WordPress ships `/wp-json/wp/v2`, and it is public and reachable — but returns **0 posts and 0 `project` entries** because content is authored as Divi Pages. The one machine-readable surface the office already owns is dormant.
3. **Open Data is nearly absent — but not zero.** Exactly **two** datasets, both about community boards: members (`rps4-dwwk`, 4c) and district managers & chairs (`8z5h-tzdr`, 20c).
4. **The core BP acts have no contract.** Advisory **land-use (ULURP) recommendations**, tens of millions in **discretionary funding**, events, and press releases are HTML/PDF only.

> **Reframe (fifth distinct pattern):** Parks = *replatform*; DOE = *reclaim*; Council = *consolidate + own*; NYCHA = *unlock*; **Queens BP = standardize.** There is barely anything to liberate here, and all five borough presidents run near-identical thin sites. The low-hanging fruit is not a fifth one-off API — it is **one shared Borough President API standard** each borough implements, starting by lighting up the WordPress REST API the platform already ships and adding the one write the office actually runs on paper: applying to serve on a community board.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Community Boards (managers & chairs) | `CommunityBoard` | SODA | ✅ District Managers & Chairs (`8z5h-tzdr`, 20c) |
| 2 | Community Board Members | `CommunityBoardAppointment` | SODA | ✅ Members (`rps4-dwwk`, 4c) |
| 3 | Land Use / ULURP recommendations | `LandUseRecommendation` | Divi HTML/PDF | ❌ gap |
| 4 | Discretionary funding | `DiscretionaryFundingAward` | Divi HTML | ❌ gap |
| 5 | Events | `Event` | Divi Pages (WP REST returns 0) | ❌ gap |
| 6 | Newsroom press releases | `PressRelease` | WordPress, **but REST returns 0** | 🟡 API exists but empty |
| 7 | **Apply to a community board** | `CommunityBoardApplication` | HTML/PDF form | ❌ **net-new** |
| 8 | Constituent services request | `CommunityBoardApplication` | HTML form | ❌ gap |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **WordPress REST API (`wp/v2`)** — enabled and public, but **empty** (0 posts / 0 projects). The dormant surface.
- **Socrata SODA** — two QBP datasets, both community boards (the only substantive machine-readable data).
- Platform: **WordPress / Divi on WP Engine behind Cloudflare** (Yoast, Wordfence, Google Language Translator) — the fifth distinct platform after Parks' Smarty/PHP, DOE's Sitefinity/.NET, Council's WordPress, and NYCHA's Livesite + Oracle Siebel.

## Reverse-engineered entities

`CommunityBoard` · `CommunityBoardAppointment` · `LandUseRecommendation` (ULURP) · `DiscretionaryFundingAward` · `Event` · `PressRelease` · `CommunityBoardApplication` (net-new write; also stands in for the constituent-services request) — join keys: **community board number**, the NYC **geography spine** (BBL/BIN, council district, census tract, NTA), and **ULURP number**.

## Next

1. **JSON Schema** per entity, reconciling the two Socrata datasets' real column names and the NYC geography spine — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the community-board data + land-use/funding/newsroom as clean resources + the net-new `POST /community-board-applications` — done ([openapi/queensbp.yaml](openapi/queensbp.yaml)).
3. **MCP** artifact: `find_community_boards`, `get_community_board`, `find_community_board_members`, `find_appointments`, `find_land_use_recommendations`, `find_discretionary_funding`, `find_events`, `find_press_releases`, `apply_to_community_board` — done ([mcp/queensbp-mcp.json](mcp/queensbp-mcp.json)).
4. **Generalize:** propose the same contract as a **shared Borough President API** across all five boroughs.
