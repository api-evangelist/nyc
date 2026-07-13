# dcwp — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Department of Consumer and Worker Protection (DCWP, formerly DCA)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (licenses, applications, inspections, charges, consumer complaints, worker-protection matters, and the two portal-locked writes).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace; the **Java NYC Business** licensing portal; CityPay; 311).
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA over 37 datasets) vs. the **portals with no API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (37 DCWP datasets) with coverage verdicts.
- [opendata-dcwp.md](opendata-dcwp.md) / [opendata-dcwp.json](opendata-dcwp.json) — all 37 DCWP Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `business-license` · `license-application` · `inspection` · `charge` · `consumer-complaint` · `worker-protection-case` (+ shared `_common`).
- [openapi/dcwp.yaml](openapi/dcwp.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/dcwp-mcp.json](mcp/dcwp-mcp.json) — design-first MCP server definition (10 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

DCWP is the **most-open domain** in the project, and that openness is the finding:

1. **The whole lifecycle is already open.** 37 NYC Open Data datasets publish apply → issue → inspect → charge → complain → revoke, plus the Office of Labor Policy & Standards' worker-protection matters — all joinable on **Business Unique ID** and **License Number**.
2. **But nothing binds it, and the writes are locked.** No owned contract binds the 37 datasets into one model, and the two things a person *does* — **apply for a license** (Java NYC Business portal) and **file a consumer complaint** (311 / web form) — have no API.

**The gap here is binding + the two writes, not liberation.** A consumer or agent asking "is this contractor licensed and what has DCWP charged them with?" must stitch 37 Socrata IDs; asking "file a complaint that this shop overcharged me" has nothing to call.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **DCWP** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | NYC.gov Livesite + Oracle Siebel | **NYC.gov Livesite + Java NYC Business portal + CityPay/311** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **whole lifecycle open across 37 IDs, no owned contract, two citizen writes locked** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **bind + add the writes** |

## Reverse-engineered entities

`BusinessLicense` · `LicenseApplication` (net-new write) · `Inspection` · `Charge` (violation) · `ConsumerComplaint` (net-new write) · `WorkerProtectionCase` (aggregate only) — join keys **Business Unique ID**, **License Number**, **Application ID**, **Inspection Number**, **NOH Number**, **BBL/BIN**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite v22, Dynatrace); the NYC Business portal was identified as a Java/Spring app from its `SESSION` cookie and app path without authenticating. Open Data agency label verified via the Socrata Discovery API; all 37 assets pulled with columns. A sample, not a full spider; the portals' internal workflows are inferred from DCWP's documented services, not scraped behind login.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (37 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (11 ops) ✅ · MCP artifact (10 tools) ✅.
- **Next:** an example implementation binding the 37 datasets and fronting the NYC Business portal / 311 for `apply_for_license` and `file_complaint`; then the next domain from [../domains.md](../domains.md).
