# NYC Open Data — Manhattan District Attorney Datasets

**Zero.** There is **no** NYC Open Data asset published under a Manhattan District Attorney agency label. Verified via the Socrata Discovery API on 2026-07-13. Machine-readable (empty) index: [opendata-manhattanda.json](opendata-manhattanda.json).

## How this was verified

Queried the Socrata Discovery API (`api.us.socrata.com/api/catalog/v1`) four ways:

| Query | Result |
|---|---|
| `Dataset-Information_Agency = "New York County District Attorney's Office"` | **0 assets** |
| `Dataset-Information_Agency = "Manhattan District Attorney"` | **0 assets** |
| `Dataset-Information_Agency = "Manhattan District Attorney's Office"` | **0 assets** |
| `Dataset-Information_Agency = "New York County District Attorney"` | **0 assets** |

A broad keyword search (`q=district attorney`, `q=prosecution`) returns 146 / 129 assets, but **none** carry a NYC (`data.cityofnewyork.us`) Manhattan-DA agency label — they belong to other jurisdictions (Cook County State's Attorney, Santa Clara County, Austin Police, Hawaii, Connecticut) or to *other* NYC agencies (IBO, OPA payroll, HPD, DOE) that merely mention "district attorney" in content. Filtering `domains=data.cityofnewyork.us` for `district attorney` yields six assets, all owned by IBO / Office of Payroll Administration / HPD / DOE / DCWP / Commission on Women's Issues — **not** the DA.

## Why this is the finding, not a gap in the crawl

Unlike a city *agency*, each of New York's five District Attorneys is an independently elected county prosecutor. They are **not** part of the mayoral NYC Open Data program and publish nothing to `data.cityofnewyork.us`. What data the Manhattan DA does release — caseload figures, conviction and diversion counts — appears only as **prose inside press releases and periodic reports** on manhattanda.org, never as a dataset.

The one thing that *is* machine-readable is unintentional: the site's **WordPress REST API** (`/wp-json/wp/v2/posts`, ~3,029 posts) exposes the newsroom as JSON. That is a content API, not a data program. See [apis-observed.md](apis-observed.md) and [crosswalk.md](crosswalk.md).

## Consequence for the schemas

With no Open Data columns to reconcile, the [schemas/](schemas/) are **design-first** — reverse-engineered from the website's own structure (Our Work bureaus, Victim Resources, offices, the newsroom) and from the shape of the WP REST post. The only source-backed object is `PressRelease` (from the WP REST API); `Prosecution`, `Program`, `VictimService`, `Office`, and the net-new `TipSubmission` are proposed contracts, not reflections of an existing feed.
