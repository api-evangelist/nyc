# Crosswalk — Website/API Fruit ↔ APIs ↔ NYC Open Data (Comptroller)

Maps the low-hanging fruit on **comptroller.nyc.gov** + **checkbooknyc.com** to (a) the **existing Checkbook NYC API**, (b) the **WordPress REST API**, and (c) the **15 Comptroller datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-comptroller.json](opendata-comptroller.json).

## The reframe — the "existing-but-not-agent-native API" pattern

- **Parks:** data-rich HTML, machine-readable twins on Open Data, legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** three APIs (vendor Legistar, WP REST, SODA), none owned/coherent → *consolidate + own.*
- **Comptroller:** a **real public API already exists** — Checkbook NYC (spending/contracts/budget/revenue/payroll) — but it is **XML-first, vendor-hosted, and disconnected** from the office's Open Data (pension, claims, audits, bonds) and its eClaim workflow → **consolidate & own** (JSON-first, resource-oriented, agent-native).

Comptroller is the clearest "a partial/older API exists but isn't unified or agent-native" case in the project. A resident or agent asking "how much did the City pay vendor X, and were there claims against that agency?" must today speak XML to Checkbook, query Socrata for claims, and read HTML for audits.

Coverage: ✅ strong twin/API · 🟡 partial · ❌ gap.

## Entity crosswalk

| Entity | Where it lives | Checkbook API | Open Data | Cov. |
|---|---|---|---|---|
| `SpendingTransaction` | Checkbook | **Spending** domain (3.2M FY24) | Checkbook NYC 2.0 (`mxwn-eh3b`, href) | ✅ (API; XML) |
| `Contract` | Checkbook + contract-registration | **Contracts** domain | — (late-contracts dashboard on site) | ✅ (API; XML) |
| Budget / Revenue / Payroll | Checkbook | **Budget/Revenue/Payroll** domains | — | 🟡 API-only (XML) |
| `Audit` | site `report` posts | — | Published Audit List (`nekg-b6tw`, 6c) | ✅ |
| `ClaimAgainstCity` | claims dashboard | — | Claims Report (`ex6k-ym48`, 10c) | ✅ (report only) |
| `PensionHolding` | investment pages | — | 5 holdings assets (NYCERS/TRS/BERS/Police/Fire, 25c each) | ✅ |
| Proxy voting | boardroom-accountability | — | Proxy Voting Records (`fpxc-zjtm`, 16c) | ✅ |
| Bonds / debt service | `nyc_bonds` posts | — | GO Debt Service (`dfr8-nudu`), Bond Update (`d334-62hi`) | ✅ |
| Asset allocation | investment pages | — | Five-System Asset Allocation (`rh3d-kgz3`, 9c) | ✅ |
| `ClaimFiling` | **eClaim** file-a-claim form | — | — | ❌ **net-new write** |

## The existing-API problem, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Checkbook NYC API** | Real, open, high-volume (spending/contracts/budget/revenue/payroll); no key | XML request/response envelope, POST-only; no OpenAPI/JSON Schema/MCP; vendor Drupal app; not an owned/branded API contract; no agent surface |
| **WordPress REST API** | Open; audits/RFPs/events/bonds as content | CMS content, not financial resources; no spending/contract/claim objects |
| **Open Data (SODA)** | Open; pension holdings, claims report, audits, bonds, debt service | Flattened periodic snapshots; disconnected from the live Checkbook record and from eClaim; top "asset" is just an href to Checkbook |

## Implications for the API-first + MCP proposal

1. **Own the contract; return JSON.** Publish one Comptroller API (this project's [OpenAPI](openapi/comptroller.yaml)) that fronts Checkbook for spending/contracts, Open Data for audits/claims/pension holdings — presenting one resource model in JSON, not an XML envelope plus Socrata plus HTML.
2. **Make claims first-class both ways** — the reported `ClaimAgainstCity` (read) *and* the net-new `ClaimFiling` (write) via eClaim.
3. **Keep the pipeline, change the shape.** Checkbook's data pipeline is fine; the modernization is a resource-oriented, agent-native façade over it.
4. **MCP server** so an agent can answer "what did the City pay vendor X / which contracts did agency Y register late / what claims were paid in my borough?" — and *file a claim* — in one place.
