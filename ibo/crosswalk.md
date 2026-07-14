# Crosswalk — Website/Content Fruit ↔ APIs ↔ NYC Open Data (IBO)

Maps the low-hanging fruit on **www.ibo.nyc.gov** to (a) the **existing APIs** (the NYC.gov Content API v2; Socrata SODA) and (b) the **20 IBO datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-ibo.json](opendata-ibo.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, every resident transaction locked in a vendor CRM → *unlock the service layer.*
- **IBO:** the content API and the datasets **already exist** — but undocumented, unversioned, Excel-shaped, and not agent-native → **formalize.**

IBO inverts the usual problem twice over. The publications are *not* trapped in HTML — they already flow as JSON from the NYC.gov Content API. The fiscal data is *not* missing — it is 20 open Socrata datasets. What is missing is a **contract**: documentation, versioning, a clean long-form model, and a way for an agent to ask a question. And unlike operational agencies, IBO has almost nothing to *write* — its one citizen transaction is **Ask IBO**, a form/email with no API.

Coverage: ✅ machine-readable & modelable · 🟡 machine-readable but awkward (wide/undocumented) · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Content | API today | Open Data | Cov. |
|---|---|---|---|---|
| `Publication` | `/content/publications` | **Content API v2 (undocumented)** | — | 🟡 undocumented |
| `FiscalDataTable` | data catalog | SODA | All 20 IBO datasets | ✅ |
| `FiscalSeries` (revenue/spending/capital/debt/positions) | budget resources | SODA | Revenue & Spending (`7zhs-43jt`), Capital (`hukm-snmq`), Debt (`5i9t-mvdt`/`6ggx-itps`), Agency Exp. (`cwjy-rrh3`), Positions (`uaj7-9szf`), Non-Tax (`ypbd-r4kg`), Categorical Aid (`fu34-wamz`) | 🟡 wide/pivoted |
| `SchoolSpending` | Education Indicators interactive | SODA | School Spending Since 1990 (`p26e-k6k9`, 29c); Public School Indicators (`29nk-6u2k`) | 🟡 wide/pivoted |
| `TaxDistribution` | — | SODA | Personal Income (`ipc3-2nbm`), Income by Type (`gffu-ps8j`), Tax Liability (`3vvi-fwjs`), Tax Credits (`nwet-nc6h`), Tax Revenue (`hdnu-nbrh`) | ✅ |
| COVID / stimulus trackers | — | SODA | ARPA Tracker (`sg72-pis5`), COVID Spending (`ke6f-vhnd`, `khqt-g67n`, `duk5-k5fk`) | ✅ |
| **`DataRequest`** (Ask IBO) | `/content/ask-ibo` | **form / email only** | — | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Content API v2** (`apps.nyc.gov`) | Already returns ~1,145 publications as structured JSON with topic/type/fiscal-year facets | Undocumented, unversioned, no OpenAPI, not offered as a consumer API; a page-rendering backend |
| **Socrata SODA (20 datasets)** | Open, machine-readable; strong on tax/income distribution and stimulus trackers | Tables are **wide** (one column per fiscal year); reshaping required; historical, updated "Annually" / "As needed" |
| **Ask IBO** | IBO's one interactive citizen input | Web form / email to `info@ibo.nyc.gov`; no API, no status, no Open Data twin |

## Implications for the API-first + MCP proposal

1. **Publish a contract over the content API.** Present publications as one clean, filterable resource ([OpenAPI](openapi/ibo.yaml) `GET /publications`) by topic, publication type, and fiscal year — a documented surface over the JSON `apps.nyc.gov` already returns.
2. **Pivot the wide tables to long-form.** Republish the fiscal series as `(series, lineItem, fiscalYear, value)` observations (`GET /fiscal-series`), plus a table catalog (`GET /data-tables`), so consumers stop parsing 42-column spreadsheets.
3. **Model the distributional and education data cleanly** — `TaxDistribution` by AGI band, `SchoolSpending` by category/year.
4. **Add the one net-new write** — `POST /data-requests` (Ask IBO), replacing the form/email so a resident, journalist, or Council staffer (or their agent) can submit a fiscal question and track its status.
5. **MCP server** so an agent can answer "what did IBO say about the FY2025 budget?", "capital expenditures by purpose since FY2010?", and — the point — "ask IBO how much the city spends per pupil."
