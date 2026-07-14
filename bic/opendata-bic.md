# NYC Open Data — BIC Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Business Integrity Commission (BIC)"** (verified via the Socrata Discovery API, 2026-07-13). 9 assets, sorted by lifetime page views. Machine-readable: [opendata-bic.json](opendata-bic.json).

The shape of the corpus is the story: it is a **regulatory registry** — who is licensed, who is registered, who operates in the wholesale markets, every truck in their fleet, every violation issued, and every company denied. There is **no dataset for the transaction layer** (apply, renew, pay a fine); that lives only in the Salesforce Experience Cloud portal (`bicportal.nyc.gov`). Only the *denials* (`exsg-kpya`) hint at the application lifecycle. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 77,997 | dataset | `867j-5pgi` | Trade Waste Hauler Licensees | 27 |
| 33,791 | dataset | `cspg-yi7g` | Construction Demolition Registrants | 25 |
| 33,479 | dataset | `a8wp-rerh` | Self Hauler Registrants | 25 |
| 24,690 | dataset | `krx7-u82t` | Trade Waste Broker Registrants | 25 |
| 24,040 | dataset | `87fx-28ei` | Wholesale Markets | 26 |
| 7,858 | dataset | `upii-frjc` | BIC Issued Violations | 31 |
| 5,606 | dataset | `n84m-kx4j` | Licensees and Registrants Fleet Information | 18 |
| 3,448 | dataset | `p2d7-vcsb` | BIC Complaints Inquiries | 42 |
| 3,282 | dataset | `exsg-kpya` | Denied TW and Wholesale Market Companies | 22 |

## Groupings

- **Licensed accounts:** Trade Waste Hauler Licensees (`867j-5pgi`, 27c) — BIC's core licensed account and most-viewed asset.
- **Registered accounts:** Construction Demolition Registrants (`cspg-yi7g`), Self Hauler Registrants (`a8wp-rerh`), Trade Waste Broker Registrants (`krx7-u82t`) — three parallel registration streams, same shape.
- **Public wholesale markets:** Wholesale Markets (`87fx-28ei`, 26c) — businesses in Hunts Point Produce/Meat and the Fulton Fish Market.
- **Fleet:** Licensees and Registrants Fleet Information (`n84m-kx4j`, 18c) — BIC-plated hauler trucks, incl. side-guard safety compliance.
- **Enforcement:** BIC Issued Violations (`upii-frjc`, 31c) — fines, rule codes, OATH/settlement dispositions.
- **Complaints:** BIC Complaints Inquiries (`p2d7-vcsb`, 42c) — complaints/inquiries about regulated accounts (intake via 311; only closed records here).
- **Application decisions:** Denied TW and Wholesale Market Companies (`exsg-kpya`, 22c) — the only public trace of the apply/review lifecycle.

## The join key

Every dataset keys on **BIC NUMBER** — the account identifier BIC assigns to a licensee, registrant, or market business. That single key ties licensees ↔ registrants ↔ market businesses ↔ their fleet vehicles ↔ their violations ↔ complaints against them, and would tie a live application to the record it becomes. The full NYC geography spine (BORO, Community Board, Council District, Census Tract, NTA, BIN, BBL, lat/long) rides along on every row.
