# Low-Hanging Fruit Index — Bronx Borough President

**Agency:** Office of the Bronx Borough President
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA; the site serves no real `robots.txt` — the path returns a 404 CMS page). Fingerprinted `bronxboropres.nyc.gov` (Oracle Cloud IP `129.153.208.86`) as a **Revize** government SaaS CMS — PHP front end (`index.php`, `news_detail_T4_R<n>.php`, `calendar.php`), Revize `document_center` + `revize_calendar` plugins, Bootstrap 4.6 / jQuery 3.7.1, JSP CMS admin at `cms2.revize.com/revize/security`. Verified the NYC Open Data agency label `Bronx Borough President (BPBX)` via the Socrata Discovery API and pulled all **2** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-bronxbp.md](opendata-bronxbp.md).

## Headline findings

1. **A thin brochure site on a vendor CMS.** The Bronx BP site is a Revize SaaS CMS (PHP front end, JSP back end) on Oracle Cloud — **not** the shared NYC.gov "Livesite" platform (`nyc.gov/site/bronxbp` 404s). It exposes **no API and no OpenAPI**.
2. **Only two entities are machine-readable.** NYC Open Data holds exactly **2** datasets under `Bronx Borough President (BPBX)`: Capital Funding (`mdgu-ar69`, 20c) and Bronx Community Boards (`wbau-xy7g`, 7c) — both essentially hand-published.
3. **The charter work is unstructured.** ULURP land-use recommendations are PDFs in a document center; the newsroom is PHP pages; events are a borrowed Google Calendar. None has a feed or a twin.
4. **Intake is analog.** Applying to serve on a community board is a downloadable PDF / email — no structured application, no confirmation, no status. That is the net-new write surface.

> **Reframe (fifth distinct pattern):** Parks = *replatform*; DOE = *reclaim*; Council = *consolidate + own*; NYCHA = *unlock*; **Bronx BP = templatize.** The problem here is less liberating trapped data (there is barely any) and more that the office is **one of five structurally identical Borough Presidents**, each running its own thin site. The fix is **one shared, templatable Borough President API** instantiated per borough — not a bespoke Bronx build.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Discretionary Funding Awards | `DiscretionaryFundingAward` | SODA | ✅ Capital Funding (`mdgu-ar69`, 20c) |
| 2 | Community Board Appointments | `CommunityBoardAppointment` | SODA | ✅ Bronx Community Boards (`wbau-xy7g`, 7c) |
| 3 | Land-Use / ULURP Recommendations | `LandUseRecommendation` | document-center PDFs | 🟡 PDFs only |
| 4 | Newsroom (releases, statements, letters, testimonies) | `PressRelease` | PHP pages | 🟡 HTML only |
| 5 | Events & Meetings | `Event` | Google Calendar | 🟡 borrowed |
| 6 | **Apply to a Community Board** | `CommunityBoardApplication` | PDF / email | ❌ **net-new** |
| 7 | Constituent Services / Advisory Councils | `CommunityBoardApplication` | static pages | ❌ gap |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 2 Bronx BP datasets (the only real, open data; funding + appointments).
- **Revize** — the government SaaS CMS running the whole site; no API.
- **Google Calendar** (via the Revize calendar plugin) — events; **Curator.io** social wall; **Constant Contact** newsletter; **UserWay** accessibility; **GA4** (`G-DMD6JC0H5S`).
- Platform: **Revize on Oracle Cloud** — the fifth distinct platform after Parks' Smarty/PHP, DOE's Sitefinity/.NET, Council's WordPress, and NYCHA's Livesite + Siebel.

## Reverse-engineered entities

`DiscretionaryFundingAward` · `CommunityBoardAppointment` (both open) · `LandUseRecommendation` (ULURP; PDFs) · `PressRelease` (newsroom) · `Event` (Google Calendar) · `CommunityBoardApplication` (net-new write) — join keys: **Community Board (1–12)**, **BBL/BIN**, **Council District**, **Fiscal Year**.

## Next

1. **JSON Schema** per entity, reconciling the two real Open Data column sets and the unstructured surfaces — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the funding + appointment data as clean resources, giving recommendations/newsroom/events a shape, and adding `POST /community-board-applications` — done ([openapi/bronxbp.yaml](openapi/bronxbp.yaml)).
3. **MCP** artifact: `find_discretionary_funding`, `find_community_board_appointments`, `find_land_use_recommendations`, `find_press_releases`, `find_events`, `apply_to_community_board`, `list_my_community_board_applications` — done ([mcp/bronxbp-mcp.json](mcp/bronxbp-mcp.json)).
4. **Templatize:** run the same contract across the four other Borough President offices from one shared definition.
