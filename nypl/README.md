# nypl — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **New York Public Library (NYPL)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (digital collections, branches/hours, events, catalog, and the net-new hold).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYPL-owned open-source stack: Rails Digital Collections API + PHP/Slim Locations API + Node/AWS discovery-api + **Sierra** ILS; Imperva Incapsula edge).
- [apis-observed.md](apis-observed.md) — the **three real, owned public APIs** vs. the one write gap (holds).
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (6 NYPL datasets) with coverage verdicts.
- [opendata-nypl.md](opendata-nypl.md) / [opendata-nypl.json](opendata-nypl.json) — all 6 NYPL Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `digital-item` · `collection` · `branch` · `event` · `catalog-item` · `hold` (+ shared `_common`).
- [openapi/nypl.yaml](openapi/nypl.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/nypl-mcp.json](mcp/nypl-mcp.json) — design-first MCP server definition (11 agent tools; artifact, not a deployment).

## What was found — the counter-example

NYPL is the **counter-example** of this project, and that is the finding:

1. **NYPL already has real public APIs.** It is an independent nonprofit, not a city agency, and it has built and operated genuinely good APIs for years: the **Digital Collections API** (`api.repo.nypl.org/api/v2`, token-authenticated Rails, over millions of digitized items with MODS metadata, captures, and rights); the open, hypermedia **Locations API** (`refinery.nypl.org`, with hours, amenities, access, and links to events/exhibitions/alerts); and the **Research Catalog** behind the open-source `discovery-api` + Sierra ILS.
2. **NYPL owns and open-sources its stack.** Nearly everything is on **github.com/NYPL** — the `nypl-core` ontology, an accessibility-first React design system, a web ebook reader, and patron/hold microservices.
3. **NYC Open Data is a thin afterthought.** Only **6** NYPL datasets, mostly **stale 2010-2011** branch-services stats — NYPL's living data is on its own APIs, not Open Data.

**The gap here is unification and one write, not liberation.** The three good APIs are separate contracts, and placing a **hold** — though backed by real internal services — has no clean, documented, agent-native public API.

**Reframe (vs. the earlier domains):**

| | NYCHA | BIC | **NYPL** |
|---|---|---|---|
| Platform | NYC.gov + Oracle Siebel CRM | NYC.gov + Salesforce portal | **NYPL-owned open-source stack (Rails/PHP/Node) + Sierra ILS** |
| Core problem | data open, service layer locked | registry open, transactions locked | **already has good public APIs; needs unifying + one write** |
| Modernization verb | **unlock** | **transact** | **lead** |

## Reverse-engineered entities

`DigitalItem` · `Collection` · `Branch` (Location) · `Event` · `CatalogItem` (Bib/Book) · `Hold` (net-new write) — join keys **UUID** (Digital Collections), Locations **slug**, Sierra **bib id**; `ResearchDivision` carried as a field.

## Method & caveats

Outside-in crawl (browser UA). `www.nypl.org` sits behind Imperva Incapsula, so its origin headers are edge-obscured; the substantive findings come from probing NYPL's own APIs directly (the Digital Collections API's 401 auth gate and Rails/Passenger fingerprint; the Locations API's live hypermedia payload and PHP/Slim error namespace) and from enumerating the github.com/NYPL open-source org. Open Data agency label verified via the Socrata Discovery API; all 6 assets pulled with columns. A sample, not a full spider; the internal hold/patron services are identified from their public open-source repos, not exercised behind patron authentication.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (6 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (13 paths/ops) ✅ · MCP artifact (11 tools) ✅.
- **Next:** an example implementation unifying the three APIs and exposing `place_hold` over NYPL's existing internal hold services; then the next domain from [../domains.md](../domains.md).
