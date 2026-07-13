# dhs — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Department of Homeless Services (DHS)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (daily shelter census, drop-in centers, shelter facilities, DHS contacts, street counts, and the 311-locked outreach action).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace; **no DHS-owned service portal** — transactions route through NYC311).
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA over 23 datasets) vs. **NYC311 with no DHS-owned API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (23 DHS datasets) with coverage verdicts.
- [opendata-dhs.md](opendata-dhs.md) / [opendata-dhs.json](opendata-dhs.json) — all 23 DHS Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `shelter-census` · `drop-in-center` · `shelter-facility` · `dhs-contact` · `street-homeless-count` · `outreach-request` (+ shared `_common`).
- [openapi/dhs.yaml](openapi/dhs.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/dhs-mcp.json](mcp/dhs-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

DHS is an **observational-data agency with no transaction system of its own**, and that is the finding:

1. **Reference data is wide open.** 23 NYC Open Data datasets publish the picture of homelessness generously — the flagship **DHS Daily Report** (`k46n-sa2m`, the daily shelter census and DHS's most-viewed asset), drop-in centers, DHS contacts/intake centers, buildings and individual census, the **Shelter Repair Scorecard** (`dvaj-b7yx`, 55 columns), and years of unsheltered street-count history.
2. **There is no service layer to expose.** DHS ships no application; **applying for shelter** is in-person and **reporting a person on the street for outreach** is a **NYC311** call. Neither has a machine-readable contract, and DHS does not own the 311 channel that stands in for one.

**The gap here is the action, not the data.** A New Yorker or agent asking "get outreach to the person sleeping at this corner, and tell me what happened?" has nothing to call.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **DHS** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | NYC.gov Livesite + Oracle Siebel | **NYC.gov Livesite; no service portal (NYC311)** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **data open, no service layer at all** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **connect** |

## Reverse-engineered entities

`ShelterCensus` (DailyReport) · `DropInCenter` · `ShelterFacility` (buildings + repair scorecard) · `DHSContact` (offices/intake centers) · `StreetHomelessCount` (aggregate only) · `OutreachRequest` (net-new write) — join keys **date of census**, **DHS Building ID**, **BIN/BBL**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite, Dynatrace) — the same chassis as NYCHA's informational site. DHS was confirmed to have **no self-service portal**; its shelter and outreach pages point to NYC311 and in-person intake. Open Data agency label verified via the Socrata Discovery API; all 23 assets pulled with columns. A sample, not a full spider; the outreach/intake workflows are inferred from DHS's documented services and the NYC311 "Homeless Person Assistance" channel, not scraped.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (23 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (9 paths/10 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** an example implementation fronting NYC311 for `request_outreach`; then the next domain from [../domains.md](../domains.md).
