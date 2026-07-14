# coib — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Conflicts of Interest Board (COIB)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (enforcement dispositions, donations, policymakers, legal defense trusts, advisory opinions, and the locked filing/attestation transactions).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace; the login-gated **Annual Financial Disclosure filing website**).
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA over 8 datasets) vs. the **filing website with no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (8 COIB datasets) with coverage verdicts.
- [opendata-coib.md](opendata-coib.md) / [opendata-coib.json](opendata-coib.json) — all 8 COIB Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `enforcement-disposition` · `agency-donation` · `policymaker` · `legal-defense-trust-transaction` · `advisory-opinion` · `financial-disclosure-filing` (+ shared `_common`).
- [openapi/coib.yaml](openapi/coib.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/coib-mcp.json](mcp/coib-mcp.json) — design-first MCP server definition (8 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

COIB is a **transparency-out / attestation-in** agency, and that direction is the finding:

1. **Transparency outputs are open.** 8 NYC Open Data datasets publish the enforcement/transparency record generously — **Enforcement Fines** (`p39r-nm7f`, 13 columns, the most-viewed asset), three donation streams, the monthly **Policymakers List**, and three **legal defense trust** streams.
2. **The compliance input is locked.** The **Annual Financial Disclosure filing website** is a login-gated electronic system — no API. Filing/attesting an annual disclosure report, completing ethics training, and requesting waivers have no machine-readable contract at all.

**The gap here is the attestation transaction, not the transparency data.** A public servant or agent asking "is my annual disclosure filed?" or "submit my report" has nothing to call.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **COIB** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | NYC.gov Livesite + Oracle Siebel | **NYC.gov Livesite + login-only filing website** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **transparency open, compliance filing locked in a login-only system** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **attest** |

## Reverse-engineered entities

`EnforcementDisposition` · `AgencyDonation` (three donation streams) · `Policymaker` · `LegalDefenseTrustTransaction` (donations/refunds/expenditures) · `AdvisoryOpinion` (PDF reference) · `FinancialDisclosureFiling` (net-new write) — join keys **Case Number**, **Agency Name**, **Trust Name**, **Donation ID**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, AWS ALB, Livesite v22, Dynatrace, mPulse); the filing system was identified from the Annual Disclosure pages ("file electronically through COIB's filing website") without authenticating. Open Data agency label verified via the Socrata Discovery API; all 8 assets pulled with columns. A sample, not a full spider; the filing website's internal workflow is inferred from COIB's documented disclosure process, not scraped behind login.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (8 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (10 ops) ✅ · MCP artifact (8 tools) ✅.
- **Next:** an example implementation fronting the filing website for `file_financial_disclosure`; then the next domain from [../domains.md](../domains.md).
