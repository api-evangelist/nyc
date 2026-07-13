# NYC Open Data — ACS Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Administration for Children's Services (ACS)"** (verified via the Socrata Discovery API, 2026-07-13). 21 assets, sorted by lifetime page views. Machine-readable: [opendata-acs.json](opendata-acs.json).

The shape of the corpus is the story. Unlike the physical-stock agencies, ACS's footprint is **thin and mostly non-tabular**: of 21 assets, **16 are `file` attachments** (uploaded Excel/PDF accountability reports, `columns = 0` — you cannot query them with SODA) and **only 5 are real tabular datasets**. Of those five, exactly **one is address-level and machine-readable** — *ACS Community Partners* (`9hyh-zkx9`, 39 columns), the provider directory. Everything else is **aggregate accountability reporting** on child welfare, prevention, foster care, and youth justice — published as counts by period and geography, never per case, because ACS's operational data is confidential by statute. There is **no dataset for the public service layer** (report abuse → NY State Central Register; complain about a child care provider → NYC 311). See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 7,512 | dataset | `9hyh-zkx9` | ACS Community Partners | 39 |
| 5,422 | file | `rnjn-x48k` | Abuse/Neglect by Community District (CD) | 0 |
| 5,299 | file | `abgy-h8ag` | High School Graduation Rates in Foster Care | 0 |
| 4,646 | file | `3m2q-9maw` | Child Welfare Indicators – Annual and quarterly report indicators | 0 |
| 3,543 | file | `xg3x-h3g7` | Foster Care Placements by Community District (CD) | 0 |
| 3,349 | file | `gx5n-2nma` | Adolescents in Foster Care (permanency outcomes) | 0 |
| 2,883 | file | `2ubh-v9er` | Monthly Flash Report indicators | 0 |
| 2,613 | file | `kkjw-ny95` | Annual Child Abuse Allegation Detention and Placement | 0 |
| 2,545 | file | `bhs9-p657` | Detention and Placement Demographic reports | 0 |
| 2,240 | file | `ding-39n6` | Children Served in Preventive Services by Borough and CD | 0 |
| 2,105 | file | `hfa5-7rzg` | Children In 24-hour Foster Care by Community District | 0 |
| 1,697 | file | `j4t9-dyts` | Educational Continuity of Children in Foster Care | 0 |
| 1,678 | file | `a2ju-qb9a` | Preventive New Cases | 0 |
| 1,651 | file | `2jnq-tef6` | Detention and Placement Incident Reports | 0 |
| 1,642 | dataset | `uhvm-6sct` | Report to City Council on Demographics of Children and Parents at Steps in the Child Welfare System | 13 |
| 1,509 | dataset | `2hrw-qfsu` | Detention Admissions by Community District | 4 |
| 1,165 | file | `n5e5-z493` | Government-Issued Personal Identification for Youth in Foster Care | 0 |
| 1,064 | file | `x48i-xnrz` | Preventive Services Utilization Report LL 11 | 0 |
| 1,035 | dataset | `qw7r-btyb` | Report to City Council on Use of Psychiatric Medication for Youth in Foster Care | 15 |
| 946 | file | `q663-gvx6` | Outcome of Preventive Cases Closed By Borough And CD (CY 2014) | 0 |
| 420 | dataset | `iwat-y983` | Report to City Council on Preplacement | 9 |

## Groupings

- **Provider directory (the one machine-readable asset):** ACS Community Partners (`9hyh-zkx9`, 39c) — program name, agency, address, weekly office hours, contact, and full NYC geography spine (BBL/BIN, council district, community board, NTA, lat/long).
- **Child welfare (aggregate):** Child Welfare Indicators (`3m2q-9maw`), Monthly Flash Report (`2ubh-v9er`), Report to City Council on Demographics (`uhvm-6sct`, 13c — SCR intakes, investigations, removals, Article X filings), Abuse/Neglect by CD (`rnjn-x48k`).
- **Preventive services (aggregate):** Children Served (`ding-39n6`), Preventive New Cases (`a2ju-qb9a`), Utilization Report LL 11 (`x48i-xnrz`), Outcome of Cases Closed (`q663-gvx6`).
- **Foster care (aggregate):** Children in 24-hour Foster Care (`hfa5-7rzg`), Foster Care Placements by CD (`xg3x-h3g7`), Adolescents / permanency (`gx5n-2nma`), HS Graduation Rates (`abgy-h8ag`), Educational Continuity (`j4t9-dyts`), Government-Issued ID for Youth (`n5e5-z493`), Psychiatric Medication (`qw7r-btyb`, 15c).
- **Youth & family justice (aggregate):** Detention Admissions by CD (`2hrw-qfsu`, 4c), Detention & Placement Demographics (`bhs9-p657`), Incident Reports (`2jnq-tef6`), Annual Abuse-Allegation Detention/Placement (`kkjw-ny95`), Report to City Council on Preplacement (`iwat-y983`, 9c).

## Caveat

Child care *licensing/permit* data — the regulated day-care programs themselves — is published by **DOHMH**, not ACS (e.g. "Active NYC Health Code Regulated Child Care Programs" carries `Dataset-Information_Agency = Department of Health and Mental Hygiene (DOHMH)`). ACS's own child-care role is captured in the Community Partners directory and its Head Start / EarlyLearn contracting, not in a licensing dataset under the ACS label.
