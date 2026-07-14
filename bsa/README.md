# bsa — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Board of Standards & Appeals (BSA)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (applications, resolutions, hearings, pre-application meetings, zoning lots, and the locked paper intake).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + AWS ALB + Dynatrace; **paper PDF-form intake**, no online portal).
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA over 4 datasets) vs. the **Livesite search widget and PDF forms with no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (4 BSA datasets) with coverage verdicts.
- [opendata-bsa.md](opendata-bsa.md) / [opendata-bsa.json](opendata-bsa.json) — all 4 BSA Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `application` · `resolution` · `hearing` · `pre-application-meeting` · `zoning-lot` · `variance-application` (+ shared `_common`).
- [openapi/bsa.yaml](openapi/bsa.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/bsa-mcp.json](mcp/bsa-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

BSA is a **records-forward agency with no online portal**, and that is the finding:

1. **Case outcomes are wide open.** 4 NYC Open Data datasets publish every application filed 1998–present — the **Applications Status** table (`yvxd-uipr`, 34 columns) with type, premises, zoning district, status, and decision-PDF link; the **Decisions Map**; a legacy **Action Portal** calendar index (`f72e-3i4c`) back to 1916; and a **Pre-Application Meetings** log.
2. **The intake is locked in paper.** Filing a variance, special permit, extension, or appeal is a **download-a-PDF-and-file-on-paper** process (`bz_form.pdf`, `appeal_form.pdf`, `bzy_form.pdf`, `soc_form.pdf`). There is **no online application portal and no API** — not even a way to track a filing before decision.

**The gap here is intake, not outcomes.** A property owner or agent asking "file my variance" or "what's the status of my application?" has nothing to call.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **BSA** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | NYC.gov Livesite + Oracle Siebel | **NYC.gov Livesite + paper PDF forms** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **outcomes open, intake locked in paper** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **digitize** |

## Reverse-engineered entities

`Application` (case) · `Resolution` (decision) · `Hearing` (calendar) · `PreApplicationMeeting` · `ZoningLot` (property) · `VarianceApplication` (net-new write) — join keys **calendar number**, **BBL/BIN**, **block/lot**, **zoning district**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, AWS ALB, Livesite v22, Dynatrace); the records/resolutions search was identified as a server-rendered Livesite component (`searchRecords()`, `submit=true&componentID=…`) and the intake as paper PDF forms, without authenticating anywhere. Open Data agency label verified via the Socrata Discovery API; all 4 assets pulled with columns and live data sampled for case types (BZ / BZY / SOC / Appeal) and statuses (Granted / Denied / Withdrawn / Dismissed). A sample, not a full spider; the paper filing workflow is inferred from BSA's published forms and instructions, not from an internal system.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (4 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (9 paths/10 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** an example implementation digitizing the intake for `file_variance_application`; then the next domain from [../domains.md](../domains.md).
