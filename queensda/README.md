# queensda — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **Queens County District Attorney**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (press releases, prosecution activity, cold cases, programs, resources, victim services, and the net-new inbound submission).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (**WordPress 7.0.1** + Divi + Beaver Builder + WPML on **Kinsta** behind **Cloudflare**; FacetWP; self-hosted Matomo).
- [apis-observed.md](apis-observed.md) — the **accidental API** (fully-exposed WordPress REST) vs. **zero open data** and **no inbound write channel**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping with coverage verdicts.
- [opendata-queensda.md](opendata-queensda.md) / [opendata-queensda.json](opendata-queensda.json) — the honest zero: no NYC Open Data assets exist for a District Attorney.
- [schemas/](schemas/) — individual JSON Schema per object: `press-release` · `case` · `cold-case` · `program` · `community-resource` · `victim-service` · `tip-submission` (+ shared `_common`).
- [openapi/queensda.yaml](openapi/queensda.yaml) — OpenAPI 3.1 contract `$ref`ing each object, with the net-new write path.
- [mcp/queensda-mcp.json](mcp/queensda-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

Queens DA **already has an API — by accident.** WordPress ships a REST API, and on `queensda.org` it is fully exposed: 1,557 posts, 1,216 of them press releases, all readable as JSON right now. But:

1. **It is undesigned and uncontracted.** The accidental API models blog posts, not prosecutions — bodies are HTML, cases are just category tags, and there is no stable domain contract.
2. **There is no open data.** Verified **zero** NYC Open Data / Socrata datasets; DAs are county/state agencies that don't publish there.
3. **The structured data is trapped in prose.** The prosecution lifecycle (arraignment → charges → indictment → court case → conviction) is only press-release text tagged by category, and the cold-case / unidentified-persons dataset encodes NamUs IDs, sex, age, and dates in post *titles*.
4. **There is no way in.** No inbound tip, cold-case lead, or FOIL channel beyond a phone number and a static page.

**The gap here is structure, not access.** The bytes are reachable; the model is not.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **Queens DA** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | Livesite + Oracle Siebel | **WordPress/Divi on Kinsta + Cloudflare** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service locked in a CRM | **accidental API, no open data, data only as prose** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **structure** |

And the strategic note: **all five borough DA offices run the same functions on similar WordPress stacks.** The fruit is not five accidental REST APIs — it is **one shared five-borough DA API** with a designed contract and an agent-native MCP layer.

## Reverse-engineered entities

`PressRelease` · `Case` (public-record, aggregate; no sealed/non-public or victim-identifying data) · `ColdCase` (NamUs ID, sex, age, date/location — recovered from titles) · `Program` · `CommunityResource` · `VictimService` (services, not people) · `TipSubmission` (net-new write) — join keys **WordPress post ID**, **NamUs case number**, and the **NYC geography spine**.

## Method & caveats

Outside-in crawl (browser UA; `queensda.org/robots.txt` disallows nothing). The stack was fingerprinted from response headers and markup (Cloudflare, Kinsta, WordPress 7.0.1, Divi, Beaver Builder, WPML, Matomo, FacetWP); content was enumerated through the site's own exposed WordPress REST API (post/category/page counts read live 2026-07-13). NYC Open Data absence verified via the Socrata Discovery API across four agency-label spellings. Case, cold-case, program, resource, and victim-service structures are reverse-engineered from public content, not scraped from any internal case-management system; nothing here implies access to sealed or non-public records.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (zero, documented) ✅ · JSON Schemas (7 + common) ✅ · OpenAPI 3.1 (9 paths/11 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** generalize into a **shared five-borough DA API** (Manhattan, Brooklyn, Bronx, Staten Island); then a reference implementation that parses cold-case titles into structured `ColdCase` records and fronts the WordPress REST API. Then the next domain from [../domains.md](../domains.md).
