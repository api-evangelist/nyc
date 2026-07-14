# NYC Open Data — NYC Health + Hospitals Datasets

Assets on NYC Open Data (`data.cityofnewyork.us`) whose **`Dataset-Information_Agency`** is owned by **NYC Health + Hospitals** — queried via the Socrata Discovery API, 2026-07-13. Machine-readable: [opendata-hhc.json](opendata-hhc.json).

## Result: zero — and that is the finding

**No NYC Open Data dataset is published under a "NYC Health + Hospitals" (or "Health and Hospitals Corporation (HHC)") agency label.** Verified three ways:

- `Dataset-Information_Agency = "NYC Health + Hospitals"` → **0 assets**.
- `Dataset-Information_Agency = "Health and Hospitals Corporation (HHC)"` → **0 assets**.
- Free-text `q=hospital` / `q=Health and Hospitals` across `data.cityofnewyork.us` → the health-related datasets that come back are **all owned by the Department of Health and Mental Hygiene (DOHMH)** (COVID counts, HIV/AIDS, maternal morbidity, air quality) — a *different* agency. The two "Health and Hospitals System" outpatient-registration datasets that surface in a global Socrata search (`c62y-v8ri`, `h2ke-7kt8`) resolve to **Cook County, Illinois** (`datacatalog.cookcountyil.gov`), not NYC.

## Why the corpus is empty

Unlike NYCHA (24 open datasets) or the other NYC agencies in this project, **H+H is a public benefit corporation whose core data is clinical** — it lives in an **Epic electronic health record**, not in a Socrata open-data catalog. Patient-level health data is protected (HIPAA) and by design is never published as open data. What machine-readable surface H+H *does* have is not on Open Data at all — it is the **live Epic FHIR R4 / SMART on FHIR API** (`epicproxypda.nychhc.org`), which is patient-authorized rather than open. See [apis-observed.md](apis-observed.md) and [crosswalk.md](crosswalk.md).

Citywide health *statistics* about the population H+H serves are published by **DOHMH**, and hospital-discharge / SPARCS data is published by the **NY State Department of Health** — but those belong to other agencies and are outside this domain's ownership.

## Implication

There is **no Open Data twin** for any H+H entity — not for the facility directory, not for service lines, not for providers, not for appointments. The reference layer that other agencies expose through Socrata (`Facility`, `Location`) is, for H+H, either bot-walled on the marketing site or auth-gated behind the Epic FHIR `Location`/`Organization` resources. The [OpenAPI](openapi/hhc.yaml) here therefore proposes an **open facility/service directory** H+H does not publish today, alongside the net-new booking write surface.
