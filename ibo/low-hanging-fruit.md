# Low-Hanging Fruit Index — IBO

**Agency:** New York City Independent Budget Office (IBO)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, robots-respecting). IBO's legacy own domain `ibo.nyc.ny.us` **301-redirects** to `www.ibo.nyc.gov`, a client-side SPA on the NYC.gov **"Content API v2"** chassis (Akamai edge, nginx origin, Dynatrace/ruxit RUM, WebTrends analytics). Every route returns the same 36 KB shell; content is loaded by jQuery from an undocumented JSON API at `apps.nyc.gov/content-api/v2` (confirmed ~**1,145** publications). Verified the NYC Open Data agency label `NYC Independent Budget Office (IBO)` via the Socrata Discovery API and pulled all **20** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-ibo.md](opendata-ibo.md).

## Headline findings

1. **IBO gave up its own domain.** The legacy `ibo.nyc.ny.us` now 301-redirects to `www.ibo.nyc.gov` — the "Independent" Budget Office moved its public identity onto the shared NYC.gov chassis.
2. **The site is a SPA on the NYC.gov "Content API v2" platform.** Every path returns the same shell; content is fetched by jQuery from a real but **undocumented** JSON API at `apps.nyc.gov/content-api/v2`. A third distinct NYC.gov platform after NYCHA's Livesite.
3. **IBO's product is analysis, already flowing as JSON.** ~**1,145** publications (reports, testimony, letters, budget options, explainers, interactives) come back from the content API with structured metadata — but with no documented, versioned, agent-native contract.
4. **The 20 Open Data datasets are wide and pivoted** — one column per fiscal year (`FY 1980` … `FY 2020`). Excel-on-Socrata; a modern API would pivot to long-form.
5. **No citizen transaction.** As a reference agency, IBO has no payments, permits, or applications. Its single interactive input is **Ask IBO** — a data/analysis request, today a form/email to `info@ibo.nyc.gov` with no API. That is the net-new **write** surface.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a CRM-locked service layer; **IBO = formalize.** Here the API and the data already exist — the work is least about liberating anything and most about giving an existing but undocumented content API, a set of Excel-shaped fiscal tables, and a form-only "Ask IBO" one owned, documented, agent-native contract.

## The fruit

| # | Name | Entity | Where the data lives | Open Data / API twin |
|---|---|---|---|---|
| 1 | IBO Publications | `Publication` | Content API v2 | 🟡 undocumented content API (~1,145) |
| 2 | Fiscal data tables (catalog) | `FiscalDataTable` | SODA | ✅ all 20 IBO datasets |
| 3 | Revenue/spending, capital, debt, positions | `FiscalSeries` | SODA (×8, wide) | 🟡 `7zhs-43jt`, `hukm-snmq`, `5i9t-mvdt`, `cwjy-rrh3`, … |
| 4 | School spending & education indicators | `SchoolSpending` | SODA + interactive | 🟡 `p26e-k6k9` (29c), `29nk-6u2k` |
| 5 | Tax & income distribution by AGI | `TaxDistribution` | SODA | ✅ `ipc3-2nbm`, `gffu-ps8j`, `3vvi-fwjs`, `nwet-nc6h`, `hdnu-nbrh` |
| 6 | COVID / stimulus spending trackers | `FiscalDataTable` | SODA | ✅ `sg72-pis5`, `ke6f-vhnd`, … |
| 7 | Budget 101 / NYC Budget Resources | `Publication` | Content API v2 | 🟡 undocumented content API |
| 8 | **Ask IBO (submit a data request)** | `DataRequest` | Web form / email | ❌ **net-new** (no API) |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **NYC.gov Content API v2** — `apps.nyc.gov/content-api/v2` (undocumented JSON; the ~1,145 publications).
- **Socrata SODA** — 20 IBO datasets (fiscal time-series; mostly wide).
- Platform: **NYC.gov "Content API v2"** SPA (Akamai edge, nginx origin, Dynatrace RUM, WebTrends) + jQuery 3.3.1 / Bootstrap 4.3.1 — the fifth distinct platform after Parks' Smarty/PHP, DOE's Sitefinity/.NET, Council's WordPress, and NYCHA's Livesite/Siebel.
- Vendors: **ArcGIS Online** (`ibomap.maps.arcgis.com`), **Airtable**, **Infogram** (data-viz embeds); **Google Custom Search** (on-site search).

## Reverse-engineered entities

`Publication` (Content API v2) · `FiscalDataTable` (the 20 Socrata tables as a catalog) · `FiscalSeries` (wide tables pivoted long: revenue/spending, capital, debt, positions) · `SchoolSpending` · `TaxDistribution` (by AGI band) · `DataRequest` (net-new Ask IBO write) — organizing spine: **fiscal year**, **series/line-item**, **publication type + topic**, **AGI range**.

## Next

1. **JSON Schema** per entity, reconciling the real content-API fields and Socrata column names (wide FY columns, AGI ranges, dollars-in-millions) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the content API + pivoted fiscal data as clean resources + the net-new `POST /data-requests` (Ask IBO) — done ([openapi/ibo.yaml](openapi/ibo.yaml)).
3. **MCP** artifact: `find_publications`, `get_publication`, `find_data_tables`, `find_fiscal_series`, `find_school_spending`, `find_tax_distribution`, `ask_ibo` — done ([mcp/ibo-mcp.json](mcp/ibo-mcp.json)).
