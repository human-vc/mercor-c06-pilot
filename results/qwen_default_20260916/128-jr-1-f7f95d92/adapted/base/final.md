## What I did

I rebuilt the v2 scoring model from the two new files, using the exact mechanics Jessee confirmed in the 20 Nov check‑in: **points per criterion = 5 − |Rating (R) − Ideal (I)|, summed across the 5 criteria → max 25 per path.**

**Step 1 – v2 ideal matrix** (`Business Unit Assessment Framework (v2).xlsx` converts the v1 single numbers into word bands; words mapped with the 1–5 descriptor scales on the BU Assessment tabs — very low/very weak = 1, low/weak = 2, moderate/medium = 3, high/strong = 4, very high/very strong = 5, and "X to Y" = the band):

| Criterion | Continue | Graduate | Spin out | Sell | Discontinue |
|---|---|---|---|---|---|
| Technical risk remaining | 1‑2 | 3‑4 | 5 | 3‑4 | 2‑3 |
| Strategic alignment | 3‑4 | 5 | 1‑2 | 1 | 4‑5 |
| Commercial viability | 4‑5 | 4‑5 | 1 | 2‑3 | 3 |
| Capital/ops intensity | 1 | 3‑4 | 4‑5 | 1‑2 | 3 |
| Feasibility of external ownership | 1‑2 | 5 | 3‑4 | 2‑3 | 1 |

**Step 2 – SkyLink v2 ratings** (`Strategic Options Ratings (v2).xlsx`, col C): Tech risk 2 · Alignment 5 · Commercial viability 2 · Capital intensity 3 · External ownership 3.

## SkyLink scores — literal v2 inputs (out of 25)

| Path | Continue | Graduate | Spin out | Sell | Discontinue |
|---|---|---|---|---|---|
| **Total** | **19** | **20** | **17** | **19** | **22** |

Per criterion (Continue / Graduate / Spin / Sell / Discontinue): Tech 5‑4‑2‑4‑5 · Align 4‑5‑2‑1‑5 · Comm 3‑3‑4‑5‑4 · Capital 3‑5‑4‑4‑5 · Ext‑ownership 4‑3‑5‑5‑3.
**→ Literal result: DISCONTINUE (22/25).**

## ⚠️ Two problems in the v2 inputs you should know about

1. **SkyLink's "Strategic Alignment = 5" contradicts every other source.** The SkyLink tab of `BU Assessment.xlsx` rates it 2 ("interesting, but not clearly core"), and the final client deck says outright "**Low strategic alignment**… limited synergies with mobility, robotics or solar." A 5 ("core to long‑term Amensa strategy") is the opposite. The v2 grid also has no rationale rows (v1 did), so it reads like a mis‑keyed/mis‑aligned column set.
2. **The v2 framework structurally rewards Discontinue.** It assigns Discontinue "very high to high" strategic alignment and "low to moderate" technical risk, so *any* BU rated high‑alignment/low‑risk wins on shutting down. Proof: the same run puts **SolisOne at Discontinue 24** (vs Graduate 19) — clearly wrong for the lowest‑burn, strongest‑revenue BU.

**Corrected run (SkyLink alignment = 2, as per its own narrative):** Continue 19 · Graduate 17 · Spin out 20 · **Sell 22** · Discontinue 20 → **SELL**, robust across all four band‑interpretation methods (first‑listed, last‑listed, midpoint, band‑distance).

Cross‑check of the other BUs with v2 ratings as supplied: SolisOne 21/19/14/20/**24 (Discontinue)** · AmensaMech **22 (Sell)**/13/15/21/20 · AmensaDrive 17/**23 (Graduate)**/18/18/20. (Separately, note a pre‑existing bug: SolisOne's published v1 totals 20/22/20/19/12 do **not** match its own formula, which yields 22/20/18/17/14 — the same numbers now shown in the v2 template block.)

## Recommended path for SkyLink

**SELL — IP transfer + selective licensing** (Continue 19, Graduate 17, Spin out 20, **Sell 22**, Discontinue 20). Sell wins on the corrected inputs and remains the only path consistent with the evidence base: <$10B niche TAM, balloon lifespan 30–90 days, 12–24 month spectrum approvals, telcos refusing capex ownership, and credible external owners (defence integrators, HAPS/aerospace operators, satellite constellations). Discontinue at 20 is the runner‑up only because of the v2 rubric inversion — it should be treated as the downside case, not the recommendation, since the IP (navigation/atmospheric‑routing algorithms, NOC tooling, prototype fleet) has salvage value. If you want the literal v2 numbers unfiltered, the answer is Discontinue 22 — I recommend against publishing that without fixing the SkyLink alignment rating and the Discontinue row of the framework.

## Files produced

- **`SkyLink_Strategic_Option_Scores_v2.xlsx`** — v2 ideal matrix translation, SkyLink per‑criterion scoring grid, literal totals, the alignment‑corrected sensitivity run, and the same totals for SolisOne / AmensaMech / AmensaDrive.

**Values to print:** SkyLink v2 — Continue internally 19, Graduate to an Amensa company 20, Spin out 17, Sell 19, Discontinue 22 (literal inputs → Discontinue); with SkyLink's strategic alignment corrected to 2 per its own rationale and final deck — Continue 19, Graduate 17, Spin out 20, **Sell 22**, Discontinue 20 → **Recommended path: SELL (IP transfer / licensing).**