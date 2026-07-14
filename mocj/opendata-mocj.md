# NYC Open Data — MOCJ Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Mayor's Office of Criminal Justice (MOCJ)"** (verified via the Socrata Discovery API, 2026-07-13). **1 asset.** Machine-readable: [opendata-mocj.json](opendata-mocj.json).

The shape of the corpus is the story: it is **almost empty**. MOCJ — a policy, convening, and grant-making office — publishes exactly **one** dataset to NYC Open Data, and it has not been updated since June 2023. Everything the office actually produces (jail-population analyses, re-arrest studies, program directories, procurement notices, briefs) lives either as **PDF explainers on its WordPress site** or as **outbound links to other agencies' data** (DOC, NYPD, DCJS, BOC). See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols | Updated |
|--:|---|---|---|--:|---|
| 1,074 | dataset | `atne-2dki` | Supervised Release Dockets | 6 | 2023-06-12 |

## The one dataset

**Supervised Release Dockets** (`atne-2dki`) — "Supervised Release entry data for each court docket that was released into the program." Six columns:

| Column | Type | Description |
|---|---|---|
| `program_entry_date` | date | Date the docket was mandated to Supervised Release by the judge |
| `gender` | text | Gender of the participant |
| `program_name` | text | The organization (CBO) supervising the docket |
| `supervision_level` | text | Supervision level mandated by the judge at release |
| `intake_max_severity` | text | Severity of the top charge on the docket |
| `docket_id` | number | Numeric identifier for a single court case |

This is a **CourtCase-adjacent** grain — one row per released docket — and the only machine-readable trace of any MOCJ program on Open Data.

## Where the rest of MOCJ's "data" actually lives

- **PDF explainers (WordPress `data_reports` / `data_stories` / `reports` / `briefs`):** jail-population increase explainers, justice-system role analyses, open-case and yearly re-arrest studies — narrative + source-data downloads, **not** datasets. (109 `data_reports`, 54 `briefs`, 26 `reports`, 6 `data_stories` counted via the WordPress REST API.)
- **Outbound links to other agencies (System Data page):** NYPD CompStat 2.0, DOC Daily Population in Custody / Monthly Admissions & Discharges / Flash Indicators, NYS DCJS, Board of Correction, DATA2GO, NYC Community Health Profiles. MOCJ **convenes and links; it does not own** the jail-population numbers.

See [tech-stack.md](tech-stack.md) and [apis-observed.md](apis-observed.md).
