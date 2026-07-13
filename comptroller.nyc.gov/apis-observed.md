# APIs Observed While Crawling — comptroller.nyc.gov + checkbooknyc.com

Backend/service APIs the Comptroller's properties call or expose, surfaced during the crawl (2026-07-13). Like Council, this domain is unusual: **a real public API already exists** — the **Checkbook NYC API** — yet it is XML-first, vendor-hosted, and disconnected from the office's other data. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`POST checkbooknyc.com/api`** | Financial-data API (XML in/out) | **NYC Comptroller** (Checkbook NYC) | **Yes — open, no key** | The existing public spending API. `type_of_data` ∈ {Spending, Contracts, Budget, Revenue, Payroll}; bespoke `search_criteria`/`response_columns` XML envelope. **Probed live** — see below. |
| `comptroller.nyc.gov/wp-json` (`wp/v2`) | WordPress REST API | NYC Comptroller | **Yes — open** | Posts, pages, media, and custom types (`report`, `rfp`, `event`, `nyc_bonds`, `job`). Content, not financial resources. |
| `data.cityofnewyork.us` (SODA) | Open Data API | NYC (Socrata/Tyler) | Yes | 15 Comptroller assets — pension holdings (5 systems), claims report, published audits, bonds, debt service. Flattened snapshots; the top asset is a federated *href* to Checkbook, not a table. |
| `facetwp/v1` (on comptroller.nyc.gov) | Faceted-search REST | FacetWP (plugin) | Internal | Powers site search/filtering; not a data API. |
| New Relic (`*.nr-data.net`) | RUM/monitoring API | New Relic (vendor) | Vendor | On checkbooknyc.com. |
| Google Analytics / AddToAny | Analytics / sharing | Google / AddToAny | Vendor | Both properties. |

## The Checkbook NYC API — probed live

`POST https://www.checkbooknyc.com/api` with an XML body. A minimal Spending request returned real data:

```
type_of_data=Spending, fiscal_year=2024  →  record_count 3,227,575
  top rows: Police Department $414,069,787.65 ; Department of Education $155,467,775.81
```

Confirmed reachable domains and their FY2024 volumes: **Spending 3.23M**, **Payroll 10.2M**, **Revenue 1.25M**; **Contracts** (requires `status` + `category`) and **Budget** (keyed on `year`/budget codes) both validated. No API key required. Default response is **XML**.

## Takeaways

- **The API problem here is shape and ownership, not absence.** Checkbook NYC is a genuine, high-volume public API — but XML-envelope, POST-only, no OpenAPI/JSON Schema/MCP, and not published under an owned Comptroller API contract.
- **The office's data is split across three surfaces** — Checkbook (spending/contracts), NYC Open Data (pension, claims, audits, bonds), and the WordPress site (eClaim, reports) — with no unifying resource model.
- **No agent-native surface.** The [OpenAPI](openapi/comptroller.yaml) + [MCP artifact](mcp/comptroller-mcp.json) here propose one owned, JSON-first contract that consolidates the three and adds the net-new **eClaim filing** write workflow.
