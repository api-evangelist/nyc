# mome — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Mayor's Office of Media & Entertainment (MOME)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (film permits, held locations, MARCH inspections, MOME programs, and the locked E-Apply application workflow).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace; the **ASP.NET Core "MOME E-Apply"** film-permit portal).
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA over the famous Film Permits dataset) vs. the **E-Apply portal with no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (2 MOME datasets + the DOT twin) with coverage verdicts.
- [opendata-mome.md](opendata-mome.md) / [opendata-mome.json](opendata-mome.json) — both MOME Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `film-permit` · `screen-activity` · `march-inspection` · `media-program` · `production-company` · `film-permit-application` (+ shared `_common`).
- [openapi/mome.yaml](openapi/mome.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/mome-mcp.json](mcp/mome-mcp.json) — design-first MCP server definition (8 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

MOME is an **inverted domain**, and that inversion is the finding:

1. **The output is heroically open.** **Film Permits** (`tg4x-b46p`) is one of the most-viewed datasets in the entire NYC Open Data catalog (~530k views), automated and updated **daily** — every location shoot the Film Office greenlights, published as a public geography record.
2. **The intake is locked.** The **film-permit application system** (`nyceventpermits.nyc.gov/film`) is a login-walled **ASP.NET Core** app ("MOME E-Apply") — **no API**. Applying for a permit — the everyday production transaction — has no machine-readable contract at all.

**The gap here is the application, not the data.** A production or agent asking "apply to shoot on Varick Street next Tuesday" has nothing to call — even though, once granted, that same shoot appears in Open Data the next morning.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **MOME** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | Livesite + Oracle Siebel | **Livesite + ASP.NET "MOME E-Apply" portal** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **output the busiest dataset in the city, intake locked in a portal** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **greenlight** |

## Reverse-engineered entities

`FilmPermit` · `ScreenActivity` (held location) · `MarchInspection` · `MediaProgram` (incl. PublicAccessMedia) · `ProductionCompany` (applicant; never published) · `FilmPermitApplication` (net-new write) — join key **EventID** + the geography spine (borough, community board, police precinct, ZIP).

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite, Dynatrace); the application portal was identified as ASP.NET Core "MOME E-Apply" from its login redirect and headers (`Microsoft-IIS/10.0`, `X-Powered-By: ASP.NET`, `.AspNetCore.Antiforgery`, page title) without authenticating. Open Data agency label verified via the Socrata Discovery API (`Mayor's Office of Media And Entertainment (MOME)`, capitalized "And"); both assets pulled with columns. A sample, not a full spider; the E-Apply portal's internal workflow is inferred from MOME's documented permit steps, not scraped behind login.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (2 datasets + DOT twin) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (8 paths/9 ops) ✅ · MCP artifact (8 tools) ✅.
- **Next:** an example implementation fronting the E-Apply portal for `apply_for_film_permit`; then the next domain from [../domains.md](../domains.md).
