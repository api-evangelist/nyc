# Interface Localization with OpenAPI Overlays

*Translate the **interface** — not the data — into the ten citywide languages NYC serves, from one base contract, using the open [OpenAPI Overlay Specification 1.0](https://spec.openapis.org/overlay/latest.html). Because the MCP tool layer is generated 1:1 from the OpenAPI operations, the same overlay also produces a **localized MCP server**.*

Interactive: **[nyc.apievangelist.com/experience.html](https://nyc.apievangelist.com/experience.html)** (Localization showcase).

## The idea

NYC **Local Law 30 (2017)** requires City agencies to provide services in ten designated citywide languages. That mandate has always applied to the *human* interface — web pages, forms, signage. As government becomes programmable, the **API and agent interface** need the same treatment: an agent helping a New Yorker apply to the affordable-housing lottery should be able to describe every operation — "Apply to an affordable-housing lottery," "Check the status of your application" — in the language that New Yorker actually speaks.

An **OpenAPI Overlay** is the exact tool for this. An overlay is a small, separate document that lists **targeted updates** (via JSONPath) to apply to a base OpenAPI description. So instead of forking the contract ten times, you keep **one** base contract and **ten** thin overlays — one per language — each translating only the human-readable strings.

**Crucially, this localizes the interface, never the data.** The overlay touches `info.title`, operation `summary`/`description`, tag descriptions, and parameter descriptions. It does **not** touch — and must never touch — paths, `operationId`s, schema field names, enum values, or any record returned by the API. A `borough` field stays `borough`; `createLotteryApplication` stays `createLotteryApplication`. Only the words a human (or an agent, on that human's behalf) reads get translated. The data flows in one canonical shape; the *description* of that data is what speaks ten languages.

## The ten languages (Local Law 30)

Spanish · Chinese (Traditional) · Russian · Bengali · Haitian Creole · Korean · Arabic · Urdu · French · Polish — plus the English base. See [`languages.json`](languages.json) (codes, endonyms, and text direction; Arabic and Urdu are right-to-left).

## Worked example: HPD Housing Connect

The demonstration localizes the citizen-facing surface of the **[HPD](../../hpd/) affordable-housing lottery** API — whose applicants are precisely the limited-English population Local Law 30 exists to serve.

```
translations.json  ──►  hpd.<lang>.overlay.yaml        (10 Overlay documents — the standard artifact)
                   ──►  dist/hpd.<lang>.openapi.yaml    (10 localized OpenAPI contracts)
                   ──►  dist/hpd.<lang>.mcp.json        (10 localized MCP servers)
                   ──►  index.json                      (manifest, also copied to data/overlays.json)
```

- **[`hpd/translations.json`](hpd/translations.json)** — the source strings: six interface strings (title + five operation summaries), each with its JSONPath target and `operationId`, and the ten translations.
- **`hpd/hpd.<lang>.overlay.yaml`** — the generated Overlay documents. Each is a real, spec-valid `overlay: 1.0.0` file whose `actions` are `{target, update}` pairs — e.g. `target: $.paths['/lottery-applications'].post.summary`.
- **`hpd/dist/hpd.<lang>.openapi.yaml`** — the base contract with the overlay applied: identical paths, operations, and schemas; localized summaries.
- **`hpd/dist/hpd.<lang>.mcp.json`** — the base MCP server with tool descriptions localized for every tool whose `x-openapi-operation` matches a translated operation. **This is the payoff: a Spanish-, Bengali-, or Arabic-speaking agent gets the same tools, described in its user's language.**

Regenerate with `python3 scripts/build-overlays.py`.

## Honest caveat on the translations

The translations in this repo are **illustrative** — they demonstrate the *pipeline*, not certified copy. In production, the City routes interface strings through its existing Local Law 30 **certified-translation workflow** (the same vendors that already translate nyc.gov). The overlay is the mechanism; professional translators supply the words — and because each language is an isolated overlay, a translation can be reviewed, corrected, and re-applied without ever touching the base contract or the data. Program and product names (HPD, Housing Connect, Housing New York, NYC) are kept in English by convention, matching nyc.gov practice.

## Why this belongs in the stack

This is the same design-first discipline as the rest of the study: one canonical source, transformed by open standards. Overlays join **JSON Schema → OpenAPI → MCP → Agent Skills → Arazzo → APIs.json** as the **interface-transformation** layer — the standard that lets a single programmable-government contract meet every New Yorker in their own language, across both the API and the agent surface. See [STANDARDS.md](../../STANDARDS.md).

---
*Part of the [Programmable City](../../EXPERIENCE.md) experience layer. Design-first artifacts, not deployments. Not an official City document.*
