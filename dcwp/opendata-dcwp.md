# NYC Open Data — DCWP Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Department of Consumer and Worker Protection (DCWP)"** (verified via the Socrata Discovery API, 2026-07-13). 37 assets, sorted by lifetime page views. Machine-readable: [opendata-dcwp.json](opendata-dcwp.json).

The shape of the corpus is the story: it is **a full regulatory lifecycle in the open** — license applications → issued licenses → inspections → charges/violations → consumer complaints → revocations — plus the Office of Labor Policy & Standards' worker-protection matters and a cluster of financial-empowerment datasets. Everything joins on `Business Unique ID` and `License Number`. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 147,430 | dataset | `w7w3-xahh` | Issued Licenses | 31 |
| 36,346 | dataset | `ptev-4hud` | License Applications | 35 |
| 20,423 | dataset | `5fn4-dr26` | DCWP Charges | 18 |
| 19,104 | dataset | `jzhd-m6uv` | DCWP Inspections | 28 |
| 19,062 | dataset | `qcdj-rwhu` | HISTORICAL Sidewalk Café Licenses and Applications | 47 |
| 18,974 | dataset | `nre2-6m2s` | DCWP Consumer Complaints | 33 |
| 18,005 | dataset | `6y5g-5hkj` | Waiting List for General Vendor Licenses | 10 |
| 12,541 | dataset | `p2wf-m8zt` | Tobacco Retail Dealer and Electronic Cigarette Retail Dealer Caps by Community District | 10 |
| 9,388 | dataset | `r3dx-pew9` | Neighborhood Financial Health Digital Mapping and Data Tool | 52 |
| 8,751 | dataset | `2k3g-r445` | DCWP Fines and Fees (Historical) | 11 |
| 8,190 | dataset | `q5u8-89nv` | DARP-ROTOW Enrollment Status of Active Tow Truck Companies | 27 |
| 7,991 | dataset | `dt2z-amuf` | Financial Empowerment Centers | 32 |
| 6,282 | dataset | `5kqf-fg3n` | NYC Free Tax Prep Sites | 81 |
| 4,917 | dataset | `2xab-argn` | DCWP Payments Received | 14 |
| 4,830 | dataset | `rpeq-j89e` | License Revocations, Suspensions, Surrenders, and Reinstatements | 7 |
| 4,301 | dataset | `8fei-z6rz` | Weights, Measures, and Other Tests | 31 |
| 4,047 | dataset | `b9yk-4pzk` | Action Taken Against Process Servers | 5 |
| 3,483 | dataset | `j46y-iqiq` | NYC Mobile Services Study | 79 |
| 3,401 | dataset | `v5w4-adxa` | Where Are the Unbanked and Underbanked in New York City | 17 |
| 2,969 | dataset | `2z24-2htf` | Office of Labor Policy & Standards Workplace Inquiries (Historical) | 13 |
| 2,857 | dataset | `m4ph-grrm` | Historical Licenses | 27 |
| 2,765 | dataset | `u42f-se8e` | Lottery Applications for Tobacco Retail Dealer (TRD) and Electronic Cigarette Dealer Licenses (ECD) | 16 |
| 2,577 | dataset | `c292-vzrn` | Office of Labor Policy & Standards Enforcement Matters (Historical) | 15 |
| 2,529 | dataset | `azp6-hepu` | Licensing Center Customer Information | 6 |
| 2,497 | dataset | `wapz-jfhq` | DCWP Language Line Interpretation Services | 4 |
| 1,999 | dataset | `ga3c-v25a` | Trust Fund Invasions | 9 |
| 1,790 | dataset | `8hgr-brxd` | DCA Monthly Compliance Report Date for Process Servers | 3 |
| 1,530 | dataset | `ayx3-dixq` | Pedicab Registration Plate Lottery Applications | 19 |
| 1,421 | dataset | `9vpn-rpgs` | DCWP Licensed Vehicles | 15 |
| 1,241 | dataset | `2c9f-2ta9` | Financial Services for NYCHA Residents by Borough - Local Law 163 | 30 |
| 1,172 | dataset | `vnz6-h2k4` | Historical License Applications | 28 |
| 1,105 | dataset | `kwss-yksz` | Archived DCWP Inspections | 26 |
| 1,038 | dataset | `vk6p-jwjf` | Financial Services for NYCHA Residents by Council District - Local Law 163 | 30 |
| 1,035 | dataset | `wyj6-frpa` | Archived DCWP Charges | 31 |
| 986 | dataset | `r9ax-4va4` | Waiting List Applications for Midtown Core Zone Vending License | 12 |
| 967 | dataset | `g4tm-nibn` | 2017-18 Financial Services for NYCHA Residents - Local Law 163 | 27 |
| 820 | dataset | `fiag-ac7u` | Financial Services for NYCHA Residents by Development - Local Law 163 | 26 |

## Groupings

- **Licensing lifecycle:** Issued Licenses (`w7w3-xahh`, 31c), License Applications (`ptev-4hud`, 35c), Historical Licenses (`m4ph-grrm`), Historical License Applications (`vnz6-h2k4`), Revocations/Suspensions (`rpeq-j89e`), Licensed Vehicles (`9vpn-rpgs`), Licensing Center Customer Information (`azp6-hepu`), Sidewalk Café (`qcdj-rwhu`).
- **Inspections & enforcement:** DCWP Inspections (`jzhd-m6uv`, 28c) + Archived (`kwss-yksz`), Weights, Measures & Other Tests (`8fei-z6rz`), DCWP Charges (`5fn4-dr26`, 18c) + Archived (`wyj6-frpa`), Fines & Fees (`2k3g-r445`), Payments Received (`2xab-argn`).
- **Consumer complaints:** DCWP Consumer Complaints (`nre2-6m2s`, 33c).
- **Worker protection (OLPS, aggregate only):** Enforcement Matters (`c292-vzrn`), Workplace Inquiries (`2z24-2htf`).
- **Vendor / license lotteries & waitlists:** General Vendor Waiting List (`6y5g-5hkj`), Midtown Core Zone Vending (`r9ax-4va4`), Pedicab Plate Lottery (`ayx3-dixq`), Tobacco/E-Cig caps (`p2wf-m8zt`) & lottery (`u42f-se8e`), DARP-ROTOW Tow Trucks (`q5u8-89nv`).
- **Process servers / trust funds:** Action Against Process Servers (`b9yk-4pzk`), Monthly Compliance Report Date (`8hgr-brxd`), Trust Fund Invasions (`ga3c-v25a`).
- **Financial empowerment:** Financial Empowerment Centers (`dt2z-amuf`), Free Tax Prep Sites (`5kqf-fg3n`), Neighborhood Financial Health tool (`r3dx-pew9`), Unbanked/Underbanked (`v5w4-adxa`), Mobile Services Study (`j46y-iqiq`), Language Line (`wapz-jfhq`), Financial Services for NYCHA Residents / LL163 (`2c9f-2ta9`, `vk6p-jwjf`, `g4tm-nibn`, `fiag-ac7u`).
