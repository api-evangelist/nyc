# Crosswalk — Website/System Fruit ↔ APIs ↔ NYC Open Data (MOER/OER)

Maps the low-hanging fruit on **nyc.gov/site/oer**, the **SPEED** map, and OER's remedial workflow to (a) the **existing APIs** (Socrata SODA; the CARTO-backed SPEED map; the login-walled EPIC portal) and (b) the **10 OER datasets** on NYC Open Data (plus the DCP-owned E-Designation assets). Built 2026-07-16 from [fruit.json](fruit.json) × [opendata-moer.json](opendata-moer.json).

## The reframe

- **DDC:** a vendor-facing agency whose own data is thin and historical and whose transactions all run on citywide systems it doesn't own → *surface.*
- **OER:** an agency whose **reference data is open and partly live** — a **Daily** cleanup feed, a public SPEED map — but whose **multi-step regulatory workflow is trapped** inside its own login-walled legacy portal (EPIC), and whose authoritative **(E)-designation inventory is published by another agency (DCP)** → **expose** the site data as one clean, BBL-keyed API *and* expose the workflow (status + the net-new request) as an owned contract.

OER inverts the DDC data problem. The rows are good; what is missing is an **API over them** and, above all, an API over the **process**: the remedial phases, the determinations OER issues (Notice to Proceed, Notice of Satisfaction), and the intake that starts a cleanup. A developer or agent asking "does this Brooklyn lot carry an E-designation, is its cleanup far enough along for a building permit, and how do I request a Notice to Proceed?" has open data for the first clause, a DCP dataset for the second, and **nothing at all** for the third and fourth.

Coverage: ✅ open twin · 🟡 partial/derived/not-OER-owned · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / System | API today | Open Data | Cov. |
|---|---|---|---|---|
| `EnvironmentalSite` | SPEED / `/remediation` | SODA + SPEED (CARTO) | **OER Cleanup Sites** (`3279-pp7v`, 18c, **Daily**) | ✅ live, BBL-keyed |
| `EDesignation` | `/remediation/e-designation` | **DCP** SODA only | **DCP**: `hxm3-23vy`, `mzjp-98aw`, `jsrs-ggnx` | 🟡 not OER-owned |
| `CleanupProject` (VCP) | `/remediation` → EPIC | **EPIC UI only** | partial (`3279-pp7v` phase/class) | 🟡 no live status |
| `NoticeToProceed` (issued) | EPIC / document repository | **EPIC UI only** | — | ❌ gap (no API) |
| `RemediationStatus` | EPIC | **EPIC UI only** | — | ❌ gap (reconstruct from docs) |
| **`NoticeToProceedRequest`** (request / enroll) | EPIC + email | **EPIC UI + manual** | — | ❌ **net-new** (B2G; no citizen write) |

Supporting reference data: Historic Land Use (`r9ca-6t4q`), Clean Soil Bank (`b4dv-8mq4` + `hywf-9b6t`), and the six-layer BOA / community brownfield planning suite are all open (annual) — useful due-diligence context around a site, not the workflow.

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (10 OER datasets)** | Open, machine-readable; the flagship cleanup feed is **daily** and carries a full BBL/BIN spine; strong brownfield-planning geospatial layers | No workflow data — no remedial phases beyond a coarse `Phase`/`Class`, no determinations, no live status; the (E) inventory isn't here (it's DCP's) |
| **SPEED (CARTO/Leaflet map)** | Great public "Do I have an E?" / site-lookup experience | A front-end over a CARTO SQL backend — **not a documented API**; an agent can't call it |
| **EPIC (`a002-epic.nyc.gov`)** | The real, OER-**owned** system of record for the remedial process and every determination | Login-walled .NET/AngularJS app with **no API**; the process, the sign-offs, and the intake are invisible to machines |
| **DCP E-Designations** | Authoritative, monthly, geospatial | **Owned by City Planning, not OER** — the most-demanded environmental record sits on a surface OER doesn't control |

## Implications for the API-first + MCP proposal

1. **Expose the site data live.** Present environmental sites, (E)-designations, and cleanup projects behind one owned OER contract ([OpenAPI](openapi/moer.yaml)) — keyed on **BBL** and OER Project Number — instead of a Socrata ID plus a CARTO map. Lean on nyc-commons BBL so an OER site resolves to the same parcel as a DOB, HPD, or Finance record.
2. **Expose the workflow, not just the rows.** `getRemediationStatus` answers the question that actually blocks development — where the cleanup stands and whether the site is cleared for a building permit / certificate of occupancy — which today means reading EPIC documents.
3. **Add the one net-new write workflow** — `requestNoticeToProceed` (request a Notice to Proceed / enroll a brownfield site in the VCP), fronting the manual EPIC intake. Be honest: this is **B2G** (owner/developer), not a citizen write.
4. **Name the ownership split.** OER *owns* its transaction system (EPIC) — the gap is that it's a legacy portal with no API — but it does **not** own the authoritative (E)-designation inventory (DCP does). Modernization here is *exposing* an owned-but-locked workflow and *reconciling* with DCP's designation data.
5. **MCP server** so an agent can answer "does BBL 3012340045 carry an E for hazardous materials, is it resolved?", "where does OER project X stand and can DOB issue a permit?", and — the point — "enroll my brownfield site in the VCP / request a Notice to Proceed."
