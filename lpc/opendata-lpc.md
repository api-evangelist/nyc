# NYC Open Data — LPC Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Landmarks Preservation Commission (LPC)"** (verified via the Socrata Discovery API, 2026-07-13). 15 assets, sorted by lifetime page views. Machine-readable: [opendata-lpc.json](opendata-lpc.json).

The shape of the corpus is the story: it is **designation and building heavy** — individual/interior/scenic landmarks, the rich building database, and historic districts, each published as both a tabular dataset and an interactive map — plus the **issued permit history**, complaints, violations, grants, and archaeology reports. Unlike NYCHA, even the permit record is here as an open READ twin (`dpm2-m9mq`). What is **not** here is the WRITE surface: filing a permit application lives only in the Salesforce Portico portal. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 22,249 | map | `xbvj-gfnw` | Historic Districts (Map) | 0 |
| 19,853 | map | `7mgd-s57w` | Individual Landmark and Historic District Building Database (Map) | 0 |
| 10,071 | dataset | `ncre-qhxs` | Designated and Calendared Buildings and Sites | 34 |
| 7,037 | dataset | `gpmc-yuvp` | Individual Landmark and Historic District Building Database | 37 |
| 6,048 | map | `ts56-fkf5` | Individual Landmark Sites (Map) | 0 |
| 6,011 | dataset | `ck4n-5h6x` | Landmarks Complaints | 18 |
| 5,489 | dataset | `dpm2-m9mq` | LPC Permit Application Information | 32 |
| 5,462 | map | `gi7d-8gt5` | Scenic Landmarks (Map) | 0 |
| 3,895 | dataset | `skyk-mpzq` | Historic Districts | 15 |
| 3,711 | dataset | `wycc-5aqt` | Landmarks Violations | 20 |
| 2,684 | map | `jcj6-zji6` | Designated and Calendared Buildings and Sites (Map) | 0 |
| 2,617 | dataset | `97zg-4p9t` | Grant Applications Tracking Table | 22 |
| 2,569 | dataset | `buis-pvji` | Individual Landmark Sites | 23 |
| 1,880 | dataset | `fuzb-9jre` | Archaeology Reports Database | 6 |
| 1,734 | dataset | `qexa-qpj6` | Scenic Landmarks | 12 |

## Groupings

- **Designations / landmarks:** Individual Landmark Sites (`buis-pvji`, 23c) + map (`ts56-fkf5`), Designated and Calendared Buildings and Sites (`ncre-qhxs`, 34c) + map (`jcj6-zji6`), Scenic Landmarks (`qexa-qpj6`) + map (`gi7d-8gt5`).
- **Building database:** Individual Landmark and Historic District Building Database (`gpmc-yuvp`, 37c) + map (`7mgd-s57w`) — architect, style, materials, dates per building.
- **Historic districts:** Historic Districts (`skyk-mpzq`, 15c) + map (`xbvj-gfnw`) — the most-viewed LPC asset.
- **Permits (read twin):** LPC Permit Application Information (`dpm2-m9mq`, 32c) — issued Certificates of Appropriateness / No Effect and related permits.
- **Enforcement:** Landmarks Complaints (`ck4n-5h6x`, 18c), Landmarks Violations (`wycc-5aqt`, 20c).
- **Grants & reports:** Grant Applications Tracking Table (`97zg-4p9t`, 22c), Archaeology Reports Database (`fuzb-9jre`, 6c).
