# Crosswalk — Website/Portal Fruit ↔ APIs ↔ FHIR ↔ NYC Open Data (H+H)

Maps the low-hanging fruit on **nychealthandhospitals.org** and **MyChart** to (a) the **existing APIs** (the live Epic FHIR R4 endpoint; MyChart), (b) the **FHIR standard** H+H already runs, and (c) **NYC Open Data** (which owns **no** H+H datasets). Built 2026-07-13 from [fruit.json](fruit.json) × the Epic FHIR CapabilityStatement × the Socrata Discovery API.

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, service layer locked in a vendor CRM → *unlock the service layer.*
- **H+H:** a **real health-data standard (Epic FHIR R4 / SMART on FHIR) is already live**, but it is read-mostly, patient-scoped, vendor-owned, with **no open directory and no booking** → **extend the standard.**

H+H inverts NYCHA's problem again. It is not that the transaction layer has *no* API — it is that a genuine, standards-based API (**FHIR**) is *already in production*, and yet the two things a New Yorker most needs — an **open directory** ("which hospital near me does this?") and the ability to **book** ("get me an appointment") — still have no contract. The standard exists; it just stops short.

Coverage: ✅ open/usable API · 🟡 exists but auth-gated / read-only · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Portal | API today | FHIR resource | Open Data | Cov. |
|---|---|---|---|---|---|
| `Facility` | `/locations` | site bot-walled | `Location` / `Organization` (read+search, **auth-gated**) | — | 🟡 auth-gated, no open directory |
| `Service` | `/services` | site bot-walled | `HealthcareService` (**not exposed**) | — | ❌ gap |
| `Provider` | `/doctors` (Find a Doctor) | site bot-walled | `Practitioner` / `PractitionerRole` (read+search, **auth-gated**) | — | 🟡 auth-gated |
| `FinancialAssistance` (NYC Care, sliding scale) | `/help-paying-your-bill` | site bot-walled | — (no analogue) | — | ❌ gap |
| `Pharmacy` | `/pharmacy` | site bot-walled | `Location` (pharmacy) | — | ❌ gap |
| `Appointment` (booked) | MyChart | **FHIR read** | `Appointment` (**read + search only**) | — | 🟡 read-only |
| **`AppointmentRequest`** (book a visit) | MyChart / 1-844-NYC-4NYC | **UI / phone only** | `Appointment` create / `$book` / `Slot` — **none exposed** | — | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Epic FHIR R4 (live, SMART on FHIR)** | Real, modern, standards-based; 59 resource types; production ("Epic November 2025"); discoverable via Epic's directory | Patient-scoped and read-mostly; no open directory (Location → 401); `Appointment` read-only; **no `Slot`, no `$book`**; entirely Epic-owned |
| **MyChart portal** | The real patient transaction system — appointments, messaging, refills, bill pay | Login-walled Epic UI; no open API of its own; booking is a UI flow, not a contract |
| **Bot-walled marketing site** | Human-readable directory of locations/services/doctors/financial help | Radware bot wall blocks automated access; no content API; not agent-reachable |
| **NYC Open Data** | — | H+H owns **zero** datasets; health data there is DOHMH's |

## Implications for the API-first + MCP proposal

1. **Publish an OPEN directory.** Facilities, service lines, providers, pharmacies, and financial-assistance programs behind one owned H+H contract ([OpenAPI](openapi/hhc.yaml)) — the "which H+H hospital near me does cardiology and takes new patients?" surface that neither the bot-walled site nor auth-gated FHIR provides. Align `Facility`→`Location`/`Organization`, `Provider`→`Practitioner`, `Service`→`HealthcareService` so it composes with the FHIR H+H already runs.
2. **Extend the standard to booking.** Add the one net-new write workflow — `request_appointment` (`AppointmentRequest`) — that is missing from both MyChart's machine surface and the live FHIR endpoint. Model it as a *request* (proposed) that intake triages, matching how safety-net scheduling actually works.
3. **Mirror the FHIR read.** Expose the patient's `Appointment` read (SMART on FHIR) so an agent can answer "when is my next visit?" using the same authorization model Epic already implements.
4. **Route the uninsured.** Because H+H is the safety-net system, wire the `coverage` block on a request to **NYC Care** / financial counseling; keep eligibility immigration-status-blind.
5. **Keep clinical data protected.** The proposal never widens access to protected FHIR data (Conditions, Observations, Medications); it publishes the *directory* openly and mediates *booking* under patient auth.
6. **MCP server** so an agent can answer "find me a Gotham Health center in the Bronx with behavioral health," "does H+H help if I have no insurance?", and — the point — "request a primary-care appointment for me next week."
