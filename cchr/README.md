# cchr — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Commission on Human Rights (CCHR)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (the Report Discrimination intake, the Human Rights Law's protected classes, legal guidance, trainings, and three aggregate operational datasets).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + AWS ALB + Dynatrace/mPulse; the **Report Discrimination HTML form**).
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA over 3 aggregate datasets) vs. the **untyped intake form with no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (3 CCHR datasets) with coverage verdicts.
- [opendata-cchr.md](opendata-cchr.md) / [opendata-cchr.json](opendata-cchr.json) — all 3 CCHR Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `discrimination-complaint` · `protected-class` · `legal-guidance` · `training-event` · `inquiry-statistic` · `resolution-statistic` (+ shared `_common`).
- [openapi/cchr.yaml](openapi/cchr.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/cchr-mcp.json](mcp/cchr-mcp.json) — design-first MCP server definition (8 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

CCHR is the **thinnest** domain yet, and that thinness is the finding:

1. **Almost nothing is machine-readable.** NYC Open Data carries just **3** CCHR datasets, all aggregate operational counts (inquiries received, mediation cases, pre-complaint resolutions). There is no case data, no law-as-data, no guidance catalog, no outreach calendar.
2. **The core transaction is an untyped web form.** Reporting discrimination — the most important thing a person does with CCHR — is a plain server-rendered HTML `<form>` on the shared NYC.gov "Livesite" platform, posting into an opaque Law Enforcement Bureau backend. No API, no OpenAPI, no JSON.

**The gap here is structure, not vendor lock-in.** Unlike NYCHA, CCHR isn't trapped in a packaged CRM — it runs on the city's own platform. What's missing is a *type*: the intake form, the protected classes, and the legal guidance have no machine-readable contract at all.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **CCHR** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | NYC.gov Livesite + Oracle Siebel | **NYC.gov Livesite (form-only)** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer in a CRM | **intake + law untyped; data almost absent** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **structure** |

## Reverse-engineered entities

`DiscriminationComplaint` (net-new write) · `ProtectedClass` · `LegalGuidance` · `TrainingEvent` · `InquiryStatistic` (aggregate) · `ResolutionStatistic` (aggregate; never individual case) — organizing vocabularies: the **protected classes** and **protected areas** (employment, housing, public accommodations, lending, discriminatory harassment, bias-based profiling) of the NYC Human Rights Law (Title 8).

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The site was fingerprinted from headers (Akamai, nginx, AWS ALB, Livesite, Dynatrace, mPulse); the Report Discrimination form was read from page markup (its fields and category choices) without submitting anything. Open Data agency label verified via the Socrata Discovery API; all 3 assets pulled with columns. A sample, not a full spider; the Law Enforcement Bureau case-management backend is opaque and its workflow is inferred from CCHR's documented complaint process, not scraped.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (3 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (8 paths/9 ops) ✅ · MCP artifact (8 tools) ✅.
- **Next:** an example implementation typing the Report Discrimination intake as `POST /complaints` (report_discrimination); then the next domain from [../domains.md](../domains.md).
