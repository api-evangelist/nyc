# NYC Open Data — Department of Finance (DOF) Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Department of Finance (DOF)"** (verified via the Socrata Discovery API, 2026-07-13). **145 assets**, sorted by lifetime page views. Machine-readable: [opendata-dof.json](opendata-dof.json).

The shape of the corpus is the story: it is the **widest footprint of any NYC agency assessed so far** — property valuation & assessment, exemptions and abatements, tax-charge balances, the full **ACRIS** recorded-document register (deeds, mortgages, parties, legals), and every **parking/camera violation**. Yet none of the *transactions* those datasets describe — paying a ticket, paying a tax bill, recording a document — has an API. Those live only in the legacy **a836-*.nyc.gov** apps (ACRIS, CityPay, PTS). See [crosswalk.md](crosswalk.md).

Showing the top 40 by page views (full set of 145 in the JSON).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 350,713 | dataset | `nc67-uf89` | Open Parking and Camera Violations | 19 |
| 222,937 | filter | `bnx9-e6tj` | ACRIS - Real Property Master | 14 |
| 152,315 | dataset | `9rz4-mjek` | Tax Lien Sale Lists | 13 |
| 142,229 | dataset | `pvqr-7yc4` | Parking Violations Issued - Fiscal Year 2026 | 44 |
| 103,169 | dataset | `muvi-b6kx` | Property Exemption Detail | 70 |
| 87,195 | file | `smk3-tmxj` | Department of Finance Digital Tax Map | 0 |
| 79,920 | filter | `636b-3b5g` | ACRIS - Real Property Parties | 11 |
| 73,263 | dataset | `y7az-s7wc` | J-51 Exemption and Abatement (Historical) | 15 |
| 68,234 | filter | `8h5j-fqxa` | ACRIS - Real Property Legals | 14 |
| 62,402 | dataset | `8y4t-faws` | Property Valuation and Assessment Data Tax Classes 1,2,3,4 | 139 |
| 59,883 | dataset | `ncbg-6agr` | DOF Parking Violation Codes | 4 |
| 55,883 | story | `i4p3-pe6a` | Open Parking and Camera Violations | 0 |
| 50,420 | dataset | `yjxr-fw8i` | Property Valuation and Assessment Data | 45 |
| 47,332 | dataset | `7zb8-7bpk` | Property Tax Rates by Tax Class | 5 |
| 41,874 | file | `uzf5-f8n2` | NYC Calendar Sales (Archive) | 0 |
| 32,132 | dataset | `jt7v-77mi` | Parking Violations Issued - Fiscal Year 2014 | 43 |
| 29,124 | file | `rgy2-tti8` | Property Valuation and Assessment Data | 0 |
| 27,407 | filter | `6y3e-jcrc` | ACRIS - Personal Property References | 6 |
| 26,365 | filter | `9p4w-7npp` | ACRIS - Real Property Remarks | 5 |
| 25,354 | dataset | `kiv2-tbus` | Parking Violations Issued - Fiscal Year 2016 | 43 |
| 25,264 | filter | `uqqa-hym2` | ACRIS - Personal Property Legals | 14 |
| 22,862 | filter | `sv7x-dduq` | ACRIS - Personal Property Master | 17 |
| 22,571 | dataset | `2bnn-yakx` | Parking Violations Issued - Fiscal Year 2017 | 43 |
| 21,965 | dataset | `94g4-w6xz` | ACRIS - Property Types Codes | 3 |
| 21,710 | dataset | `w2pb-icbu` | NYC Citywide Annualized Calendar Sales Update | 29 |
| 20,765 | dataset | `scjx-j6np` | DOF: Property Charges Balance | 34 |
| 20,695 | dataset | `92iy-9c3n` | Storefronts Reported Vacant or Not | 31 |
| 20,586 | dataset | `7isb-wh4c` | ACRIS - Document Control Codes | 7 |
| 19,935 | dataset | `wvts-6tdf` | Real Property Income and Expense Form non-compliance list | 20 |
| 19,518 | filter | `nbbg-wtuz` | ACRIS - Personal Property Parties | 11 |
| 19,166 | dataset | `usep-8jbt` | NYC Citywide Rolling Calendar Sales | 21 |
| 18,748 | dataset | `8vgb-zm6e` | Revised Notice of Property Value (RNOPV) | 39 |
| 18,480 | dataset | `rgyu-ii48` | DOF Property Abatement Detail | 101 |
| 18,339 | filter | `pwkr-dpni` | ACRIS - Real Property References | 11 |
| 15,818 | href | `nzvw-cjc2` | DOF: Building Classification Codes | 0 |
| 15,666 | dataset | `5ebm-myj7` | DOF: Summary of Neighborhood Sales by Neighborhood Citywide by Borough | 9 |
| 15,152 | dataset | `dxru-eun8` | Storefront Registration Class 2 and 4 Statistics | 25 |
| 14,890 | dataset | `tjus-cn27` | Hotels Properties Citywide | 21 |
| 12,601 | dataset | `faiq-9dfq` | Parking Violations Issued - Fiscal Year 2019 | 43 |
| 12,191 | dataset | `7mxj-7a6y` | Parking Violations Issued - Fiscal Year 2022 | 43 |

## Groupings

- **Property valuation & assessment:** Property Valuation and Assessment Data (`yjxr-fw8i`, 45c) and the wide Tax-Classes edition (`8y4t-faws`, 139c); NYC Citywide Annualized Calendar Sales (`w2pb-icbu`); Digital Tax Map (`smk3-tmxj`).
- **Exemptions & abatements:** Property Exemption Detail (`muvi-b6kx`, 70c); J-51 Exemption and Abatement (`y7az-s7wc`).
- **Tax charges / liens:** DOF Property Charges Balance (`scjx-j6np`, 34c); Property Tax Rates by Tax Class (`7zb8-7bpk`); Tax Lien Sale Lists (`9rz4-mjek`).
- **ACRIS recorded-document register:** Real Property Master (`bnx9-e6tj`), Legals (`8h5j-fqxa`), Parties (`636b-3b5g`), plus Personal Property Master/Legals/Parties/References and the Document Control / Property Type code tables (`7isb-wh4c`, `94g4-w6xz`).
- **Parking & camera violations:** Open Parking and Camera Violations (`nc67-uf89`, 19c, the live balance) and Parking Violations Issued by fiscal year (`pvqr-7yc4` FY2026 + prior years, ~43c each); DOF Parking Violation Codes (`ncbg-6agr`).
- **Other:** Storefronts Reported Vacant or Not (`92iy-9c3n`); Real Property Income and Expense non-compliance (`wvts-6tdf`).
