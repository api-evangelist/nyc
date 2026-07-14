# manhattanbp — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **Office of the Manhattan Borough President (MBPO)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (community boards, ULURP recommendations, appointments, funding awards, legislation, constituent cases, and the net-new community-board application).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (**WordPress + Divi** on WP Engine, behind Cloudflare; Forminator forms; Google Site Kit).
- [apis-observed.md](apis-observed.md) — the **open Socrata API** (21 datasets) and the **generic WordPress REST API** vs. the **community-board application that has no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (21 MBPO datasets) with coverage verdicts.
- [opendata-manhattanbp.md](opendata-manhattanbp.md) / [opendata-manhattanbp.json](opendata-manhattanbp.json) — all 21 MBPO Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `community-board` · `land-use-recommendation` · `board-appointment` · `funding-award` · `legislation` · `constituent-case` · `community-board-application` (+ shared `_common`).
- [openapi/manhattanbp.yaml](openapi/manhattanbp.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/manhattanbp-mcp.json](mcp/manhattanbp-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

The Manhattan BP is **not** the data desert the hypothesis expected. The finding is fragmentation and duplication:

1. **The data is open but fragmented.** 21 NYC Open Data datasets cover the office's real outputs — ULURP recommendations, appointments, community-board leadership, constituent services, and funding — but published as one-off assets **per program per fiscal year** (`Capital Grant Awards` is five separate datasets, 2014–2018).
2. **The site is a generic WordPress/Divi template.** `manhattanbp.nyc.gov` is an off-the-shelf WordPress build on WP Engine behind Cloudflare, whose only API is the default WordPress REST API. The flagship citizen action — **applying to serve on a community board** — is a Forminator web form with no contract.
3. **Five identical offices.** All five borough presidents run near-identical thin sites and publish the same shapes of data. That is the argument for building the API **once** and deploying it per office.

**The gap here is coherence, ownership, and a write surface — not raw openness.**

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **Manhattan BP** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | NYC.gov Livesite + Oracle Siebel | **WordPress/Divi on WP Engine** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **data open but fragmented; generic CMS; five identical offices** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **federate** |

## Reverse-engineered entities

`CommunityBoard` · `LandUseRecommendation` (ULURP; body is a PDF) · `BoardAppointment` · `FundingAward` (unifies five per-year capital datasets + tourism/community/MCAP/police-community) · `Legislation` (links out) · `ConstituentCase` (de-identified) · `CommunityBoardApplication` (net-new write) — join keys **community board (1–12)**, **council district**, **BBL/BIN**, **fiscal year**.

## Method & caveats

Outside-in crawl (browser UA; `manhattanbp.nyc.gov/robots.txt` disallows nothing). The site was fingerprinted from headers and markup (Cloudflare, WP Engine, WordPress `wp-json`, Divi theme + plugins, Forminator, Google Site Kit) without authenticating. Open Data agency label verified via the Socrata Discovery API; all 21 assets pulled with columns. A sample, not a full spider; the community-board application workflow is inferred from the office's documented process and the Forminator form surface, not scraped behind submission. The five-borough "federate" argument is grounded in the parallel Socrata agency labels (`BPBK`, `BPBX`, `QBP`, `BPSI`) observed in the same Discovery API query.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (21 datasets) ✅ · JSON Schemas (7 + common) ✅ · OpenAPI 3.1 (10 paths/ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** federate this contract across the other four borough presidents as one shared Borough President API; then the next domain from [../domains.md](../domains.md).
