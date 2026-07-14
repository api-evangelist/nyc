# law — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **New York City Law Department (Office of the Corporation Counsel)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (litigation case index, divisions, publications, M/WBE statistics, pro bono program, and the net-new internship application).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (the shared NYC.gov "Livesite" chassis + Akamai + Dynatrace; **no Law-specific platform, portal, or application system**).
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA over 7 datasets) and the note that the **claims ledger belongs to the Comptroller**, not Law.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (7 Law datasets + the Comptroller's claims dataset) with coverage verdicts.
- [opendata-law.md](opendata-law.md) / [opendata-law.json](opendata-law.json) — all 7 Law Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `legal-case` · `legal-division` · `publication` · `mwbe-statistic` · `public-service-program` · `law-internship-application` (+ shared `_common`).
- [openapi/law.yaml](openapi/law.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/law-mcp.json](mcp/law-mcp.json) — design-first MCP server definition (8 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

The Law Department is an **agency-facing legal office**, and that is the finding:

1. **Almost no citizen transactions.** It is the City's in-house law firm. Its public site is content-only on the shared NYC.gov "Livesite" chassis — no portal, no search vendor, no application system.
2. **Thin, stale data.** Only **7 Open Data datasets** under `Law Department (LAW)`, every one **'No' automation / 'Annually'** updated: a civil-litigation case index, a divisions list, three publication feeds, M/WBE statistics, and a pro bono firm list.
3. **The core data is another agency's.** The ledger of **claims filed and settlement dollars** is the **Comptroller's** (`ex6k-ym48`), not Law's.

**The gap here is that there is barely a surface to assess.** The work is not to liberate trapped data or unlock a locked service — it is to *catalog* the little that exists and route the questions that matter to the right agency.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **Law** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | NYC.gov Livesite + Oracle Siebel | **NYC.gov Livesite only (no Law-specific stack)** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **agency-facing; thin stale data; claims owned by the Comptroller** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **catalog** |

## Reverse-engineered entities

`LegalCase` (litigation index; claims dollars owned by the Comptroller) · `LegalDivision` · `Publication` (press release / speech / column) · `MwbeStatistic` · `PublicServiceProgram` · `LawInternshipApplication` (net-new write) — join keys **docket/index**, **division name**, **Lead BBL**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, AWS ALB, Livesite v22, Dynatrace); no Law-specific portal or application system was found. Open Data agency label verified via the Socrata Discovery API; all 7 assets pulled with columns, and the Comptroller's ownership of the claims dataset (`ex6k-ym48`) confirmed separately. A sample, not a full spider; the internship-application workflow is inferred from the Careers page, which directs applicants to email/PDF.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (7 datasets + Comptroller note) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (8 paths/9 ops) ✅ · MCP artifact (8 tools) ✅.
- **Next:** an example implementation of `submit_internship_application`; then the next domain from [../domains.md](../domains.md).
