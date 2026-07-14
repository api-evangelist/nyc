# Low-Hanging Fruit Index — CCRB

**Agency:** NYC Civilian Complaint Review Board (CCRB)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/ccrb` (Akamai + nginx + AWS ALB + NYC.gov "Livesite" platform + Dynatrace), the online complaint intake (`.../file-a-complaint/file-online.page`), and the **Complaint Status Lookup** app (`apps.nyc.gov/ccrb-status-lookup`). Verified the NYC Open Data agency label `Civilian Complaint Review Board (CCRB)` via the Socrata Discovery API and pulled all **4** assets with column schemas — daily-updated, automated mirrors of the CCRB Complaints Database behind the Data Transparency Initiative dashboards.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-ccrb.md](opendata-ccrb.md).

## Headline findings

1. **CCRB is a transparency model — delivered without an API.** The **Data Transparency Initiative** and **4 daily-updated Socrata datasets** publish disaggregated, officer-level misconduct data (complaints, allegations, officers, penalties). But it ships as **dashboards and CSV**, not a queryable contract.
2. **The corpus is a tight accountability model.** Keyed on **Complaint Id** and **Tax ID**: officer-level `Total`/`Substantiated` complaint counts, per-allegation **FADO** records with **CCRB-vs-NYPD** dispositions, and the **APU-vs-NYPD** penalty gap.
3. **The intake it exists for is a web form.** Filing a misconduct complaint (`.../file-online`) and checking its status (`apps.nyc.gov/ccrb-status-lookup`) are two **disconnected JavaScript screens** with no machine-readable contract.
4. **The gap is delivery, not openness.** The record is model-grade; it just is not an agent-native API, and intake is not connected to it.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a service layer locked in a vendor CRM; **CCRB = expose it as a contract.** Here the data is already open and even exemplary — the work is least about liberating datasets and most about turning dashboards-and-CSV into a **queryable, agent-native API** and giving the **act of filing a complaint** the contract it has never had.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Complaints Against Police Officers | `Complaint` | SODA + DTI dashboard | ✅ Complaints (`2mby-ccnw`, 14c) |
| 2 | Allegations Against Police Officers | `Allegation` | SODA + DTI dashboard | ✅ Allegations (`6xgr-kwjq`, 18c) |
| 3 | Police Officers (members of service) | `PoliceOfficer` | SODA + DTI dashboard | ✅ Police Officers (`2fir-qns4`, 14c) |
| 4 | Penalties (discipline outcomes) | `Penalty` | SODA + discipline pages | ✅ Penalties (`keep-pkmh`, 13c) |
| 5 | Data Transparency Initiative dashboards | `Complaint` | DTI (HTML/JS) | 🟡 same corpus, not an API |
| 6 | Check complaint status | `MisconductComplaint` | Status Lookup app | ❌ gap (read-only UI, no API) |
| 7 | **File a misconduct complaint online** | `MisconductComplaint` | Online form + 311 + mail | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 4 CCRB datasets, updated daily (the one real, open API; read side of the CCRB Complaints Database).
- **Online complaint form + Complaint Status Lookup** — two disconnected NYC.gov/`apps.nyc.gov` screens; no API.
- Platform: informational site + DTI dashboards on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, AWS ALB, Dynatrace RUM) — the same chassis seen at NYCHA.

## Reverse-engineered entities

`Complaint` · `Allegation` (FADO; CCRB-vs-NYPD disposition) · `PoliceOfficer` (accused/subject; Total & Substantiated counts) · `Penalty` (APU trial track + NYPD final penalty) · `MisconductComplaint` (net-new write; the intake counterpart to the closed-case Complaint) — join keys: **Complaint Id**, **Tax ID**.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (Complaint Id, Tax ID, FADO Type, the CCRB/NYPD disposition pair, APU/NYPD penalty fields) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open accountability data as clean resources + the net-new `POST /complaints/file` (file a MisconductComplaint) with a tracked status — done ([openapi/ccrb.yaml](openapi/ccrb.yaml)).
3. **MCP** artifact: `find_complaints`, `get_complaint`, `get_complaint_allegations`, `find_allegations`, `find_officers`, `get_officer`, `find_penalties`, `file_misconduct_complaint`, `check_complaint_status` — done ([mcp/ccrb-mcp.json](mcp/ccrb-mcp.json)).
