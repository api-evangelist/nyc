# NYC Open Data — NYCHA Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "New York City Housing Authority (NYCHA)"** (verified via the Socrata Discovery API, 2026-07-13). 24 assets, sorted by lifetime page views. Machine-readable: [opendata-nycha.json](opendata-nycha.json).

The shape of the corpus is the story: it is **physical-stock and utility heavy** — developments, addresses, facilities, and six parallel streams of consumption-and-cost metering — plus aggregate resident demographics and Local Law 163 workforce/REES rollups. There is **no dataset for the resident service layer** (rent, recertification, applications, work orders); that lives only in the Oracle Siebel Self Service Portal. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 39,933 | dataset | `jr24-e7cr` | Electric Consumption And Cost (2010 - Sep 2025) | 27 |
| 39,036 | dataset | `evjd-dqpz` | NYCHA Development Data Book | 52 |
| 24,620 | dataset | `5r5y-pvs3` | NYCHA Resident Data Book Summary | 43 |
| 17,036 | dataset | `3ub5-4ph8` | NYCHA Residential Addresses | 26 |
| 14,568 | map | `npwq-dpkb` | NYCHA Public Housing Developments Map | 0 |
| 12,956 | dataset | `66be-66yr` | Water Consumption And Cost (2013 - May 2025) | 25 |
| 12,765 | dataset | `crns-fw6u` | Directory of NYCHA Community Facilities | 16 |
| 10,260 | dataset | `phvi-damg` | NYCHA Public Housing Developments | 4 |
| 9,608 | dataset | `d4iy-9uh7` | NYCHA Facilities and Service Centers | 15 |
| 9,240 | dataset | `it56-eyq4` | Heating Gas Consumption And Cost (2010 -  Sep 2025) | 25 |
| 9,027 | map | `72wx-vdjr` | NYCHA PSA (Police Service Areas) | 0 |
| 7,200 | dataset | `smdw-73pj` | Steam Consumption And Cost (2010 – Sep 2025) | 23 |
| 6,349 | dataset | `avhb-5jhc` | Cooking Gas Consumption And Cost (2010 - Sep 2025) | 25 |
| 6,211 | dataset | `37fm-7uaa` | NYCHA Customer Contact Centers | 17 |
| 5,163 | dataset | `bhwu-wuzu` | Heating Oil Consumption And Cost (2010 - Sep 2025) | 21 |
| 4,770 | dataset | `an6v-iuem` | NYCHA Resident Jobs Programs and Training | 6 |
| 3,927 | map | `pv8j-5ywy` | Map of NYCHA Community Facilities | 0 |
| 2,589 | dataset | `7iqz-npua` | NYCHA Citywide Special Events | 4 |
| 2,290 | dataset | `dsyc-npkh` | Air Quality Testing at Saratoga Village | 17 |
| 2,160 | dataset | `dggd-3jfu` | Resident Economic Empowerment and Sustainability (REES) for NYCHA Residents – NYCHA Development - Local Law 163 | 13 |
| 2,147 | map | `4p5v-sqmv` | Map of NYCHA Community Engagement & Partnership Zones | 0 |
| 1,356 | dataset | `7su9-xgtn` | Recurring Resident Economic Empowerment and Sustainability Programs | 17 |
| 1,349 | dataset | `snck-inhz` | Resident Economic Empowerment and Sustainability (REES) for NYCHA Residents - Borough - Local Law 163 | 12 |
| 1,100 | dataset | `h65x-gk9r` | Resident Economic Empowerment and Sustainability (REES) for NYCHA Residents – Council District - Local Law 163 | 13 |

## Groupings

- **Physical stock / geography:** Development Data Book (`evjd-dqpz`, 55c), Public Housing Developments (`phvi-damg`) + map (`npwq-dpkb`), Residential Addresses (`3ub5-4ph8`, 26c), PSA / Police Service Areas map (`72wx-vdjr`).
- **Facilities:** Directory of Community Facilities (`crns-fw6u`) + map (`pv8j-5ywy`), Facilities & Service Centers (`d4iy-9uh7`), Customer Contact Centers (`37fm-7uaa`), Community Engagement & Partnership Zones map (`4p5v-sqmv`).
- **Utility metering (PropertyMeter):** Electric (`jr24-e7cr`), Water (`66be-66yr`), Heating Gas (`it56-eyq4`), Cooking Gas (`avhb-5jhc`), Steam (`smdw-73pj`), Heating Oil (`bhwu-wuzu`) — parallel consumption-and-cost bill lines.
- **Residents (aggregate only):** Resident Data Book Summary (`5r5y-pvs3`, 43c).
- **Economic empowerment / Local Law 163:** REES by development / borough / council district (`dggd-3jfu`, `snck-inhz`, `h65x-gk9r`), Recurring REES programs (`7su9-xgtn`), Resident Jobs Programs & Training (`an6v-iuem`).
- **Other:** Citywide Special Events (`7iqz-npua`), Air Quality Testing at Saratoga Village (`dsyc-npkh`).
