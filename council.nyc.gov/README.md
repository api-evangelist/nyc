# council.nyc.gov — Low-Hanging Fruit Assessment

Third domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **New York City Council**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (members, districts, committees, legislation, hearings, funding, testimony).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (WordPress/WP Engine, Legistar/Granicus, CARTO, Viebit, StreamText…).
- [apis-observed.md](apis-observed.md) — the **three existing APIs** (Legistar Web API, WordPress REST API, Socrata SODA) + vendors.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (11 NYCC datasets) with coverage verdicts.
- [opendata-nycc.md](opendata-nycc.md) / [opendata-nycc.json](opendata-nycc.json) — the 11 NYCC Open Data datasets + column schemas.
- [schemas/](schemas/) — individual JSON Schema per object: `council-member` · `district` · `committee` · `legislation` · `meeting` · `discretionary-funding` · `testimony-registration` (+ shared `_common`).
- [openapi/nyc-council.yaml](openapi/nyc-council.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/nyc-council-mcp.json](mcp/nyc-council-mcp.json) — design-first MCP server definition (10 agent tools; artifact, not a deployment).

## What was found — the third distinct pattern

Council is the **most API-covered** domain in the project, and that is precisely the finding. Its data already lives behind **three APIs**:

1. **Legistar Web API** (`webapi.legistar.com/v1/nyc`) — the authoritative legislative record (bills, votes, hearings, members). A **Granicus vendor** API, access-gated (it 403'd our client), OData-shaped — not a Council product.
2. **WordPress REST API** (`council.nyc.gov/wp-json`) — **open**, but serves CMS content (members/committees/reports as posts), not legislative resources.
3. **NYC Open Data SODA** — 11 NYCC datasets (Members, Legislation, Discretionary Funding, Participatory Budgeting, Meetings…), but flattened periodic snapshots, disconnected from Legistar and the site.

**None is an owned, coherent, agent-native NYC Council API.** A resident asking "what did my member sponsor, and when's the next hearing?" must stitch three vendor systems together.

**Reframe (vs. the first two domains):**

| | Parks | DOE | **Council** |
|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | **WordPress / WP Engine** |
| Core problem | data as HTML, no API | search rented, backend hidden | **three APIs, none owned/unified** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** |

## Reverse-engineered entities

`CouncilMember` · `District` · `Committee` (incl. caucus) · `Legislation` · `Meeting` · `Vote` (Legistar) · `DiscretionaryFunding` · `TestimonyRegistration` (net-new) — join keys **councilMemberId**, **matterId** (Legistar), **district**.

## Method & caveats

Outside-in crawl (browser UA; `Crawl-delay: 10`, `/wp-admin` disallowed). WordPress `wp-sitemap.xml` → 121 pages + custom types (40 committees, 9 caucuses, 47 reports); `/district-1..51/`. Legistar Web API probed (403 to our client — documented as the vendor legislative API). A sample, not a full spider.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed (3 existing APIs) ✅ · Open Data crosswalk (11 NYCC datasets) ✅ · JSON Schemas (7) ✅ · OpenAPI 3.1 (14 paths/15 ops) ✅ · MCP artifact (10 tools) ✅.
- **Next:** publish caucuses + reports as resources (close the two gaps); an example implementation fronting Legistar + WP + SODA; then the fourth domain from [../domains.md](../domains.md).
