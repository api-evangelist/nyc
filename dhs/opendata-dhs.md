# NYC Open Data — DHS Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Department of Homeless Services (DHS)"** (verified via the Socrata Discovery API, 2026-07-13). 23 assets, sorted by lifetime page views. Machine-readable: [opendata-dhs.json](opendata-dhs.json).

The shape of the corpus is the story: it is **observational** — the flagship **DHS Daily Report** (the daily shelter census, by far the most-viewed asset), directories of drop-in centers and DHS contacts/intake centers, borough/community-district census and building breakdowns, the Shelter Repair Scorecard, and years of unsheltered street-homeless ratio reports. There is **no dataset for the service layer** (apply for shelter, request street outreach); those actions live only in NYC311, a phone call, or an in-person intake center. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 87,033 | dataset | `k46n-sa2m` | DHS Daily Report | 13 |
| 23,653 | dataset | `cete-9g3v` | Directory Of DHS Contacts | 14 |
| 19,690 | dataset | `bmxf-3rd4` | Directory Of Homeless Drop- In Centers | 13 |
| 18,618 | dataset | `5t4n-d72c` | Directory Of Homeless Population By Year | 3 |
| 12,687 | dataset | `veav-vj3r` | Individual Census by Borough, Community District, and Facility Type | 11 |
| 11,916 | dataset | `3qem-6v3v` | Buildings by Borough and Community District | 10 |
| 9,589 | dataset | `5e9h-x6ak` | DHS Data Dashboard | 58 |
| 9,497 | dataset | `dvaj-b7yx` | Shelter Repair Scorecard | 55 |
| 6,113 | dataset | `ur7y-ziyb` | Associated Address by Borough and Community District | 6 |
| 3,895 | dataset | `483x-fy9e` | Directory Of Unsheltered Street Homeless To General Population Ratio 2012 | 13 |
| 3,495 | dataset | `sci4-yqgk` | Daily Report Of Single Adult And Family Intake | 3 |
| 3,422 | dataset | `985h-mtct` | FWC and AF Monthly Eligibility Rate | 3 |
| 3,261 | dataset | `e3qr-idgg` | Local Law 19 - Annual Report DHS Shelter (Historical) | 4 |
| 2,318 | dataset | `y7z5-rhh5` | Directory Of Family Shelter Performance Ranking FY 2012 Q4 and 2013 Q1 | 4 |
| 2,259 | dataset | `7tu6-bcih` | Local Law 19 of 1999 Report - Quarterly Unsheltered Street Homeless Individuals | 3 |
| 1,944 | dataset | `jhn3-4vdj` | Directory Of Adult Shelter Performance Ranking FY 2011 Q3 2011 Q4 | 4 |
| 1,918 | dataset | `rkad-22be` | Local Law 217 of 2017 Report | 3 |
| 1,820 | dataset | `ivbu-e2q7` | Directory Of Unsheltered Street Homeless To General Population Ratio 2011 | 13 |
| 1,807 | dataset | `8kiv-2ukd` | Directory Of Unsheltered Street Homeless To General Population Ratio 2010 | 13 |
| 1,630 | dataset | `dwrg-kzni` | DHS Daily Report (Historical) | 13 |
| 1,335 | dataset | `x56h-7iwp` | Directory Of Unsheltered Street Homeless To General Population Ratio 2009 | 13 |
| 1,157 | dataset | `5284-7vfz` | Local Law 19 of 1999 Report - Monthly Placements | 4 |
| 986 | dataset | `5nux-zfmw` | Local Law 97 of 2021 - Pets in Shelter Report | 24 |

## Groupings

- **Daily shelter census (flagship):** DHS Daily Report (`k46n-sa2m`, 13c) + its historical twin (`dwrg-kzni`), Daily Report Of Single Adult And Family Intake (`sci4-yqgk`), Directory Of Homeless Population By Year (`5t4n-d72c`), and the composite DHS Data Dashboard (`5e9h-x6ak`, 58c).
- **Facilities / buildings:** Shelter Repair Scorecard (`dvaj-b7yx`, 55c), Buildings by Borough and Community District (`3qem-6v3v`), Individual Census by Borough, Community District, and Facility Type (`veav-vj3r`), Associated Address by Borough and Community District (`ur7y-ziyb`).
- **Directories:** Directory Of DHS Contacts / offices & intake centers (`cete-9g3v`, 14c), Directory Of Homeless Drop-In Centers (`bmxf-3rd4`, 13c).
- **Street homelessness (aggregate):** Unsheltered Street Homeless To General Population Ratio, four years (`483x-fy9e` 2012, `ivbu-e2q7` 2011, `8kiv-2ukd` 2010, `x56h-7iwp` 2009), Local Law 19 Quarterly Unsheltered Street Homeless Individuals (`7tu6-bcih`).
- **Performance / compliance reports:** Family & Adult Shelter Performance Rankings (`y7z5-rhh5`, `jhn3-4vdj`), FWC and AF Monthly Eligibility Rate (`985h-mtct`), Local Law 19 Annual/Monthly reports (`e3qr-idgg`, `5284-7vfz`), Local Law 217 of 2017 (`rkad-22be`), Local Law 97 of 2021 Pets in Shelter (`5nux-zfmw`).
