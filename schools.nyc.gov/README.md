# schools.nyc.gov — Low-Hanging Fruit Assessment

Second domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of **New York City Public Schools (NYCPS / DOE)**, taken through the full design-first method: assessment → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact — plus, new to this domain, a **technology/vendor inventory** and an **APIs-observed inventory**.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (School directory, calendar, enrollment, quality, demographics, test results).
- [crosswalk.md](crosswalk.md) — fruit ↔ Open Data mapping (638 DOE assets) with coverage verdicts.
- [opendata-doe.md](opendata-doe.md) / [opendata-doe.json](opendata-doe.json) — all 638 DOE Open Data assets + column schemas.
- **[tech-stack.md](tech-stack.md)** — technology & vendor inventory (Sitefinity, HawkSearch, Azure Blob, Esri, Siteimprove, GTM…).
- **[apis-observed.md](apis-observed.md)** — backend/service APIs the site calls (HawkSearch, internal `/CustomApi`, Azure blob, ArcGIS, Socrata, NYCSA auth).
- [schemas/](schemas/) — individual JSON Schema per object: `school` · `school-demographics` · `calendar-event` · `test-result` · `enrollment-application` (+ shared `_common`, DBN-keyed).
- [openapi/nyc-schools.yaml](openapi/nyc-schools.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/nyc-schools-mcp.json](mcp/nyc-schools-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found

NYCPS is **more** data-rich than Parks — **638 DOE Open Data assets**, including High School Directories with **462 columns**, School Locations, and Demographic Snapshots — and the public site never consumes them. The school directory is **3,343 pages** (`/schools/<LocationCode>`), each a `School` profile rendered client-side. Same core disconnect as Parks, with two extra twists specific to DOE:

1. **Discovery is rented.** "Find a School" runs on **HawkSearch**, a vendor search API — DOE owns neither a public school-search API nor the index behind it.
2. **The backend is hidden.** School pages are driven by an internal **`/CustomApi/*`** (robots-disallowed, undocumented). A machine-readable API *exists* — it just isn't public.
3. **Enrollment is the net-new gap.** The **MySchools** admissions workflow (3K–12) is transactional with **no Open Data twin** — the flagship API opportunity, analogous to Parks permits.

**Reframe:** integration + productization *and* **reclaiming** capabilities that are outsourced (search) or hidden (backend) into an owned, public, agent-native API keyed on **DBN**.

## Reverse-engineered entities

`School` · `SchoolDemographics` · `CalendarEvent` · `EnrollmentApplication` · `TestResult` · `SchoolQualityReport` — join key **DBN** (District-Borough-Number), the school equivalent of Parks' gisPropNum.

## Method & caveats

Bounded outside-in crawl (browser UA; `/CustomApi`, `/Sitefinity`, `/System` disallowed and avoided). Sitemap decompressed (gzip) → 4,617 URLs. Page data is JS-rendered, so on-page counts understate the real records; scale figures come from the sitemap and the Open Data twins. A sample, not a full spider.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (638 assets) ✅ · JSON Schemas (6) ✅ · OpenAPI 3.1 (9 paths/11 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** publish the school-year calendar as a dataset (closes a gap); example implementation wiring reads to SODA + owning search; then the third domain from [../domains.md](../domains.md).
