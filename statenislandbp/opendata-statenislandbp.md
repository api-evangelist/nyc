# NYC Open Data — Staten Island Borough President Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Staten Island Borough President (BPSI)"** (verified via the Socrata Discovery API, 2026-07-13). **2 assets**, sorted by lifetime page views. Machine-readable: [opendata-statenislandbp.json](opendata-statenislandbp.json).

Note the display **attribution** on both is "Office of the Staten Island Borough President", but the machine-readable agency facet is `Staten Island Borough President (BPSI)` — that is the string to query.

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 839 | dataset | `3fes-huds` | BP Assist Helpline Requests | 4 |
| 752 | file | `mmut-uup9` | Category Master File | 0 |

## The shape of the corpus is the story — there almost isn't one

Two assets, ~1,600 lifetime views between them, and neither describes the office's actual work:

- **`3fes-huds` — BP Assist Helpline Requests.** The only real dataset. It is an **aggregate tally**: three columns of annual complaint *counts* (FY18, FY19, FY20) by a single `Request Type` dimension. It publishes *how many* pothole/litter/graffiti calls came in, never the individual request, and it stops at FY20.
- **`mmut-uup9` — Category Master File.** A "file" asset (a blob, zero columns exposed) — a lookup list, not a queryable dataset.

There is **no dataset** for anything the Borough President is chartered to do: **land-use / ULURP recommendations, community board appointments, discretionary budget awards, or borough board resolutions**. Those live only as PDFs and HTML pages on the Weebly site `statenislandusa.com`, or inside *other* agencies' citywide systems (City Planning ZAP, the adopted budget's Schedule C). See [crosswalk.md](crosswalk.md).

## Groupings

- **Constituent services (aggregate only):** BP Assist Helpline Requests (`3fes-huds`).
- **Reference / lookup:** Category Master File (`mmut-uup9`).
- **Everything else (no Open Data at all):** land use, appointments, budget, resolutions, events — a total gap.
