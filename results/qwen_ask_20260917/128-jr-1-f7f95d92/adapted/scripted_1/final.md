Verified the workbook writes cleanly. Here are the results.

## SkyLink Atmos — scores under the v2 framework + v2 ratings

**Method (unchanged):** per-criterion score = `5 − ABS(Rating R − Ideal I)`, summed over the 5 criteria (max 25); highest total wins. **Per your instruction, each v2 framework range was translated to its worst case** — the unfavourable endpoint of the stated range on that criterion's own 1–5 scale (more residual risk, less alignment, weaker viability, heavier capital/ops intensity, lower external-ownership feasibility).

**SkyLink v2 actual ratings (R):** Technical risk 2 · Strategic alignment 5 · Commercial viability 2 · Capital & ops intensity 3 · Feasibility of external ownership 3

| Ideal (I), worst case | Continue | Graduate | Spin out | Sell | Discontinue |
|---|---|---|---|---|---|
| Technical risk remaining | 2 | 4 | 5 | 4 | 3 |
| Strategic alignment | 3 | 5 | 1 | 1 | 4 |
| Commercial viability | 4 | 4 | 1 | 2 | 3 |
| Capital & ops intensity | 1 | 4 | 5 | 2 | 3 |
| Feasibility of external ownership | 1 | 5 | 3 | 2 | 1 |

| Calculation (5 − \|R−I\|) | Continue | Graduate | Spin out | Sell | Discontinue |
|---|---|---|---|---|---|
| Technical risk remaining | 5 | 3 | 2 | 3 | 4 |
| Strategic alignment | 3 | 5 | 1 | 1 | 4 |
| Commercial viability | 3 | 3 | 4 | 5 | 4 |
| Capital & ops intensity | 3 | 4 | 3 | 4 | 5 |
| Feasibility of external ownership | 3 | 3 | 5 | 4 | 3 |
| **TOTAL (max 25)** | **17** | **18** | **15** | **17** | **20** |
| Rank | 3 | 2 | 5 | 4 | **1** |

### Recommended path: **DISCONTINUE** (20/25), with Graduate (18) second, Continue/Sell tied at 17, Spin out last at 15.

This **reverses the v1 conclusion** (v1 was 18 / 16 / 20 / 21 / 16 → Sell). The driver is the v2 ratings moving SkyLink to *very high* strategic alignment (5, up from 2) and *low* residual technical risk (2) — which kills the two criteria that previously made Sell/Spin-out attractive — while the v2 framework makes Sell/Spin-out demand very low alignment and very weak viability. The ranking is robust: worst-case, midpoint, and best-case readings of the ranges all put Discontinue first (20 / 21 / 22).

### Portfolio cross-check (same v2 method, all four BUs)
- SolisOne: Continue 20 · Graduate 17 · Spin out 12 · Sell 18 · **Discontinue 23**
- SkyLink: **Discontinue 20**
- AmensaMech: **Continue internally 20** (Sell 20, Discontinue 19)
- AmensaDrive: **Graduate 22** (Discontinue 20)

⚠️ **Flag for you:** taken literally, the v2 ratings also flip SolisOne — the previous "Graduate" flagship — to Discontinue (23). That's a strong hint that either the polarity of the new ratings table or the wording of the new framework ranges needs a sanity check before the four BU decks are re-issued. I did not change any formula to avoid this; I'm reporting the model as it computes.

**File produced:** `SkyLink_Strategic_Option_Scores_v2.xlsx` — tabs/sections for actual ratings, worst-case ideal mapping, the calculation grid, a sensitivity block (worst/mid/best case + v1 baseline), and the four-BU cross-check.