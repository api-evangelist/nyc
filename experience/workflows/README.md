# Cross-Agency Workflows (Arazzo)

*Multi-agency citizen and builder journeys, expressed as open [Arazzo](https://spec.openapis.org/arazzo/latest.html) workflow documents that chain the per-agency operations already drafted across the [NYC Modernization](../../README.md) study.*

A single government outcome rarely lives in one agency. Building housing, opening a business, or clearing a site touches a dozen portals in sequence — each with its own form, queue, and status page, and no shared thread between them. The per-agency [OpenAPI contracts](../../README.md) in this repo model each gate; an **Arazzo** document models the **path through them** — the connective tissue that lets a central project-management team, a builder's software, or an AI agent see every step, its inputs, and its status in one place.

## Workflows

### [`build-affordable-housing.arazzo.yaml`](build-affordable-housing.arazzo.yaml)

The end-to-end journey to build one affordable housing project, ordered across the four phases of the development lifecycle and gated on the project's shape (rezoning vs. as-of-right, City-owned vs. private, landmark, environmental designation, office conversion):

| Phase | Steps | Agencies |
|---|---|---|
| **1 · Environmental Review & Planning** | geocode site → check parcel → certify land use (ULURP) → environmental Notice to Proceed → poll remediation | DCP, DOF, MOER |
| **2 · Pre-Development & Financing** | apply for financing → poll financing → HPD project record | HDC, HPD |
| **3 · Permitting & Approvals** | PDC design review → LPC Certificate of Appropriateness → DEP stormwater (SWPPP) → DEP asbestos (conversions) → DOB building permit → FDNY fire-alarm plan → DOT street work → DEP sewer/water connection → DPR tree sign-off | PDC, LPC, DEP, DOB, FDNY, DOT, DPR |
| **4 · Marketing & Lease-Up** | Certificate of Occupancy → HPD lottery lease-up | DOB, HPD |

**Twelve agencies, one thread.** Data flows on the parcel's **BBL** — the [`nyc-commons`](../../nyc-commons/README.md) geography spine — so every agency composes around the project rather than the org chart. The workflow is the single artifact a "link the permitting portals and automate approval management across agencies" mandate needs, expressed as an open standard instead of another siloed portal.

## Design-first, not a deployment

Like everything in this study, these are **design artifacts**. The workflow references the agencies' modeled OpenAPI operations (`sourceDescriptions`); it is meant to be forked and implemented against real endpoints, not run as-is. Steps annotated **"(read touchpoint)"** point at an agency's existing modeled *read* operation where that specific *write* workflow is not yet drafted as its own net-new operation — those are called out explicitly as the honest next writes to model (a DOF tax-lot subdivision, a dedicated DEP SWPPP and asbestos-abatement submission, a DCP pre-certification write).

## Why Arazzo

Arazzo is the OpenAPI Initiative's standard for describing sequences of API calls across one or more APIs. It gives a City the same thing a builder needs: a **portable, versionable, testable** description of a multi-agency process — one that documents the journey, drives an agent, and can be conformance-checked as the underlying agency APIs come online.

---
*Part of the [Programmable City](../../EXPERIENCE.md) experience layer. Not an official City document.*
