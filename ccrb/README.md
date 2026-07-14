# ccrb — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Civilian Complaint Review Board (CCRB)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (complaints, allegations, accused officers, penalties, the DTI dashboards, and the locked intake/status apps).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + AWS ALB + Dynatrace; the **Data Transparency Initiative** dashboards; the online form and Status Lookup app).
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA over 4 daily-updated datasets) vs. the **intake and status apps with no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (4 CCRB datasets) with coverage verdicts.
- [opendata-ccrb.md](opendata-ccrb.md) / [opendata-ccrb.json](opendata-ccrb.json) — all 4 CCRB Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `complaint` · `allegation` · `police-officer` · `penalty` · `misconduct-complaint` (+ shared `_common`).
- [openapi/ccrb.yaml](openapi/ccrb.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/ccrb-mcp.json](mcp/ccrb-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

CCRB is a **transparency model delivered without an API**, and that mismatch is the finding:

1. **The accountability data is model-grade and open.** The **Data Transparency Initiative** and **4 daily-updated Socrata datasets** publish disaggregated, officer-level misconduct data — complaints (`2mby-ccnw`), allegations (`6xgr-kwjq`), police officers (`2fir-qns4`), penalties (`keep-pkmh`) — keyed on **Complaint Id** and **Tax ID**, with CCRB-vs-NYPD dispositions and the APU-vs-NYPD penalty gap.
2. **But it ships as dashboards and CSV, not a contract.** There is **no queryable API** over the corpus, and the two acts a member of the public performs — **filing a misconduct complaint** (`.../file-online`) and **checking its status** (`apps.nyc.gov/ccrb-status-lookup`) — are disconnected JavaScript screens with no machine-readable surface.

**The gap here is delivery, not openness.** A resident or agent asking "how many substantiated force allegations came from this precinct?" or "help me file a complaint about what happened" has nothing to call.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **CCRB** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | NYC.gov Livesite + Oracle Siebel | **NYC.gov Livesite + DTI dashboards + status app** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **data model-grade & open, but dashboards/CSV only — no API; intake is a web form** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **expose** |

## Reverse-engineered entities

`Complaint` · `Allegation` (FADO; CCRB-vs-NYPD disposition) · `PoliceOfficer` (accused/subject; Total & Substantiated counts) · `Penalty` (APU trial track + NYPD final penalty) · `MisconductComplaint` (net-new write) — join keys **Complaint Id**, **Tax ID**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site and DTI dashboards were fingerprinted from headers (Akamai, nginx, AWS ALB, Livesite, Dynatrace); the online complaint form and the `apps.nyc.gov/ccrb-status-lookup` app were identified from their landing markup and titles without submitting anything. Open Data agency label verified via the Socrata Discovery API; all 4 assets pulled with columns and confirmed daily-updated. A sample, not a full spider; the intake form's internal fields are modeled from CCRB's documented complaint process and the FADO framework, not scraped from behind the form.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (4 datasets) ✅ · JSON Schemas (5 + common) ✅ · OpenAPI 3.1 (9 paths/9 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** an example implementation fronting the online form for `file_misconduct_complaint` and joining it to the status lookup; then the next domain from [../domains.md](../domains.md).
