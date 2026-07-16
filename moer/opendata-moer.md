# NYC Open Data — MOER/OER Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Mayor's Office of Environmental Remediation (OER)"** (verified via the Socrata Discovery API, 2026-07-16). **10** OER-labeled assets, sorted by lifetime page views, plus the **DCP-owned** E-Designation assets that are *related but not OER's*. Machine-readable: [opendata-moer.json](opendata-moer.json).

The shape of the corpus is the story, and it inverts the DDC pattern: OER's reference data is **genuinely open and, at its core, live**. The flagship **OER Cleanup Sites** dataset is updated **Daily** and carries a full BBL/BIN geography spine — it is the machine-readable backing of the public SPEED map. Around it sits a **Historic Land Use** due-diligence layer and the **Clean Soil Bank** and **Brownfield Opportunity Area (BOA)** planning suites. What is *missing* is not the data but the **workflow**: there is no dataset (and no API) for the remedial process itself — the (E)-resolution steps, the determinations OER issues (Notice to Proceed, Notice of Satisfaction), or where a cleanup stands. Those live only in the login-walled **EPIC** portal (`a002-epic.nyc.gov`). And the authoritative **(E)-designation inventory** is published under the **Department of City Planning (DCP)** label, not OER. See [crosswalk.md](crosswalk.md).

## OER-owned assets (10)

| Views | Type | ID | Name | Cols | Freq |
|--:|---|---|---|--:|---|
| 7,449 | dataset | `3279-pp7v` | OER Cleanup Sites | 18 | **Daily** |
| 6,599 | dataset | `r9ca-6t4q` | Historic Land Use Data | 9 | Historical |
| 2,215 | dataset | `b4dv-8mq4` | NYC Clean Soil Bank Generating and Receiving Sites | 21 | Annually |
| 1,713 | map | `22gm-5ceg` | Shapefiles of BOA and Community Brownfield Planning Areas | — | Annually |
| 1,103 | map | `hywf-9b6t` | NYC Clean Soil Bank Generating and Receiving Sites | — | Annually |
| 1,064 | dataset | `w5ew-m3sm` | BOA and Community Brownfield Planning Areas - Designated BOAs | 11 | Annually |
| 991 | dataset | `wnhn-bgpv` | ...EPA Area Wide Planning Areas | 6 | Annually |
| 790 | dataset | `mfxb-aygx` | ...OER Community Grant Projects | 3 | Annually |
| 766 | dataset | `qj7d-vb9s` | BOA and Community Brownfield Planning Areas - BOA Studies | 7 | Annually |
| 640 | dataset | `bztk-4g6r` | ...OER Existing Conditions Studies | 8 | Annually |

## Related but NOT OER-owned — published under DCP

| Views | Type | ID | Name | Owner |
|--:|---|---|---|---|
| 8,989 | dataset | `mzjp-98aw` | E Designations: shapefile | **Department of City Planning (DCP)** |
| 4,653 | dataset | `hxm3-23vy` | E-Designations | **Department of City Planning (DCP)** |
| 1,775 | dataset | `jsrs-ggnx` | E-Designations | **Department of City Planning (DCP)** |

The most-viewed E-designation asset (8,989 views) is DCP's, not OER's — the demand for (E) data sits on a surface OER does not own, even though OER is the office that *resolves* the (E) requirement.

## Groupings

- **Cleanup sites (live):** OER Cleanup Sites (`3279-pp7v`, 18c, Daily) — OER Project Numbers, Project Name, OER Program, Class, Phase, full address + BBL/BIN + Borough/CB/Council/CT/NTA + coordinates, and a link to the project-specific document repository.
- **Due-diligence history:** Historic Land Use Data (`r9ca-6t4q`, 9c) — BBL-keyed historic environmental concerns (former gas stations, dry cleaners, etc.).
- **Clean Soil Bank:** dataset (`b4dv-8mq4`) + map (`hywf-9b6t`) — generating/receiving sites, tonnage, boroughs.
- **Brownfield planning (BOA) suite:** six geospatial layers (Designated BOAs, EPA Area-Wide, Community Grant Projects, BOA Studies, Existing Conditions Studies, parent shapefile), several carrying `epic_link` back to the EPIC portal.

## What is missing

- **No remedial-workflow data** — no dataset (and no API) for the OER Remedial Process phases, the determinations OER issues (Notice to Proceed / Decision Document, Notice of Satisfaction / Completion), or live cleanup status. Those live only in **EPIC** (`a002-epic.nyc.gov`).
- **No OER-owned (E)-designation inventory** — the authoritative (E) data is published by **DCP** (`hxm3-23vy`, `mzjp-98aw`, `jsrs-ggnx`).
- **No documented API for SPEED** — the public site-lookup map (`speed.cityofnewyork.us`) is a CARTO/Leaflet app that pulls its own `clientData.json`; there is no documented, versioned OER API over it.
- **No intake surface** — the request that starts everything (enroll in the VCP / request a Notice to Proceed) has no dataset and no API; it is a manual EPIC-and-email process.
