# comptroller.nyc.gov — Low-Hanging Fruit Assessment

A domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **New York City Office of the Comptroller**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (spending, contracts, budget/revenue/payroll, audits, claims, pension holdings, eClaim).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory for **both** properties (WordPress/Imperva office site; Drupal/New Relic Checkbook app).
- [apis-observed.md](apis-observed.md) — the **existing Checkbook NYC API** (probed live) + WordPress REST + SODA + vendors.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (15 Comptroller datasets) with coverage verdicts.
- [opendata-comptroller.md](opendata-comptroller.md) / [opendata-comptroller.json](opendata-comptroller.json) — the 15 Comptroller Open Data assets + column schemas.
- [schemas/](schemas/) — individual JSON Schema per object: `spending-transaction` · `contract` · `audit` · `claim` · `pension-holding` · `claim-filing` (+ shared `_common`).
- [openapi/comptroller.yaml](openapi/comptroller.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/comptroller-mcp.json](mcp/comptroller-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — an XML-era public API that isn't agent-native

The Comptroller is different from the other domains in one crucial way: **it already runs a public API.** [Checkbook NYC](https://www.checkbooknyc.com/api) exposes the City's financial record — **Spending, Contracts, Budget, Revenue, Payroll** — over `POST checkbooknyc.com/api`. We probed it live: **3,227,575** FY2024 spending transactions, **10.2M** payroll, **1.2M** revenue records, **no API key required**.

And yet it is not a modern, owned, agent-native contract:

1. **XML request/response, POST-only**, with a bespoke `search_criteria` / `response_columns` envelope — not resource-oriented REST, not JSON-first.
2. **No OpenAPI, no JSON Schema, no MCP** — nothing an SDK generator or agent can consume.
3. **Bolted onto a vendor Drupal application**, not published under an owned Comptroller API brand.
4. **Disconnected** from the office's *other* data — pension holdings, claims, audits, and bonds live on **NYC Open Data** (15 Socrata assets); the **eClaim** filing workflow lives on the **WordPress** site.

**None of this is one coherent, agent-native NYC Comptroller API.** A resident or agent asking "how much did the City pay vendor X, and were there claims against that agency?" must speak XML to Checkbook, query Socrata for claims, and read HTML for audits.

**Reframe:**

| | Parks | DOE | Council | **Comptroller** |
|---|---|---|---|---|
| Platform | Smarty/PHP | Sitefinity (.NET) | WordPress | **WordPress + Drupal (Checkbook)** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | **a real public API — but XML-era, siloed, not agent-native** |
| Modernization verb | replatform | reclaim | consolidate + own | **consolidate & own (JSON-first)** |

## Reverse-engineered entities

`SpendingTransaction` · `Contract` · `Audit` · `ClaimAgainstCity` (reported) · `PensionHolding` (five systems) · `ClaimFiling` (net-new write) — join keys **agency**, **vendor**, **fiscalYear**, **contractId**, **borough**.

## Method & caveats

Outside-in crawl (browser UA; both properties respect robots). WordPress `wp-json`/`wp-sitemap` for the office site; Drupal fingerprint + a live `POST /api` probe of every Checkbook `type_of_data` domain. Open Data via the Socrata Discovery API, verified label `Office of the Comptroller (COMPTROLLER)` (15 assets — some are federated hrefs, not tables). A sample, not a full spider.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory (2 properties) ✅ · APIs-observed (Checkbook API probed live) ✅ · Open Data crosswalk (15 datasets) ✅ · JSON Schemas (6 + `_common`) ✅ · OpenAPI 3.1 (11 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** a JSON-first, resource-oriented façade over Checkbook + Open Data; wire the eClaim filing write path; then the next domain from [../domains.md](../domains.md).
