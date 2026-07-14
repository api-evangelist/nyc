# Low-Hanging Fruit Index — Brooklyn DA

**Agency:** Kings County (Brooklyn) District Attorney's Office
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `brooklynda.org/robots.txt` is a Yoast block with no disallows). Fingerprinted `www.brooklynda.org` from headers and markup: **Apache + WordPress 6.8.5 + GeneratePress/GP Premium**, with Wordfence, Yoast, MonsterInsights (Google Analytics), MetaSlider, FileBird, Redirection, UserFeedback, Google Language Translator, and Embed Any Document. Enumerated the WordPress REST API (`/wp-json`) namespaces and `wp/v2` categories (**Press Releases = 911 posts**). Verified via the Socrata Discovery API that **NO NYC Open Data** exists under any Brooklyn/Kings County DA label (`resultSetSize` 0 for every variant).

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-brooklynda.md](opendata-brooklynda.md).

## Headline findings

1. **A content-only domain with no data.** One self-hosted **WordPress 6.8.5** brochure site — no portal, no application, no data platform. It runs on its own domain (`brooklynda.org`), *not* the shared NYC.gov chassis.
2. **The only machine-readable surface is accidental.** The **WordPress REST API** (`/wp-json/wp/v2`) exposes ~911 press releases plus notifications, statements, and bureau/program pages. It is the CMS default, not a designed contract.
3. **Zero open data.** There is **no NYC Open Data for any DA office**. Caseloads, arraignments, dispositions, declined prosecutions, diversions, and conviction-review outcomes — the actual administration of justice — are published **nowhere as data**, only as prose inside press releases.
4. **No inbound machine surface.** Submitting a **tip** has only a captcha-gated web form, a phone hotline, or a bureau email. No API, no status tracking.
5. **Five identical offices.** Manhattan, Bronx, Kings, Queens, and Richmond DAs share the same functions. This is a candidate for **one shared DA API**, built once and adopted five times.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a vendor-locked service layer; **Brooklyn DA = template.** Here there is almost nothing to liberate — the work is least about freeing datasets and most about *creating* the data the office never published (aggregate case statistics), promoting an accidental content API into a designed one, and doing it as a **shared template** the other four county DA offices reuse.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Press Releases, Statements & Notifications | `PressRelease` | WP REST API (~911 posts) | ❌ none (content API only) |
| 2 | Programs, Bureaus & Initiatives | `Program` | WP REST API (pages) | ❌ none (content API only) |
| 3 | Community Resources (brochures, hotlines) | `CommunityResource` | WP REST API (pages + PDFs) | ❌ none |
| 4 | Victim Services | `VictimService` | bureau pages (prose) | ❌ none |
| 5 | Case / Prosecution Statistics | `CaseStatistics` | **nowhere** (prose in press releases) | ❌ **gap — not data anywhere** |
| 6 | **Submit a confidential tip** | `TipSubmission` | captcha form + hotline | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **WordPress REST API (`wp/v2`)** — the one real, open, machine-readable surface; accidental, content-only.
- **No NYC Open Data** — zero datasets for any DA office (verified).
- **Captcha contact form / phone / email** — the only inbound tip channels; no API.
- Platform: **self-hosted WordPress 6.8.5** on Apache with GeneratePress + Wordfence + Yoast + MonsterInsights — the fifth distinct platform after Parks' Smarty/PHP, DOE's Sitefinity/.NET, Council's WordPress-on-nyc, and NYCHA's Livesite + Oracle Siebel.

## Reverse-engineered entities

`PressRelease` · `Program` · `CommunityResource` · `VictimService` · `CaseStatistics` (aggregate; never individual cases) · `TipSubmission` (net-new write) — the model is deliberately **office-neutral** so all five county DA offices can share it. Organizing key: **Bureau**.

## Next

1. **JSON Schema** per entity, grounded in the WordPress content model and the office's bureau structure — done ([schemas/](schemas/)).
2. **OpenAPI** promoting the accidental content API into clean resources + a proposed aggregate `case-statistics` surface + the net-new `POST /tips` (submit a tip) — done ([openapi/brooklynda.yaml](openapi/brooklynda.yaml)).
3. **MCP** artifact: `find_press_releases`, `get_press_release`, `find_programs`, `get_program`, `find_community_resources`, `find_victim_services`, `find_case_statistics`, `submit_tip`, `get_tip_status` — done ([mcp/brooklynda-mcp.json](mcp/brooklynda-mcp.json)).
4. **The bigger move:** propose this as **one shared DA API** across all five NYC county District Attorney offices.
