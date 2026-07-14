# Crosswalk — Website Fruit ↔ APIs ↔ NYC Open Data (Queens DA)

Maps the low-hanging fruit on **queensda.org** to (a) the **APIs actually present** (the accidental WordPress REST API; FacetWP) and (b) **NYC Open Data** — which, for a District Attorney, has **nothing**. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-queensda.json](opendata-queensda.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, every transaction locked in an Oracle Siebel CRM → *unlock the service layer.*
- **Queens DA:** prolific narrative on modern WordPress that is **already a machine-readable API by accident**, with **zero open data** and prosecution facts only as prose → **structure it into a designed, shared contract.**

Queens DA inverts NYCHA. NYCHA's data was open but its service layer was locked; Queens DA's "service layer" (the WordPress REST API) is wide open, but the *data has no structure* — press releases are HTML, cases are just category tags, and the one structured dataset (cold cases) is encoded in post titles. A resident or agent asking "which unidentified persons were found in Queens?" or "how many indictments this quarter?" can reach the bytes but not the answer.

Coverage: ✅ structured + queryable · 🟡 present but unstructured (prose/tags) · ❌ gap (no surface at all).

## Entity crosswalk

| Entity | Website | API today | NYC Open Data | Cov. |
|---|---|---|---|---|
| `PressRelease` | `/category/press-releases/` | WordPress REST (accidental) | — (none) | 🟡 readable JSON, but HTML body, no contract |
| `Case` (public record) | `/upcoming-cases/`, lifecycle categories | WordPress REST (category tags only) | — (none) | 🟡 prose tagged by category; no structured charges/disposition |
| `ColdCase` (NamUs) | `/category/cold-cases/` | WordPress REST (title-encoded) | — (none) | 🟡 structured data trapped in post titles |
| `Program` | `/special-initiatives/`, `/community-partnerships/` | WordPress REST (pages) | — (none) | 🟡 bespoke pages, no common shape |
| `CommunityResource` | `/resources/` | WordPress REST (page prose) | — (none) | 🟡 prose links (FOIL, property release, CIU, helplines) |
| `VictimService` | `/resources/` | — | — (none) | ❌ no directory, prose only |
| **`TipSubmission`** (tip / lead / FOIL) | `/contact-us/` | **phone / static page only** | — (none) | ❌ **net-new — no inbound API** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **WordPress REST API (`wp-json/wp/v2`)** | Live, fully open, machine-readable; 1,557 posts + 60 pages queryable as JSON right now | Accidental and uncontracted; models blog posts not prosecutions; bodies are HTML; cold-case facts live in titles; no write surface; could close at any time |
| **NYC Open Data (Socrata)** | — | **Does not exist for a DA** — zero datasets; DAs don't publish here |
| **FOIL** | The formal records path | Manual, human-mediated, no API, slow |

## Implications for the API-first + MCP proposal

1. **Design a contract over the accidental API.** Map WordPress posts → `PressRelease`, lifecycle categories → `Case`, cold-case posts → `ColdCase`, pages → `Program`/`CommunityResource`, behind one owned [OpenAPI](openapi/queensda.yaml) — so consumers learn a District Attorney's model, not WordPress's.
2. **Recover the structured data.** Parse the NamUs ID, sex, age range, and date/location out of cold-case titles into [cold-case.json](schemas/cold-case.json) — the single highest-value read for families, journalists, and investigators.
3. **Add the one net-new write workflow** — `submit_tip` (a tip, cold-case lead, case inquiry, or FOIL request), anonymous-capable for tips, contact-required for FOIL.
4. **Keep it public-record only.** `Case` carries no sealed, non-public, or victim-identifying data; `VictimService` describes services, not people.
5. **Share one API across five DAs.** Manhattan, Brooklyn, Bronx, and Staten Island run the same functions on similar WordPress stacks. The fruit is **one shared five-borough DA API** and an [MCP layer](mcp/queensda-mcp.json), so an agent can answer "which unidentified persons were found in Queens?", "how many indictments did the office announce this quarter?", and "submit this anonymous tip."
