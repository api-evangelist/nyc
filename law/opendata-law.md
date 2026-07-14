# NYC Open Data — Law Department Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Law Department (LAW)"** (verified via the Socrata Discovery API, 2026-07-13). **7 assets**, sorted by lifetime page views. Machine-readable: [opendata-law.json](opendata-law.json).

The shape of the corpus is the story: it is **thin, administrative, and stale** — a civil-litigation case index, a two-column list of divisions, three parallel publication feeds (press releases / speeches / columns), M/WBE contracting statistics, and a single-column pro bono firm list. Every dataset is flagged **'No' automation** and **'Annually'** updated. There is **no dataset for a service or transaction** — because this is an agency-facing legal office, not a citizen-service agency. And the ledger of **claims filed and settlement dollars** is published **not by Law but by the Office of the Comptroller** (`ex6k-ym48`). See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 7,475 | dataset | `svyi-maaj` | Minority and Women-Owned Business Enterprise Statistics | 7 |
| 5,486 | dataset | `pjgc-h7uv` | Case-Related Information About Civil Litigation | 17 |
| 2,228 | dataset | `4se9-mk53` | LAW Divisions | 2 |
| 1,568 | dataset | `yk6f-pa7p` | LAW Public Service Program | 1 |
| 1,509 | dataset | `kewa-q4dq` | LAW Press Releases | 3 |
| 1,222 | dataset | `g7ir-4pf8` | LAW Speeches | 4 |
| 1,098 | dataset | `d84z-5kap` | LAW Published Columns | 3 |

## Groupings

- **Litigation:** Case-Related Information About Civil Litigation (`pjgc-h7uv`, 17c) — the Law Department's own case index (matter, docket, court, judge, division, disposition, dates, Lead BBL, payout/received/expense totals). NOT the claims ledger.
- **Organization:** LAW Divisions (`4se9-mk53`, 2c) — division + parent department.
- **Publications:** LAW Press Releases (`kewa-q4dq`), LAW Speeches (`g7ir-4pf8`), LAW Published Columns (`d84z-5kap`) — three parallel title/date/PDF feeds, unified into one `Publication` resource.
- **Contracting / equity:** M/WBE Statistics (`svyi-maaj`, 7c) — participation shares by category; LAW Public Service Program (`yk6f-pa7p`, 1c) — pro bono firms since 2007.

## Not published by the Law Department (published by the Comptroller)

- **Claims Report — Underlying Settlements and Claims Filed** (`ex6k-ym48`, agency: **Office of the Comptroller**). This is the dataset most users expect from the City's litigation function; it is documented here so consumers are routed to the right agency. See [apis-observed.md](apis-observed.md).
