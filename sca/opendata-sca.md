# NYC Open Data — SCA Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "School Construction Authority (SCA)"** (verified via the Socrata Discovery API, 2026-07-13). 43 assets, sorted by lifetime page views. Machine-readable: [opendata-sca.json](opendata-sca.json).

The shape of the corpus is the story: it is **capital-plan and procurement heavy** — active projects under construction, schedules and budgets, capacity by school, the upcoming CIP/CAP contract pipeline, current/anticipated RFPs, change orders, and the prequalified/disqualified vendor roster — plus the enrollment/capacity demand and demographic projections that justify the plan, and a construction-inspection stream. There is **no dataset for the vendor transaction layer** (obtaining bid documents, submitting a prequalification application); that lives only behind the login-walled bidset SharePoint portal. See [crosswalk.md](crosswalk.md).

Datasets carry two Open Data categories: **Housing & Development** (the capital/construction/procurement rows) and **Education** (RFPs, enrollment/capacity, inspections).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 130,924 | dataset | `8586-3zfm` | Active Projects Under Construction | 29 |
| 18,601 | dataset | `tsak-vtv3` | Upcoming contracts to be awarded (CIP) | 9 |
| 12,214 | dataset | `2xh6-psuq` | Capital Project Schedules and Budgets | 14 |
| 12,060 | dataset | `szkz-syh6` | Prequalified Firms | 15 |
| 6,660 | dataset | `gkd7-3vk7` | Enrollment Capacity And Utilization Reports | 16 |
| 6,492 | dataset | `krwf-eng6` | SCA Disqualified Firms | 4 |
| 5,509 | dataset | `wavz-fkw8` | DOE Building Space Usage | 8 |
| 5,111 | dataset | `bzjf-rmtp` | Current RFP | 7 |
| 4,037 | dataset | `e649-r223` | Statistical Forecasting Demographic Projection Report - Enrollment Projections | 19 |
| 3,020 | dataset | `xzy8-qqgf` | Demographic Projection Report - Enrollment Projections | 20 |
| 2,945 | dataset | `pa5t-ktd3` | Projected New Housing Starts (Enrollment Projection) | 3 |
| 2,935 | dataset | `gzvm-na49` | Contractor / Sub Contractor Change Order Report | 14 |
| 2,806 | dataset | `6m3u-8rbh` | Upcoming contracts to be awarded (CAP) | 10 |
| 2,554 | dataset | `esmb-8zkm` | School Based Programs by Borough | 9 |
| 2,536 | dataset | `p8e4-uwuv` | Anticipated RFP | 5 |
| 2,479 | dataset | `a94k-kjys` | Capacity Projects by School | 25 |
| 2,418 | dataset | `q9xk-w9iv` | Enrollment Capacity And Utilization Reports - Historical by Organization | 12 |
| 2,355 | dataset | `n7ta-pz8k` | Projected Public School Ratio | 6 |
| 2,316 | dataset | `8a4n-zmpj` | Art in DOE buildings | 10 |
| 1,972 | dataset | `n4tc-j6kh` | Inspections Requested | 7 |
| 1,681 | dataset | `hq56-zhrp` | Enrollment Capacity And Utilization Reports - Historical by Building | 16 |
| 1,593 | dataset | `gshi-yqza` | Transportable Classroom Units - Buildings & Schools | 9 |
| 1,570 | dataset | `6246-94tp` | Observations And Statuses For Inspections | 7 |
| 1,537 | dataset | `bjmk-35w5` | Current Plan Programs | 7 |
| 1,531 | dataset | `3spy-rjpw` | Transportable Classroom Units - Buildings Only | 17 |
| 1,489 | dataset | `cwqt-nvfg` | Cancelled Projects | 6 |
| 1,467 | dataset | `24nr-gahi` | Five Year Plan Summary by Capital Category | 9 |
| 1,454 | dataset | `8gpu-s594` | Application for State Aid | 17 |
| 1,395 | dataset | `xs6e-ka4w` | 3K Projects by School | 14 |
| 1,357 | dataset | `nfz9-tzba` | Pre-K Projects By School | 14 |
| 1,355 | dataset | `kydh-ijhc` | Replacement Projects by school | 14 |
| 1,324 | dataset | `yiqb-mq9h` | Advanced Projects | 5 |
| 1,280 | dataset | `9ddq-vbjj` | Five Year Summary By Citywide Category | 8 |
| 1,270 | dataset | `yv4m-nu6d` | 3K Projects by Site Locations | 13 |
| 1,225 | dataset | `7xjx-2mhj` | Added Projects | 5 |
| 1,167 | dataset | `tzwr-vksx` | New Capacity Program By Borough | 11 |
| 1,145 | dataset | `ujdf-5byz` | Funded Capacity Seats and Additional Needs | 6 |
| 1,053 | dataset | `4zdr-zwdi` | Pre-K Project Site Location | 13 |
| 1,029 | dataset | `gk83-aa6y` | Update to Submitted State Aid Projects | 17 |
| 744 | dataset | `dtmw-avzj` | Capacity Projects in Process Site Locations | 15 |
| 708 | dataset | `mpg8-b8s5` | Class Size Reduction Projects | 14 |
| 611 | dataset | `vmfm-wic2` | Early Learn Project Sites | 24 |
| 527 | dataset | `32rn-zwi7` | Capacity Supporting Transportable Classroom Units (TCU) Removals | 25 |

