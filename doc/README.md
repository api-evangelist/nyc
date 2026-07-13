# doc — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **New York City Department of Correction (DOC)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (people in custody, the live lookup, facilities, incidents, security indicators, and the locked visit/complaint transactions).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace; the legacy **Apache MyFaces / JSF** "P.I.C. Lookup").
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA over 15 datasets) vs. the **live lookup with no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (15 DOC datasets) with coverage verdicts.
- [opendata-doc.md](opendata-doc.md) / [opendata-doc.json](opendata-doc.json) — all 15 DOC Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `person-in-custody` · `facility` · `daily-population` · `incident-report` · `visit` · `complaint` (+ shared `_common`).
- [openapi/doc.yaml](openapi/doc.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/doc-mcp.json](mcp/doc-mcp.json) — design-first MCP server definition (8 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

DOC is **transparency-heavy but transaction-poor**, and that split is the finding:

1. **Accountability data is wide open.** 15 NYC Open Data datasets publish the daily in-custody population (`7479-ugqb`, the most-viewed asset), admissions/discharges, deaths, and five more parallel safety/security incident streams, plus Local Law 33/85 indicators.
2. **A live lookup runs, but has no API.** The **Inmate Lookup Service / "P.I.C. Lookup"** (`a073-ils-web.nyc.gov`) is a real-time person-in-custody search — a legacy **JavaServer Faces** app, browser-only, no OpenAPI, no JSON.
3. **The public transactions have no surface.** Scheduling a **visit** and filing a **complaint / records request** are phone/mail/in-person or vendor/OpenRecords portals — no API, no status.

**The gap here is the live lookup and the transactions, not the datasets.** A person or agent asking "is my relative in custody, and can I book a visit?" can neither call the lookup nor schedule the visit.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **DOC** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | NYC.gov Livesite + Oracle Siebel | **NYC.gov Livesite + legacy Apache MyFaces (JSF) lookup** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **data open + a live lookup, but the lookup is a JSF screen and the transactions have no surface** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **expose** |

## Reverse-engineered entities

`PersonInCustody` · `Facility` (derived; mostly Rikers Island) · `DailyPopulation` (security indicators / ADP) · `IncidentReport` (six unified incident streams) · `Visit` (net-new write) · `Complaint` (net-new write; complaint / records / FOIL) — join keys **INMATEID**, **NYSID**, **Book & Case number**, **INCIDENT_ID**, **FACILITY**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite, Dynatrace); the lookup was identified as Apache MyFaces / JavaServer Faces from its landing markup (`javax.faces.ViewState`, `myfaces`, `<title>P.I.C Lookup</title>`, WebSphere-style `JSESSIONID`) without submitting any search. Open Data agency label verified via the Socrata Discovery API; all 15 assets pulled with columns. A sample, not a full spider; the lookup's internal workflow is inferred from its documented search keys, not scraped. Person-in-custody data is treated as sensitive throughout.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (15 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (9 paths/10 ops) ✅ · MCP artifact (8 tools) ✅.
- **Next:** an example implementation fronting the JSF "P.I.C. Lookup" for `find_people_in_custody` and the net-new `schedule_visit`; then the next domain from [../domains.md](../domains.md).
