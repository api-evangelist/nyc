# NYC Open Data — HRA / DSS Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Human Resources Administration (HRA)"** (verified via the Socrata Discovery API, 2026-07-13; the alternate label "Department of Social Services (DSS)" returns 0 assets). 49 assets, sorted by lifetime page views. Machine-readable: [opendata-hra.json](opendata-hra.json).

The shape of the corpus is the story: it is **benefits-caseload and directory heavy** — recipient/enrollee counts and case actions for the three big public-benefit programs (SNAP, Cash Assistance, Medicaid), plus directories of the offices where residents apply (Benefits Access Centers, SNAP Centers, Medicaid Offices, Homebase). What is missing is any dataset for the **individual application or case** a resident actually files; the aggregate numbers are published, but the transactional layer lives only in the ACCESS HRA application portal. The eligibility *logic*, uniquely, is open source — the ACCESS NYC screener runs on a public Drools rules engine ([ACCESS-NYC-Rules](https://github.com/NYCOpportunity/ACCESS-NYC-Rules)). See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 23,322 | dataset | `ntcm-2w4k` | Directory Of Homebase Locations | 14 |
| 17,529 | dataset | `5c4s-jwtq` | Total SNAP Recipients (Historical) | 2 |
| 12,599 | dataset | `9d9t-bmk7` | Directory of Benefits Access Centers | 16 |
| 8,986 | dataset | `tc6u-8rnp` | Directory of SNAP Centers | 15 |
| 8,517 | dataset | `33db-aeds` | Citywide HRA- Administered Medicaid Enrollees | 6 |
| 7,455 | dataset | `mpqk-skis` | Community Food Connection (Quarterly Report) | 4 |
| 5,155 | dataset | `5awp-wfkt` | Cash Assistance, Medicaid, and SNAP - Borough/Community District Report | 9 |
| 4,792 | dataset | `gqk4-hny9` | SNAP Center Wait Time | 4 |
| 4,346 | dataset | `wjvv-6yxq` | HASA Facts | 92 |
| 4,070 | dataset | `ibs4-k445` | Medicaid Offices | 16 |
| 3,547 | dataset | `4c8i-cnte` | SNAP Program Access Index (PAI) | 3 |
| 3,294 | dataset | `fq4m-vjs9` | Benefits Access Center Wait Times | 4 |
| 3,247 | dataset | `qtrj-g3nm` | Cash Assistance Recipients in NYC (Historical) | 5 |
| 2,963 | dataset | `vnwq-9b7b` | Special Initiatives Moveouts and Placements | 5 |
| 2,769 | dataset | `5vgr-4tp3` | Cash Assistance Emergency Assistance Requests | 23 |
| 2,682 | dataset | `tbf6-u8ea` | HRA Domestic Violence Partners | 3 |
| 2,509 | dataset | `ay6v-3gm3` | SNAP and Cash Assistance for NYCHA Residents - Local Law 163 | 8 |
| 2,429 | dataset | `np6w-pies` | HRA Facts, Programs and Services | 8 |
| 2,354 | dataset | `hb7y-b986` | Cash Assistance Engagement Report | 10 |
| 2,255 | dataset | `g6pg-qint` | Cash Assistance and SNAP Cases Rejections | 75 |
| 2,138 | dataset | `thqd-deec` | Cash Assistance Recipients Since 1955 (Historical) | 12 |
| 2,110 | dataset | `3tw8-6si8` | Fair Fares Enrollees | 2 |
| 1,989 | dataset | `5fs5-yi3e` | Cash Assistance and SNAP Cases Closed | 75 |
| 1,899 | dataset | `afsf-hz68` | Credited Job Placement Report (Historical) | 7 |
| 1,676 | dataset | `xjur-zbxw` | Home Care Caseload (Historical) | 5 |
| 1,586 | dataset | `9jbx-hna8` | Citywide Cash Assistance Cases (Historical) | 5 |
| 1,560 | dataset | `pqmq-sk82` | Youth Engagement By Category | 4 |
| 1,545 | dataset | `mefg-rpis` | JobStat (Historical) | 4 |
| 1,525 | dataset | `uwx4-aafe` | Local Law 49 Reporting | 18 |
| 1,521 | dataset | `5uf6-jjmy` | Cash Assistance and SNAP Cases Reopenings | 75 |
| 1,460 | dataset | `j7wp-ax4x` | Total HASA Cases (Historical) | 2 |
| 1,407 | dataset | `wd9h-xwk5` | Youth Engagement Summary | 4 |
| 1,369 | dataset | `auj6-ur3j` | Cash Assistance Applications for Youth Heads of Household, Ages 16 - 20 | 7 |
| 1,308 | dataset | `vibf-3qrq` | Adult Protective Services - Ineligible Referral | 31 |
| 1,292 | dataset | `au2c-rs69` | District Resource Statement (DRS) | 10 |
| 1,194 | dataset | `ftyx-fhnc` | Work Progress Program (WPP) for NYCHA Residents - Local Law 163 | 11 |
| 1,160 | dataset | `4kkh-qhtc` | Jobs Plus for NYCHA Residents - Local Law 163 | 11 |
| 1,105 | dataset | `g2dh-zf5t` | Child Support Caseload and Collections | 6 |
| 1,026 | dataset | `bkui-39n8` | Adult Protective Services - Refer to Close | 10 |
| 951 | dataset | `28gm-7ump` | Cash Assistance and SNAP Cases Reopenings with a Missed Benefits Cycle | 75 |
| 939 | dataset | `rtmc-bhid` | IDNYC Applications and Cards Issued | 3 |
| 632 | dataset | `mpw3-7xyh` | Adult Protective Services - Refer to Close by Referral Source | 4 |
| 585 | dataset | `tzsf-n2j8` | Local Law 161 - Escorts at Benefits Access Centers and SNAP Centers | 16 |
| 387 | dataset | `gxfj-gcr2` | Local Law 161 - Use of Force (UoF) Incidents at Benefits Access Centers and SNAP Centers | 19 |
| 356 | dataset | `7wa7-cvt5` | Local Law 161 Arrests by Peace Officers at Benefits Access Centers and SNAP Centers | 16 |
| 348 | dataset | `wh8n-imgd` | Local Law 3 of 2022 - Supportive Housing - Reporting on Coordinated Assessment and Placement System | 4 |
| 345 | dataset | `wn4z-dw55` | Local Law 161 Summons Issued by Peace Officers  at Benefits Access Centers and SNAP Centers | 17 |
| 300 | dataset | `ejux-uh6h` | Local Law 161- Agency Calls to NYPD for Assistance at Job and SNAP Centers | 21 |
| 289 | dataset | `tm9k-c4na` | Local Law 161 Removals by Peace Officers at Benefits Access Centers and SNAP Centers | 16 |

## Groupings

- **Where residents apply (directories + wait times):** Directory of Benefits Access Centers (`9d9t-bmk7`, 16c), Directory of SNAP Centers (`tc6u-8rnp`, 15c), Medicaid Offices (`ibs4-k445`, 16c), Directory of Homebase Locations (`ntcm-2w4k`, 14c), Benefits Access Center Wait Times (`fq4m-vjs9`), SNAP Center Wait Time (`gqk4-hny9`).
- **Program caseloads & enrollment (aggregate):** Total SNAP Recipients (`5c4s-jwtq`), Cash Assistance Recipients (`qtrj-g3nm`; since 1955 `thqd-deec`), Citywide HRA-Administered Medicaid Enrollees (`33db-aeds`), Cash Assistance/Medicaid/SNAP by Borough/Community District (`5awp-wfkt`), Citywide Cash Assistance Cases (`9jbx-hna8`), District Resource Statement (`au2c-rs69`), Fair Fares Enrollees (`3tw8-6si8`), IDNYC Applications & Cards Issued (`rtmc-bhid`).
- **Case actions (aggregate, ~75 columns each):** Cash Assistance and SNAP Cases Rejections (`g6pg-qint`), Closed (`5fs5-yi3e`), Reopenings (`5uf6-jjmy`), Reopenings with a Missed Benefit (`28gm-7ump`) — broken out by council district, race, age band, sex, and reason code.
- **Programs & services reference:** HRA Facts, Programs and Services (`np6w-pies`), HRA Facts (`np6w-pies`), Cash Assistance Emergency Assistance Requests (`5vgr-4tp3`, 23c), Cash Assistance Engagement Report (`hb7y-b986`), Community Food Connection (`mpqk-skis`).
- **Special populations:** HASA Facts (HIV/AIDS Services, `wjvv-6yxq`, 92c) + Total HASA Cases (`j7wp-ax4x`), Adult Protective Services (`vibf-3qrq`, `bkui-39n8`, `mpw3-7xyh`), Home Care Caseload (`xjur-zbxw`), Child Support Caseload & Collections (`g2dh-zf5t`), HRA Domestic Violence Partners (`tbf6-u8ea`), Youth Engagement (`pqmq-sk82`, `wd9h-xwk5`), Special Initiatives Moveouts & Placements (`vnwq-9b7b`).
- **Workforce / NYCHA (Local Law 163):** SNAP and Cash Assistance for NYCHA Residents (`ay6v-3gm3`), Work Progress Program for NYCHA Residents (`ftyx-fhnc`), Jobs Plus for NYCHA Residents (`4kkh-qhtc`), Credited Job Placement Report (`afsf-hz68`), JobStat (`mefg-rpis`).
- **Oversight (Local Law 161 — peace officers at Benefits Access & Job Centers):** Escorts (`tzsf-n2j8`), Use of Force (`gxfj-gcr2`), Arrests (`7wa7-cvt5`), Summons (`wn4z-dw55`), Removals (`tm9k-c4na`), Calls to NYPD (`ejux-uh6h`); plus Local Law 49 Reporting (`uwx4-aafe`) and Local Law 3 of 2022 Supportive Housing (`wh8n-imgd`).

## The one thing Open Data does not publish

There is **no dataset for an individual application or case** — no per-resident SNAP/Cash Assistance/Medicaid application record, status, or determination. That transactional surface lives only inside the **ACCESS HRA** application portal (`a069-access.nyc.gov/accesshra`, a React SPA behind Akamai bot protection) with no public API. The aggregate case-action datasets (rejections/closings/reopenings) are the closest published twin, and they are counts only.
