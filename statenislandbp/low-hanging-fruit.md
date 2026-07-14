# Low-Hanging Fruit Index — Staten Island Borough President

**Agency:** Office of the Staten Island Borough President (BPSI)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `statenislandusa.com/robots.txt` disallows only `/ajax/`, `/apps/`, and a couple of pages). Fingerprinted the site `www.statenislandusa.com` (**Weebly** behind **Cloudflare**; `x-host: *.weebly.net`, `weebly-anchor.js`, Constant Contact sign-up). Walked the sitemap and key pages (community board application, BP Assist, budget, borough board, events, notices, staff directory). Verified the NYC Open Data agency label `Staten Island Borough President (BPSI)` via the Socrata Discovery API and pulled all **2** assets.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-statenislandbp.md](opendata-statenislandbp.md).

## Headline findings

1. **This is the thinnest domain assessed.** The office's entire public surface is a **Weebly brochure site** behind Cloudflare — no CMS of record, no application, **no API**, no JSON.
2. **Two trivial datasets, and that is all.** Under the `Staten Island Borough President (BPSI)` label there are only `3fes-huds` (BP Assist Helpline Requests — *aggregate* annual counts by request type, ending FY20) and `mmut-uup9` (Category Master File — a zero-column blob).
3. **The office's actual charter work is invisible as data.** Land-use / ULURP recommendations, community board appointments, discretionary capital/expense funding, and Borough Board resolutions live only as PDFs and HTML, or inside *other* agencies' systems (City Planning ZAP, the adopted budget's Schedule C).
4. **The two real transactions are un-contracted.** BP Assist (report a pothole/litter/graffiti issue) is a web widget; the Community Board Membership Application is an opaque Weebly form posting to `weebly.com/apps/formSubmit.php`.

> **Reframe (fifth distinct pattern):** Parks = *replatform*; DOE = *reclaim*; Council = *consolidate + own*; NYCHA = *unlock*; **Staten Island BP = federate.** Here there is nothing to liberate because almost nothing is built — and all five NYC borough-president offices run near-identical thin sites with identical charter roles. The work is to define the office's first data model and expose it as **one shared Borough President API** keyed by borough, not five bespoke ones.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Land-use / ULURP recommendations | `LandUseRecommendation` | PDFs / notices; City Planning ZAP | ❌ gap |
| 2 | Community board appointments | `CommunityBoardAppointment` | HTML / recruited via form | ❌ gap |
| 3 | Discretionary funding awards | `DiscretionaryFundingAward` | `/budget` (mail/email); Schedule C | ❌ gap |
| 4 | Borough Board resolutions & reports | `Resolution` | monthly PDFs | ❌ gap |
| 5 | Community events & concerts | `Event` | HTML calendars | ❌ gap |
| 6 | BP Assist help line | `ConstituentRequest` | web widget | 🟡 aggregate (`3fes-huds`, ends FY20) |
| 7 | **Apply to a community board** | `CommunityBoardApplication` | Weebly form | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **NYC Open Data (Socrata SODA)** — 2 BPSI assets; one aggregate, one blob. The office does not consume them.
- **Weebly** (Square) — the site builder and form relay; the only "backend."
- **Cloudflare** — edge. **Constant Contact** — newsletter capture.
- Platform: **Weebly** — the fifth distinct platform after Parks' Smarty/PHP, DOE's Sitefinity/.NET, Council's WordPress, and NYCHA's Livesite + Oracle Siebel.

## Reverse-engineered entities

`LandUseRecommendation` · `CommunityBoardAppointment` · `DiscretionaryFundingAward` · `Resolution` · `Event` · `ConstituentRequest` (BP Assist; aggregate only in Open Data) · `CommunityBoardApplication` (net-new write) — spine keys: **borough**, **community board (1-3)**, **council district (49-51)**, **ULURP application number**.

## Next

1. **JSON Schema** per entity, modeling charter functions that have no existing columns — done ([schemas/](schemas/)).
2. **OpenAPI** publishing those as clean resources + two net-new writes (`POST /community-board-applications`, `POST /constituent-requests`) — done ([openapi/statenislandbp.yaml](openapi/statenislandbp.yaml)).
3. **MCP** artifact: `find_land_use_recommendations`, `get_land_use_recommendation`, `find_community_board_appointments`, `find_discretionary_funding_awards`, `find_resolutions`, `find_events`, `find_constituent_requests`, `report_quality_of_life_issue`, `apply_to_community_board` — done ([mcp/statenislandbp-mcp.json](mcp/statenislandbp-mcp.json)).
4. **Federate:** run the same assessment for the other four borough presidents and collapse into one shared contract.
