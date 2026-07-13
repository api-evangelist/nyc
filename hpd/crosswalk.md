# Crosswalk — Website Fruit ↔ APIs ↔ NYC Open Data (HPD)

Maps the low-hanging fruit on HPD's surfaces (agency site, HPD Online, Housing Connect) to (a) the **existing APIs** (the private `hpdonline.api` backend, GeoSearch) and (b) the **47 HPD datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-hpd.json](opendata-hpd.json).

## The reframe — fourth distinct pattern

- **Parks:** data-rich HTML, machine-readable twins on Open Data, legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** data already has three APIs (vendor Legistar, WP REST, SODA), none owned/coherent → *consolidate + own.*
- **HPD:** the city has **already built a modern, owned REST API** (`hpdonline.api/1.0`, behind a WSO2 gateway) — but it's **private, single-purpose, and undocumented**, while the public surface is 47 flattened Open Data snapshots and the lottery is a closed silo → **expose.**

HPD is the least about *building* an API and the most about **publishing the one that already exists** as an owned, documented, agent-native contract — and connecting the transactional lottery workflow. A tenant or agent asking "does my building have open C-class violations, who owns it, and is it in litigation?" today must stitch the private HPD Online SPA against several flattened Open Data snapshots.

Coverage: ✅ strong twin/API · 🟡 partial · ❌ gap.

## Entity crosswalk

| Entity | Surface | HPD Online backend API | Open Data | Cov. |
|---|---|---|---|---|
| `Building` | HPD Online lookup | buildings (private) | Buildings Subject to HPD Jurisdiction (`kj4p-ruqc`, 23c) | ✅ |
| `HousingMaintenanceViolation` | HPD Online → Violations | violations (private) | HMC Violations (`wvxf-dwi5`, 41c — flagship, 215k views) | ✅ |
| `Complaint` (+ problems) | HPD Online → Complaints | complaints (private) | Complaints & Problems (`ygpa-z7cr`, 33c) | ✅ |
| `Registration` (+ contacts) | HPD Online → Registration | registration (private) | Multiple Dwelling Registrations (`tesw-yqqr`, 16c) + Registration Contacts (`feu5-w2e2`, 15c) | ✅ |
| `LitigationCase` | HPD Online → Litigation | litigation (private) | Housing Litigations (`59kj-x8nc`, 24c) | ✅ |
| `AffordableHousingProject` | HPD site / annual report | — | Production by Building (`hg8x-zxpr`, 41c) + by Project (`hq68-rnsi`, 19c) | ✅ |
| Vacate / Repair orders | HPD Online → Charges | vacate (private) | Order to Repair/Vacate Orders (`tb8q-a3ar`, 20c) | ✅ |
| Charges (OMO/HWO/Fee) | HPD Online → Charges | charges (private) | OMO (`mdbu-nrqn`), HWO (`sbnd-xujn`), Fee (`cp6j-7bjj`) | ✅ |
| Bedbug report | HPD Online → Bedbug | bedbug (private) | Bedbug Reporting (`wz6d-d3jb`, 21c) | ✅ |
| Enforcement programs | HPD site | — | AEP (`hcir-3275`), Underlying Conditions (`xpbf-ithr`), Heat Sensor (`h4mf-f24e`), CONH (`bzxi-2tsw`) | ✅ |
| Local Law 44 (financed projects) | HPD site | — | 14-dataset LL44 family (`hu6m-9cfi`, `ucdy-byxd`, `9s68-zggy`…) | ✅ |
| Advertised lottery (read) | Housing Connect | — | Advertised Lotteries by Building (`nibs-na6y`) / by Lottery (`vy5i-a666`) | 🟡 read-only twin |
| `HousingLotteryApplication` | Housing Connect apply flow | — (UI only) | — | ❌ **net-new write** |

## The exposure problem, concretely

| Source | Strength | Weakness |
|---|---|---|
| **HPD Online backend** (`hpdonline.api/1.0`) | Modern, owned, versioned REST API; the live record; already behind a WSO2 gateway with GeoSearch | Private, undocumented, single-purpose (feeds one SPA); no public/agent contract |
| **Open Data (SODA)** | Open; 47 datasets; heavily used; per-column schemas | Flattened periodic snapshots; two descriptions of the same data; not the live record |
| **Housing Connect** | The city's affordable-housing lottery of record | Closed transactional silo; UI-only; no application API (only read-only advertised-lottery twins) |

## Implications for the API-first + MCP proposal

1. **Expose the backend.** Publish `hpdonline.api` as the owned, documented [OpenAPI](openapi/hpd.yaml) contract — one resource model for buildings, violations, complaints, registrations, litigation, affordable housing.
2. **Unify the two descriptions.** Front the live backend and reconcile the 47 Open Data snapshots to the same schemas/keys (`buildingId`, `registrationId`, `bbl`, `bin`) so consumers learn one model.
3. **Open the lottery.** Add lottery search (Open Data twins already exist) and the net-new **`apply_to_lottery`** write; also expose **`file_complaint`** so maintenance complaints have an API beyond 311.
4. **MCP server** so an agent can answer "what's the condition and ownership record for this building, and can you help me apply to this lottery?" in one place.
