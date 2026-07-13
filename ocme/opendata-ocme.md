# NYC Open Data — OCME Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Office of Chief Medical Examiner (OCME)"** (verified via the Socrata Discovery API, 2026-07-13). **Exactly one** asset is filed under OCME. Machine-readable: [opendata-ocme.json](opendata-ocme.json).

The number *is* the story. OCME is the most **data-dark** agency assessed so far: a single dataset carries its label, and that dataset is not casework — it is a **Mayor's Management Report (MMR) performance-indicators passthrough**, a wide "indicator × month" pivot whose only real months run **July 2015 – May 2016**. It is a stale snapshot, not a live feed.

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 2,180 | dataset | `8r6c-ydwk` | Monthly Indicators | 16 |

## What is *not* here

There is **no Open Data twin** for anything OCME actually does:

- **No death-investigation / case data** — not even in aggregate. OCME's core object (a medical-examiner case) is never published; per-decedent records are, correctly, confidential.
- **No manner-of-death, cause-of-death, or drug-overdose aggregates** under the OCME label. (Overdose and mortality aggregates that exist on Open Data are published by **DOHMH**, the Department of Health, not OCME.)
- **No forensic-service, laboratory, or identification data** (Forensic Pathology, Forensic Biology/DNA, Toxicology, Anthropology, Missing Persons/NamUs).
- **No records-request, family-services-center, or FOIL data.**

## Caveat on the one dataset

`8r6c-ydwk` is a shared MMR reporting artifact, not an OCME-owned casework release. The dataset's own description points readers to the Mayor's Office of Operations MMR datasets for later years. Treat it as a **performance-indicator** record ([schemas/monthly-indicator.json](schemas/monthly-indicator.json)), not as death-investigation data. See [crosswalk.md](crosswalk.md).
