# queensbp — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **Office of the Queens Borough President (QBP)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (community boards & appointments, land-use/ULURP recommendations, discretionary funding, events, newsroom, and the net-new community board application).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (**WordPress/Divi on WP Engine behind Cloudflare**; Yoast + Wordfence; `queensbp.org` 301s to `www.queensbp.nyc.gov`).
- [apis-observed.md](apis-observed.md) — the **WordPress REST API that is switched on but empty** vs. the **two community-board Socrata datasets**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (2 QBP datasets) with coverage verdicts.
- [opendata-queensbp.md](opendata-queensbp.md) / [opendata-queensbp.json](opendata-queensbp.json) — both QBP Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `community-board` · `community-board-appointment` · `land-use-recommendation` · `discretionary-funding-award` · `event` · `press-release` · `community-board-application` (+ shared `_common`).
- [openapi/queensbp.yaml](openapi/queensbp.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/queensbp-mcp.json](mcp/queensbp-mcp.json) — design-first MCP server definition (11 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

QBP is the **thinnest domain** in the survey, and that thinness is the finding:

1. **A commodity WordPress brochure.** `queensbp.org` 301-redirects to `www.queensbp.nyc.gov`, a **Divi page-builder site on WP Engine behind Cloudflare**. Everything — land use, community boards, budget, constituent services, newsroom — is a Divi Page.
2. **The REST API is on, but empty.** WordPress ships `/wp-json/wp/v2`, and it is public — but returns **0 posts and 0 `project` entries**. The one machine-readable surface the office already owns is dormant because content is authored as Pages, not posts.
3. **Almost no open data.** Just **two** datasets, both about community boards (members `rps4-dwwk`; district managers & chairs `8z5h-tzdr`). The core BP acts — advisory **ULURP recommendations**, tens of millions in **discretionary funding**, events, press — have no machine-readable contract.

**The gap here is that there's barely anything to expose — and five offices duplicate it.** All five borough presidents run near-identical thin sites.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **Queens BP** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | Livesite + Oracle Siebel | **WordPress/Divi on WP Engine + Cloudflare** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked | **thin brochure; REST API on but empty; almost no open data** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **standardize** |

## Reverse-engineered entities

`CommunityBoard` · `CommunityBoardAppointment` · `LandUseRecommendation` (ULURP) · `DiscretionaryFundingAward` · `Event` · `PressRelease` · `CommunityBoardApplication` (net-new write; also stands in for the constituent-services request) — join keys **community board number**, the NYC **geography spine** (BBL/BIN, council district, census tract, NTA), and **ULURP number**.

## Method & caveats

Outside-in crawl (browser UA; `queensbp.nyc.gov/robots.txt` is a Yoast block disallowing nothing, `Crawl-delay: 10`). The site was fingerprinted from headers (`server: cloudflare`, `x-powered-by: WP Engine`), `wp-json` namespaces (`wp/v2`, `divi/v1`, `yoast/v1`, `wordfence/v1`, `wpe/cache-plugin/v1`), theme markup (Divi), and the sitemap — without authenticating. The empty REST API was confirmed by `X-WP-Total: 0` on `/wp-json/wp/v2/posts` and `/wp-json/wp/v2/project`. Open Data agency label verified via the Socrata Discovery API; both assets pulled with columns. A sample, not a full spider; the borough-president functions (ULURP, funding, events) are modeled from their site pages, not scraped as structured data (none exists).

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (2 datasets) ✅ · JSON Schemas (7 + common) ✅ · OpenAPI 3.1 (12 paths/ops) ✅ · MCP artifact (11 tools) ✅.
- **Next:** propose the contract as a **shared Borough President API** across all five boroughs; light up the existing WordPress REST API by authoring Newsroom/events as posts; then the next domain from [../domains.md](../domains.md).
