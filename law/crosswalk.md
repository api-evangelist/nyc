# Crosswalk — Website Fruit ↔ APIs ↔ NYC Open Data (NYC Law Department)

Maps the low-hanging fruit on **nyc.gov/site/law** to (a) the **existing APIs** (Socrata SODA) and (b) the **7 datasets** on NYC Open Data under `Law Department (LAW)`. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-law.json](opendata-law.json).

## The reframe — a fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, every transaction locked in a vendor CRM → *unlock the service layer.*
- **Law:** an **agency-facing legal office** with almost no citizen transactions — thin annual data, no service layer, and the claims dollars that matter owned by the **Comptroller** → **catalog what little exists and route claims to the right agency.**

Law inverts the usual assessment. There is no trapped data to liberate and no service layer to unlock — there is *barely any public surface at all*. Seven small, manually-updated annual datasets, a content-only site, and the single citizen-initiated transaction (applying for an internship) handled by email. And the dataset a user most often wants from "the City's lawyers" — **claims and settlements** — isn't Law's to give; it is the **Office of the Comptroller's** (`ex6k-ym48`).

Coverage: ✅ strong open twin · 🟡 partial/thin · ❌ gap (no API) · ↪ owned by another agency.

## Entity crosswalk

| Entity | Website | API today | Open Data | Cov. |
|---|---|---|---|---|
| `LegalCase` (litigation index) | — | SODA | Case-Related Information About Civil Litigation (`pjgc-h7uv`, 17c) | 🟡 index only |
| Claims & settlement dollars | — | SODA | Claims Report (`ex6k-ym48`) — **Comptroller, not Law** | ↪ other agency |
| `LegalDivision` | `/divisions/legal-divisions` | SODA | LAW Divisions (`4se9-mk53`, 2c) | ✅ |
| `Publication` (press/speech/column) | `/news` | SODA | Press Releases (`kewa-q4dq`), Speeches (`g7ir-4pf8`), Columns (`d84z-5kap`) | ✅ |
| `MwbeStatistic` | `/public-resources/mwbe-opportunity` | SODA | M/WBE Statistics (`svyi-maaj`, 7c) | ✅ |
| `PublicServiceProgram` | — | SODA | LAW Public Service Program (`yk6f-pa7p`, 1c) | ✅ thin |
| **`LawInternshipApplication`** (apply) | `/careers/lawyers-law-students` | **email/PDF only** | — | ❌ **net-new** |

## The scarcity, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (7 datasets)** | Open, machine-readable; covers divisions, publications, M/WBE, pro bono, and a litigation index | All 'No' automation / annual snapshots; several are 1–4 columns; no claims/settlement dollars |
| **Comptroller claims dataset (`ex6k-ym48`)** | The real claims-and-settlements ledger | Owned by a *different* agency — not discoverable from the Law Department's own surface |
| **Law Department site** | Clear content on divisions, careers, public resources | Content only; no API, no application system, no service layer |

## Implications for the API-first + MCP proposal

1. **Catalog the seven datasets as one clean resource model.** Cases, divisions, publications, M/WBE, and the Public Service Program behind one owned Law contract ([OpenAPI](openapi/law.yaml)) — so consumers learn one model, not seven Socrata IDs.
2. **Route claims questions to the Comptroller.** The contract and [MCP instructions](mcp/law-mcp.json) explicitly note that claims filed and settlement dollars live in `ex6k-ym48` (Comptroller), not in Law's case index.
3. **Add the one net-new write workflow** — `submit_internship_application` (apply to the legal internship / fellowship program), the single transaction the public initiates with this agency, today handled only by email/PDF.
4. **MCP server** so an agent can answer "which divisions handle tax matters?", "what were the Law Department's M/WBE shares?", "find the Corporation Counsel's recent speeches", and — the net-new bit — "apply me to the summer law intern program."
