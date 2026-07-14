# Crosswalk — Website/Portal Fruit ↔ APIs ↔ NYC Open Data (CCRB)

Maps the low-hanging fruit on **nyc.gov/site/ccrb** and the complaint intake/status apps to (a) the **existing APIs** (Socrata SODA; the online form; the status-lookup app) and (b) the **4 CCRB datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-ccrb.json](opendata-ccrb.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data open, every resident transaction locked in a vendor CRM → *unlock the service layer.*
- **CCRB:** the accountability data is **model-grade and open** — but delivered only as **dashboards and CSV**, with **no API**, and the intake it exists for is a **web form** → **expose it as a contract.**

CCRB is the transparency inverse of the earlier problems. It is not that the data is trapped in HTML or a CRM — the officers, complaints, allegations, and penalties are all published, disaggregated, and refreshed **daily** on NYC Open Data and the Data Transparency Initiative dashboards. It is that none of it is a **queryable, agent-native API**, and the two acts a member of the public performs — **filing a complaint** and **checking its status** — are disconnected web screens with no contract at all.

Coverage: ✅ strong open twin · 🟡 partial · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / App | API today | Open Data | Cov. |
|---|---|---|---|---|
| `Complaint` | DTI complaints dashboard | SODA | Complaints Against Police Officers (`2mby-ccnw`, 14c) | ✅ |
| `Allegation` | DTI allegations dashboard | SODA | Allegations Against Police Officers (`6xgr-kwjq`, 18c) | ✅ |
| `PoliceOfficer` (subject) | DTI members-of-service dashboard | SODA | Police Officers (`2fir-qns4`, 14c) | ✅ |
| `Penalty` (discipline) | police-discipline / APU-trials pages | SODA | Penalties (`keep-pkmh`, 13c) | ✅ |
| Complaint status | Status Lookup app (`apps.nyc.gov/ccrb-status-lookup`) | **UI only** | — | 🟡 read-only screen, no API |
| **`MisconductComplaint`** (file a complaint) | Online form (`.../file-online`) + 311 + mail | **Web form only** | — | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (4 datasets)** | Open, machine-readable, **daily**-updated, disaggregated to the officer/allegation level — a police-oversight transparency model | Read-only snapshots delivered as CSV/dashboards; no query API for consumers who want live filters; nothing about intake |
| **Online form + Status Lookup** | The real intake and status surfaces the public uses | Two disconnected JavaScript screens; no API, no OpenAPI, no JSON; not agent-accessible; status can't be joined back to the record programmatically |

## Implications for the API-first + MCP proposal

1. **Publish the open accountability data as one clean, queryable resource model.** Complaints, allegations, officers, and penalties behind one owned CCRB contract ([OpenAPI](openapi/ccrb.yaml)) — so consumers learn one model keyed on `Complaint Id` and `Tax ID`, not four Socrata IDs and five dashboards.
2. **Expose the intake.** Front the online form with an API so the core civic act — **filing a misconduct complaint** — has a machine-readable, agent-native contract, and connect it to a tracked status (today a separate lookup app).
3. **Add the one net-new write workflow** — `file_misconduct_complaint` (create a MisconductComplaint), capturing FADO category, incident geography, and accused-officer identification, with anonymous filing supported.
4. **Preserve CCRB's disaggregation.** Keep officer-level `Total Complaints` / `Total Substantiated Complaints` and the CCRB-vs-NYPD disposition/penalty gap — the data that makes CCRB a transparency model — first-class in the contract.
5. **MCP server** so an agent can answer "how many substantiated force allegations came from this precinct?", "what penalty did NYPD actually impose vs. what the Board recommended?", and — the point — "help me file a complaint about what happened to me, and tell me its status."
