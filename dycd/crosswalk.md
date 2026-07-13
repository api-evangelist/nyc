# Crosswalk — Website/Finder Fruit ↔ APIs ↔ NYC Open Data (DYCD)

Maps the low-hanging fruit on **nyc.gov/site/dycd**, the **DiscoverDYCD** program finder, and the **DYCD Connect** portal to (a) the **existing APIs** (Socrata SODA; the private DiscoverDYCD `/api/`) and (b) the **15 DYCD datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-dycd.json](opendata-dycd.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, every transaction locked in an Oracle Siebel CRM → *unlock the service layer.*
- **DYCD:** the supply data is **wide open** (15 Socrata datasets) **and** DYCD **already built a public program finder** (DiscoverDYCD) — but the finder is an app with a private `/api/`, and there is no way to apply → **surface the finder (and add the apply write).**

DYCD is a different animal: a **funder/intermediary** that contracts hundreds of CBOs to run programs at physical sites. Its supply chain — sites, providers, contracts, service areas, aggregate demographics — is all machine-readable on Open Data. And unlike DOE, DYCD didn't rent its finder: it built DiscoverDYCD itself. The gap is that the finder was built as a **human-only app over a private backend**, and the thing a young person actually needs to *do* — **apply to a program** (SYEP, COMPASS, Beacon) — has no API at all.

Coverage: ✅ strong open twin · 🟡 partial/aggregate/app-only · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Finder | API today | Open Data | Cov. |
|---|---|---|---|---|
| `Program` (offering) | DiscoverDYCD finder | **private `/api/` only** | taxonomy echoed on Program Sites; no catalog dataset | 🟡 app-only |
| `ProgramSite` | finder + `/services` | SODA | DYCD Program Sites (`ebkm-iyma`, 34c); Evaluation & Monitoring (`9f5n-qdib`) | ✅ |
| `Provider` (CBO) | provider resources | SODA | DYCD Contractors (`75e9-fg2t`); Provider on Sites/Contracts | ✅ |
| `Contract` | — | SODA | DYCD Contracts (`graj-69em`, 15c) | ✅ |
| `ServiceArea` (NDA) | — | SODA | Neighborhood Development Areas (`vd7c-qjsx`) + map (`p57r-4v4f`) | ✅ |
| `ParticipantDemographics` (Enrollment) | — | SODA | Participant Demographics (`k9kq-67vm`, 52c) — **aggregate only**; Youth Count; RHY reporting | 🟡 aggregate |
| SYEP for NYCHA residents (LL163) | — | SODA | by borough (`x4x8-m3ds`), development (`acek-a5z6`), council (`73rz-5b7x`) | ✅ |
| **`ProgramApplication`** (apply — SYEP/COMPASS) | DYCD Connect / seasonal form | **app / form only** | — | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (15 datasets)** | Open, machine-readable; strong on program sites, providers, contracts, NDAs, aggregate demographics | Supply-side only; no catalog of the offerings themselves; static snapshots; nothing about applying |
| **DiscoverDYCD finder** | A real, DYCD-owned program finder with maps and taxonomy | Angular UI over a **private, undocumented `/api/`**; not agent-accessible; no OpenAPI |
| **DYCD Connect portal** | The real application/enrollment and provider-contract system | Login-walled; no public API; applying to a program has no machine-readable contract |

## Implications for the API-first + MCP proposal

1. **Surface the finder as an owned API.** Expose the same program-discovery capability DiscoverDYCD already has — `find_programs`, `find_program_sites` — as a documented, agent-callable contract ([OpenAPI](openapi/dycd.yaml)) instead of a private `/api/`.
2. **Publish the open supply data as one clean resource model.** Programs, sites, providers, contracts, and NDAs behind one owned DYCD contract — so consumers learn one model, not 15 Socrata IDs.
3. **Add the one net-new write workflow** — `apply_to_program` (`POST /applications`): submit a program application (e.g. SYEP), with a guardian block for minors and the Local Law 163 NYCHA set-aside flag.
4. **Keep participants private.** Demographic data stays aggregate-only; the API never exposes an individual participant.
5. **MCP server** so an agent can answer "what summer programs can a 15-year-old in the Bronx apply to?", "which providers run Beacon programs in my council district?", and — the point — "apply me to SYEP and tell me the status."
