# NYC Open Data — BSA Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Board of Standards and Appeals (BSA)"** (verified via the Socrata Discovery API, 2026-07-13). **4 assets**, sorted by lifetime page views. Machine-readable: [opendata-bsa.json](opendata-bsa.json).

The corpus is small but sharp: it is entirely a **case index**. The BSA publishes the *status and disposition* of zoning cases — applications, their granted/denied/withdrawn/dismissed outcome, and a link to each decision PDF — plus a legacy calendar index back to 1916 and a log of pre-application meetings. There is **no dataset for the filing workflow itself** (there is no online application portal — applicants download PDF forms and file on paper), and **no dataset for the hearing calendar**. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 12,717 | dataset | `yvxd-uipr` | Board of Standards and Appeals (BSA) Applications Status | 34 |
| 3,660 | map | `99rv-74dm` | Board of Standards and Appeals (BSA) Decisions Map | 0 |
| 1,495 | dataset | `f72e-3i4c` | Board of Standards and Appeals (BSA) Action Portal | 18 |
| 616 | dataset | `855v-w7mc` | Pre-Application Meetings | 17 |

## Groupings

- **Case / application status (the core):** Applications Status (`yvxd-uipr`, 34c) — every case filed 1998–present with its calendar number, application type (`BZ` variance/special-permit, `BZY` extension of time/vested rights, `SOC` Special Order Calendar amendment, `Appeal`), ZR/GCL section, premise address, block/lot, BBL/BIN, zoning district, project description, **status** (Granted · Withdrawn · Denied · Dismissed), decision date, and a `decisions_url` to the resolution PDF. Decisions Map (`99rv-74dm`) is the geospatial twin.
- **Legacy calendar index:** Action Portal (`f72e-3i4c`, 18c) — the docket keyed on the parsed calendar number (`C1`-`C2`-`C3` = number-year-type, e.g. `6`-`1916`-`S`), with premise address, block/lot, BBL/BIN, and the geography spine. Reaches back to 1916.
- **Pre-application:** Pre-Application Meetings (`855v-w7mc`, 17c) — applicant name, meeting date, application type, address, block/lot, and geography for cases in the pre-filing consultation stage.

## What is NOT here

- **No filing/intake data.** There is no online BSA application portal; applicants download PDF forms (`bz_form.pdf`, `appeal_form.pdf`, `bzy_form.pdf`, `soc_form.pdf`, `lsc_form.pdf`, TAHP forms) and file on paper. The act of *filing* a variance or appeal has no dataset and no API.
- **No structured resolutions.** Each decision is a linked PDF (`/assets/bsa/downloads/pdf/decisions/<calendar>.pdf`), not structured data — the reasoning, conditions, and vote are locked in the document.
- **No hearing calendar.** Upcoming public hearings are published as HTML/PDF on nyc.gov (and Zoom webinar links), not as an Open Data asset.
