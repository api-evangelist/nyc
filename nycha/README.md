# nycha — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **New York City Housing Authority (NYCHA)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (developments, addresses, facilities, utility metering, resident statistics, and the locked portal transactions).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace; the **Oracle Siebel** Self Service Portal).
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA over 24 datasets) vs. the **Siebel portal with no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (24 NYCHA datasets) with coverage verdicts.
- [opendata-nycha.md](opendata-nycha.md) / [opendata-nycha.json](opendata-nycha.json) — all 24 NYCHA Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `development` · `residential-address` · `community-facility` · `utility-consumption` · `resident-statistics` · `work-order` (+ shared `_common`).
- [openapi/nycha.yaml](openapi/nycha.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/nycha-mcp.json](mcp/nycha-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the fourth distinct pattern

NYCHA is a **split domain**, and that split is the finding:

1. **Reference data is wide open.** 24 NYC Open Data datasets publish the physical stock generously — the **Development Data Book** (`evjd-dqpz`, 55 columns), residential addresses, community facilities, **six** streams of utility consumption-and-cost metering, and aggregate resident demographics.
2. **The resident service layer is locked.** The **Self Service Portal** (`selfserve.nycha.info`) is an **Oracle Siebel CRM** — login-walled, JavaScript-only, **no API**. Rent, recertification, waitlist applications, and repair **work orders** have no machine-readable contract at all.

**The gap here is transactions, not data.** A resident or agent asking "what's the status of my repair?" or "report that my radiator is broken" has nothing to call.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | **NYCHA** |
|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | **NYC.gov Livesite + Oracle Siebel portal** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | **data open, service layer locked in a CRM** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** |

## Reverse-engineered entities

`Development` · `ResidentialAddress` · `CommunityFacility` · `UtilityConsumption` (PropertyMeter) · `ResidentStatistics` (aggregate only) · `WorkOrder` (net-new write) — join keys **TDS #**, **EDP #**, **HUD AMP #**, **BIN/BBL**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite, Dynatrace); the Self Service Portal was identified as Oracle Siebel from its landing markup (`SWECmd`, `OracleSiebel_logo.gif`, page title) without authenticating. Open Data agency label verified via the Socrata Discovery API; all 24 assets pulled with columns. A sample, not a full spider; the Siebel portal's internal workflows are inferred from NYCHA's documented resident services, not scraped behind login.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (24 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (9 paths/10 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** an example implementation fronting the Siebel portal for `report_repair`; then the next domain from [../domains.md](../domains.md).
