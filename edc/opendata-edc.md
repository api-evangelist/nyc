# NYC Open Data — EDC Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Economic Development Corporation (EDC)"** (verified via the Socrata Discovery API, 2026-07-13). Only **5 assets**, sorted by lifetime page views. Machine-readable: [opendata-edc.json](opendata-edc.json).

The shape of the corpus is the story — and the story is how *little* of EDC is here. EDC is a **public benefit corporation**, not a mayoral agency, so it is not systematically on Open Data. What it does publish is **peripheral to its mission**: a promotional company map, NYC Ferry ridership, and three WiredNYC broadband-certification tables. There is **no dataset for EDC's real business** — its ~60M sq ft real-estate portfolio, its development/capital projects, or its solicitations (RFPs/RFEIs). Those live only as Drupal pages on edc.nyc behind a Cloudflare bot challenge. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 18,159 | dataset | `f4yq-wry5` | Mapped In NY Companies | 19 |
| 9,543 | dataset | `t5n6-gx8c` | NYC Ferry Ridership | 7 |
| 7,235 | dataset | `a6nj-cfbz` | WiredNYC – All Buildings Data | 19 |
| 2,126 | dataset | `37it-gmcp` | WiredNYC – Certified Buildings | 31 |
| 1,564 | dataset | `cfzn-4iza` | WiredNYC – Participating Buildings | 30 |

## Groupings

- **Business promotion:** Mapped In NY Companies (`f4yq-wry5`, 19c) — a marketing map of notable NYC companies with hiring links. EDC's most-viewed dataset, and its only company directory.
- **NYC Ferry (operational):** NYC Ferry Ridership (`t5n6-gx8c`, 7c) — boardings by route, stop, hour, and day type. The one genuinely operational EDC dataset; NYC Ferry is run on behalf of EDC.
- **WiredNYC (broadband certification):** All Buildings (`a6nj-cfbz`, 19c), Certified Buildings (`37it-gmcp`, 31c), Participating Buildings (`cfzn-4iza`, 30c) — three parallel telecom-readiness / WiredScore certification tables for a niche EDC program.

## What is *not* here

- **No real-estate / asset dataset** — EDC's managed property portfolio (industrial parks, markets, piers, campuses, ground leases) is unpublished.
- **No projects dataset** — EDC's development and capital projects exist only as site pages.
- **No solicitations dataset** — open RFPs/RFEIs have no machine-readable feed.

The gap is the point: EDC's peripheral programs are on Open Data; its core mission is not.
