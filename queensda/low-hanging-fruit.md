# Low-Hanging Fruit Index — Queens District Attorney

**Agency:** Queens County District Attorney
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `queensda.org/robots.txt` disallows nothing). Fingerprinted `queensda.org` as **WordPress 7.0.1** on **Kinsta** managed hosting behind **Cloudflare**, with the **Divi** theme (+ a `queensdistrictattorney` child theme), **Beaver Builder** page builder, **WPML** multilingual, **Yoast** SEO, **Google Site Kit**, **FacetWP** faceted search, and **self-hosted Matomo** analytics. Confirmed **zero** NYC Open Data assets via the Socrata Discovery API across four agency-label spellings. Enumerated content through the fully-exposed **WordPress REST API** (`wp-json/wp/v2`): 1,557 posts, 60 pages, full category taxonomy with counts.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-queensda.md](opendata-queensda.md).

## Headline findings

1. **Queens DA is already an API — by accident.** It publishes prolifically (1,557 WordPress posts, 1,216 press releases) and WordPress's REST API (`wp-json/wp/v2`) is fully exposed, so all of it is machine-readable JSON right now. But it is **undesigned and uncontracted** — it models blog posts, not prosecutions.
2. **There is no open data at all.** Verified **zero** Socrata / NYC Open Data datasets. District Attorneys are county/state prosecutorial agencies and do not publish to NYC Open Data.
3. **The prosecution lifecycle is only prose.** Arraignment (131) → charges (127) → indictment (119) → court-case (378) → conviction exists solely as press-release text tagged by WordPress category. No structured `Case`, no queryable charges, dispositions, or sentences.
4. **The one structured dataset is hiding in post titles.** The cold-case / unidentified-persons initiative encodes NamUs case numbers, sex, age range, and date/location found in the titles themselves (e.g. `MALE 4-12-2014 NAMUS UP13060`).
5. **There is no way in.** No inbound tip, cold-case lead, or FOIL channel beyond a phone number and a static contact page.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search; Council = *consolidate + own* fragmented APIs; NYCHA = *unlock* a locked service layer; **Queens DA = structure** an accidental content API into a designed contract. Here the bytes are already reachable — the work is least about access and most about giving the office's narrative a real domain model, recovering the structured data trapped in prose, and adding the missing write surface. And because **all five borough DAs run the same functions on similar WordPress stacks**, the fruit is one **shared five-borough DA API**, not five accidental REST endpoints.

## The fruit

| # | Name | Entity | Where the data lives | Machine-readable today |
|---|---|---|---|---|
| 1 | Press Releases | `PressRelease` | WordPress posts (cat 16) | 🟡 accidental WordPress REST (HTML body) |
| 2 | Prosecution activity (public record) | `Case` | Lifecycle categories over prose | 🟡 category tags only |
| 3 | Cold Cases / Unidentified Persons (NamUs) | `ColdCase` | Post titles + bodies | 🟡 structured data in titles |
| 4 | Community Programs & Initiatives | `Program` | Hand-built pages | 🟡 WordPress REST (pages) |
| 5 | Resources (FOIL, Property Release, CIU, helplines) | `CommunityResource` | Resources page prose | 🟡 page prose |
| 6 | Victim / Witness Services | `VictimService` | Scattered prose | ❌ no directory |
| 7 | **Submit a tip / lead / FOIL request** | `TipSubmission` | Contact page / phone | ❌ **net-new (no API)** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **WordPress REST API** (`wp-json/wp/v2`) — the accidental, fully-open content API (1,557 posts). The de facto Queens DA API.
- **FacetWP** — faceted search endpoints under wp-json.
- **Self-hosted Matomo** — first-party analytics (an ownership plus); **Google Site Kit / Yoast** for third-party SEO/analytics.
- Platform: **WordPress 7.0.1 / Divi / Beaver Builder / WPML** on **Kinsta** behind **Cloudflare** — the fifth distinct platform after Parks' Smarty/PHP, DOE's Sitefinity/.NET, Council's WordPress, and NYCHA's Livesite + Siebel.
- **NYC Open Data:** none (zero datasets). **FOIL:** manual records path, no API.

## Reverse-engineered entities

`PressRelease` · `Case` (public-record, aggregate; no sealed/non-public data) · `ColdCase` (NamUs ID, sex, age, date/location — recovered from titles) · `Program` · `CommunityResource` · `VictimService` (services, not people) · `TipSubmission` (net-new write; tip / cold-case lead / case inquiry / FOIL request) — join keys: **WordPress post ID**, **NamUs case number**, **NYC geography spine**.

## Next

1. **JSON Schema** per entity, reconciling the WordPress REST shape and the title-encoded cold-case fields — done ([schemas/](schemas/)).
2. **OpenAPI** presenting the accidental API as designed resources + the net-new `POST /submissions` (submit a tip / FOIL request) — done ([openapi/queensda.yaml](openapi/queensda.yaml)).
3. **MCP** artifact: `find_press_releases`, `get_press_release`, `find_cases`, `get_case`, `find_cold_cases`, `find_programs`, `find_community_resources`, `find_victim_services`, `submit_tip` — done ([mcp/queensda-mcp.json](mcp/queensda-mcp.json)).
4. **Shared DA API:** generalize this contract across Manhattan, Brooklyn, Bronx, and Staten Island DA offices — one five-borough API instead of five accidental WordPress REST endpoints.
