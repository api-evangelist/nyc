# bronxda — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **Office of the Bronx District Attorney** (Darcel D. Clark), through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (press releases, case-statistic dashboards, bureaus/programs, community resources, victim services, and the net-new tip/complaint/FOIL intake).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (legacy NYC.gov `/html/` **SHTML** on Akamai + AWS ALB; the **Power BI (Gov)** data iframes).
- [apis-observed.md](apis-observed.md) — the finding of **absence**: no Bronx DA API, zero Open Data, one data asset trapped in Power BI.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (an empty Open Data set) with coverage verdicts.
- [opendata-bronxda.md](opendata-bronxda.md) / [opendata-bronxda.json](opendata-bronxda.json) — the honest zero-dataset result and where the data actually lives.
- [schemas/](schemas/) — individual JSON Schema per object: `press-release` · `case-statistic` · `program` · `community-resource` · `victim-service` · `tip-submission` (+ shared `_common`).
- [openapi/bronxda.yaml](openapi/bronxda.yaml) — OpenAPI 3.1 contract `$ref`ing each object, with the net-new `POST /submissions` write path.
- [mcp/bronxda-mcp.json](mcp/bronxda-mcp.json) — design-first MCP server definition (8 agent tools; artifact, not a deployment).

## What was found — the emptiest surface, and a shared fix

The Bronx DA is the barest domain assessed so far. The modernization verb is **standardize**:

1. **No API, zero Open Data.** The Socrata Discovery API returns **0** datasets under every agency label. The office publishes no JSON, no OpenAPI, no feed. Prosecution is a county function that sits outside the NYC Open Data program.
2. **A legacy `.shtml` site.** `bronxda.nyc.gov` is a hand-built NYC.gov `/html/` SHTML application — server-side-includes, a JavaScript-built nav (`nav-nodes.js`), jQuery/Bootstrap — behind Akamai and an AWS ALB. Not the shared "Livesite" chassis.
3. **The one data asset is trapped in Power BI.** Aggregate prosecution figures (arrests, charging decisions, case outcomes, defendant demographics) are published only as **Microsoft Power BI (Gov)** iframes — rendered pixels with no download, no query endpoint, no Open Data twin.
4. **No trackable intake.** Tips and Civilian Complaint Unit complaints are a phone call (718-590-2300); FOIL requests are a plain email. Neither returns a tracking number.

**The gap here is everything at once — data, API, and intake.** And because all **five** borough DA offices run the same charter functions, the low-hanging fruit is **one shared District Attorney API**, not a bespoke Bronx build.

**Reframe (vs. the earlier domains):**

| | Parks | NYCHA | Borough President | **Bronx DA** |
|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | NYC.gov Livesite + Oracle Siebel | Revize vendor CMS | **Legacy `/html/` SHTML + Power BI iframes** |
| Core problem | data as HTML, no API | data open, service layer locked | thin brochure, two datasets | **no API, zero Open Data, data trapped in Power BI** |
| Modernization verb | **replatform** | **unlock** | **templatize** | **standardize** |

## Reverse-engineered entities

`PressRelease` · `CaseStatistic` (aggregate only — never an individual case/defendant) · `Program` (bureau/division/outreach) · `CommunityResource` · `VictimService` · `TipSubmission` (net-new write; also the FOIL request + Civilian Complaint intake) — cross-office key **`OfficeReference`** (office / county / borough / DA) so the same model backs all five borough DAs.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The site was fingerprinted from headers (Akamai `ak_p`, `AWSALB` cookie, Dynatrace `ruxit`, Akamai mPulse Boomerang) and markup (`.shtml`, `nav-nodes.js`, the Power BI iframe). The Open Data agency label was queried via the Socrata Discovery API — zero results, documented honestly. Every entity is reverse-engineered from HTML and BI iframes, not a machine-readable source, because none exists. A sample, not a full spider; the Power BI dashboards' internal fields are inferred from their titles/glossary, not scraped from the BI service.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (0 datasets, documented) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (8 paths/8 ops) ✅ · MCP artifact (8 tools) ✅.
- **Next:** promote this to a shared `io.nyc.districtattorney` contract for all five borough offices; then the next domain from [../domains.md](../domains.md).
