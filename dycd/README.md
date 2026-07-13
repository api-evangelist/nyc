# dycd — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Department of Youth and Community Development (DYCD)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (programs, program sites, providers, contracts, service areas, participant demographics, and the app-only application transaction).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace; the **DYCD Connect / DiscoverDYCD** Angular app on **Microsoft-IIS** with a private `/api/`).
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA over 15 datasets) vs. the **DiscoverDYCD finder with a private, undocumented backend**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (15 DYCD datasets) with coverage verdicts.
- [opendata-dycd.md](opendata-dycd.md) / [opendata-dycd.json](opendata-dycd.json) — all 15 DYCD Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `program` · `program-site` · `provider` · `contract` · `service-area` · `participant-demographics` · `program-application` (+ shared `_common`).
- [openapi/dycd.yaml](openapi/dycd.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/dycd-mcp.json](mcp/dycd-mcp.json) — design-first MCP server definition (10 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

DYCD is a **funder/intermediary**, and the shape of that is the finding:

1. **The supply chain is wide open.** 15 NYC Open Data datasets publish the whole delivery network — **program sites** (`ebkm-iyma`, 34 columns with a full geography spine, slots, and participants), **contracts** (`graj-69em`), **contractors/providers** (`75e9-fg2t`), **Neighborhood Development Areas** (`vd7c-qjsx`), and aggregate **participant demographics** (`k9kq-67vm`, 52 columns).
2. **DYCD already built the finder — as an app, not an API.** **DiscoverDYCD** (`discoverdycd.dycdconnect.nyc`) is a DYCD-owned Angular application on Microsoft-IIS that helps the public find programs — but its backend is a **private, undocumented `/api/`**, there is no clean Open Data catalog of the program offerings, and **there is no public API to apply**.

**The gap here is the finder-as-API and the apply transaction, not the supply data.** A young person or agent asking "what summer programs can I apply to?" or "apply me to SYEP" has nothing to call.

**Reframe (vs. the earlier domains):**

| | DOE | Council | NYCHA | **DYCD** |
|---|---|---|---|---|
| Platform | Sitefinity (.NET) | WordPress | NYC.gov Livesite + Oracle Siebel portal | **NYC.gov Livesite + DYCD Connect / DiscoverDYCD (IIS + Angular)** |
| Core problem | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | **supply open + a finder DYCD owns, but the finder is an app with a private API and applying has none** |
| Modernization verb | **reclaim** | **consolidate + own** | **unlock** | **surface** |

## Reverse-engineered entities

`Program` · `ProgramSite` · `Provider` · `Contract` · `ServiceArea` (Neighborhood Development Area) · `ParticipantDemographics` (aggregate only) · `ProgramApplication` (net-new write) — join keys **PortfolioID**, **Contract Number**, **Provider**, **NDA**, BBL/BIN.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite, Dynatrace, AWS ALB); the DYCD Connect / DiscoverDYCD apps were identified as Microsoft-IIS + Angular from response headers and page markup (hashed bundles, `<title>discoverDYCD</title>`, an internal `/api/` that returns 404 to public probes) without authenticating. Open Data agency label verified via the Socrata Discovery API; all 15 assets pulled with columns. A sample, not a full spider; the finder's internal API contract and the application flow are inferred from DYCD's documented services, not scraped behind login.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (15 datasets) ✅ · JSON Schemas (7 + common) ✅ · OpenAPI 3.1 (11 paths/ops) ✅ · MCP artifact (10 tools) ✅.
- **Next:** an example implementation surfacing the DiscoverDYCD finder and fronting the application flow for `apply_to_program`; then the next domain from [../domains.md](../domains.md).
