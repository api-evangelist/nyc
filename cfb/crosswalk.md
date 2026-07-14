# Crosswalk — Website/App Fruit ↔ APIs ↔ NYC Open Data (CFB)

Maps the low-hanging fruit on **nyccfb.info** (the Follow the Money database and C-SMART) to (a) the **existing APIs** (the FTM Web API; Socrata SODA; bulk CSV) and (b) the **16 CFB datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-cfb.json](opendata-cfb.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, every resident transaction locked in an Oracle Siebel CRM → *unlock the service layer.*
- **CFB:** reference data **and a real search API already exist** — but the API is undocumented and unowned, and the one write (filing) is locked in C-SMART → **document the API you already have, and give filing a contract.**

CFB inverts the usual complaint. The problem is not that data is trapped in HTML (it isn't — 16 datasets, 56 CSVs, and a live JSON API) and not that the agency depends on a vendor for its core function (it doesn't — CFB built and runs its own search app on its own domain). The problem is **maturity, not access**: the Follow the Money Web API has no OpenAPI, no docs, no stable public contract, no agent surface — and the transaction the CFB uniquely owns, **submitting a disclosure statement**, has no API at all.

Coverage: ✅ strong open twin · 🟡 partial/status-only · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / App | API today | Open Data | Cov. |
|---|---|---|---|---|
| `Candidate` | `/follow-the-money/candidates` | FTM Web API (typeahead) + SODA | Campaign Financial Analysis (`m3tj-a2pb`, 26c); Public Funds (`u69g-mvrb`) | ✅ |
| `Committee` | `/follow-the-money/registered-political-committees` | FTM Web API (derived) | Derived from `COMMITTEE`/`RECIPID` across `rjkp-yttg` et al. — no standalone dataset | 🟡 derived |
| `Contribution` | Follow the Money search | FTM Web API + SODA + CSV | Campaign Contributions (`rjkp-yttg`, 54c); Intermediaries (`tcwb-nry3`); Doing Business (`fbkk-n4e3`) | ✅ |
| `Expenditure` | Follow the Money search | FTM Web API + SODA + CSV | Campaign Expenditures (`qxzj-vkn2`, 32c) | ✅ |
| `PublicMatchingFundsPayment` | `/program` | SODA + CSV | Campaign Public Funds Payments (`u69g-mvrb`); off-year (`7f4s-uwi7`) | ✅ |
| `DisclosureFiling` (status) | `/follow-the-money/latemissing-disclosure` | SODA | Late/Missing Disclosure Statements (`2ujk-6z7u`, 6c) | 🟡 status only |
| **`DisclosureFiling`** (submit) | **C-SMART / IEDS** | **login UI only** | — | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **FTM Web API** (`FTMSearchWebAPI`) | A real, working JSON API over the core entities; already powers production search | Undocumented, backend-only, no OpenAPI, no stable/public contract, not agent-accessible, no write |
| **Socrata SODA (16 datasets)** | Open, machine-readable, rich (contributions with bundler detail, financial analysis) | Static snapshots split across 16 IDs + citywide/off-year twins; a second uncoordinated copy of the same facts |
| **Data Library (56 CSVs)** | Bulk history back to 2001 | Flat files, per-cycle, no query surface — a third copy |
| **C-SMART / IEDS** | The real filing system for disclosure statements | Login-walled app, no API, no OpenAPI, no JSON; only *filing status* escapes (Late/Missing dataset) |

## Implications for the API-first + MCP proposal

1. **Document and own the FTM Web API.** The lowest-hanging fruit in the whole project: an [OpenAPI](openapi/cfb.yaml) contract, docs, and a stable public surface over the JSON API that already exists — then treat it as a product, not a hidden backend.
2. **Collapse three copies into one resource model.** Present candidates, committees, contributions, expenditures, and public funds once — so consumers stop choosing between 16 Socrata IDs, 56 CSVs, and an undocumented API.
3. **Add the one net-new write workflow** — `file_disclosure` (submit a disclosure statement), authenticated per filer, with amendment support — replacing the C-SMART-only path.
4. **Keep enforcement/audit visible.** Wire Late/Missing filings, penalties, and audit determinations into the disclosure surface so compliance is queryable, not just published.
5. **MCP server** so an agent can answer "which contributions to this candidate were bundled, and by whom?", "how much public match did they receive?", and — the point — "file this disclosure statement."
