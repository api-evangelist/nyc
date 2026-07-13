# ocme — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Office of Chief Medical Examiner (OCME)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (indicators, aggregate case statistics, forensic services, family services centers, NamUs listings, and the paper/311 records request).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + AWS ALB + Dynatrace; **no OCME application at all** — records requests run on paper forms + NYC 311).
- [apis-observed.md](apis-observed.md) — the **one stale Open Data asset** vs. **no OCME API and no application**, with 311 and federal NamUs as the only structured channels.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (1 OCME dataset) with coverage verdicts.
- [opendata-ocme.md](opendata-ocme.md) / [opendata-ocme.json](opendata-ocme.json) — the single OCME Open Data asset + column schema, and an honest account of everything that is *not* there.
- [schemas/](schemas/) — individual JSON Schema per object: `monthly-indicator` · `case-statistics` · `forensic-service` · `family-services-center` · `missing-person` · `death-record-request` (+ shared `_common`).
- [openapi/ocme.yaml](openapi/ocme.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/ocme-mcp.json](mcp/ocme-mcp.json) — design-first MCP server definition (8 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

OCME is the **most data-dark and most privacy-constrained** domain assessed, and that is the finding:

1. **Almost nothing is published.** Exactly **one** dataset carries the OCME label on NYC Open Data — 'Monthly Indicators' (`8r6c-ydwk`), a Mayor's Management Report passthrough whose real values run only July 2015 - May 2016. It is not casework.
2. **There is no application to expose an API.** No portal, no CRM, no login. Requesting a decedent's casefile record — the core family transaction — is a **notarized paper form and NYC 311**, with a **three-to-six-month** wait.
3. **The core object is confidential by law.** A **death investigation** is never published, per-decedent or in aggregate. Any responsible surface must stay non-identifying.

**The gap here is near-total, over the most sensitive of domains.** A family asking "how do I get my father's autopsy report, and where is it?" has no digital contract to call — only a notary and a wait.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **OCME** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | NYC.gov Livesite + Oracle Siebel | **NYC.gov Livesite only — no app** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **almost no data, no application, core object confidential** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **instrument** |

## Reverse-engineered entities

`MonthlyIndicator` · `CaseStatistics` (aggregate only — never an individual death investigation) · `ForensicService` · `FamilyServicesCenter` · `MissingPerson` (public NamUs listing) · `DeathRecordRequest` (net-new write; also the status surface for a submitted request) — the deliberately non-identifying join key is an OCME **case number**, never a decedent's clinical record.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, AWS ALB, Livesite, Dynatrace); the absence of an OCME application was confirmed by crawling the services / records-requests / locations pages, all of which route transactions to paper forms and `portal.311.nyc.gov`. The Open Data agency label was verified via the Socrata Discovery API — one asset. A sample, not a full spider; casework is modeled only at a proposed, non-identifying aggregate level, because OCME does not (and should not) publish individual death investigations.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (1 dataset) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (7 paths/8 ops) ✅ · MCP artifact (8 tools) ✅.
- **Next:** an example implementation fronting the 311/paper records process for `request_record`, plus a publisher-side aggregation job for `CaseStatistics` with small-cell suppression; then the next domain from [../domains.md](../domains.md).
