# hpd — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Department of Housing Preservation & Development (HPD)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

**Modernization verb: `expose`.** **Net-new write object: `HousingLotteryApplication`** (NYC Housing Connect). Accent `#3f8f6a`.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (buildings, violations, complaints, registrations, litigation, affordable housing, lottery).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (Angular SPAs, WSO2 gateway, GeoSearch, ArcGIS, Akamai, ASP.NET Housing Connect…).
- [apis-observed.md](apis-observed.md) — the APIs found: the **private owned backend** (`hpdonline.api/1.0`), DocService, WSO2 gateway, SODA, GeoSearch.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping with coverage verdicts.
- [opendata-hpd.md](opendata-hpd.md) / [opendata-hpd.json](opendata-hpd.json) — all **47** HPD Open Data datasets + column schemas.
- [schemas/](schemas/) — one JSON Schema per object: `building` · `violation` · `complaint` · `registration` · `litigation` · `affordable-housing-project` · `housing-lottery-application` (+ shared `_common`).
- [openapi/hpd.yaml](openapi/hpd.yaml) — OpenAPI 3.1 contract `$ref`ing each object (incl. the net-new lottery + complaint writes).
- [mcp/hpd-mcp.json](mcp/hpd-mcp.json) — design-first MCP server definition (11 agent tools; artifact, not a deployment).

## What was found — the fourth distinct pattern

HPD is the first domain in the project where the city has **already built the modern API** — and simply doesn't publish it. HPD Online's Angular bundle hard-codes its backend as **`https://mspwvw-hpdleov3.nyc.gov/hpdonline.api/1.0/api`**: a versioned REST API on an owned `.nyc.gov` host, sitting behind a **WSO2 API gateway** (`*.hpdnyc.org:8243`) with **NYC GeoSearch** integration. It serves exactly one consumer — the SPA — and has no public documentation or agent surface.

Meanwhile the public, machine-readable surface is **47 flattened NYC Open Data datasets** (Housing Maintenance Code Violations alone: 215k+ views) that describe the same buildings, violations, complaints, registrations, and litigation with the same keys. And the single highest-value citizen transaction — **applying to an affordable-housing lottery on Housing Connect** — is a **closed ASP.NET silo with no public API** (only read-only "advertised lotteries" twins on Open Data).

So a tenant or agent asking *"does my building have open C-class violations, who owns it, is it in housing court — and can you help me apply to this lottery?"* must stitch a private SPA against several batch snapshots, and then hit a wall at the lottery.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | **HPD** |
|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress / WP Engine | **Angular SPA + WSO2 gateway; ASP.NET lottery** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned/unified | **owned modern API exists but is private + 47 batch snapshots + a closed lottery** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **expose** |

## Reverse-engineered entities

`Building` · `HousingMaintenanceViolation` · `Complaint` (+ problems) · `Registration` (+ contacts) · `LitigationCase` · `AffordableHousingProject` · `HousingLotteryApplication` (net-new) — join keys: **buildingId**, **registrationId**, **BBL**, **BIN**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` disallows only `/html/misc/`). Backend base URLs and vendor hosts were recovered by parsing the HPD Online `main.js` bundle and its CSP `connect-src`; the private `hpdonline.api` endpoints were **not** called (undocumented, no auth). The Open Data agency label was verified against the Socrata Discovery API and all 47 datasets pulled with per-column schemas. A design-first assessment, not a deployment.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (47 datasets) ✅ · JSON Schemas (7 + `_common`) ✅ · OpenAPI 3.1 ✅ · MCP artifact (11 tools) ✅.
- **Next:** publish `hpdonline.api` as the documented contract; reconcile the 47 Open Data snapshots to the same schemas/keys; open the Housing Connect lottery workflow; then the next domain from [../domains.md](../domains.md).
