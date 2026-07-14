# NYC Open Data — Bronx District Attorney Datasets

All NYC Open Data assets whose **Dataset-Information_Agency** matches the Office of the Bronx District Attorney (queried via the Socrata Discovery API, 2026-07-13). Machine-readable: [opendata-bronxda.json](opendata-bronxda.json).

## Result: zero datasets

**There are no NYC Open Data datasets published by the Bronx District Attorney.** The Socrata Discovery API returns **0** results for every plausible agency label:

| Agency label queried | Datasets |
|---|--:|
| `Bronx District Attorney` | 0 |
| `Office of the Bronx District Attorney` | 0 |
| `Bronx County District Attorney` | 0 |
| `District Attorney` | 0 |
| `Bronx DA` | 0 |

A broad free-text search of the citywide catalog for "district attorney" surfaces only KPI/budget rollups belonging to *other* jurisdictions' Socrata domains (2510-series line items, "Project ORCA," etc.) and NYC IBO budget lines — **none** is a data.cityofnewyork.us asset owned by any of the five NYC borough District Attorneys.

This is not an oversight in the crawl; it is the finding. Prosecution in New York State is a **county-level** function that sits outside the executive-branch agencies which populate NYC Open Data, so the DA offices publish **nothing** to the citywide catalog.

## Where the data actually lives

The Bronx DA does publish aggregate prosecution figures — but not as data. They are embedded as **Microsoft Power BI (Gov) dashboards** (`app.powerbigov.us/view?...`, report "Public Dash Case v9a") on the office's own `/html/data/` pages:

- **Case Decision Points / Case Outcomes** — `dashboard-prosecutor-charging-decisions`
- **Arrests** — `dashboard-arrests`
- **Defendant Demographics** — `dashboard-defendant-demographics`
- **Data & Legal Glossary** — `dashboard-glossary`
- **Data, Facts & Insights** / **Data Stories** — narrative pages

None of these exposes a download, a query endpoint, or an Open Data twin. The numbers are rendered pixels inside a vendor BI iframe. See [crosswalk.md](crosswalk.md) and [apis-observed.md](apis-observed.md).

## Implication

Because there is **no** open data and **no** API, every entity in this assessment is reverse-engineered from the public HTML site and the Power BI dashboards, not from a machine-readable source. The modernization opportunity is therefore not "publish more datasets" but "**stand up the first data + API layer at all**" — and, because all five borough DA offices run the same functions, to do it once as a **shared District Attorney API** rather than a bespoke Bronx build.
