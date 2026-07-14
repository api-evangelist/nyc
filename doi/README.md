# doi — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **New York City Department of Investigation (DOI)** — the city's Inspector General — through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (PDF-only public reports, the PPR recommendations tracker, City Marshal evictions/revenue, performance indicators, and the vendor complaint intake).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace; PDF report library; the **Kaseware** complaint portal).
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA over 4 datasets) vs. the **PDF reports and Kaseware form with no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (4 DOI datasets) with coverage verdicts.
- [opendata-doi.md](opendata-doi.md) / [opendata-doi.json](opendata-doi.json) — all 4 DOI Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `public-report` · `policy-recommendation` · `eviction` · `marshal-revenue` · `performance-indicator` · `corruption-complaint` (+ shared `_common`).
- [openapi/doi.yaml](openapi/doi.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/doi-mcp.json](mcp/doi-mcp.json) — design-first MCP server definition (8 agent tools; artifact, not a deployment).

## What was found — digitize the outputs and the intake

DOI is New York City's **Inspector General**, and the finding is that the two things that define it have no structured surface:

1. **The core output is PDF-only.** DOI's public investigation reports — findings, subject agencies, reform recommendations — are published only as PDFs under `/assets/doi/reports/pdf/<year>/`. No structured data, no report API.
2. **The core transaction is a vendor form.** Reporting fraud, waste, or corruption — the tip that starts every investigation — runs through a **third-party Kaseware** intake portal (`app.kaseware.us`), a client-rendered SPA with no API, backed by phone/fax/mail.
3. **What's open is oversight, not investigations.** The **4 Open Data datasets** are dominated by City Marshal oversight — **Evictions** (`6z8x-wfk4`, ~237k views) and **City Marshals Revenue** — plus the **PPR recommendations** tracker (the one structured twin of DOI's casework) and monthly performance indicators.

**The gap here is DOI's own outputs, not third-party data.** An agent asking "what did DOI recommend to NYCHA?" or "help me report corruption anonymously" has almost nothing to call.

**Reframe (vs. the earlier domains):**

| | DORIS | OCME | DVS | **DOI** |
|---|---|---|---|---|
| Platform | Livesite + Preservica DAMS | Livesite (info only) | Livesite + Combined Arms portal | **Livesite + PDF library + Kaseware SaaS** |
| Core problem | records trapped in a DAMS | bare agency, paper forms | referral on a vendor form | **reports are PDFs, complaints are a vendor form** |
| Modernization verb | **retrieve** | **instrument** | **coordinate** | **digitize** |

## Reverse-engineered entities

`PublicReport` (PDF-only; net gap) · `PolicyRecommendation` (structured twin) · `Eviction` · `MarshalRevenue` · `PerformanceIndicator` · `CorruptionComplaint` (net-new write) — join keys **Court Index / Docket Number**, **Marshal Last Name + Year**, **BBL/BIN**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite v22, Dynatrace); the report library from the `/assets/doi/reports/pdf/` link pattern; the complaint intake identified as Kaseware from its landing markup (`<title>Kaseware Portal</title>`, `cf-ray`) without submitting anything. Open Data agency label verified via the Socrata Discovery API; all 4 assets pulled with columns. A sample, not a full spider; the Kaseware form's internal fields are inferred from DOI's documented complaint guidance, not scraped.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (4 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (8 paths/9 ops) ✅ · MCP artifact (8 tools) ✅.
- **Next:** an example implementation fronting the Kaseware portal for `file_complaint` and indexing the PDF reports; then the next domain from [../domains.md](../domains.md).
