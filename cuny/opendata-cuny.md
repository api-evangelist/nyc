# NYC Open Data — CUNY Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "City University of New York (CUNY)"** (verified via the Socrata Discovery API, 2026-07-13). The result is the story: **the CUNY agency label returns exactly one asset — and it is not even a dataset**, it is an external-link (`href`) BigApps entry. A `q=CUNY` search across NYC Open Data surfaces only ~13 loosely-matching results, of which just one (`wusu-mzmq`, a city budget rollup tagged to OMB) is genuinely CUNY-subject. Machine-readable: [opendata-cuny.json](opendata-cuny.json).

| Views | Type | ID | Name | Cols | Agency label |
|--:|---|---|---|--:|---|
| 3,114 | href | `vijr-8gr7` | Community Connect: Bronx Information Portal | 0 | **City University of New York (CUNY)** |
| 2,001 | dataset | `wusu-mzmq` | CUNY Community College Expenditures By Source | 5 | Mayor's Office of Management & Budget (OMB) |

## Why the corpus is empty

CUNY is a **New York State public benefit corporation**, not a New York City agency. Unlike NYCHA, DOE, or the Council, it is **not a publisher on NYC Open Data** — so its reference and institutional data does not appear under a CUNY agency label at all. That data lives in three other places:

- **cuny.edu / OIRA** — the CUNY [Office of Institutional Research and Assessment](https://www.cuny.edu/about/administration/offices/oira/) publishes enrollment, degrees, and demographic **data books as PDF/Excel**, not as an API.
- **CUNYfirst** — the transactional system of record (Oracle PeopleSoft Campus Solutions): applications, courses, enrollment, financial aid. No public API.
- **data.ny.gov** — state-level SUNY/CUNY enrollment tables live on the New York **State** open data portal, not the city's.

## Implication

There is **no NYC Open Data twin** for any CUNY entity — campuses, degree programs, courses, enrollment, faculty/research, or applications. Every object in this assessment is reverse-engineered from HTML on cuny.edu and the CUNYfirst PeopleSoft screens, not from a Socrata dataset. See [crosswalk.md](crosswalk.md).
