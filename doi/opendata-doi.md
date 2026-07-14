# NYC Open Data — DOI Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Department of Investigation (DOI)"** (verified via the Socrata Discovery API, 2026-07-13). 4 assets, sorted by lifetime page views. Machine-readable: [opendata-doi.json](opendata-doi.json).

The shape of the corpus is the story: it is **City Marshal oversight heavy** — executed evictions and marshal revenue for the officials DOI appoints and regulates — plus the Policy & Procedure Recommendations tracker and monthly performance indicators. There is **no dataset for DOI's investigations**: the public reports live only as PDFs (`/assets/doi/reports/pdf/`), and the corruption-complaint intake lives only in the third-party Kaseware portal. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 236,945 | dataset | `6z8x-wfk4` | Evictions | 20 |
| 5,731 | dataset | `7ewi-9cdf` | City Marshals Revenue | 5 |
| 2,931 | dataset | `jstn-jaut` | Policy and Procedure Recommendations (PPR) Portal | 7 |
| 1,819 | dataset | `i8ua-bnkj` | Monthly Performance Management Reports (Corruption Lectures & Customer Service indicators) | 3 |

## Groupings

- **City Marshal oversight:** Evictions (`6z8x-wfk4`, 20c — DOI's most-viewed asset by far, with a full NYC geography spine), City Marshals Revenue (`7ewi-9cdf`, 5c). DOI appoints and regulates the City Marshals; these are the enforcement and financial records of that oversight.
- **Investigative output (structured):** Policy and Procedure Recommendations (PPR) Portal (`jstn-jaut`, 7c) — recommendations DOI issues to agencies, with acceptance, agency-reported, and implementation status. The one structured twin of DOI's own casework.
- **Operations:** Monthly Performance Management Reports (`i8ua-bnkj`, 3c) — indicators reported to the Mayor's Office of Operations, including corruption-lecture counts and customer-service measures.

## What is NOT here (the finding)

- **No investigation reports.** DOI's public reports — its core work product — are PDFs, not data. No `PublicReport` dataset exists.
- **No complaints.** The corruption-complaint intake (`app.kaseware.us`) is a third-party vendor form; nothing about tips or cases reaches Open Data.
