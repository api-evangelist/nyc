# Crosswalk — Website/App Fruit ↔ APIs ↔ NYC Open Data (DOF)

Maps the low-hanging fruit on **nyc.gov/site/finance** and the **a836 legacy apps** to (a) the **existing APIs** (Socrata SODA; the ACRIS/CityPay/PTS apps) and (b) the **145 DOF datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-dof.json](opendata-dof.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, one service layer locked in a vendor CRM → *unlock.*
- **DOF:** reference data **wildly open** (145 Socrata datasets), but every transaction is spread across a **fleet of aging in-house `a836` legacy apps** (ACRIS, CityPay, PTS) with no API → **modernize the app layer.**

DOF is the most open domain assessed *and* the most siloed at the transaction layer. The developments, valuation, exemptions, tax charges, ACRIS register, and parking summonses are all machine-readable on Open Data. But the things a resident *does* — pay a ticket, pay a tax bill, record a document — live only behind a PayPal/Braintree form (CityPay) or a 2013-era ASP.NET screen (ACRIS). A resident or agent asking "pay this summons" has no API to call, even though the balance is already published.

Coverage: ✅ strong open twin · 🟡 partial/snapshot · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / App | API today | Open Data | Cov. |
|---|---|---|---|---|
| `PropertyValuation` | `/property` | SODA | Valuation & Assessment (`yjxr-fw8i`, 45c); Tax-Classes edition (`8y4t-faws`, 139c) | ✅ |
| `PropertyExemption` | `/benefits` | SODA | Property Exemption Detail (`muvi-b6kx`, 70c); J-51 (`y7az-s7wc`) | ✅ |
| `PropertyTaxBill` | PTS / CityPay | SODA snapshot; **app only** for live | Property Charges Balance (`scjx-j6np`, 34c); Tax Rates (`7zb8-7bpk`); Tax Lien Sale (`9rz4-mjek`) | 🟡 snapshot |
| `ACRISDocument` | ACRIS app | SODA mirror; **app only** for live | Master (`bnx9-e6tj`), Legals (`8h5j-fqxa`), Parties (`636b-3b5g`), code tables (`7isb-wh4c`, `94g4-w6xz`) | 🟡 lagged mirror |
| `ParkingViolation` | `/parking` | SODA | Open Parking & Camera Violations (`nc67-uf89`, 19c); Issued FY2026 (`pvqr-7yc4`, 44c); codes (`ncbg-6agr`) | ✅ |
| Pay a property tax bill | CityPay / PTS | **App UI only** | — | ❌ gap |
| Record a document | ACRIS | **App UI only** | mirror only | ❌ gap |
| **`ParkingTicketPayment`** (pay a ticket) | CityPay | **App UI only** (PayPal/Braintree) | balance twin `nc67-uf89` (read-only) | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (145 datasets)** | Open, machine-readable; the widest footprint assessed — valuation, exemptions, charges, ACRIS, parking | Reference/snapshot data only; static extracts; nothing about live transactions |
| **a836 legacy apps (ACRIS / CityPay / PTS)** | The real transaction systems — record, pay a ticket, pay a tax bill | Browser-only; ACRIS is a 2013 ASP.NET frameset; no API, no OpenAPI, no JSON; not agent-accessible |

## Implications for the API-first + MCP proposal

1. **Publish the open reference data as one clean resource model keyed on the BBL.** Valuation, exemptions, tax bills, ACRIS legals, and parking violations behind one owned DOF contract ([OpenAPI](openapi/dof.yaml)) — so consumers learn one model, not 145 Socrata IDs and three legacy screens.
2. **Modernize the app layer.** Front the `a836` fleet with an API so the core resident transaction — **paying a parking/camera ticket** — has a machine-readable, agent-native contract.
3. **Add the one net-new write workflow** — `pay_parking_ticket` (submit a payment against a summons), accepting only a tokenized instrument (PayPal/Braintree), never raw card numbers.
4. **Keep the payment surface safe.** The write path handles money; it is authenticated, mutating, and tokenized — the MCP tool is annotated non-read-only and requires confirmation.
5. **MCP server** so an agent can answer "what's the assessed value of this BBL?", "what exemptions does this parcel carry?", "what's the deed history here?", and — the point — "pay this parking ticket."