## Groupings

- **Capital projects / construction:** Active Projects Under Construction (`8586-3zfm`, 29c), Capital Project Schedules and Budgets (`2xh6-psuq`), Capacity Projects by School (`a94k-kjys`, 25c) + in-process site locations (`dtmw-avzj`), Advanced / Added / Cancelled / Replacement projects (`yiqb-mq9h`, `7xjx-2mhj`, `cwqt-nvfg`, `kydh-ijhc`), 3K / Pre-K / Early Learn project sites (`xs6e-ka4w`, `nfz9-tzba`, `4zdr-zwdi`, `vmfm-wic2`, `yv4m-nu6d`), Class Size Reduction (`mpg8-b8s5`), TCUs (`gshi-yqza`, `3spy-rjpw`, `32rn-zwi7`).
- **Capital plan summaries:** Five Year Plan Summary by Capital Category (`24nr-gahi`), Five Year Summary By Citywide Category (`9ddq-vbjj`), Current Plan Programs (`bjmk-35w5`), New Capacity Program By Borough (`tzwr-vksx`), Funded Capacity Seats and Additional Needs (`ujdf-5byz`).
- **Procurement / vendors:** Upcoming contracts CIP (`tsak-vtv3`) + CAP (`6m3u-8rbh`), Current RFP (`bzjf-rmtp`), Anticipated RFP (`p8e4-uwuv`), Change Order Report (`gzvm-na49`), Prequalified Firms (`szkz-syh6`, 15c), SCA Disqualified Firms (`krwf-eng6`).
- **Enrollment / capacity / demand:** Enrollment Capacity And Utilization Reports (`gkd7-3vk7`, 16c) + historical by org/building (`q9xk-w9iv`, `hq56-zhrp`), DOE Building Space Usage (`wavz-fkw8`), demographic projections (`e649-r223`, `xzy8-qqgf`), Projected New Housing Starts (`pa5t-ktd3`), Projected Public School Ratio (`n7ta-pz8k`), School Based Programs by Borough (`esmb-8zkm`).
- **Inspections:** Inspections Requested (`n4tc-j6kh`), Observations And Statuses For Inspections (`6246-94tp`).
- **State aid:** Application for State Aid (`8gpu-s594`), Update to Submitted State Aid Projects (`gk83-aa6y`).
- **Other:** Art in DOE buildings (`8a4n-zmpj`).
