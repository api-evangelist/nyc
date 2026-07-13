# nypd — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **New York City Police Department**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (complaints, arrests, shootings, summonses, use of force, stops, precincts, officers, CompStat, collisions, report requests).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (Oracle WebCenter Sites, Akamai, Dynatrace; Angular + Kendo SPAs; Azure Government backend).
- [apis-observed.md](apis-observed.md) — the APIs actually seen: Socrata SODA (42 datasets) + the undocumented `officer.search.azure.us` officer backend + vendors.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (42 NYPD datasets) with coverage verdicts.
- [opendata-nypd.md](opendata-nypd.md) / [opendata-nypd.json](opendata-nypd.json) — the 42 NYPD Open Data datasets + column schemas for the top ones.
- [schemas/](schemas/) — individual JSON Schema per object: `complaint` · `arrest` · `shooting-incident` · `precinct` · `officer` · `police-report-request` (+ shared `_common`).
- [openapi/nypd.yaml](openapi/nypd.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/nypd-mcp.json](mcp/nypd-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the fourth distinct pattern

NYPD is the **most data-rich** domain in the project, and that is precisely the finding. Its data already exists in enormous volume — but not as an API you can query, and not in a shape an agent can use:

1. **42 Open Data datasets** under the Socrata agency label `Police Department (NYPD)` — including `h9gi-nx95` (Motor Vehicle Collisions - Crashes), the **single most-viewed dataset in the entire NYC Open Data portal**. But these are **flattened periodic snapshots**, not a live incident API.
2. **An undocumented Azure Government backend** (`officer.search.azure.us`) powers the **Officer Profile** app on `nypdonline.org` — names, shields, commands, arrests, **disciplinary history** — reachable by a browser, not by an integrator or agent.
3. **CompStat 2.0** (`compstat.nypdonline.org`) renders current weekly crime stats client-side in an Angular SPA, with **no documented API**.

**None is an owned, coherent, agent-native NYPD API.** A resident asking "how many felony complaints in my precinct last month, who's my neighborhood coordination officer, and does this officer have a disciplinary record?" must download three CSV snapshots and scrape two single-page apps.

**Reframe (vs. the prior domains):**

| | Parks | DOE | Council | **NYPD** |
|---|---|---|---|---|
| Platform | Smarty/PHP | Sitefinity (.NET) | WordPress | **WebCenter Sites + Angular/Azure Gov** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | **most data of all — but snapshots + app-trapped** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **expose** |

## Reverse-engineered entities

`ComplaintReport` · `Arrest` · `ShootingIncident` · `Precinct` (incl. sectors + NCOs) · `Officer` (incl. discipline history) · `PoliceReportRequest` (net-new) — join keys **complaintNumber**, **arrestKey**, **incidentKey**, **precinct number**, **profileId**.

## Method & caveats

Outside-in crawl (browser UA; nyc.gov robots disallows only `/html/misc/`). Socrata agency label `Police Department (NYPD)` **verified** via the Discovery API, then all 42 assets fetched by agency facet. The two SPAs (Officer Profile, CompStat 2.0) were fingerprinted and their bundles inspected for backend endpoints (`officer.search.azure.us`); their APIs are undocumented and were not exercised. A sample, not a full spider. Motor Vehicle Collisions are returned under the NYPD label but are jointly owned with OTI/DOT (noted throughout).

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (42 datasets) ✅ · JSON Schemas (6 + `_common`) ✅ · OpenAPI 3.1 (13 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** an example implementation exposing the SODA snapshots + fronting `officer.search.azure.us` behind one owned contract; unify a precinct directory; then the next domain from [../domains.md](../domains.md).
