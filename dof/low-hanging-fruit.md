# Low-Hanging Fruit Index — DOF

**Agency:** New York City Department of Finance (DOF)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/finance` (Akamai + nginx + NYC.gov "Livesite" platform + Dynatrace) and the legacy **`a836-*.nyc.gov`** application layer: **ACRIS** (`a836-acris.nyc.gov`, ASP.NET/IIS, `iso-8859-1` meta-refresh framesets, `Last-Modified 2013`), **CityPay** (`a836-citypay.nyc.gov`, a PayPal/Braintree payment form per its CSP), and the **Property Tax System** (`a836-pts-access.nyc.gov`, session-cookie gated). Verified the NYC Open Data agency label `Department of Finance (DOF)` via the Socrata Discovery API and pulled all **145** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-dof.md](opendata-dof.md).

## Headline findings

1. **DOF is an app-layer legacy domain.** An informational site on the shared NYC.gov chassis, and a **fleet of aging `a836-*.nyc.gov` apps** — ACRIS, CityPay, and the Property Tax System — that carry every transaction, none with an API.
2. **The reference data is the widest open footprint assessed.** **145 NYC Open Data datasets** cover property valuation & assessment (`yjxr-fw8i` 45c, `8y4t-faws` 139c), exemptions/abatements (`muvi-b6kx` 70c), tax-charge balances (`scjx-j6np`), the full **ACRIS** register (master/legals/parties), and every **parking/camera violation**.
3. **But the transaction layer is locked.** Paying a ticket, paying a tax bill, and recording a document — the things residents actually *do* — live only inside a PayPal/Braintree form (CityPay), a session-gated tax app (PTS), or a 2013-era ASP.NET screen (ACRIS). None has a machine-readable contract.
4. **The reference model joins on the BBL.** Valuation, exemptions, tax charges, and ACRIS legals all key on the Borough-Block-Lot — one owned resource model spares consumers 145 Socrata IDs.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* one locked vendor CRM; **DOF = modernize the app layer.** Here the data is already the most open of any domain — the work is least about liberating datasets and most about giving the **transaction layer** (above all, paying a parking ticket) an owned, agent-native API instead of a fleet of aging `a836` screens.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Property Valuation & Assessment | `PropertyValuation` | SODA | ✅ Valuation & Assessment (`yjxr-fw8i`, 45c) |
| 2 | Property Exemptions & Abatements | `PropertyExemption` | SODA | ✅ Property Exemption Detail (`muvi-b6kx`, 70c) |
| 3 | Property Tax Charges / Balance | `PropertyTaxBill` | SODA snapshot + PTS/CityPay | 🟡 Property Charges Balance (`scjx-j6np`) |
| 4 | ACRIS Recorded Documents | `ACRISDocument` | ACRIS app + SODA mirror | 🟡 Master/Legals/Parties (`bnx9-e6tj`…) |
| 5 | Parking & Camera Violations | `ParkingViolation` | SODA | ✅ Open Parking & Camera Violations (`nc67-uf89`) |
| 6 | **Pay a parking / camera ticket** | `ParkingTicketPayment` | CityPay | ❌ **net-new** (balance twin only) |
| 7 | Pay a property tax bill | `PropertyTaxBill` | CityPay / PTS | ❌ gap (no API) |
| 8 | Record / search a document | `ACRISDocument` | ACRIS | ❌ gap (mirror only) |
| 9 | Digital Tax Map | `PropertyValuation` | SODA (file/map) | ✅ Digital Tax Map (`smk3-tmxj`) |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 145 DOF datasets (the one real, open API; reference data only).
- **ACRIS** — `a836-acris.nyc.gov`; a 2013-era ASP.NET/IIS frameset app; no API.
- **CityPay** — `a836-citypay.nyc.gov`; PayPal/Braintree-backed payment form; no API.
- **Property Tax System (PTS)** — `a836-pts-access.nyc.gov`; session-gated; no API.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, Dynatrace RUM) — the same chassis as Parks/DOE/Council/NYCHA; DOF's distinct stack is the `a836` app fleet.

## Reverse-engineered entities

`PropertyValuation` (TaxLot) · `PropertyExemption` · `PropertyTaxBill` · `ACRISDocument` (deeds/mortgages, with parties + legals) · `ParkingViolation` · `ParkingTicketPayment` (net-new write; also stands in for the CityPay-locked PropertyTaxPayment) — universal join key: the **Borough-Block-Lot (BBL / BBLE / PARID)**; parking keys on **Summons Number**; ACRIS on **Document ID / CRFN**.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (BBLE, PARID, CRFN, the geography spine) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open reference data as clean resources + the net-new `POST /parking/payments` (pay a ticket) — done ([openapi/dof.yaml](openapi/dof.yaml)).
3. **MCP** artifact: `find_property_valuations`, `get_property_valuation`, `find_property_exemptions`, `get_property_tax_bill`, `find_acris_documents`, `get_acris_document`, `find_parking_violations`, `get_parking_violation`, `pay_parking_ticket` — done ([mcp/dof-mcp.json](mcp/dof-mcp.json)).
