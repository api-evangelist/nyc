# ddc — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Department of Design and Construction (DDC)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (capital projects, awarded contracts, vendors, divisions, solicitations, and the net-new prequalification write).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace + mPulse + AWS ALB; the **citywide** PASSPort/MOCS, City Record, Checkbook NYC, and DDC Anywhere systems).
- [apis-observed.md](apis-observed.md) — the **one open data surface** (Socrata SODA over 4 datasets) vs. the **citywide transaction systems DDC doesn't own** and no DDC API.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (4 DDC datasets) with coverage verdicts.
- [opendata-ddc.md](opendata-ddc.md) / [opendata-ddc.json](opendata-ddc.json) — all 4 DDC Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `capital-project` · `awarded-contract` · `vendor` · `division` · `solicitation` · `vendor-prequalification` (+ shared `_common`).
- [openapi/ddc.yaml](openapi/ddc.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/ddc-mcp.json](mcp/ddc-mcp.json) — design-first MCP server definition (10 agent tools; artifact, not a deployment).

## What was found — the sixth distinct pattern

DDC is a **vendor-facing, business-to-government agency**, and that is the finding:

1. **DDC owns almost none of its surface.** Its only machine-readable data is **4 NYC Open Data datasets** — three frozen `(Historical)` snapshots of active projects plus a 4-column directory of awarded contracts. There is **no DDC API** of any kind, and the richer live capital data is published under OMB/Comptroller, not DDC.
2. **Every transaction is outsourced.** Solicitations and vendor prequalification run in **PASSPort** (MOCS), notices go to the **City Record**, contract records live on **Checkbook NYC** (Comptroller), and DDC's own **DDC Anywhere** portal exposes no API.

**The gap here is ownership, not just data.** A firm or agent asking "what DDC solicitations are open and how do I prequalify?" has no DDC API to call — and there is **no citizen surface at all**, because DDC builds for other agencies.

**Reframe (vs. the earlier domains):**

| | NYCHA | DFTA | **DDC** |
|---|---|---|---|
| Platform | NYC.gov Livesite + Oracle Siebel | NYC.gov Livesite + phone contact center | **NYC.gov Livesite + citywide PASSPort/MOCS, City Record, Checkbook** |
| Core problem | data open, service layer locked in a CRM | provider network open, connecting is a phone call | **data thin & historical, transactions on systems DDC doesn't own** |
| Modernization verb | **unlock** | **connect** | **surface** |

## Reverse-engineered entities

`CapitalProject` · `AwardedContract` · `Vendor` (firm/consultant) · `Division` · `Solicitation` (citywide, no DDC twin) · `VendorPrequalification` (net-new B2G write) — join keys **Project ID**, **PIN**, **SELECTED FIRM**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite, Dynatrace, mPulse, AWS ALB); the vendor/procurement systems were identified from the "Work With DDC" page, which explicitly routes all solicitations through citywide PASSPort/MOCS. Open Data agency label verified via the Socrata Discovery API; all 4 assets pulled with columns. A sample, not a full spider; the citywide systems' internal workflows are inferred from DDC's documented procurement guidance, not scraped behind login. There is **no citizen write** in this domain — the net-new write is honestly B2G (vendor prequalification).

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (4 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (10 paths/11 ops) ✅ · MCP artifact (10 tools) ✅.
- **Next:** an example implementation fronting PASSPort for `submit_prequalification`; then the next domain from [../domains.md](../domains.md).
