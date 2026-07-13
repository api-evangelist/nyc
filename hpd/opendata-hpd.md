# NYC Open Data — HPD Datasets

All **47** datasets published on [NYC Open Data](https://data.cityofnewyork.us) under the agency label **"Department of Housing Preservation and Development (HPD)"** (verified 2026-07-13 via the Socrata Discovery API, filtering `Dataset-Information_Agency`). Machine-readable index with per-column schemas: [opendata-hpd.json](opendata-hpd.json).

This is HPD's real public, machine-readable surface. It is broad and heavily used — the top dataset (Housing Maintenance Code Violations) has **215k+** views — but every dataset is a **flattened periodic snapshot** exported from HPD's systems, joined only by shared keys (`buildingid`, `registrationid`, `bbl`, `bin`). None is a live, resource-oriented, agent-native API; the live record lives behind HPD Online's private backend (see [apis-observed.md](apis-observed.md)).

## The families

- **Conditions record** — Housing Maintenance Code Violations (`wvxf-dwi5`, the flagship), Complaints & Problems (`ygpa-z7cr`), Order to Repair/Vacate Orders (`tb8q-a3ar`), Bedbug Reporting (`wz6d-d3jb`), NYCHA violations (`im9z-53hg`).
- **Property & ownership** — Buildings Subject to HPD Jurisdiction (`kj4p-ruqc`), Multiple Dwelling Registrations (`tesw-yqqr`), Registration Contacts (`feu5-w2e2`).
- **Litigation & enforcement** — Housing Litigations (`59kj-x8nc`), Alternative Enforcement Program (`hcir-3275`), Underlying Conditions (`xpbf-ithr`), Heat Sensor Program (`h4mf-f24e`), CONH Pilot (`bzxi-2tsw`), OMO/HWO/Fee/Vacate charge tables.
- **Affordable-housing production** — Housing New York: Production by Building (`hg8x-zxpr`) & by Project (`hq68-rnsi`); LIHTC awards; Inclusionary Housing; 421-a / 485-x programs.
- **Lottery (Housing Connect)** — Advertised Lotteries by Building (`nibs-na6y`) & by Lottery (`vy5i-a666`) — the read-only twin of the closed Housing Connect application portal.
- **Local Law 44** — a 14-dataset family (Building, Projects, Rent Affordability, Development Team, Wages, Funding, LIHTC, Tax Incentive…) on financed-project transparency.

## All datasets (sorted by page views)

| # | Dataset | ID | Type | Cols | Views | Category |
|---|---|---|---|---|---|---|
| 1 | [Housing Maintenance Code Violations](https://data.cityofnewyork.us/d/wvxf-dwi5) | `wvxf-dwi5` | dataset | 41 | 215,745 | Housing & Development |
| 2 | [Affordable Housing Production by Building](https://data.cityofnewyork.us/d/hg8x-zxpr) | `hg8x-zxpr` | dataset | 41 | 99,022 | Housing & Development |
| 3 | [Bedbug Reporting](https://data.cityofnewyork.us/d/wz6d-d3jb) | `wz6d-d3jb` | dataset | 21 | 58,188 | Housing & Development |
| 4 | [Multiple Dwelling Registrations](https://data.cityofnewyork.us/d/tesw-yqqr) | `tesw-yqqr` | dataset | 16 | 54,522 | Housing & Development |
| 5 | [Affordable Housing Production by Project](https://data.cityofnewyork.us/d/hq68-rnsi) | `hq68-rnsi` | dataset | 19 | 33,815 | Housing & Development |
| 6 | [Buildings Subject to HPD Jurisdiction](https://data.cityofnewyork.us/d/kj4p-ruqc) | `kj4p-ruqc` | dataset | 23 | 28,564 | Housing & Development |
| 7 | [Housing Litigations](https://data.cityofnewyork.us/d/59kj-x8nc) | `59kj-x8nc` | dataset | 24 | 28,123 | Housing & Development |
| 8 | [Registration Contacts](https://data.cityofnewyork.us/d/feu5-w2e2) | `feu5-w2e2` | dataset | 15 | 27,312 | Housing & Development |
| 9 | [Order to Repair/Vacate Orders](https://data.cityofnewyork.us/d/tb8q-a3ar) | `tb8q-a3ar` | dataset | 20 | 23,134 | Housing & Development |
| 10 | [Buildings Selected for the Alternative Enforcement Program (AEP)](https://data.cityofnewyork.us/d/hcir-3275) | `hcir-3275` | dataset | 19 | 19,003 | Housing & Development |
| 11 | [Housing Maintenance Code Complaints and Problems](https://data.cityofnewyork.us/d/ygpa-z7cr) | `ygpa-z7cr` | dataset | 33 | 18,531 | Housing & Development |
| 12 | [Open Market Order (OMO) Charges](https://data.cityofnewyork.us/d/mdbu-nrqn) | `mdbu-nrqn` | dataset | 32 | 18,305 | Housing & Development |
| 13 | [Certification of No Harassment (CONH) Pilot Building List](https://data.cityofnewyork.us/d/bzxi-2tsw) | `bzxi-2tsw` | dataset | 22 | 13,582 | Housing & Development |
| 14 | [Local Law 44 Disqualified List](https://data.cityofnewyork.us/d/9s68-zggy) | `9s68-zggy` | dataset | 42 | 8,473 | Housing & Development |
| 15 | [Speculation Watch List](https://data.cityofnewyork.us/d/adax-9mit) | `adax-9mit` | dataset | 29 | 8,404 | Housing & Development |
| 16 | [Handyman Work Order (HWO) Charges](https://data.cityofnewyork.us/d/sbnd-xujn) | `sbnd-xujn` | dataset | 32 | 8,091 | Housing & Development |
| 17 | [485-x Affordable Neighborhoods for New Yorkers: Registrations of Prospective Applicants for Tax Benefits](https://data.cityofnewyork.us/d/rrtd-iyd7) | `rrtd-iyd7` | dataset | 25 | 8,084 | Housing & Development |
| 18 | [Local Law 44 - Building](https://data.cityofnewyork.us/d/hu6m-9cfi) | `hu6m-9cfi` | dataset | 24 | 7,652 | Housing & Development |
| 19 | [Local Law 44 - Projects](https://data.cityofnewyork.us/d/ucdy-byxd) | `ucdy-byxd` | dataset | 15 | 7,348 | Housing & Development |
| 20 | [Local Law 44 - Rent Affordability](https://data.cityofnewyork.us/d/93d2-wh7s) | `93d2-wh7s` | dataset | 4 | 7,337 | Housing & Development |
| 21 | [421-a(16) Affordable New York Housing Program Completion Extension - Letters of Intent](https://data.cityofnewyork.us/d/pq4c-wbq4) | `pq4c-wbq4` | dataset | 27 | 6,973 | Housing & Development |
| 22 | [Local Law 44 - Unit Income Rent](https://data.cityofnewyork.us/d/9ay9-xkek) | `9ay9-xkek` | dataset | 11 | 6,699 | Housing & Development |
| 23 | [Fee Charges](https://data.cityofnewyork.us/d/cp6j-7bjj) | `cp6j-7bjj` | dataset | 27 | 5,538 | Housing & Development |
| 24 | [Housing Maintenance Code Violations NYCHA properties](https://data.cityofnewyork.us/d/im9z-53hg) | `im9z-53hg` | dataset | 35 | 5,474 | Housing & Development |
| 25 | [Advertised Lotteries on Housing Connect By Building](https://data.cityofnewyork.us/d/nibs-na6y) | `nibs-na6y` | dataset | 30 | 5,196 | Housing & Development |
| 26 | [Low Income Housing Tax Credits Awarded by HPD: Project-Level (9% Awards)](https://data.cityofnewyork.us/d/frre-6z6q) | `frre-6z6q` | dataset | 26 | 4,983 | Housing & Development |
| 27 | [Invoices for Open Market Order (OMO) Charges](https://data.cityofnewyork.us/d/emrz-5p35) | `emrz-5p35` | dataset | 13 | 4,819 | Housing & Development |
| 28 | [Inclusionary Housing Projects](https://data.cityofnewyork.us/d/jafx-rvrb) | `jafx-rvrb` | dataset | 7 | 4,427 | Housing & Development |
| 29 | [Inclusionary Housing Properties](https://data.cityofnewyork.us/d/cm6g-t7ye) | `cm6g-t7ye` | dataset | 18 | 4,071 | Housing & Development |
| 30 | [Advertised Lotteries on Housing Connect by Lottery](https://data.cityofnewyork.us/d/vy5i-a666) | `vy5i-a666` | dataset | 30 | 3,947 | Housing & Development |
| 31 | [Local Law 44 - Development Team](https://data.cityofnewyork.us/d/6anw-twe4) | `6anw-twe4` | dataset | 28 | 3,916 | Housing & Development |
| 32 | [Local Law 44 - Wage Information](https://data.cityofnewyork.us/d/34zf-iv73) | `34zf-iv73` | dataset | 7 | 3,651 | Housing & Development |
| 33 | [Buildings Selected for the Underlying Conditions Program](https://data.cityofnewyork.us/d/xpbf-ithr) | `xpbf-ithr` | dataset | 16 | 3,279 | Housing & Development |
| 34 | [Local Law 7-2018 Qualified Transactions](https://data.cityofnewyork.us/d/8wi4-bsy4) | `8wi4-bsy4` | dataset | 33 | 3,121 | Housing & Development |
| 35 | [Local Law 159 of 2019: Vacate Relocation Charges By Building](https://data.cityofnewyork.us/d/3bkg-usya) | `3bkg-usya` | dataset | 23 | 3,053 | Housing & Development |
| 36 | [Low Income Housing Tax Credits Awarded by HPD: Project-Level (4% Awards)](https://data.cityofnewyork.us/d/p8i7-ix2s) | `p8i7-ix2s` | dataset | 26 | 2,651 | Housing & Development |
| 37 | [Local Law 44 - Funding](https://data.cityofnewyork.us/d/gmi7-62cd) | `gmi7-62cd` | dataset | 5 | 2,356 | Housing & Development |
| 38 | [Buildings Selected for the Heat Sensor Program (HSP)](https://data.cityofnewyork.us/d/h4mf-f24e) | `h4mf-f24e` | dataset | 17 | 2,259 | Housing & Development |
| 39 | [Local Law 44 - Other City Financial Assistance](https://data.cityofnewyork.us/d/7r6i-tdj2) | `7r6i-tdj2` | dataset | 9 | 2,220 | Housing & Development |
| 40 | [Low Income Housing Tax Credits Awarded by HPD: Building-Level (9% Awards)](https://data.cityofnewyork.us/d/kmtx-45c9) | `kmtx-45c9` | dataset | 3 | 2,176 | Housing & Development |
| 41 | [Local Law 44 - LIHTC](https://data.cityofnewyork.us/d/sgvu-nui7) | `sgvu-nui7` | dataset | 4 | 2,020 | Housing & Development |
| 42 | [Local Law 44 - Tax Incentive](https://data.cityofnewyork.us/d/72vt-ykjc) | `72vt-ykjc` | dataset | 4 | 1,968 | Housing & Development |
| 43 | [Low Income Housing Tax Credits Awarded by HPD: Building-Level (4% Awards)](https://data.cityofnewyork.us/d/h9ws-rfd9) | `h9ws-rfd9` | dataset | 3 | 1,855 | Housing & Development |
| 44 | [Local Law 44 - Developer Selection](https://data.cityofnewyork.us/d/abnr-s7g4) | `abnr-s7g4` | dataset | 5 | 1,511 | Housing & Development |
| 45 | [Inclusionary Housing Transfers](https://data.cityofnewyork.us/d/ej3f-9dad) | `ej3f-9dad` | dataset | 5 | 1,406 | Housing & Development |
| 46 | [Local Law 44 (2009-2012)](https://data.cityofnewyork.us/d/7zf5-7vum) | `7zf5-7vum` | file | 0 | 1,380 | Housing & Development |
| 47 | [Inclusionary Housing Floor Area Generated](https://data.cityofnewyork.us/d/qcru-xhuq) | `qcru-xhuq` | dataset | 3 | 1,230 | Housing & Development |
