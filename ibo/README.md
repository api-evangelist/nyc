# ibo — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **New York City Independent Budget Office (IBO)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (publications, fiscal series, school spending, tax distribution, stimulus trackers, and the form-only Ask IBO transaction).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov **"Content API v2"** SPA + Akamai + Dynatrace + WebTrends; the undocumented **`apps.nyc.gov/content-api/v2`** backend; ArcGIS/Airtable/Infogram embeds).
- [apis-observed.md](apis-observed.md) — the **two real-but-uncontracted APIs** (the NYC.gov content API and Socrata SODA over 20 datasets) vs. the **form-only Ask IBO**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (20 IBO datasets) with coverage verdicts.
- [opendata-ibo.md](opendata-ibo.md) / [opendata-ibo.json](opendata-ibo.json) — all 20 IBO Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `publication` · `fiscal-data-table` · `fiscal-series` · `school-spending` · `tax-distribution` · `data-request` (+ shared `_common`).
- [openapi/ibo.yaml](openapi/ibo.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/ibo-mcp.json](mcp/ibo-mcp.json) — design-first MCP server definition (10 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

IBO is a **reference / analysis agency**, and its finding is different again:

1. **The API already exists — undocumented.** The site is a client-side SPA on the NYC.gov "Content API v2" platform; every route serves the same shell and fetches content from `apps.nyc.gov/content-api/v2`, which returns ~**1,145** publications as structured JSON. But there is no OpenAPI, no versioning, no consumer contract.
2. **The data already exists — Excel-shaped.** 20 NYC Open Data datasets publish IBO's fiscal time-series, but **wide**: one column per fiscal year (`FY 1980` … `FY 2020`). Machine-readable, but awkward.
3. **There is nothing to write — except Ask IBO.** IBO has no payments, permits, or applications. Its single citizen transaction is **Ask IBO**, a web form / email with no API.

**The gap here is a contract, not access.** A consumer or agent asking "what did IBO publish on the FY2025 budget?" or "capital expenditures by purpose since FY2010?" has JSON and datasets available — but no documented, agent-native surface, and no way to ask IBO a question programmatically.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **IBO** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | Livesite + Oracle Siebel | **NYC.gov Content API v2 SPA** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked | **API + data exist, but undocumented/Excel-shaped** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **formalize** |

## Reverse-engineered entities

`Publication` · `FiscalDataTable` · `FiscalSeries` (wide tables pivoted long) · `SchoolSpending` · `TaxDistribution` (by AGI band) · `DataRequest` (net-new Ask IBO write) — organizing spine: **fiscal year**, **series/line-item**, **publication type + topic**, **AGI range**.

## Method & caveats

Outside-in crawl (browser UA). The site was fingerprinted from headers and the client-side loader scripts (Akamai, nginx, Dynatrace, WebTrends, jQuery/Bootstrap, the `content-api/v2` endpoints). The content API was confirmed by fetching `apps.nyc.gov/content-api/v2/custom-contents/ibo/IBO-Publications/1` (~1,145 records) and `/nav/ibo` — read-only, no authentication. Open Data agency label verified via the Socrata Discovery API (the correct label is `NYC Independent Budget Office (IBO)`; the un-prefixed `Independent Budget Office (IBO)` returns zero); all 20 assets pulled with columns. A sample, not a full spider; the Ask IBO workflow is inferred from the public form, not scraped behind submission.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (20 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (10 ops) ✅ · MCP artifact (10 tools) ✅.
- **Next:** an example implementation fronting `apps.nyc.gov/content-api/v2` as a documented `GET /publications`, plus a pivoted `GET /fiscal-series`; then the next domain from [../domains.md](../domains.md).
