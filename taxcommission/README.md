# taxcommission — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **New York City Tax Commission** — the City's independent property-tax appeals body — through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (assessment actions, Article 7 petitions, property, representative, determination, and the net-new appeal filing).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace + mPulse + AWS ALB; the browser-only **online filing system**).
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA over 2 datasets) vs. the **online filing system with no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (2 datasets) with coverage verdicts.
- [opendata-taxcommission.md](opendata-taxcommission.md) / [opendata-taxcommission.json](opendata-taxcommission.json) — both Tax Commission Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `property` · `assessment-appeal` · `determination` · `assessment-action` · `article7-petition` · `representative` (+ shared `_common`).
- [openapi/taxcommission.yaml](openapi/taxcommission.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/taxcommission-mcp.json](mcp/taxcommission-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

The Tax Commission is a **quasi-judicial appeals body**, and its shape is the finding:

1. **The open data is thin and outcome-only.** Just **2 datasets** — **Assessment Actions** (`4nft-bihw`, the reductions granted) and **Open Article 7 Petitions** (`aht6-vxai`, the court challenges that escalate a determination) — and both are published under the **Office of Administrative Tax Appeals (OATA)** label, not a Tax Commission label. Neither describes the appeal process itself.
2. **The core transaction has no API.** Filing an **Application for Correction** — challenging DOF's tentative assessed value and/or tax class — lives only in **PDF forms** (TC101/TC108/TC109/TC106 + income & expense TC201/203/208/214 + TC309) and a **browser-only online filing system**, on a hard March 15/16 deadline with a **$175 fee** at $2M+ assessed value.

**The gap is the transaction, and even the data is thin.** An owner or agent asking "file my appeal" or "what did the Commission offer?" has nothing to call.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **Tax Commission** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | NYC.gov Livesite + Oracle Siebel | **NYC.gov Livesite + browser-only online filing** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **thin outcome-only data; the appeal is PDF forms with no API** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **digitize** |

## Reverse-engineered entities

`Property` (BBL tax lot; assessed by DOF) · `AssessmentAction` (published reductions) · `Article7Petition` (judicial escalation) · `Representative` (attorney/agent) · `Determination` (offer / hearing result) · `AssessmentAppeal` (net-new write) — join keys **BBL**, **Borough Code / Block / Lot**, **Tax Class**, **Tax Year**, **Petition Index Number**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite, Dynatrace, mPulse/Boomerang, AWS ALB); the appeal workflow, forms, fee, and deadline were read from the process and forms pages without filing. Open Data was verified via the Socrata Discovery API — there is **no `Tax Commission (TC)` label**; both assets sit under **`Office of Administrative Tax Appeals (OATA)`** and were pulled with columns. A sample, not a full spider; the online filing system's internal workflow is inferred from the published forms and process, not scraped behind the filing UI.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (2 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (8 paths / 9 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** an example implementation fronting the online filing system for `file_appeal`; then the next domain from [../domains.md](../domains.md).
