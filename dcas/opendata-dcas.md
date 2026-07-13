# NYC Open Data — DCAS Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Department of Citywide Administrative Services (DCAS)"** (verified via the Socrata Discovery API, 2026-07-13). 32 assets, sorted by lifetime page views. Machine-readable: [opendata-dcas.json](opendata-dcas.json).

The shape of the corpus is the story: it is **civil-service heavy** — the Civil Service List (Active) alone has 3.5M lifetime views, and the top five assets are all workforce data (eligible lists, titles, job postings) — plus procurement notices (City Record Online, Greenbook, solicitations), DCAS-managed **buildings and their energy**, and the municipal **fleet**. There is **no dataset for the citizen transaction layer** (registering for an exam, applying to a job, buying from the CityStore); those live only in the aNNN application layer — OASys / the City Jobs portal (`cityjobs.nyc.gov`), Employee Self-Service (`a127-ess.nyc.gov`, PeopleSoft/NYCAPS), and the Shopify CityStore. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 3,503,510 | dataset | `vx8i-nprf` | Civil Service List (Active) | 20 |
| 1,057,430 | dataset | `a9md-ynri` | Civil Service List Certification | 21 |
| 254,442 | dataset | `dg92-zbpx` | City Record Online | 37 |
| 248,323 | dataset | `nzjr-3966` | NYC Civil Service Titles | 11 |
| 156,789 | dataset | `kpav-sd4t` | Jobs NYC Postings | 30 |
| 117,186 | dataset | `ye3c-m4ga` | Civil List | 7 |
| 110,691 | filter | `qyyg-4tf5` | Recent Contract Awards | 37 |
| 62,953 | dataset | `mdcw-n682` | Greenbook | 23 |
| 41,543 | dataset | `4e2n-s75z` | Suitability of City-Owned and Leased Property for Urban Agriculture (LL 48 of 2011) | 75 |
| 39,470 | filter | `3khw-qi8f` | Current Solicitations | 37 |
| 34,551 | dataset | `qu8g-sxqf` | Civil Service List (Terminated) | 21 |
| 19,473 | dataset | `ynic-uz5i` | Vehicle Auction List | 5 |
| 19,014 | dataset | `vvj6-d5qx` | NYC Municipal Building Energy Benchmarking Results | 20 |
| 17,156 | dataset | `rfu7-paqe` | Deed Restriction Database | 25 |
| 13,582 | dataset | `ww83-bcks` | M/WBE Upcoming Procurements | 5 |
| 10,926 | dataset | `4ptz-hmtc` | Annual Examination Schedule of Each Fiscal Year | 7 |
| 9,238 | dataset | `fc53-9hrv` | NYC EV Fleet Station Network | 18 |
| 6,629 | dataset | `ubdi-jgw2` | DCAS Managed Building Energy Usage | 17 |
| 6,429 | dataset | `xx2p-4jnq` | DCAS Managed Public Buildings | 22 |
| 5,675 | dataset | `hpid-63r5` | NYC Municipal Building Energy Benchmarking Results (2014) | 12 |
| 5,521 | dataset | `mqdy-gu73` | CityStore - The Official Store of the City of New York | 9 |
| 4,704 | dataset | `mn2p-34if` | Real-World Fuel Efficiency | 14 |
| 4,441 | dataset | `5rzx-3686` | New York City Fleet Daily Service Report | 12 |
| 3,624 | dataset | `vyk9-wyct` | Civil Service Exams for NYCHA Residents - Local Law 163 | 5 |
| 3,484 | dataset | `whux-iuiu` | Oil Usage For Select City Owned Buildings (Historical) | 17 |
| 3,299 | dataset | `56u5-n9sa` | DCAS Managed Building Fuel Usage (Historical) | 17 |
| 2,282 | dataset | `uxsm-hzx3` | Charter Mandated Quarterly Report on Provisionals | 14 |
| 2,239 | dataset | `xphq-immx` | Non-Public School Security Guard Reimbursement Program - Qualified Provider List | 18 |
| 2,143 | dataset | `dbpt-pbmd` | EEO-4 Reports | 22 |
| 1,703 | dataset | `cfz5-6fvh` | City of New York Municipal Solar-Readiness Assessment (Local Law 24 of 2016) data | 32 |
| 949 | dataset | `qjzt-ytn9` | Annual City Council Report on Eligible List Utilization (Local Law 50 of 2004) | 29 |
| 282 | dataset | `9cgq-8a58` | Building Auditing Report | 20 |

## Groupings

- **Civil service — lists & titles (the signature corpus):** Civil Service List (Active) (`vx8i-nprf`, 20c) + Certification (`a9md-ynri`) + Terminated (`qu8g-sxqf`), Civil List (`ye3c-m4ga`), NYC Civil Service Titles (`nzjr-3966`), Charter-Mandated Quarterly Report on Provisionals (`uxsm-hzx3`), EEO-4 Reports (`dbpt-pbmd`), Eligible List Utilization report (`qjzt-ytn9`).
- **Hiring & exams:** Jobs NYC Postings (`kpav-sd4t`, 30c), Annual Examination Schedule (`4ptz-hmtc`), Civil Service Exams for NYCHA Residents / Local Law 163 (`vyk9-wyct`).
- **Procurement / City Record:** City Record Online (`dg92-zbpx`, 37c), Recent Contract Awards (`qyyg-4tf5`), Current Solicitations (`3khw-qi8f`), Greenbook (`mdcw-n682`), M/WBE Upcoming Procurements (`ww83-bcks`).
- **Buildings & energy:** DCAS Managed Public Buildings (`xx2p-4jnq`, 22c), Managed Building Energy Usage (`ubdi-jgw2`) + Fuel Usage (`56u5-n9sa`) + Oil Usage (`whux-iuiu`), Municipal Building Energy Benchmarking (`vvj6-d5qx`, `hpid-63r5`), Solar-Readiness Assessment (`cfz5-6fvh`), Building Auditing Report (`9cgq-8a58`), Deed Restriction Database (`rfu7-paqe`), Urban Agriculture suitability (`4e2n-s75z`).
- **Fleet:** Fleet Daily Service Report (`5rzx-3686`), Vehicle Auction List (`ynic-uz5i`), Real-World Fuel Efficiency (`mn2p-34if`), EV Fleet Station Network (`fc53-9hrv`).
- **CityStore & other:** CityStore product catalog (`mqdy-gu73`), Non-Public School Security Guard Reimbursement Qualified Providers (`xphq-immx`).
