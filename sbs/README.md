# sbs — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Department of Small Business Services (SBS)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (certified businesses, BIDs, Workforce1 events and jobs, service centers, incentives, and the locked portal workflows).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace; the **MyCity Business** portal on **Spring + Adobe AEM**, hosting the **Step-by-Step** wizard).
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA over 28 datasets) vs. the **MyCity Business portal with no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (28 SBS datasets) with coverage verdicts.
- [opendata-sbs.md](opendata-sbs.md) / [opendata-sbs.json](opendata-sbs.json) — all 28 SBS Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `certified-business` · `business-improvement-district` · `service-location` · `workforce-event` · `job-listing` · `business-incentive` · `mwbe-certification-application` (+ shared `_common`).
- [openapi/sbs.yaml](openapi/sbs.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/sbs-mcp.json](mcp/sbs-mcp.json) — design-first MCP server definition (10 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

SBS is a **navigator agency**, and that is the finding:

1. **Program data is reasonably open.** 28 NYC Open Data datasets publish the directories generously — the **SBS Certified Business List** (`ci93-uc8s`, 56 columns), **Business Improvement Districts** (directory, maps, and a 64-column FY24 trends report), **Workforce1** recruitment events and job listings, service-center locations, and business-incentive rolls.
2. **The guidance and eligibility engine is locked.** The **MyCity Business** portal (`nyc-business.nyc.gov`) is a **Spring + Adobe AEM** application — session-walled, JavaScript-only, **no API**. The **Step-by-Step licensing wizard**, incentive eligibility, and the M/WBE **certification** and Workforce1 **enrollment** flows have no machine-readable contract at all.

**The gap here is navigation, not directories.** A business or agent asking "what do I need to open a café?" or "help me apply for women-owned business certification" has nothing to call.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **SBS** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | NYC.gov Livesite + Oracle Siebel portal | **NYC.gov Livesite + MyCity Business (Spring + Adobe AEM)** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **directories open, guidance/eligibility engine locked in a stateful portal** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **navigate** |

## Reverse-engineered entities

`CertifiedBusiness` · `BusinessImprovementDistrict` · `WorkforceEvent` · `JobListing` · `ServiceLocation` · `BusinessIncentive` · `MWBECertificationApplication` (net-new write) — join keys **Account_Number**, **NAICS**, **org_id**, **BBL/BIN**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite, Dynatrace); the MyCity Business portal was identified as Spring + Adobe AEM from its `SESSION` cookie, `universal-editor-service.adobe.io` include, and jQuery/Handlebars bundles, and the Step-by-Step wizard confirmed at `/nycbusiness/wizard` — all without authenticating. Open Data agency label verified via the Socrata Discovery API; all 28 assets pulled with columns. A sample, not a full spider; the portal's internal workflows are inferred from SBS's documented services, not scraped behind login.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (28 datasets) ✅ · JSON Schemas (7 + common) ✅ · OpenAPI 3.1 (11 paths/ops) ✅ · MCP artifact (10 tools) ✅.
- **Next:** an example implementation fronting the MyCity Business portal for `apply_for_mwbe_certification`; then the next domain from [../domains.md](../domains.md).
