# NYC Open Data — NYPL Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "New York Public Library (NYPL)"** (verified via the Socrata Discovery API, 2026-07-13). **Only 6 assets**, sorted by lifetime page views. Machine-readable: [opendata-nypl.json](opendata-nypl.json).

**The finding is the near-absence.** NYPL is an independent nonprofit, not a city agency, so it barely uses NYC Open Data at all. What is here is thin and mostly **stale**: a facilities point layer (`feuq-due4` / the "Library" map `p4pf-fyc4`) and a set of **2010–2011 branch-services statistics** (circulation, attendance, reference transactions) that were never updated. NYPL's real, living data does not live on NYC Open Data — it lives on **NYPL's own public APIs**: the Digital Collections API (`api.repo.nypl.org`), the Locations API (`refinery.nypl.org`), and the Research Catalog (`discovery-api`). See [apis-observed.md](apis-observed.md) and [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 17,342 | map | `p4pf-fyc4` | Library | 0 |
| 5,602 | dataset | `3nja-bsch` | NYPL Branch Services - Manhattan | 22 |
| 5,513 | dataset | `ne9z-skhf` | New York Public Library (NYPL) Branch Services from 7-2010 to 6-2011 | 22 |
| 3,315 | dataset | `feuq-due4` | LIBRARY | 13 |
| 2,465 | dataset | `pfys-fabf` | NYPL Branch Services - Bronx | 22 |
| 1,820 | dataset | `wibz-uqui` | NYPL Branch Services - Staten Island | 22 |

## Groupings

- **Facilities / geography (2):** `p4pf-fyc4` (Library map) and `feuq-due4` ("LIBRARY" — a geocoded point layer with NAME, address, ZIP, X/Y, BBL, BIN, SYSTEM, BOROCODE). These are the only assets that overlap NYPL's live Locations API, and the Locations API is far richer (hours, amenities, access, events).
- **Branch-services statistics, 2010–2011 (4):** `3nja-bsch` (Manhattan), `pfys-fabf` (Bronx), `wibz-uqui` (Staten Island), and the citywide `ne9z-skhf`. Each carries the same 22 columns — circulation, attendance, program counts, and reference transactions broken out by Adult / Young Adult / Juvenile, plus weekly public-service hours. **Historical snapshots; not maintained.** Note the boroughs present (Manhattan, Bronx, Staten Island) confirm NYPL's service footprint — Brooklyn (BPL) and Queens (QPL) are separate systems.

## Why this matters

For every other domain in this project, NYC Open Data is where the good data hides. For NYPL it is the opposite: Open Data is a thin, stale afterthought, and the substance is on APIs NYPL built and open-sourced itself. That inversion is the whole point of this assessment — NYPL is the counter-example.
