# NYC Open Data — DDC Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Department of Design and Construction (DDC)"** (verified via the Socrata Discovery API, 2026-07-13). Only **4** assets, sorted by lifetime page views. Machine-readable: [opendata-ddc.json](opendata-ddc.json).

The shape of the corpus is the story: it is **tiny and stale**. Three of the four datasets describe the capital-project portfolio (one current, two frozen `(Historical)` snapshots), and the fourth is a bare directory of awarded contracts. There is **no dataset for solicitations, vendor prequalification, or live project status** — those live in citywide systems (PASSPort/MOCS, City Record, Checkbook NYC). Note too that the richer, live citywide capital data (the Capital Commitment Plan / Capital Project Detail Data) is published under **OMB/Comptroller**, not the DDC label. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 14,114 | dataset | `rukc-mmqu` | Active Projects - Infrastructure (Historical) | 9 |
| 7,246 | dataset | `j7gw-gcxi` | Directory Of Awarded Construction Contracts | 4 |
| 5,665 | dataset | `g9ub-hrve` | Active Projects - Public Buildings (Historical) | 9 |
| 2,710 | dataset | `3ss8-m844` | Active Projects | 8 |

## Groupings

- **Capital projects (current):** Active Projects (`3ss8-m844`, 8c) — Description, Status, Phase, Project ID, Division, Scope, Client Agency, Projected Construction Completion.
- **Capital projects (historical snapshots):** Active Projects – Infrastructure (`rukc-mmqu`, 9c) and Active Projects – Public Buildings (`g9ub-hrve`, 9c) — same shape plus a Dollar Amount column, frozen as historical.
- **Awarded contracts:** Directory Of Awarded Construction Contracts (`j7gw-gcxi`, 4c) — Description, Selected Firm, PIN, $Value. The only vendor-facing dataset, and just four columns wide.

## What is missing

- **No solicitations dataset** — open opportunities are only in PASSPort / City Record.
- **No vendor / prequalification dataset** — vendor identity is derivable only from the `SELECTED FIRM` field of awarded contracts.
- **No live project status** — the three project datasets are point-in-time; two are explicitly `(Historical)`.
- **No geography** — DDC datasets are project/contract oriented; they carry Division and Client Agency but not the address/BBL/BIN spine most NYC datasets do.
