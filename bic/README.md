# bic — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **New York City Business Integrity Commission (BIC)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (licensees, registrants, market businesses, fleet, violations, complaints, and the locked portal transactions).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace; the **Salesforce Experience Cloud** licensing portal).
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA over 9 datasets) vs. the **Salesforce portal with no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (9 BIC datasets) with coverage verdicts.
- [opendata-bic.md](opendata-bic.md) / [opendata-bic.json](opendata-bic.json) — all 9 BIC Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `licensee` · `registrant` · `market-business` · `vehicle` · `violation` · `complaint` · `trade-waste-license-application` (+ shared `_common`).
- [openapi/bic.yaml](openapi/bic.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/bic-mcp.json](mcp/bic-mcp.json) — design-first MCP server definition (10 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

BIC is a **split domain**, and that split is the finding:

1. **The regulatory registry is the most open yet.** 9 NYC Open Data datasets publish the whole regulated population generously — trade waste hauler **licensees** (`867j-5pgi`, ~78k views), broker/self-hauler/C&D **registrants**, public wholesale-**market** businesses (Hunts Point, Fulton Fish), the **fleet**, issued **violations**, **complaints**, and **denials** — all keyed on **BIC NUMBER**.
2. **The transaction layer is locked.** The licensing portal (`bicportal.nyc.gov`) is a **Salesforce Experience Cloud** app — login-walled, JavaScript-only, **no API**. Applying, renewing, and paying a fine (`/s/viopay`) have no machine-readable contract at all.

**The gap here is transactions, not data.** A business or agent asking "submit my trade waste license application" or "what's the status?" has nothing to call — the only public trace of that pipeline is the list of companies that were *denied*.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **BIC** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | NYC.gov Livesite + Oracle Siebel | **NYC.gov Livesite + Salesforce Experience Cloud** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **registry wide open, licensing lifecycle locked in a SaaS** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **transact** |

## Reverse-engineered entities

`Licensee` · `Registrant` · `MarketBusiness` · `Vehicle` · `Violation` · `Complaint` · `TradeWasteLicenseApplication` (net-new write) — join key **BIC NUMBER**, plus the NYC geography spine.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite v22, Dynatrace); the portal was identified as Salesforce Experience Cloud from response headers (`server: sfdcedge`, `x-sfdc-request-id`) and its Lightning `/s/` path scheme (`/s/viopay`, `/s/login`) without authenticating. Open Data agency label verified via the Socrata Discovery API; all 9 assets pulled with columns. A sample, not a full spider; the Salesforce portal's internal workflows are inferred from BIC's documented licensing services, not scraped behind login.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (9 datasets) ✅ · JSON Schemas (7 + common) ✅ · OpenAPI 3.1 (12 paths/12 ops) ✅ · MCP artifact (10 tools) ✅.
- **Next:** an example implementation fronting the Salesforce portal for `apply_for_license`; then the next domain from [../domains.md](../domains.md).
