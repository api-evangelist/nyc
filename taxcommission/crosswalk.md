# Crosswalk — Website/Filing Fruit ↔ APIs ↔ NYC Open Data (Tax Commission)

Maps the low-hanging fruit on **nyc.gov/site/taxcommission** and the **online filing system** to (a) the **existing APIs** (Socrata SODA; the filing portal) and (b) the **2 Open Data assets** covering the Tax Commission (published under the OATA label). Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-taxcommission.json](opendata-taxcommission.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, every resident transaction locked in a vendor CRM → *unlock the service layer.*
- **Tax Commission:** a quasi-judicial appeals body whose intake is **PDF forms + a browser-only online filing system**, publishing only a **thin trail of outcomes** → **digitize the appeal.**

The Tax Commission is unusual on two axes at once. First, its **open data is thin and outcome-only** — two datasets, both showing what already happened (reductions granted; court petitions filed), neither describing the appeal process. Second, the **core transaction is entirely off-line-ish**: filing an Application for Correction means PDF forms (TC101/TC108/TC109/TC106…) and a browser-only filing screen, on a hard March 15/16 deadline with a $175 fee at $2M+ assessed value. An owner or agent asking "what's the status of my appeal, and what did the Commission offer?" has no API to call.

Coverage: ✅ open twin · 🟡 partial/aggregate · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Filing | API today | Open Data | Cov. |
|---|---|---|---|---|
| `AssessmentAction` | `/reports` | SODA | Assessment Actions (`4nft-bihw`, 8c) — OATA label | ✅ |
| `Article7Petition` | — | SODA | Open Article 7 Petitions (`aht6-vxai`, 10c) — OATA label | ✅ |
| `Property` (tax lot / BBL) | how-to-appeal | **none** (DOF sets value) | — (fields inside `4nft-bihw` only) | 🟡 partial |
| `Representative` (attorney/agent) | application forms | **none** | attorney name/id in `aht6-vxai` only | 🟡 partial |
| `Determination` (offer / hearing result) | online filing system | **filing UI only** | aggregate only (`4nft-bihw`) | 🟡 aggregate |
| **`AssessmentAppeal`** (Application for Correction) | online filing system + PDF forms | **PDF / UI only** | — | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (2 datasets)** | Open, machine-readable; the granted reductions and the Article 7 court petitions | Outcome-only; thin (8 + 10 columns); filed under the OATA label, not a Tax Commission label; nothing about live appeals |
| **Online filing system + PDF forms** | The real transaction system — file the Application for Correction, income & expense, track the determination | Browser-only; PDF-form based; no API, no OpenAPI, no JSON; not agent-accessible; hard deadline and a $175 fee gate |

## Implications for the API-first + MCP proposal

1. **Publish the open outcome data as one clean resource model.** Assessment Actions and Article 7 petitions behind one owned Tax Commission contract ([OpenAPI](openapi/taxcommission.yaml)) — under a Tax-Commission-owned surface, not buried under the OATA label.
2. **Digitize the appeal.** Give the core transaction — filing an Application for Correction and tracking its **determination** — a machine-readable, agent-native contract instead of PDF forms and a browser-only screen.
3. **Add the one net-new write workflow** — `file_appeal` (create an assessment appeal), carrying the claim type, income & expense figures, representative, the $175 fee at $2M+ assessed value, and the TC309 certification required at $5.4M+.
4. **Keep the DOF / Tax Commission line explicit.** DOF **sets** the assessment (Notice of Property Value); the Tax Commission **hears** the appeal. The API models the appeal, and points at DOF for the underlying assessment.
5. **MCP server** so an agent can answer "what reductions has the Commission granted on Class 2 property in Brooklyn?", "are there open Article 7 petitions on this lot?", and — the point — "file an appeal of my tentative assessment and tell me what they offered."
