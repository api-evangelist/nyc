# NYC Open Data — DCLA Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Department of Cultural Affairs (DCLA)"** (verified via the Socrata Discovery API, 2026-07-13). 9 assets, sorted by lifetime page views. Machine-readable: [opendata-dcla.json](opendata-dcla.json).

The shape of the corpus is the story: it is **funding-outcome and directory heavy** — who DCLA funded and for how much (programs, capital, Cultural Institutions Group), a geocoded directory of cultural organizations, completed Percent for Art commissions, and Materials for the Arts donation summaries. There is **no dataset for the grant application pipeline** (apply → review → award); the application itself lives only inside the Salesforce DCLA Grants Management System (`dclagms.nyc.gov`). Open Data publishes the *result* of funding, never the *request*. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 14,716 | dataset | `y6fv-k6p7` | DCLA Programs Funding | 3 |
| 10,802 | dataset | `u35m-9t32` | DCLA Cultural Organizations | 16 |
| 3,806 | dataset | `gzdv-qiga` | Completed Percent for Art projects with artist information | 7 |
| 3,245 | dataset | `7hgn-sgmk` | DCLA Cultural Organizations Capital Funding | 6 |
| 3,148 | dataset | `ka27-qx5k` | DCLA Cultural Institutions Group Funding | 4 |
| 2,129 | dataset | `rb2h-bgai` | DCLA Cultural Organization Resources | 4 |
| 1,813 | dataset | `rskq-5bfv` | DCLA Program Funding for FY11 | 3 |
| 1,426 | dataset | `j8p3-8ufc` | DCLA: Programs Funding for FY2010 | 3 |
| 1,244 | dataset | `vhtt-kpwy` | DCLA Materials For The Arts - Donor Information | 6 |

## Groupings

- **Cultural organizations (directory):** DCLA Cultural Organizations (`u35m-9t32`, 16c — the geocoded directory, with discipline, address, and full geography spine) + DCLA Cultural Organization Resources (`rb2h-bgai` — website/description/area).
- **Program grant awards:** DCLA Programs Funding (`y6fv-k6p7`, current), DCLA Program Funding for FY11 (`rskq-5bfv`), DCLA: Programs Funding for FY2010 (`j8p3-8ufc`) — all keyed on Application # + Organization + Total Final Award.
- **Capital funding:** DCLA Cultural Organizations Capital Funding (`7hgn-sgmk` — DCLA / City Council / Borough President dollars by organization and fiscal year).
- **Cultural Institutions Group (CIG):** DCLA Cultural Institutions Group Funding (`ka27-qx5k` — operating and energy support for the ~34 City-owned institutions).
- **Public art:** Completed Percent for Art projects with artist information (`gzdv-qiga` — artist, sponsor/design agency, address, borough).
- **Materials for the Arts:** DCLA Materials For The Arts - Donor Information (`vhtt-kpwy` — aggregate donations by year and category; no individual donor exposed).

## What is missing

There is **no dataset** for: an individual grant **application** (only the award outcome is published), the panel-review process, or per-donor Materials for the Arts detail. The core transaction — a cultural organization applying to the Cultural Development Fund — is not on Open Data at all; it lives only in the Salesforce Grants Management System. See [apis-observed.md](apis-observed.md).
