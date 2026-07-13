# Low-Hanging Fruit Index — comptroller.nyc.gov

**Agency:** New York City Office of the Comptroller (Comptroller Mark Levine)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt). Two properties — **comptroller.nyc.gov** (WordPress: `wp-json`, `wp-sitemap` custom types `report`/`rfp`/`event`/`nyc_bonds`/`job`, 67 `/services/` pages) and **checkbooknyc.com** (Drupal). The **existing Checkbook NYC API** (`POST /api`, XML) was probed live across its `type_of_data` domains. Open Data reconciled via the Socrata Discovery API using the verified agency label `Office of the Comptroller (COMPTROLLER)` — 15 assets.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-comptroller.md](opendata-comptroller.md).

## Headline findings

1. **A public API already exists.** The Comptroller operates **Checkbook NYC** (`POST checkbooknyc.com/api`) covering **Spending, Contracts, Budget, Revenue, and Payroll** — probed live at **3.2M spending / 10.2M payroll / 1.2M revenue** FY2024 records, no key required.
2. **But it isn't unified or agent-native.** It is **XML request/response, POST-only**, with a bespoke `search_criteria`/`response_columns` envelope — **no OpenAPI, no JSON Schema, no MCP**, not resource-oriented, bolted onto a vendor Drupal app.
3. **The data is split across three surfaces.** Checkbook (spending/contracts), **NYC Open Data** (15 assets — pension holdings ×5, claims report, published audits, bonds, debt service), and the **WordPress** site (audits/RFPs/eClaim) — with no shared resource model.
4. **Well-covered data, one missing write surface.** Filing a claim against the City (**eClaim** / `file-a-claim`) is a real citizen transaction with **no API**.

> **Reframe (the "existing-but-not-agent-native API" case):** Parks = *replatform*; DOE = *reclaim*; Council = *consolidate + own three APIs*; **Comptroller = consolidate & own — an XML-era public API plus Socrata plus HTML — behind one JSON-first, resource-oriented, agent-native contract.** The work here is least about liberating data and most about **shape and ownership**: keep Checkbook's pipeline, change its face.

## The fruit

| # | Name | Entity | Where the data lives | Machine-readable? | Open Data twin |
|---|---|---|---|---|---|
| 1 | City Spending (payments) | `SpendingTransaction` | Checkbook API | ✅ Checkbook (XML) | 🟡 Checkbook 2.0 href (`mxwn-eh3b`) |
| 2 | City Contracts | `Contract` | Checkbook API | ✅ Checkbook (XML) | ❌ gap |
| 3 | Budget / Revenue / Payroll | `SpendingTransaction` | Checkbook API | ✅ Checkbook (XML) | ❌ gap |
| 4 | Published Audits | `Audit` | WP `report` + OD | 🟡 partial | ✅ Published Audit List (`nekg-b6tw`) |
| 5 | Claims Against the City (reported) | `ClaimAgainstCity` | claims dashboard | ✅ Open Data | ✅ Claims Report (`ex6k-ym48`) |
| 6 | Pension Fund Holdings | `PensionHolding` | investment pages | ✅ Open Data | ✅ 5 holdings assets (25c each) |
| 7 | Bonds & Debt Service | `Audit`/report | WP `nyc_bonds` + OD | 🟡 partial | ✅ Debt Service (`dfr8-nudu`) + Bond Update |
| 8 | File a Claim (eClaim) | `ClaimFiling` | file-a-claim form | ❌ | ❌ **net-new write** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Checkbook NYC API** (existing, open, XML) — spending/contracts/budget/revenue/payroll; **WordPress REST API** (open) — content; **Socrata SODA** — 15 assets.
- Platforms: **WordPress** (office site) + **Drupal** (Checkbook), both behind **Imperva**; New Relic on Checkbook; FacetWP search on the office site.

## Reverse-engineered entities

`SpendingTransaction` · `Contract` · `Audit` · `ClaimAgainstCity` (reported) · `PensionHolding` (5 systems) · `ClaimFiling` (net-new write) — join keys: **agency**, **vendor**, **fiscalYear**, **contractId**, **borough**.

## Next

1. **JSON Schema** per entity, reconciling Checkbook API fields + Open Data columns (done — see [schemas/](schemas/)).
2. **OpenAPI** consolidating Checkbook + Open Data behind one owned, JSON-first contract (+ the net-new eClaim filing) (done — [openapi/comptroller.yaml](openapi/comptroller.yaml)).
3. **MCP** artifact: `find_spending`, `find_contracts`, `find_audits`, `find_claims`, `find_pension_holdings`, `file_claim` (done — [mcp/comptroller-mcp.json](mcp/comptroller-mcp.json)).
