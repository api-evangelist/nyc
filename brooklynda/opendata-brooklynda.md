# NYC Open Data — Brooklyn District Attorney Datasets

**Result: ZERO.** No NYC Open Data asset is published under any Kings County / Brooklyn District Attorney agency label. Verified via the Socrata Discovery API on 2026-07-13. Machine-readable (empty): [opendata-brooklynda.json](opendata-brooklynda.json).

## What was checked

Queried `https://api.us.socrata.com/api/catalog/v1` with `--data-urlencode "Dataset-Information_Agency=<LABEL>" --data-urlencode "limit=400"` for every plausible label:

| Agency label tried | `resultSetSize` |
|---|--:|
| `Kings County District Attorney` | 0 |
| `Kings County District Attorney's Office` | 0 |
| `Kings County District Attorney (DA)` | 0 |
| `Brooklyn District Attorney` | 0 |
| `District Attorney` | 0 |

A broad free-text probe (`q=district attorney`, no agency filter) returns 146 assets — but **none is a NYC / Brooklyn DA dataset**. They are budget and KPI datasets from other jurisdictions' Socrata portals (e.g. municipal "District Attorney's Office (2510D)" budget lines, "District Attorney-Appellate Success Rate KPI") and one NYC IBO COVID-spending file. No Brooklyn DA data appears on `data.cityofnewyork.us` under any agency.

## The finding

This is the honest headline: **the Brooklyn DA publishes no open data at all.** Unlike NYCHA (24 datasets) or the Council (three APIs), the office's core justice information — caseloads, arraignments, dispositions, declined prosecutions, diversions, and conviction-review outcomes — exists **nowhere as data**. What little is public lives only as prose inside ~911 WordPress press releases, reachable solely through the site's accidental REST API (`/wp-json/wp/v2`). See [apis-observed.md](apis-observed.md) and [crosswalk.md](crosswalk.md).

Statewide analogs (arrest-to-disposition, criminal court caseloads) are published by the NY Office of Court Administration and the Division of Criminal Justice Services — **not** by the DA office and **not** at the county-prosecutor grain this assessment models in [schemas/case-statistics.json](schemas/case-statistics.json).
