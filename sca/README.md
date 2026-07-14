# sca — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC School Construction Authority (SCA)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (capital projects, upcoming contracts, RFP solicitations, prequalified vendors, enrollment/capacity, inspections, and the locked vendor transactions).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (a **DotNetNuke (DNN)** ASP.NET CMS behind AWS with content in Azure Blob; the login-walled **SharePoint** bidset portal).
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA over 43 datasets) vs. the **SharePoint bidset portal with no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (43 SCA datasets) with coverage verdicts.
- [opendata-sca.md](opendata-sca.md) / [opendata-sca.json](opendata-sca.json) — all 43 SCA Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `capital-project` · `upcoming-contract` · `solicitation` · `prequalified-firm` · `enrollment-capacity` · `inspection` · `vendor-prequalification` (+ shared `_common`).
- [openapi/sca.yaml](openapi/sca.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/sca-mcp.json](mcp/sca-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

SCA is a **vendor-facing agency**, and its read/write split is the finding:

1. **The capital pipeline is wide open.** 43 NYC Open Data datasets publish the plan generously — active projects under construction (`8586-3zfm`, SCA's most-viewed dataset), schedules and budgets, capacity by school, the upcoming CIP/CAP contract pipeline, current/anticipated RFP notices, change orders, the prequalified/disqualified vendor roster, enrollment/capacity demand, and inspections.
2. **The vendor transaction layer is locked.** The **bidset portal** (`bidset.nycsca.org`) is a **SharePoint** app — login-walled, no API — and prequalification is PDF forms. Getting prequalified, obtaining bid documents, and bidding have no machine-readable contract at all.

**The gap here is vendor transactions, not data.** A firm or agent asking "how do I get prequalified for this trade?" has nothing to call — even though the *roster* of who got prequalified is open.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **SCA** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | Livesite + Oracle Siebel | **DotNetNuke + SharePoint** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **data open, vendor layer locked in SharePoint** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **onboard** |

## Reverse-engineered entities

`CapitalProject` · `UpcomingContract` · `Solicitation` · `PrequalifiedFirm` · `EnrollmentCapacity` · `Inspection` · `VendorPrequalification` (net-new write) — join keys **Building ID/BIN**, **DSF Number**, **Geographic (school) District**, **Master Trade Code**, **BBL**.

## Method & caveats

Outside-in crawl (browser UA; `nycsca.org/robots.txt` disallows DNN system paths, not content). The site was fingerprinted from headers and markup (DotNetNuke, obvio skin, ASP.NET `__VIEWSTATE`, AWS ALB cookies, Azure Blob document URLs); the bidset portal was identified as SharePoint from its custom-login markup (`OnlineBidsetsLogin/CustomLogin.aspx`) without authenticating. The `/WS/Reports/` path was checked and returns DNN HTML, not JSON. Open Data agency label verified via the Socrata Discovery API; all 43 assets pulled with columns. A sample, not a full spider; the bidset portal's internal workflows are inferred from SCA's documented vendor process, not scraped behind login.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (43 datasets) ✅ · JSON Schemas (7 + common) ✅ · OpenAPI 3.1 (9 paths/10 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** an example implementation fronting the bidset/prequalification workflow for `apply_for_prequalification`; then the next domain from [../domains.md](../domains.md).
