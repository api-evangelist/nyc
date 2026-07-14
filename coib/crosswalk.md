# Crosswalk — Website/Filing Fruit ↔ APIs ↔ NYC Open Data (COIB)

Maps the low-hanging fruit on **nyc.gov/site/coib** and the **Annual Financial Disclosure filing website** to (a) the **existing APIs** (Socrata SODA; the filing website) and (b) the **8 COIB datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-coib.json](opendata-coib.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, every resident transaction locked in a vendor CRM → *unlock the service layer.*
- **COIB:** the transparency **outputs are already open** (8 Socrata datasets), but the core compliance **input — the annual financial disclosure filing — is locked inside a login-only filing website** with no API → **attest** (give the filing/attestation layer an owned API).

COIB is a transparency-out / attestation-in agency, and that direction is the finding. Enforcement dispositions, donations, policymaker lists, and legal defense trust transactions are all machine-readable on Open Data — the agency publishes generously on the way *out*. But the thing every senior public servant *does* on the way *in* — **file and attest an annual financial disclosure report** — lives only behind a login-gated filing website. A filer or agent asking "is my disclosure filed?" or "submit my annual report" has no API to call.

Coverage: ✅ strong open twin · 🟡 partial/reference · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Filing | API today | Open Data | Cov. |
|---|---|---|---|---|
| `EnforcementDisposition` | `/public-documents` | SODA | Enforcement Fines (`p39r-nm7f`, 13c) | ✅ |
| `AgencyDonation` | `/the-law` | SODA | Donations to NFPs (`dx8z-6nev`); Received by Agencies (`aqs7-v55z`); Official Fundraising (`basd-2jwn`) | ✅ |
| `Policymaker` | `/annual-disclosure` | SODA | Policymakers List (`wf8t-6cqt`, 7c) | ✅ |
| `LegalDefenseTrustTransaction` | `/public-documents` | SODA | LDT Expenditures (`mhyv-6iza`, 20c); Donations (`jsiv-zh9r`); Refunded (`t3pj-3dgu`) | ✅ |
| `AdvisoryOpinion` | `/public-documents` | **PDF only** | — | 🟡 reference |
| Ethics training | `/the-law/get-legal-advice` | **Training site only** | — | ❌ gap |
| Waiver / legal advice | `/contact/get-a-waiver` | **Web/email form only** | — | ❌ gap |
| **`FinancialDisclosureFiling`** (file annual disclosure) | Annual Financial Disclosure filing website | **Login-only web form** | — | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (8 datasets)** | Open, machine-readable; strong on enforcement, donations, policymakers, and legal defense trusts | Transparency outputs only; nothing about the disclosure filing itself, advisory opinions, or training |
| **Annual Disclosure filing website** | The real compliance system — every senior public servant files/attests here each spring | Login-gated web form; no API, no OpenAPI, no JSON; not agent-accessible; PDF-by-email is the only fallback |

## Implications for the API-first + MCP proposal

1. **Publish the open transparency data as one clean resource model.** Enforcement dispositions, donations, policymakers, and legal defense trusts behind one owned COIB contract ([OpenAPI](openapi/coib.yaml)) — so consumers learn one model, not 8 Socrata IDs.
2. **Unlock the attestation layer.** Front the filing website with an API so the core compliance transaction — filing and tracking a **financial disclosure report** — has a machine-readable, agent-native contract.
3. **Add the one net-new write workflow** — `file_financial_disclosure` (submit an annual disclosure report), with a filer attestation (`attestation.certified`) and the correct filer-type question set.
4. **Keep filed interests confidential.** The API exposes only what COIB already discloses publicly (elected officials); other filers' financial interests stay confidential by design.
5. **MCP server** so an agent can answer "which enforcement cases named my agency and what were the fines?", "which non-profits affiliated with elected officials received donations last year?", and — the point — "is my annual disclosure filed, and if not, file it."
