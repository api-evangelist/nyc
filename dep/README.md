# dep — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **New York City Department of Environmental Protection (DEP)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (water consumption, reservoir levels, water quality, green infrastructure, hydrants, permits, and the locked/​split billing + service-request transactions).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace; the **uMAX** utility CIS on ASP.NET + **Azure AD B2C**).
- [apis-observed.md](apis-observed.md) — the **open API** (Socrata SODA over 57 datasets) vs. the **uMAX portal with no API** and **NYC311** street-condition intake.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (57 DEP datasets) with coverage verdicts.
- [opendata-dep.md](opendata-dep.md) / [opendata-dep.json](opendata-dep.json) — all 57 DEP Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `reservoir-level` · `water-consumption` · `water-quality` · `green-infrastructure` · `hydrant` · `permit` · `water-service-request` (+ shared `_common`).
- [openapi/dep.yaml](openapi/dep.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/dep-mcp.json](mcp/dep-mcp.json) — design-first MCP server definition (11 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

DEP is **data-rich but transaction-poor**, and that asymmetry is the finding:

1. **Reference data is wide open — but messy.** 57 NYC Open Data datasets publish the water system generously — water consumption (`ia2d-e54m`, DEP's most-viewed asset), reservoir levels, harbor/drinking/watershed/lead-copper water quality, green infrastructure, hydrants, and permits. But the corpus is sprawling and inconsistently typed: **Harbor Water Quality is 100 free-text columns**, reservoir levels are cryptic SCADA tags, and a dozen near-duplicate Watershed tables coexist. Open ≠ usable.
2. **The customer service layer is split and locked.** Water-bill payment and account management run in the **uMAX** My DEP Account portal (`a826-umax.dep.nyc.gov`) — a login-walled ASP.NET SPA behind Azure AD B2C, **no API**. Street conditions — a water-main break, no water, a **sewer backup** — are funneled into generic **NYC311**. Neither is a DEP-owned, machine-readable contract.

**The gap here is transactions, not data.** A resident or agent asking "report that a water main broke on my street" or "my basement is backing up with sewage" has no DEP API to call — it goes to 311.

**Reframe (vs. the earlier domains):**

| | DOE | Council | NYCHA | **DEP** |
|---|---|---|---|---|
| Platform | Sitefinity (.NET) | WordPress | Livesite + Oracle Siebel | **Livesite + uMAX CIS (ASP.NET + Azure B2C)** |
| Core problem | search rented, backend hidden | three APIs, none owned | data open, service locked in a CRM | **data open but messy; transactions split across a billing portal + 311** |
| Modernization verb | **reclaim** | **consolidate + own** | **unlock** | **transact** |

## Reverse-engineered entities

`WaterConsumption` (citywide only) · `ReservoirLevel` · `WaterQualitySample` (analytes as a measurements map) · `GreenInfrastructure` · `Hydrant` · `Permit` (read-only) · `WaterServiceRequest` (net-new write) — join keys **tax Block/Lot/BBL**, **UNITID**, **GI_ID**, the geography spine.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite, Dynatrace); the My DEP Account portal was identified as the uMAX CIS on ASP.NET + Azure AD B2C from its redirect chain, cookies, and B2C authorize URL without authenticating. Open Data agency label verified via the Socrata Discovery API; all 57 assets pulled with columns. A sample, not a full spider; the uMAX portal's internal workflows and NYC311's DEP intake are inferred from DEP's documented services, not scraped behind login.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (57 datasets) ✅ · JSON Schemas (7 + common) ✅ · OpenAPI 3.1 (9 paths/11 ops) ✅ · MCP artifact (11 tools) ✅.
- **Next:** an example implementation fronting NYC311 + uMAX for `report_water_problem`; then the next domain from [../domains.md](../domains.md).
