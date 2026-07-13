# dvs — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Department of Veterans' Services (DVS)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (resource map, veteran-owned businesses, assistance requests, cases, client demographics, and the locked VetConnectNYC referral).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace; the third-party **VetConnectNYC** intake on **Combined Arms**).
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA over 7 datasets) vs. the **Combined Arms portal with no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (7 DVS datasets) with coverage verdicts.
- [opendata-dvs.md](opendata-dvs.md) / [opendata-dvs.json](opendata-dvs.json) — all 7 DVS Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `veteran-resource` · `veteran-owned-business` · `assistance-request` · `case` · `client-statistics` · `service-referral` (+ shared `_common`).
- [openapi/dvs.yaml](openapi/dvs.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/dvs-mcp.json](mcp/dvs-mcp.json) — design-first MCP server definition (8 agent tools; artifact, not a deployment).

## What was found — a connective agency with a vendor service layer

DVS is a **connective agency**, and where its "connection" lives is the finding:

1. **DVS is unusually open.** 7 NYC Open Data datasets publish not only reference directories — the **DVS Resource Map** (`af2s-4k4p`) and **NYC Veteran Owned Businesses** (`ybdk-jmnn`, 27 columns, fully geocoded) — but **de-identified service analytics**: assistance requests (with a `VetConnectNYC (Y/N)` flag), cases, client demographics, and historical request processing.
2. **The live referral is a third-party form.** **VetConnectNYC** — the coordinated-care intake DVS points veterans to — runs on **Combined Arms'** "Military Resource Portal" (`nyc.veteranportal.combinedarms.us`, Next.js on CloudFront), **no API**. A veteran submits the request form; DVS Care Coordinators work it manually within **3–5 business days**.

**The gap here is the live referral, not the data.** A veteran or agent asking "connect me to housing help in the Bronx and tell me the status" has nothing to call.

**Reframe (vs. the earlier domains):**

| | NYCHA | DFTA | **DVS** |
|---|---|---|---|
| Platform | NYC.gov Livesite + Oracle Siebel portal | NYC.gov Livesite + phone-based Aging Connect | **NYC.gov Livesite + third-party Combined Arms portal (VetConnectNYC)** |
| Core problem | data open, service layer locked in a CRM | data open, service layer is a contact center | **data (even service data) open, live referral locked in an out-of-city vendor form** |
| Modernization verb | **unlock** | **connect** | **coordinate** |

## Reverse-engineered entities

`VeteranResource` · `VeteranOwnedBusiness` · `AssistanceRequest` (de-identified) · `Case` (de-identified) · `ClientStatistics` (aggregate only) · `ServiceReferral` (net-new write; the VetConnectNYC referral) — join key **DVS_RES_ID** for resources/businesses.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite v22, Dynatrace); the VetConnectNYC intake was resolved from the services page to `nyc.veteranportal.combinedarms.us` and identified as the **Combined Arms** "Military Resource Portal" (`<title>CA - Military Resource Portal</title>`, `x-powered-by: Next.js`, CloudFront) — no packaged API or OpenAPI is exposed. Open Data agency label verified via the Socrata Discovery API; all 7 assets pulled with columns. A sample, not a full spider; VetConnectNYC's internal care-coordination workflow is inferred from DVS's documented services, not scraped behind login. **Vendor correction:** the assignment tentatively guessed Unite Us; the crawl shows Combined Arms.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (7 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (7 paths/9 ops) ✅ · MCP artifact (8 tools) ✅.
- **Next:** an example implementation fronting VetConnectNYC for `make_referral`; then the next domain from [../domains.md](../domains.md).
