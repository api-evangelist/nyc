# Crosswalk — Website / App Layer ↔ APIs ↔ NYC Open Data (DOB)

Maps the low-hanging fruit for the **NYC Department of Buildings** to (a) the existing interfaces (the `aNNN-*.nyc.gov` app layer + the Open Data batch dump) and (b) the **44 DOB datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-dob.json](opendata-dob.json).

## The reframe — fourth distinct pattern

- **Parks:** data-rich HTML on a legacy CMS → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** three real-but-fragmented APIs, none owned → *consolidate + own.*
- **DOB:** a mature **transactional application layer** (BIS Web, DOB NOW, eFiling) with **no public API**, whose only external interface is a **nightly one-way Socrata batch dump** → **Transact.**

DOB is the project's proof that **the real legacy surface is the application layer, not the website.** `www.nyc.gov/site/buildings` is brochureware; the systems of record are the Akamai-gated, browser-only `a810-*` apps. Modernizing DOB is not about tidying a website — it is about putting an owned, live, two-way API in front of BIS/DOB NOW.

Coverage: ✅ strong twin/extract · 🟡 partial · ❌ gap.

## Entity crosswalk

| Entity | Where it really lives | Public API today | Open Data (nightly batch) | Cov. |
|---|---|---|---|---|
| `Building` | **BIS Web** (`a810-bisweb`) | none (browser-only) | Property Data (BIS) `e98g-f8hy` (11c) | 🟡 read-only dump |
| `JobFiling` | **BIS / DOB NOW** | none | DOB Job Application Filings `ic3t-wcy2` (95c) + DOB NOW `w9ak-ipjd` | ✅ (batch) |
| `Permit` | **BIS / DOB NOW** | none | DOB Permit Issuance `ipu4-2q9a` (60c) + DOB NOW Approved `rbx6-tga4` | ✅ (batch) |
| `Violation` (DOB) | **BIS** | none | DOB Violations `3h2n-5cm9` (18c) | ✅ (batch) |
| `Violation` (ECB) | **OATH/ECB** | none | DOB ECB Violations `6bgk-3dad` (46c) | ✅ (batch) |
| `Complaint` | **BIS** (311 intake) | none | DOB Complaints Received `eabe-havv` (15c) | ✅ (batch) |
| `CertificateOfOccupancy` | **DOB NOW / BIS** | none | DOB C of O `bs8b-p36w` (34c) + DOB NOW `pkdm-hqz6` | ✅ (batch) |
| Licensed trades (party) | **BIS / DOB NOW** | none | DOB License Info `t8hj-ruu2` (22c) | ✅ (batch) |
| `PermitApplication` (file a filing) | **DOB NOW** (`a810-dobnow`) | none (browser-only) | — | ❌ **net-new write** |

## The one-way-dump problem, concretely

| Source | Strength | Weakness |
|---|---|---|
| **BIS Web / DOB NOW / eFiling** | The authoritative, live transactional systems — jobs, permits, violations, C of O, filings | Browser-only, Akamai-gated, **no API**; write-only through a UI; not agent-accessible |
| **NYC Open Data (SODA)** | Open; 44 datasets; rich columns; the *only* machine-readable surface | **Nightly one-way batch extract** (`DOBRunDate`); read-only; up to a day stale; split across legacy vs DOB NOW twins; no way to file or check live status |

## Implications for the API-first + MCP proposal

1. **Front the app layer, not the CMS.** Publish one DOB API (this project's [OpenAPI](openapi/dob.yaml)) over BIS/DOB NOW — the `Building` (BIN/BBL) spine joining filings, permits, violations, complaints, and C of O.
2. **Make it live, not nightly.** Replace/supplement the `DOBRunDate` batch dump with a real-time read surface so consumers stop scraping stale snapshots.
3. **Unify the legacy ↔ DOB NOW twins.** Present one `JobFiling`/`Permit`/`CertificateOfOccupancy` model instead of separate BIS and DOB NOW datasets.
4. **Add the missing write workflow** — [`PermitApplication`](schemas/permit-application.json): file, patch/submit, and track a DOB NOW filing via API (`file_permit_application` / `submit_permit_application`).
5. **MCP server** so an agent can answer "what's open on this BIN, and can you file the A2 alteration for me?" — read the record and (with the user's confirmation) transact.
