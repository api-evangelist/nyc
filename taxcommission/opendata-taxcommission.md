# NYC Open Data — Tax Commission Datasets

All NYC Open Data assets covering the **NYC Tax Commission**'s work (verified via the Socrata Discovery API, 2026-07-13). There is **no `Tax Commission (TC)` agency label** in NYC Open Data; both relevant assets are published under **`Office of Administrative Tax Appeals (OATA)`** — the umbrella that now houses the Tax Commission (and the Tax Appeals Tribunal). 2 assets, sorted by lifetime page views. Machine-readable: [opendata-taxcommission.json](opendata-taxcommission.json).

The shape of the corpus is the story: it is **outcome-only and thin**. Both datasets are downstream snapshots — the reductions the Commission has already granted, and the Article 7 petitions that escalate to the courts. There is **no dataset for the appeal *process*** — the application (Application for Correction), the hearing, the determination/offer, or the representative relationship — because that lives only in the PDF forms (TC101/TC108/TC109/TC106/TC201…) and the Tax Commission's online filing system. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 10,467 | dataset | `4nft-bihw` | Assessment Actions | 8 |
| 4,476 | dataset | `aht6-vxai` | Open Article 7 Petitions | 10 |

## What each is

- **Assessment Actions (`4nft-bihw`, 8c)** — the Tax Commission's own actions **reducing assessments or reclassifying property**, keyed on Tax Year, Borough Code (1=Manhattan … 5=Staten Island), Block/Lot, and Tax Class Code, with the `Granted Reduction Amount` (total actual assessed-value reduction). This is the published record of *determinations* — outcomes, not applications.
- **Open Article 7 Petitions (`aht6-vxai`, 10c)** — open petitions challenging real-property tax assessments in **NY State Supreme Court** under Article 7 of the Real Property Tax Law: petition index number and year, petitioner name, the petitioner's attorney (name + identifier), and note-of-issue codes. This is the **judicial escalation** that follows a Tax Commission determination.

## Groupings

- **Determinations / outcomes:** Assessment Actions (`4nft-bihw`) — granted reductions and reclassifications.
- **Judicial escalation:** Open Article 7 Petitions (`aht6-vxai`) — court challenges after the administrative appeal.
- **Absent (no Open Data twin):** the Application for Correction (the appeal filing itself), the determination/offer per application, income & expense statements (TC201/203/208/214), the accountant's certification (TC309), and the representative relationship — all trapped in PDF forms and the online filing system.

## Note on the related domain

`Department of Finance (DOF)` **sets** the tentative assessment (Notice of Property Value) and owns the assessment roll and exemption data; the **Tax Commission hears the appeal** of that assessment. The two are distinct agencies; DOF's `Property Exemption Detail` (`muvi-b6kx`) and assessment roll sit under the DOF label, not here.
