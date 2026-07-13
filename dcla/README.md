# dcla — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Department of Cultural Affairs (DCLA)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (cultural organizations, program & capital grants, Cultural Institutions Group, Percent for Art, Materials for the Arts, and the portal-locked grant application).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace; the **Salesforce Experience Cloud** Grants Management System).
- [apis-observed.md](apis-observed.md) — the **one open API** (Socrata SODA over 9 datasets) vs. the **Salesforce grants portal with no public API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (9 DCLA datasets) with coverage verdicts.
- [opendata-dcla.md](opendata-dcla.md) / [opendata-dcla.json](opendata-dcla.json) — all 9 DCLA Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `cultural-organization` · `program-funding` · `capital-funding` · `cultural-institution` · `public-artwork` · `materials-for-the-arts` · `grant-application` (+ shared `_common`).
- [openapi/dcla.yaml](openapi/dcla.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/dcla-mcp.json](mcp/dcla-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the grantmaker pattern

DCLA is a **grantmaker that publishes outcomes but not the application**, and that split is the finding:

1. **The funding results are open.** 9 NYC Open Data datasets publish who DCLA funded and for how much — **program grants** (`y6fv-k6p7`), **capital funding** (`7hgn-sgmk`), and **Cultural Institutions Group** operating support (`ka27-qx5k`) — plus a geocoded **cultural-organization directory** (`u35m-9t32`, 16c), completed **Percent for Art** commissions (`gzdv-qiga`), and **Materials for the Arts** donation summaries (`vhtt-kpwy`).
2. **The application is locked.** The **Grants Management System** (`dclagms.nyc.gov`) is a **Salesforce Experience Cloud** community — login-walled, browser-only, **no public API**. Applying for a Cultural Development Fund grant has no machine-readable contract at all, and no Open Data twin.

**The gap here is the request, not the result.** An organization or agent asking "apply for this grant" or "what's the status of my application?" has nothing to call.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | DCWP | **DCLA** |
|---|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | NYC.gov Livesite + Oracle Siebel | NYC.gov Livesite + Java NYC Business portal | **NYC.gov Livesite + Salesforce Grants Management System** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer locked in a CRM | lifecycle open across 37 IDs, no owned contract, writes locked | **funding outcomes open, the grant application locked in Salesforce, no owned API** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **bind + add the writes** | **open the grant pipeline** |

## Reverse-engineered entities

`CulturalOrganization` · `ProgramFunding` (grant award) · `CapitalFunding` · `CulturalInstitution` (CIG) · `PublicArtwork` (Percent for Art) · `MaterialsForTheArts` (aggregate only) · `GrantApplication` (net-new write) — join keys **Organization Name**, **Application #**, **Fiscal Year (FY)**, **BIN/BBL**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite v22, Dynatrace); the Grants Management System was identified as a Salesforce Experience Cloud community from its `/grants/s/` redirect chain, `LSKey-c$` cookies, and the `culturalaffairsnyc.my.salesforce.com` SAML issuer in its login markup — without authenticating. Open Data agency label verified via the Socrata Discovery API; all 9 assets pulled with columns. A sample, not a full spider; the portal's internal workflow is inferred from DCLA's documented Cultural Development Fund process, not scraped behind login.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (9 datasets) ✅ · JSON Schemas (7 + common) ✅ · OpenAPI 3.1 (10 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** an example implementation binding the 9 datasets and fronting the Salesforce Grants Management System for `apply_for_grant`; then the next domain from [../domains.md](../domains.md).
