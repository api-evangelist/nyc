# bronxbp — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **Office of the Bronx Borough President**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (funding awards, community-board appointments, ULURP recommendations, newsroom, events, and the net-new community-board application).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (**Revize** government SaaS CMS on Oracle Cloud; PHP front end + JSP admin; Google Calendar, Curator.io, Constant Contact, UserWay, GA4).
- [apis-observed.md](apis-observed.md) — the **near-absence** of APIs: two Socrata datasets and nothing else the office owns.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (2 datasets) with coverage verdicts.
- [opendata-bronxbp.md](opendata-bronxbp.md) / [opendata-bronxbp.json](opendata-bronxbp.json) — both Bronx BP Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `discretionary-funding-award` · `community-board-appointment` · `land-use-recommendation` · `press-release` · `event` · `community-board-application` (+ shared `_common`).
- [openapi/bronxbp.yaml](openapi/bronxbp.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/bronxbp-mcp.json](mcp/bronxbp-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

The Bronx Borough President is a **thin domain**, and that thinness — plus its duplication across five boroughs — is the finding:

1. **The site is a vendor brochure.** `bronxboropres.nyc.gov` runs on a **Revize** government SaaS CMS (PHP front end, JSP back end) on Oracle Cloud — not the shared NYC.gov platform. No API, no OpenAPI, no JSON.
2. **Only two entities are machine-readable.** NYC Open Data holds exactly two datasets under `Bronx Borough President (BPBX)` — Capital Funding (`mdgu-ar69`) and Bronx Community Boards (`wbau-xy7g`) — both hand-published. Everything else (ULURP recommendations, newsroom, events) is a PDF, a PHP page, or a borrowed Google Calendar.
3. **Intake is analog.** Applying to serve on a community board is a downloadable PDF or an email — no structured application, no confirmation, no status.

**The gap here is thinness, and the fix is reuse.** All five Borough President offices carry the *same* NYC Charter duties and run near-identical thin sites. This is a candidate for **one shared Borough President API**, not five bespoke builds.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **Bronx BP** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | Livesite + Oracle Siebel | **Revize SaaS CMS (Oracle Cloud)** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked | **thin brochure; only 2 datasets; five identical offices** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **templatize** |

## Reverse-engineered entities

`DiscretionaryFundingAward` · `CommunityBoardAppointment` (both open data) · `LandUseRecommendation` (ULURP; PDFs) · `PressRelease` (newsroom) · `Event` (Google Calendar) · `CommunityBoardApplication` (net-new write) — join keys **Community Board (1–12)**, **BBL/BIN**, **Council District**, **Fiscal Year**.

## Method & caveats

Outside-in crawl (browser UA; the site has no real `robots.txt`). The site was fingerprinted from headers and markup (Oracle Cloud IP, Revize `RZ.*` globals, `cms2.revize.com` webspace, PHP page templates, the `revize_calendar` Google Calendar import, the `document_center` ULURP PDFs). Open Data agency label verified via the Socrata Discovery API; both assets pulled with columns. A sample, not a full spider; the `LandUseRecommendation`, `PressRelease`, and `Event` schemas are reverse-engineered from the unstructured site surfaces (PDFs, PHP pages, calendar), not from a machine-readable feed — because none exists.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (2 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (9 paths/10 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** an example implementation fronting the two Socrata datasets + a structured `apply_to_community_board` intake; then **templatize** the contract across the four other Borough President offices from one shared definition — then the next domain from [../domains.md](../domains.md).
