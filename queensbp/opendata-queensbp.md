# NYC Open Data — Queens Borough President Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Queens Borough President (QBP)"** (verified via the Socrata Discovery API, 2026-07-13). **2 assets**, sorted by lifetime page views. Machine-readable: [opendata-queensbp.json](opendata-queensbp.json).

The shape of the corpus is the story: it is **entirely about community boards** — one roster of members and one directory of district managers and chairs. There is **no dataset for any other borough-president function** — not land use / ULURP recommendations, not discretionary funding, not events, not applications. The hinted "likely zero Socrata datasets" was close: QBP publishes just these two, both under the community-board umbrella. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 1,479 | dataset | `rps4-dwwk` | Queens Community Board Members | 4 |
| 1,430 | dataset | `8z5h-tzdr` | Queens Community Board District Managers and Chairs | 20 |

## Groupings

- **Community board membership:** Queens Community Board Members (`rps4-dwwk`, 4c — First/Last Name, Board, Year Appointed).
- **Community board offices:** Queens Community Board District Managers and Chairs (`8z5h-tzdr`, 20c — district manager, chair, e-mail, phone, monthly meeting, address, plus the full NYC geography spine: BBL, BIN, council district, census tract, NTA, borough, postcode, lat/long).

## What's missing

Everything else the Borough President does. There is no Open Data twin for:

- **Land-use / ULURP recommendations** — the office's advisory positions on zoning and variances.
- **Discretionary funding awards** — tens of millions a year in capital and expense grants to nonprofits, schools, and cultural institutions.
- **Events** — land-use hearings, borough board/cabinet meetings, expos, webinars.
- **Press releases / reports** — authored as Divi Pages; the WordPress REST API that could serve them returns 0.
- **Community board applications** — the flagship participatory act, an HTML/PDF form.

That absence, plus the community-board-only footprint being near-identical across boroughs, is the argument for **one standardized Borough President API**.
