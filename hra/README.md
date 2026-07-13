# hra — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Human Resources Administration / Department of Social Services (HRA/DSS)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (programs, centers, caseloads, case actions, the open eligibility rules, and the locked application portal).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace; **ACCESS NYC** on WordPress/WP Engine with an **open-source Drools** rules engine; the **ACCESS HRA** React SPA).
- [apis-observed.md](apis-observed.md) — the **open API** (Socrata SODA over 49 datasets) and the **open-source rules** (ACCESS-NYC-Rules) vs. the **screener and portal with no callable API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (49 HRA datasets) with coverage verdicts.
- [opendata-hra.md](opendata-hra.md) / [opendata-hra.json](opendata-hra.json) — all 49 HRA Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `program` · `center` · `caseload-statistic` · `case-action` · `benefits-eligibility` · `benefits-application` (+ shared `_common`).
- [openapi/hra.yaml](openapi/hra.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/hra-mcp.json](mcp/hra-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

HRA is a **three-surface benefits domain**, and the disconnection between those surfaces is the finding:

1. **The caseload data is wide open.** **49 NYC Open Data datasets** publish SNAP/Cash Assistance/Medicaid recipient and case counts, application-center directories, wait times, and 75-column case-action reports.
2. **The eligibility logic is open source.** The **ACCESS NYC** screener runs on a public **Drools** rules engine (`NYCOpportunity/ACCESS-NYC-Rules`). The hardest, most agency-specific part — who qualifies for what — is already public and city-owned.
3. **But the service layer is locked.** The **ACCESS HRA** portal (`a069-access.nyc.gov`) is a React SPA behind Akamai — login-walled, JavaScript-only, **no API**. Applying for benefits and checking a case have no machine-readable contract at all.

**The gap here is the connective tissue, not the data or the logic.** A resident or agent asking "what do I qualify for, where do I apply, and what's my case status?" must cross three disconnected apps and has nothing to call for the last one.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **HRA** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | NYC.gov Livesite + Oracle Siebel portal | **Livesite + ACCESS NYC (WordPress, open-source Drools) + ACCESS HRA (React SPA)** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **data open + eligibility engine open-sourced, but no API binds screen→eligibility→apply** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **connect** |

## Reverse-engineered entities

`Program` · `Center` · `CaseloadStatistic` (aggregate) · `CaseAction` (aggregate only) · `BenefitsEligibility` (ACCESS NYC screening result) · `BenefitsApplication` (net-new write) — join keys **program code**, **center number**, **BIN/BBL/NTA/council**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite, Dynatrace); ACCESS NYC from headers + markup (Cloudflare, WP Engine, theme `access`) and its GitHub org (`NYCOpportunity/ACCESS-NYC-Rules`, a Drools engine); ACCESS HRA from its React app shell and Akamai bot-manager cookies without authenticating. Open Data agency label verified via the Socrata Discovery API (`Human Resources Administration (HRA)` = 49; `Department of Social Services (DSS)` = 0); all 49 assets pulled with columns. A sample, not a full spider; the ACCESS HRA portal's internal workflows are inferred from HRA's documented benefits services, not scraped behind login.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (49 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (9 paths/10 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** an example implementation wrapping the ACCESS NYC Drools rules as `POST /eligibility` and fronting the ACCESS HRA portal for `apply_for_benefits`; then the next domain from [../domains.md](../domains.md).
