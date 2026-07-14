# NYC Open Data — CCHR Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Commission on Human Rights (CCHR)"** (verified via the Socrata Discovery API, 2026-07-13). Just **3 assets**, sorted by lifetime page views. Machine-readable: [opendata-cchr.json](opendata-cchr.json).

The shape of the corpus is the story: it is **thin and aggregate-only**. There are three small operational-metrics tables — inquiries received, mediation cases closed, and pre-complaint resolutions — and nothing else. There is **no dataset for the law**, no protected-class list, no legal-guidance catalog, no training/outreach calendar, and — by design — **no individual complaint or case data**. Everything a person actually interacts with (the Report Discrimination form, the Human Rights Law, legal guidance) lives only as HTML/PDF on nyc.gov/site/cchr. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 1,933 | dataset | `395v-hkhg` | Inquiries Received | 9 |
| 1,145 | dataset | `tmha-56pf` | Office of Mediation and Conflict Resolution Cases | 3 |
| 786 | dataset | `6ayi-8khd` | Pre-Complaint Resolutions | 3 |

## Groupings

- **Inquiries (annual, by protected area):** Inquiries Received (`395v-hkhg`, 9c) — number of inquiries to the Commission about discrimination and alleged Human Rights Law violations for the previously completed fiscal year, broken out by Employment, Housing, Public Accommodations, Lending Practices, Discriminatory Harassment, and Bias-Based Profiling, with a Grand Total.
- **Resolutions (monthly counts):** Office of Mediation and Conflict Resolution Cases (`tmha-56pf`, 3c) — monthly settlements negotiated to completion; Pre-Complaint Resolutions (`6ayi-8khd`, 3c) — monthly pre-complaint resolutions. Two parallel monthly-count tables.

## What is NOT here

- **No complaints or cases.** CCHR never publishes individual complaint, respondent, or case-outcome data to Open Data (privacy by design). Not even de-identified case-level records.
- **No law as data.** The NYC Human Rights Law, its protected classes, and CCHR's legal enforcement guidance exist only as prose and PDF on nyc.gov/site/cchr.
- **No intake as data.** The Report Discrimination form and its submissions have no dataset and no API.
- **No outreach as data.** Trainings, workshops, and the Stop Sexual Harassment Act training are HTML pages, not a dataset.
