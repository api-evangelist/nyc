# NYC Open Data — CCRB Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Civilian Complaint Review Board (CCRB)"** (verified via the Socrata Discovery API, 2026-07-13). 4 assets, sorted by lifetime page views. Machine-readable: [opendata-ccrb.json](opendata-ccrb.json).

The shape of the corpus is the story: it is a **single, tightly-normalized accountability model** — one row-per-officer summary, one row-per-complaint, one row-per-allegation, and one row-per-penalty — all keyed on **Complaint Id** and **Tax ID**, all classified *Public Safety*, all **updated daily and automated**, and all sourced from the "CCRB Complaints Database". These four datasets are the open-data face of the **Data Transparency Initiative** (DTI) dashboards on `nyc.gov/site/ccrb`. There is **no dataset for the intake side** — filing a complaint of misconduct lives only in the online web form and a status-lookup app. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 15,373 | dataset | `2fir-qns4` | Civilian Complaint Review Board: Police Officers | 14 |
| 12,292 | dataset | `6xgr-kwjq` | Civilian Complaint Review Board: Allegations Against Police Officers | 18 |
| 11,200 | dataset | `2mby-ccnw` | Civilian Complaint Review Board: Complaints Against Police Officers | 14 |
| 4,704 | dataset | `keep-pkmh` | Civilian Complaint Review Board: Penalties | 13 |

All four are tagged `police` · `nypd` · `allegations` · `discipline` · `policing`, category **Public Safety**, update frequency **Daily** (automated), collection **CCRB Complaints Database**, made public **12/06/2022**.

## The four objects

- **Police Officers (`2fir-qns4`, 14c) — the accused-officer roll.** `Tax ID`, `Shield No`, name, `Current Rank`/`Current Command`, `Officer Race`/`Gender`, `Active Per Last Reported Status`, and the two counts that make CCRB's transparency distinctive: **`Total Complaints`** and **`Total Substantiated Complaints`** per officer.
- **Allegations (`6xgr-kwjq`, 18c) — the finest grain.** One row per allegation against one officer: `FADO Type` (Force / Abuse of Authority / Discourtesy / Offensive Language), specific `Allegation`, `CCRB Investigations Division Recommendation`, `CCRB Allegation Disposition` vs `NYPD Allegation Disposition`, officer rank/command/`Days On Force At Incident`, and victim/alleged-victim `Race / Ethnicity`, `Gender`, and `Age Range At Incident`. Joins on `Complaint Id` and `Tax ID`.
- **Complaints (`2mby-ccnw`, 14c) — the incident.** One row per complaint: `Complaint Id`, `CCRB Received Date`, `Close Date`, `Incident Date`/`Hour`, `CCRB Complaint Disposition`, `Reason for Police Contact`, `Outcome Of Police Encounter`, `Borough`/`Precinct`/`Location Type Of Incident`, and the evidence flags **`Video Evidence`** and **`BWC Evidence`** (body-worn camera).
- **Penalties (`keep-pkmh`, 13c) — the discipline outcome.** The APU (Administrative Prosecution Unit) trial track and the NYPD's final call: `Board Discipline Recommendation`, `Officer is_APU`, `APU Case Status`, `APU CCRB Trial Recommended Penalty`, `APU Trial Commissioner Recommended Penalty`, `APU Plea Agreed Penalty`, and **`NYPD Officer Penalty`** — the gap between what CCRB recommended and what NYPD imposed.

## What is *not* here

There is no intake dataset — no "complaints received today", no per-submission status feed. The act the agency exists for, **filing a misconduct complaint**, has no Open Data twin; it is an online web form (`.../file-online`), a 311 call, mail, or in person, with status checked separately at `apps.nyc.gov/ccrb-status-lookup`. That is the net-new write surface. See [apis-observed.md](apis-observed.md).
