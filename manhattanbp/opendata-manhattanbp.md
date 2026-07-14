# NYC Open Data — Manhattan Borough President Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Manhattan Borough President (MBPO)"** (verified via the Socrata Discovery API, 2026-07-13). 21 assets, sorted by lifetime page views. Machine-readable: [opendata-manhattanbp.json](opendata-manhattanbp.json).

The shape of the corpus is the story. The office actually publishes its core civic outputs — **ULURP recommendations, appointments, community-board leadership, constituent services, and years of funding awards** — but it does so as **21 one-off datasets**, fragmented by program and by fiscal year. The single most striking pattern: **Capital Grant Awards appear as five separate datasets** (2014, 2015, 2016, 2017, 2018), and discretionary funding is further split across Tourism Grants, Manhattan Community Grants, MCAP, and Police-Community Relations Awards. There is **no dataset for the flagship citizen action** — applying to serve on a community board — which lives only in a WordPress/Forminator form. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 10,645 | dataset | `5jat-czce` | Topographical Bureau Maps | 6 |
| 3,247 | dataset | `w49t-5gha` | MBPO Broadway Storefront Vacancy Survey 2020 | 15 |
| 3,222 | dataset | `x4ud-jhxu` | Tourism Grants | 19 |
| 3,210 | dataset | `8kic-uvpz` | MBPO Pedestrian Ramp Report | 24 |
| 2,906 | dataset | `3gkd-ddzn` | Community Board Leadership | 26 |
| 2,748 | dataset | `qrb4-aqtx` | Manhattan Community Garden Sites Data | 14 |
| 2,379 | dataset | `qy7q-cb9e` | Address Assignments | 23 |
| 2,326 | dataset | `9umc-3b2y` | Capital Grant Awards 2014 | 21 |
| 2,239 | dataset | `rsnd-bbih` | Manhattan Community Grants - Historical | 20 |
| 1,639 | dataset | `66yh-nemi` | Capital Grant Awards 2018 | 14 |
| 1,462 | dataset | `gt5i-dmde` | ULURP Recommendations | 4 |
| 1,149 | dataset | `kpjg-ubxi` | Constituent Services - Historical | 10 |
| 1,095 | dataset | `4y9q-t4wb` | Broadway Curb Cut Survey Data | 13 |
| 947 | dataset | `83z6-smyr` | Capital Grant Awards 2016 | 14 |
| 851 | dataset | `y3ea-en4q` | Manhattan Community Award Program (MCAP) (2007-2017) | 5 |
| 767 | dataset | `uf8p-ervp` | Legislation | 4 |
| 710 | dataset | `k84j-firu` | Capital Grant Awards 2017 | 14 |
| 699 | dataset | `39qw-754y` | Constituent Services | 13 |
| 681 | dataset | `6wee-b7wf` | Capital Grant Awards 2015 | 14 |
| 658 | dataset | `nr9n-yqxr` | BP Appointments | 3 |
| 573 | dataset | `w38c-pyzq` | Police- Community Relations Awards 2016 | 14 |

## Groupings

- **Land use / statutory role:** ULURP Recommendations (`gt5i-dmde`) — recommendation body is a linked PDF; Topographical Bureau Maps (`5jat-czce`); Address Assignments (`qy7q-cb9e`).
- **Appointments & community boards:** BP Appointments (`nr9n-yqxr`), Community Board Leadership (`3gkd-ddzn`, 26c).
- **Discretionary & capital funding (fragmented):** Capital Grant Awards 2014 / 2015 / 2016 / 2017 / 2018 (`9umc-3b2y`, `6wee-b7wf`, `83z6-smyr`, `k84j-firu`, `66yh-nemi`), Tourism Grants (`x4ud-jhxu`), Manhattan Community Grants – Historical (`rsnd-bbih`), MCAP 2007–2017 (`y3ea-en4q`), Police-Community Relations Awards 2016 (`w38c-pyzq`).
- **Constituents (de-identified):** Constituent Services (`39qw-754y`) + Historical (`kpjg-ubxi`).
- **Policy:** Legislation (`uf8p-ervp`) — links out to external bills.
- **Neighborhood / streetscape surveys:** Broadway Storefront Vacancy Survey 2020 (`w49t-5gha`), Broadway Curb Cut Survey (`4y9q-t4wb`), Pedestrian Ramp Report (`8kic-uvpz`), Community Garden Sites (`qrb4-aqtx`).

## Note on the hypothesis

The assessment brief anticipated **zero** Socrata datasets for the Manhattan BP (on the theory that borough presidents publish only reports and PDFs on their own sites). That is **not** the case: the office maintains a genuine, agency-labeled Open Data footprint of 21 datasets. The real weakness is not absence of open data but its **fragmentation** (per-year, per-program datasets), the **generic WordPress site** wrapped around it, and the **missing write surface** for community-board applications.
