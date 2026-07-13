# NYC Open Data — SBS Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Department of Small Business Services (SBS)"** (verified via the Socrata Discovery API, 2026-07-13). 28 assets, sorted by lifetime page views. Machine-readable: [opendata-sbs.json](opendata-sbs.json).

The shape of the corpus is the story: it is **business-directory and program heavy** — the M/WBE-style **SBS Certified Business List** (56 columns), the city's **Business Improvement Districts** (directory, map, and a 64-column FY24 trends report), **Workforce1** recruitment events and job listings, **Center & Service Locations**, training/course catalogs, and business-incentive rolls (Energy Cost Savings, ICAP). What is missing is the agency's *transactional* core — the **Step-by-Step licensing wizard**, **M/WBE certification applications**, and Workforce1 **enrollment** — all of which live only inside the session-bound MyCity Business portal. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 78,306 | map | `uyj8-7rv5` | Sandy Inundation Zone | 0 |
| 53,972 | dataset | `ci93-uc8s` | SBS Certified Business List | 56 |
| 33,750 | dataset | `9a87-6m4x` | Industrial & Commercial Abatement Program (ICAP) Businesses that received EO50 certificate of approval from SBS | 16 |
| 24,341 | map | `ejxk-d93y` | Business Improvement Districts | 0 |
| 23,124 | dataset | `kf2b-aeh5` | Workforce1 Recruitment Events | 10 |
| 8,895 | dataset | `6smc-7mk6` | Center & Service Locations | 19 |
| 8,050 | dataset | `qpm9-j523` | Directory Of Business Improvement Districts | 18 |
| 7,558 | dataset | `9b9u-8989` | NYC Business Acceleration Businesses Served and Jobs Created | 9 |
| 6,969 | dataset | `y52e-hp89` | Small Business Administration (SBA) Size Standards Table | 5 |
| 6,362 | dataset | `fgq8-am2v` | Courses/Training Provider Listing | 31 |
| 5,792 | dataset | `ay9k-vznm` | Workforce1 Job Listing | 22 |
| 5,764 | dataset | `5vi6-xdpy` | Small Business Services (SBS) Equal Employment Opportunity (EO 50) Certified Businesses | 16 |
| 3,897 | dataset | `5694-9szk` | Love Your Local Business List | 19 |
| 3,213 | dataset | `uxsz-6j5j` | Worker Coops | 19 |
| 3,049 | dataset | `de8q-estm` | Business Solutions Business Courses | 32 |
| 2,516 | dataset | `bug8-9f3g` | Value of Energy Cost Savings Program Savings for Businesses | 30 |
| 1,980 | dataset | `5xsi-dfpx` | Sandy Inundation Zone | 8 |
| 1,830 | dataset | `7jdm-inj8` | Business Improvement Districts | 16 |
| 1,594 | dataset | `v7hc-c85a` | Workforce 1 for NYCHA Residents by Borough - Local Law 163 | 11 |
| 1,524 | dataset | `vhah-kvpj` | Workforce 1 for NYCHA Residents by NYCHA Development - Local Law 163 | 12 |
| 1,104 | dataset | `hzd8-k2vv` | Business Improvement District (BID) Trends Report (FY24) | 64 |
| 1,013 | dataset | `jege-pgbz` | NYC Business Solutions for NYCHA Residents by Borough - Local Law 163 | 3 |
| 994 | dataset | `hjvj-jfc9` | NYC Business Solutions for NYCHA Residents by NYCHA Development - Local Law 163 | 4 |
| 883 | dataset | `qjvp-rnsx` | Avenue NYC CFY17-CFY19 | 21 |
| 845 | dataset | `ynaw-bmnm` | Workforce 1 for NYCHA Residents by City Council District - Local Law 163 | 12 |
| 804 | dataset | `8zxg-9a5c` | NYC Business Solutions for NYCHA Residents by City Council District - Local Law 163 | 4 |
| 606 | dataset | `utpp-yxuj` | Businesses Receiving Training Fund Awards | 2 |
| 600 | dataset | `yqky-aebb` | Jobs Created by Energy Cost Savings Program Savings for Businesses | 17 |

## Groupings

- **Certified businesses (M/WBE & EO50):** SBS Certified Business List (`ci93-uc8s`, 56c — the flagship directory of certified vendors), EO 50 Certified Businesses (`5vi6-xdpy`), ICAP EO50 approvals (`9a87-6m4x`).
- **Business Improvement Districts (BIDs):** Directory of BIDs (`qpm9-j523`, 18c), BID boundary maps (`ejxk-d93y`, `7jdm-inj8`), BID Trends Report FY24 (`hzd8-k2vv`, 64c).
- **Workforce1 / jobs:** Workforce1 Recruitment Events (`kf2b-aeh5`), Workforce1 Job Listing (`ay9k-vznm`, 22c), Workforce 1 for NYCHA Residents rollups (`v7hc-c85a`, `vhah-kvpj`, `ynaw-bmnm`).
- **Service locations & training:** Center & Service Locations (`6smc-7mk6`, 19c), Courses/Training Provider Listing (`fgq8-am2v`), Business Solutions Business Courses (`de8q-estm`), Businesses Receiving Training Fund Awards (`utpp-yxuj`).
- **Business incentives:** Value of Energy Cost Savings Program (`bug8-9f3g`, 30c) + Jobs Created (`yqky-aebb`), ICAP EO50 (`9a87-6m4x`), NYC Business Acceleration (`9b9u-8989`), Avenue NYC (`qjvp-rnsx`).
- **Other business rolls:** Love Your Local Business List (`5694-9szk`), Worker Coops (`uxsz-6j5j`), NYC Business Solutions for NYCHA Residents (`jege-pgbz`, `hjvj-jfc9`, `8zxg-9a5c`), SBA Size Standards Table (`y52e-hp89`), Sandy Inundation Zone (`uyj8-7rv5`, `5xsi-dfpx` — legacy Sandy business-recovery layers).
