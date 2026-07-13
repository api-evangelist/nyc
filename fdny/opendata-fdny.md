# NYC Open Data — FDNY Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Fire Department of New York City (FDNY)"** (verified via the Socrata Discovery API, 2026-07-13). 17 assets, sorted by lifetime page views. Machine-readable: [opendata-fdny.json](opendata-fdny.json).

The shape of the corpus is the story: it is **incident- and inspection-heavy** — firehouses, two minute-level dispatch feeds (Fire and EMS), Bureau of Fire Prevention inspections, active violation orders, certificates of fitness, and building safety — but every regulatory record is published as a **historical snapshot**. There is **no dataset for the live business transaction layer** (applying for a permit, holding a Certificate of Fitness, scheduling an inspection, answering a violation); that lives only in the rented Accela FDNY Business portal. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 113,448 | dataset | `hc8x-tcnd` | FDNY Firehouse Listing | 12 |
| 99,703 | dataset | `76xm-jjuj` | EMS Incident Dispatch Data | 31 |
| 69,579 | dataset | `8m42-w767` | Fire Incident Dispatch Data | 29 |
| 30,434 | dataset | `32y8-s55c` | FDNY Line Of Duty Deaths | 4 |
| 25,208 | dataset | `tm6d-hbzd` | Incidents Responded to by Fire Companies | 24 |
| 19,706 | dataset | `j34j-vqvt` | FDNY Monthly Response Times (Historical) | 5 |
| 13,647 | dataset | `v57i-gtxb` | In-Service Alarm Box Locations | 15 |
| 13,056 | dataset | `ssq6-fkht` | Bureau of Fire Prevention - Inspections (Historical) | 20 |
| 12,261 | dataset | `bi53-yph3` | Bureau of Fire Prevention - Active Violation Orders (Historical) | 21 |
| 11,047 | dataset | `ii3r-svjz` | Bureau of Fire Investigations - Fire Causes | 10 |
| 9,276 | dataset | `n5xc-7jfa` | NYC Fire Department Building Vacate List | 11 |
| 6,262 | map | `na5f-2vg7` | In-Service Alarm Box Locations (Map) | 0 |
| 6,028 | dataset | `nvgj-hbht` | Bureau of Fire Prevention - Building Summary (Historical) | 16 |
| 5,392 | dataset | `pdiy-9ae5` | Bureau of Fire Prevention - Certificates of Fitness (Historical) | 18 |
| 3,653 | dataset | `itd7-gx3g` | Risk Based Inspections (RBIS) | 21 |
| 3,006 | dataset | `kfgh-h6re` | Mandatory Inspections by Fire Companies | 11 |
| 1,643 | dataset | `gcnt-k7eq` | Firefighter Probationary School Results Admissions and Graduation Statistics | 6 |

## Groupings

- **Physical stock / infrastructure:** FDNY Firehouse Listing (`hc8x-tcnd`, 12c), In-Service Alarm Box Locations (`v57i-gtxb`) + map (`na5f-2vg7`).
- **Incident dispatch & response:** EMS Incident Dispatch (`76xm-jjuj`, 31c), Fire Incident Dispatch (`8m42-w767`, 29c), Incidents Responded to by Fire Companies (`tm6d-hbzd`, 24c), Monthly Response Times (`j34j-vqvt`), Bureau of Fire Investigations – Fire Causes (`ii3r-svjz`).
- **Inspections:** BFP Inspections (`ssq6-fkht`, 20c), Risk Based Inspections / RBIS (`itd7-gx3g`, 21c), Mandatory Inspections by Fire Companies (`kfgh-h6re`, 11c).
- **Violations & building safety:** BFP Active Violation Orders (`bi53-yph3`, 21c), NYC Fire Department Building Vacate List (`n5xc-7jfa`), BFP Building Summary (`nvgj-hbht`, 16c).
- **Certificates:** BFP Certificates of Fitness (`pdiy-9ae5`, 18c).
- **Workforce / other:** FDNY Line of Duty Deaths (`32y8-s55c`), Firefighter Probationary School Results (`gcnt-k7eq`).
