# lpc — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Landmarks Preservation Commission (LPC)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (landmarks, buildings, historic districts, permit history, reports, violations, and the locked filing transaction).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace; the **Esri ArcGIS** Discover map; the **Salesforce** Portico permit portal).
- [apis-observed.md](apis-observed.md) — the **open read, scattered** (Socrata SODA over 15 datasets *and* ArcGIS feature services) vs. the **Salesforce portal with no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (15 LPC datasets) with coverage verdicts.
- [opendata-lpc.md](opendata-lpc.md) / [opendata-lpc.json](opendata-lpc.json) — all 15 LPC Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `landmark` · `designated-building` · `historic-district` · `permit-application` · `designation-report` · `violation-order` · `landmark-permit-application` (net-new) (+ shared `_common`).
- [openapi/lpc.yaml](openapi/lpc.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/lpc-mcp.json](mcp/lpc-mcp.json) — design-first MCP server definition (10 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

LPC is a **three-silo domain**, and that scatter is the finding:

1. **The read is open — but split across two vendors.** 15 NYC Open Data datasets publish landmarks, the **Building Database** (`gpmc-yuvp`, 37 columns), historic districts, **issued permit history**, complaints, and violations generously; the **Discover NYC Landmarks map** on **Esri ArcGIS Online** publishes the same landmarks a second time as queryable feature services. Neither is a single owned LPC API.
2. **The write layer is locked.** The **Portico portal** (`portico.lpc.nyc.gov/s/`) is a **Salesforce Experience Cloud** community — login-walled, JavaScript-only, **no API**. Filing a permit application (Certificate of Appropriateness / No Effect / Minor Work) has no machine-readable contract.

**The gap here is a missing write plus an unbound read.** A consumer or agent asking "what has LPC approved on this block, and can I file for new windows?" must reconcile Socrata *and* ArcGIS for the answer — and has nothing at all to call for the filing.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **LPC** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP | Sitefinity (.NET) | WordPress | Livesite + Oracle Siebel | **Livesite + Esri ArcGIS + Salesforce** |
| Core problem | data as HTML | search rented, backend hidden | three APIs, none owned | data open, service layer in a CRM | **read open but scattered; filing locked in Salesforce** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **bind** |

## Reverse-engineered entities

`Landmark` · `DesignatedBuilding` · `HistoricDistrict` · `PermitApplication` (issued read twin) · `DesignationReport` · `ViolationOrder` · `LandmarkPermitApplication` (net-new write) — join keys **LP_NUMBER**, **BBL/BIN**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite, Dynatrace, AWS ALB); the Discover map was identified as Esri ArcGIS Online from its `*.maps.arcgis.com` org host; the Portico portal was identified as a Salesforce Experience Cloud community from its `/s/` path and Lightning/Aura markup (`force.com`, `renderCtx`, `LSKey-c$`) without authenticating. Open Data agency label verified via the Socrata Discovery API; all 15 assets pulled with columns. A sample, not a full spider; the Portico portal's internal workflows are inferred from LPC's documented permit process, not scraped behind login.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (15 datasets) ✅ · JSON Schemas (7 + common) ✅ · OpenAPI 3.1 (11 ops) ✅ · MCP artifact (10 tools) ✅.
- **Next:** an example implementation fronting the Salesforce Portico portal for `file_permit_application`; then the next domain from [../domains.md](../domains.md).
