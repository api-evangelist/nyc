# Low-Hanging Fruit Index — COIB

**Agency:** NYC Conflicts of Interest Board (COIB)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/coib` (Akamai + nginx + NYC.gov "Livesite" v22 + Dynatrace) and read the Annual Disclosure pages, which describe filing "**electronically through COIB's filing website**" — a login-gated electronic system with no public API. Verified the NYC Open Data agency label `Conflicts of Interest Board (COIB)` via the Socrata Discovery API and pulled all **8** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-coib.md](opendata-coib.md).

## Headline findings

1. **COIB is a transparency-out / attestation-in agency.** Its enforcement and transparency *outputs* are genuinely open (**8 NYC Open Data datasets**), but its core compliance *input* — the annual financial disclosure filing — is locked in a login-gated filing website with **no API**.
2. **The open data is real but narrow.** 8 datasets cover enforcement dispositions/fines (the most-viewed asset), donations to agencies and to elected-official-affiliated non-profits, the monthly Policymakers List, and legal defense trust donations/refunds/expenditures.
3. **The filing system is the locked layer.** "File electronically through COIB's filing website," 4-week spring window — login-only, no Open Data twin, elected officials' reports only as PDFs on request. Ethics training, waivers, and advisory opinions are likewise PDF/form-only.
4. **Filed interests stay confidential by design.** Only elected officials' reports are ever public, and only as PDFs — never as data.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a vendor-CRM service layer; **COIB = attest.** Here the transparency data is already open — the work is least about liberating datasets and most about giving the **compliance attestation layer** (above all, filing an annual financial disclosure report) an owned, agent-native API instead of a login-only web form.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Enforcement Dispositions (Fines) | `EnforcementDisposition` | SODA | ✅ Enforcement Fines (`p39r-nm7f`, 13c) |
| 2 | Agency & Affiliated-NFP Donations | `AgencyDonation` | SODA (×3) | ✅ Donations to NFPs (`dx8z-6nev`) + agency streams |
| 3 | Policymakers List | `Policymaker` | SODA | ✅ Policymakers List (`wf8t-6cqt`, 7c) |
| 4 | Legal Defense Trusts | `LegalDefenseTrustTransaction` | SODA (×3) | ✅ Expenditures (`mhyv-6iza`) + donations/refunds |
| 5 | Advisory Opinions | `AdvisoryOpinion` | PDF library | 🟡 PDF only (no data) |
| 6 | Ethics Training | — (training site) | Online training | ❌ gap (no API) |
| 7 | Waiver / legal advice | — (form) | Web/email form | ❌ gap (no API) |
| 8 | **File Annual Financial Disclosure** | `FinancialDisclosureFiling` | Filing website | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 8 COIB datasets (the one real, open API; transparency outputs only).
- **COIB Annual Financial Disclosure filing website** — login-gated e-filing, no API.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, AWS ALB, Dynatrace + mPulse RUM, Google Maps embed) — the same chassis as NYCHA's informational site.

## Reverse-engineered entities

`EnforcementDisposition` · `AgencyDonation` (three donation streams) · `Policymaker` · `LegalDefenseTrustTransaction` (donations/refunds/expenditures) · `AdvisoryOpinion` (PDF reference) · `FinancialDisclosureFiling` (net-new write; also stands in for the filing-website-locked ethics-training / waiver transactions) — join keys: **Case Number**, **Agency Name**, **Trust Name**, **Donation ID**.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (Case Number, Donation ID, Trust Name, the geography spine on LDT expenditures) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open transparency data as clean resources + the net-new `POST /financial-disclosure-filings` (file an annual disclosure) — done ([openapi/coib.yaml](openapi/coib.yaml)).
3. **MCP** artifact: `find_enforcement_dispositions`, `get_enforcement_disposition`, `find_agency_donations`, `find_policymakers`, `find_legal_defense_trust_transactions`, `find_advisory_opinions`, `list_my_financial_disclosure_filings`, `file_financial_disclosure` — done ([mcp/coib-mcp.json](mcp/coib-mcp.json)).
