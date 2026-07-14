# statenislandbp — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **Office of the Staten Island Borough President (BPSI)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (land use, community board appointments, discretionary funding, borough board resolutions, events, BP Assist, and the net-new board application).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (**Weebly** brochure site behind **Cloudflare**; Weebly Forms; Constant Contact).
- [apis-observed.md](apis-observed.md) — the **absence** of any owned API, and the **two trivial** Open Data assets.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (2 datasets) with coverage verdicts.
- [opendata-statenislandbp.md](opendata-statenislandbp.md) / [opendata-statenislandbp.json](opendata-statenislandbp.json) — both BPSI Open Data assets, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `land-use-recommendation` · `community-board-appointment` · `discretionary-funding-award` · `resolution` · `event` · `constituent-request` · `community-board-application` (+ shared `_common`).
- [openapi/statenislandbp.yaml](openapi/statenislandbp.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/statenislandbp-mcp.json](mcp/statenislandbp-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

Staten Island BP is the **thinnest** domain assessed, and that thinness — repeated across all five boroughs — is the finding:

1. **No platform to speak of.** The office's entire public surface is a **Weebly brochure site** (`statenislandusa.com`, Cloudflare edge, `x-host: *.weebly.net`) — no CMS of record, no application, **no API**, no JSON.
2. **Two trivial datasets.** Under `Staten Island Borough President (BPSI)` there are only `3fes-huds` (BP Assist Helpline Requests — aggregate counts, ending FY20) and `mmut-uup9` (Category Master File — a zero-column blob).
3. **The charter work is invisible as data.** Land-use / ULURP recommendations, community board appointments, discretionary funding, and Borough Board resolutions live only as PDFs and HTML, or inside other agencies' systems.

**The gap here is existence, not access.** A resident or agent asking "what did the BP recommend on this rezoning?" or "who's on Community Board 2?" has nothing to call — and nothing to read.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **SI BP** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | Livesite + Oracle Siebel | **Weebly** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked | **almost no data or API exists at all** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **federate** |

The verb is **federate** because the fix is not one more bespoke site — it is recognizing that Manhattan, Bronx, Brooklyn, Queens, and Staten Island run near-identical thin sites with identical NYC Charter roles, and defining **one shared Borough President API** (keyed by `borough`) that all five instantiate. This assessment builds that contract for Staten Island.

## Reverse-engineered entities

`LandUseRecommendation` · `CommunityBoardAppointment` · `DiscretionaryFundingAward` · `Resolution` · `Event` · `ConstituentRequest` (BP Assist; aggregate-only twin) · `CommunityBoardApplication` (net-new write) — spine keys: **borough**, **community board (1-3)**, **council district (49-51)**, **ULURP application number**.

## Method & caveats

Outside-in crawl (browser UA; `statenislandusa.com/robots.txt` disallows only `/ajax/`, `/apps/`, `/ida.html`, `/stayonstatenisland.html`). The site was fingerprinted from headers and markup (Cloudflare, Weebly, Weebly Forms, Constant Contact); the sitemap and key pages were walked without submitting any form. The Open Data agency label was verified via the Socrata Discovery API — note the *display* attribution is "Office of the Staten Island Borough President" but the machine-readable facet is `Staten Island Borough President (BPSI)`. Because the office publishes essentially no structured data, the entity schemas are modeled from the BP's **charter functions and the site's own pages**, not reconciled against existing columns — they are a proposed target, not a mirror of production data.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (2 datasets) ✅ · JSON Schemas (7 + common) ✅ · OpenAPI 3.1 (10 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** run the same assessment for the other four borough presidents and **collapse into one shared Borough President API**; then the next domain from [../domains.md](../domains.md).
