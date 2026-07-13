# Crosswalk — Website Fruit ↔ APIs ↔ NYC Open Data (DOHMH)

Maps the low-hanging fruit on **nyc.gov/site/doh** to (a) the **existing systems/APIs** (ABC Eats, eVital, Accela, 311) and (b) the **81 DOHMH datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-dohmh.json](opendata-dohmh.json).

## The reframe — fourth distinct pattern

- **Parks:** data-rich HTML, machine-readable twins on Open Data, legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs (Legistar, WP REST, SODA), none owned/coherent → *consolidate + own.*
- **DOHMH:** the data is **already open** (81 datasets, incl. the most-viewed dataset in the city) — the gap is **agent-native, transactional services** → **transact.**

DOHMH is the least about *liberating* data and the most about **acting on it**. A resident or agent who wants to "check this restaurant's grade, see if there are rat signs on my block, then order my birth certificate" can read the first two from open data but hits a wall on the third: a paid transaction locked inside eVital/VitalChek with no API.

Coverage: ✅ strong twin/API · 🟡 partial · ❌ gap.

## Entity crosswalk

| Entity | Website / System | Existing API | Open Data | Cov. |
|---|---|---|---|---|
| `FoodEstablishment` | ABC Eats grade lookup (SPA) | Private ABC Eats Web API | Restaurant Inspection Results (`43nn-pn8j`, 31c) | ✅ |
| `Inspection` | ABC Eats detail | Private ABC Eats Web API | Restaurant Inspection Results (`43nn-pn8j`) | ✅ |
| `RodentInspection` | — | — | Rodent Inspection (`p937-wjvj`, 34c) | ✅ |
| `ChildcareCenter` | daycare lookup | — | Childcare Center Inspections (`dsg6-ifza`, 34c) | ✅ |
| `HealthFacility` | NYC Health Map / allclinics | NYC Health Map (undoc.) | — | 🟡 finder only |
| `EnvironmentalComplaint` | 311 intake | 311 (Salesforce) | Indoor Environmental Complaints (`9jgj-bmct`, 19c) | ✅ read / 🟡 intake |
| Health permit / license | Accela Citizen Access | Accela COTS (no open API) | — | 🟡 COTS-only |
| `VitalRecordRequest` | birth-death-records page | eVital VRRTS + VitalChek (no API) | — | ❌ **net-new** |

## The data/transaction split, concretely

| Source | Strength | Weakness |
|---|---|---|
| **NYC Open Data (SODA)** | 81 open datasets; the city's most-viewed dataset (restaurant inspections); full geography spine on rows | Read-only snapshots; no way to *act* (order, apply, file) |
| **ABC Eats** | Live, public restaurant grades | Private/undocumented API behind a JS SPA; duplicates the open dataset |
| **eVital VRRTS + VitalChek** | The real vital-records transaction | Session-gated .NET app + third-party vendor; no open, agent-native API |
| **Accela Citizen Access** | Working permit/license workflow | Vendor COTS; no public API; not resource-oriented |

## Reconciling schemas with real Open Data columns

The [JSON Schemas](schemas/) are reconciled to real Socrata column names:

- **[food-establishment.json](schemas/food-establishment.json)** / **[inspection.json](schemas/inspection.json)** ← `43nn-pn8j`: `camis`, `dba`, `boro`, `cuisine_description`, `inspection_date`, `action`, `violation_code`, `critical_flag`, `score`, `grade`, `grade_date`, plus the geography spine (`community_board`, `council_district`, `census_tract`, `nta`, `bbl`, `bin`, `latitude`, `longitude`). The one-row-per-violation grain is rolled up into `Inspection.violations[]`.
- **[rodent-inspection.json](schemas/rodent-inspection.json)** ← `p937-wjvj`: `job_id`, `inspection_type`, `result`, `inspection_date`, `approved_date`, `bbl`, address + geo spine.
- **[childcare-center.json](schemas/childcare-center.json)** ← `dsg6-ifza`: `dc_id`, `centername`, `permitnumber`, `permitexp`, `maximumcapacity`, `programtype`, `violationratepercent`, `inspectiondate`.
- **[environmental-complaint.json](schemas/environmental-complaint.json)** ← `9jgj-bmct`: `complaint_number`, `complaint_type_311`, `descriptor_1_311`, `complaint_status`, `date_received`, geo spine.
- **[_common.json](schemas/_common.json)** ← the recurring NYC geography spine (`communityBoard`, `councilDistrict`, `censusTract`, `nta`, `bbl`, `bin`, `Coordinates`) + `Address` + `Borough`.

## Implications for the API-first + MCP proposal

1. **Front the open data with a resource model.** Publish one DOHMH API ([OpenAPI](openapi/dohmh.yaml)) so consumers read `FoodEstablishment` / `Inspection` / `RodentInspection` / `ChildcareCenter` / `EnvironmentalComplaint` as resources rather than raw SODA columns.
2. **Promote the ABC Eats backend to a documented API** — the grade data already flows through a private API; publish it.
3. **Add the missing transaction** — `createVitalRecordRequest` (order a birth/death certificate), the one net-new write surface, plus tracking.
4. **Close the finder gap** — publish `HealthFacility` (clinics/service sites) as a resource, not just a map.
5. **MCP server** so an agent can answer "what's this restaurant's grade / are there rat signs here / where's the nearest sexual-health clinic / order my birth certificate" from one place.
