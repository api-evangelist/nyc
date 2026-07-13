# fdny — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **Fire Department of the City of New York (FDNY)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (firehouses, Fire/EMS dispatch, inspections, violations, certificates, and the locked portal transactions).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace; the **Accela Civic Platform** FDNY Business portal).
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA over 17 datasets) vs. the **rented Accela portal with no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (17 FDNY datasets) with coverage verdicts.
- [opendata-fdny.md](opendata-fdny.md) / [opendata-fdny.json](opendata-fdny.json) — all 17 FDNY Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `firehouse` · `incident-dispatch` · `inspection` · `violation` · `certificate-of-fitness` · `fire-permit-application` (+ shared `_common`).
- [openapi/fdny.yaml](openapi/fdny.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/fdny-mcp.json](mcp/fdny-mcp.json) — design-first MCP server definition (10 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

FDNY is a **split domain**, and that split is the finding:

1. **Reference and incident data is wide open.** 17 NYC Open Data datasets publish the operational picture generously — the **FDNY Firehouse Listing** (`hc8x-tcnd`), minute-level **Fire and EMS incident dispatch** (`8m42-w767`, `76xm-jjuj`), Bureau of Fire Prevention inspections, active violation orders, and certificates of fitness.
2. **The business service layer is rented and locked.** **FDNY Business** (`fires.fdnycloud.org`) is an **Accela Civic Platform** (Citizen Access) application — login-walled, JavaScript-only, **no API**. Applying for a permit, holding a Certificate of Fitness/Operation, scheduling an inspection, and answering a violation have no machine-readable contract at all.

**The gap here is transactions, not data** — and the transaction system is a commercial SaaS the city rents, not one it owns. A business or agent asking "what's the status of my permit?" or "apply for a Place of Assembly certificate" has nothing to call.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **FDNY** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | Livesite + Oracle Siebel | **Livesite + Accela Civic Platform (rented)** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer in a CRM | **data open, business layer rented to a SaaS** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **front** |

## Reverse-engineered entities

`Firehouse` · `IncidentDispatch` (Fire + EMS) · `Inspection` (BFP / RBIS / mandatory) · `Violation` · `CertificateOfFitness` · `FirePermitApplication` (net-new write) — join keys **BIN**, **BBL**, FDNY premises account **ACCT_NUM/ACCT_ID**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite, Dynatrace); the FDNY Business portal was identified as Accela Civic Platform from its redirect chain and CSP allow-list (`/CitizenAccess/Default.aspx`, `*.accela.com`, Datadog RUM, Azure App Gateway cookies) without authenticating. Open Data agency label verified via the Socrata Discovery API; all 17 assets pulled with columns. A sample, not a full spider; the Accela portal's internal workflows are inferred from FDNY's documented business services, not scraped behind login.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (17 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (9 paths/10 ops) ✅ · MCP artifact (10 tools) ✅.
- **Next:** an example implementation fronting the Accela portal for `apply_for_permit`; then the next domain from [../domains.md](../domains.md).
