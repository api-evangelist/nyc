# brooklynbp — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **Office of the Brooklyn Borough President (BPBK)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (ULURP, community boards, appointments, funding awards, publications, events, and the net-new board application).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (headless **WordPress on WP Engine** + Next.js + Cloudflare; and the **lapsed `brooklyn-usa.org`** domain now redirecting to `batman-news.com`).
- [apis-observed.md](apis-observed.md) — the open **Socrata SODA** (21 datasets) + the live **WordPress / Events Calendar REST APIs** vs. the **web-form-only** constituent layer.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (21 BPBK datasets) with coverage verdicts.
- [opendata-brooklynbp.md](opendata-brooklynbp.md) / [opendata-brooklynbp.json](opendata-brooklynbp.json) — all 21 BPBK Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `land-use-recommendation` · `community-board` · `board-appointment` · `funding-award` · `report` · `event` · `community-board-application` (+ shared `_common`).
- [openapi/brooklynbp.yaml](openapi/brooklynbp.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/brooklynbp-mcp.json](mcp/brooklynbp-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

Brooklyn BP is a **thin content office with plentiful-but-scattered surface**, and that shape is the finding:

1. **The data exists — 21 datasets, not zero.** The brief guessed zero Socrata datasets; `Brooklyn Borough President (BPBK)` in fact publishes **21**: ULURP recommendations, a community-board contact list, a dozen 'BP Appointments' tables, and capital/discretionary/tourism awards. The current site also exposes a **live WordPress REST API** (315 posts) and **The Events Calendar API** (hearings, board meetings).
2. **But nothing is owned as an API.** The data is fragmented across 21 single-purpose Socrata IDs (many thin, several stale from 2015-2018); the live API is generic CMS plumbing; and the office **let its own `brooklyn-usa.org` domain lapse** — it now redirects offsite to `batman-news.com`.
3. **The constituent write layer is missing.** Applying to serve on a **community board** — the office's most consequential yearly interaction with residents — is only an unstructured web form.

**The gap here is ownership and shape, not availability. And the leverage is that all five Borough Presidents are the same office** — so the move is to define **one shared BP API and template it across the boroughs**.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **Brooklyn BP** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | Livesite + Oracle Siebel | **WP Engine WordPress + Next.js** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked | **data scattered + unowned; domain lapsed** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **template** |

## Reverse-engineered entities

`LandUseRecommendation` (ULURP) · `CommunityBoard` · `BoardAppointment` (consolidating a dozen board tables) · `FundingAward` (capital/discretionary/tourism) · `Report` (legislation/testimony/press) · `Event` (live Events Calendar) · `CommunityBoardApplication` (net-new write) — join keys **ULURP Number**, **Community Board (1-18)**, **Council District**, **Fiscal Year**, **BBL/BIN**.

## Method & caveats

Outside-in crawl (browser UA; `brooklynbp.nyc.gov/robots.txt` disallows only `/wp-admin/`). The current site was fingerprinted from headers (Cloudflare, WP Engine) and markup (Next.js `_next`, `wp-json`, Tribe Events); the lapsed `brooklyn-usa.org` was identified as an offsite domain-flip from its redirect chain and `bm-*-api` REST namespaces. Open Data agency label verified via the Socrata Discovery API — the correct label is **`Brooklyn Borough President (BPBK)`** (the brief's guessed labels returned zero; the real one returns 21). All 21 assets pulled with columns. A sample, not a full spider; the constituent web forms were not submitted.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (21 datasets) ✅ · JSON Schemas (7 + common) ✅ · OpenAPI 3.1 (11 paths/11 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** template this contract across the other four Borough Presidents (Manhattan, Bronx, Queens, Staten Island) as one shared BP API; then the next domain from [../domains.md](../domains.md).
