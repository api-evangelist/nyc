# NYC Open Data — Brooklyn Borough President Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Brooklyn Borough President (BPBK)"** (verified via the Socrata Discovery API, 2026-07-13). **21 assets**, sorted by lifetime page views. Machine-readable: [opendata-brooklynbp.json](opendata-brooklynbp.json).

This corrects the assessment brief's guess of *zero* Socrata datasets: the office actually publishes a real, if uneven, open-data corpus. The shape of the corpus is the story — it is **land-use, appointments, and awards heavy**: one ULURP recommendations table, a community-board contact list, a dozen "BP Appointments" tables (one per board family), and capital/discretionary/tourism award tables. Many are **thin** (3-6 columns) and several are **stale snapshots** (Cornerstone Awards 2015-2017, Discretionary Contract Awards 2017-2018). There is **no dataset for the constituent write layer** (applying to a board, requesting a meeting is only a form dump). See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 6,054 | dataset | `avcv-kcyf` | Topographical Bureau Maps - Final Sections | 5 |
| 4,336 | dataset | `dy27-rrad` | Community Board Contact List | 16 |
| 2,275 | dataset | `4j6i-9rmr` | Uniform Land Use Review Procedure (ULURP) Recommendations | 6 |
| 1,918 | dataset | `rma9-fm39` | Tourism Grants | 19 |
| 1,322 | dataset | `n6ej-pebd` | Capital Awards | 5 |
| 996 | dataset | `q7f5-jwds` | BP Appointments - Brooklyn Public Library (BPL) Board | 7 |
| 955 | dataset | `tsb8-3rct` | Discretionary Contract Awards | 4 |
| 886 | dataset | `95u9-kyyu` | BP Appointments - DYCD Neighborhood Advisory Board (NABS) | 7 |
| 862 | dataset | `y6ds-67d5` | Brooklyn Borough President Office Requests for Assistance | 4 |
| 855 | dataset | `ubuy-v2nw` | Discretionary Contract Awards 2017-2018 | 3 |
| 846 | dataset | `gqzy-vhwd` | Brooklyn Borough President Meeting Requests | 5 |
| 780 | dataset | `e6ph-9uv7` | Brooklyn Borough President's Office Legislation - Passed | 4 |
| 777 | dataset | `mju7-rqph` | Heroes of the Month | 3 |
| 701 | dataset | `5mxw-kxpt` | BP Appointments - Community Education Councils (CECs) | 8 |
| 658 | dataset | `avh4-h5hx` | BP Appointments - HHC Community Advisory Boards (CAB) | 8 |
| 647 | dataset | `pvxf-9irb` | BP Appointments - BIDS | 23 |
| 594 | dataset | `ajh7-4wqg` | Cornerstone Award 2017 | 9 |
| 581 | dataset | `rbwa-m4iy` | BP Appointments - Solid Waste Advisory (SWAB) | 5 |
| 555 | dataset | `jipi-drdu` | Cornerstone Award 2015 | 13 |
| 521 | dataset | `efdc-dxuz` | BP Appointments - Miscellaneous Boards | 4 |
| 488 | dataset | `sydm-hizh` | Cornerstone Award 2016 | 9 |

## Groupings

- **Land use (statutory power):** Uniform Land Use Review Procedure (ULURP) Recommendations (`4j6i-9rmr`, 6c).
- **Community boards:** Community Board Contact List (`dy27-rrad`, 16c).
- **BP Appointments (one table per board family):** BIDS (`pvxf-9irb`, 23c — the richest), Community Education Councils (`5mxw-kxpt`), HHC Community Advisory Boards (`avh4-h5hx`), Brooklyn Public Library Board (`q7f5-jwds`), DYCD Neighborhood Advisory Boards (`95u9-kyyu`), Solid Waste Advisory Board (`rbwa-m4iy`), Miscellaneous Boards (`efdc-dxuz`).
- **Funding awards:** Capital Awards (`n6ej-pebd`), Discretionary Contract Awards (`tsb8-3rct`) + 2017-2018 (`ubuy-v2nw`), Tourism Grants (`rma9-fm39`, 19c — full geography spine).
- **Publications:** Office Legislation - Passed (`e6ph-9uv7`).
- **Recognition / awards:** Heroes of the Month (`mju7-rqph`), Cornerstone Award 2015 / 2016 / 2017 (`jipi-drdu`, `sydm-hizh`, `ajh7-4wqg`).
- **Constituent request logs (form dumps, not a service API):** Meeting Requests (`gqzy-vhwd`), Office Requests for Assistance (`y6ds-67d5`).
- **Other:** Topographical Bureau Maps - Final Sections (`avcv-kcyf`).

