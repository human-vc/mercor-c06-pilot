## What I did

**Inputs used**
- `Business Unit Assessment Framework (v2).xlsx` → the new *ideal* profile (I) per option, now written as words/bands ("Low to very low", "Moderate to high", …)
- `Strategic Options Ratings (v2).xlsx` → the new *actual* ratings (R) per BU (SkyLink = 2 / 5 / 2 / 3 / 3)
- The 1–5 rubric tabs in `4_Business Unit Assessment/BU Assessment.xlsx` to convert words → numbers (1 = Very low/very weak … 5 = Very high/very strong)
- The scoring mechanic confirmed in the 11/20 check‑in transcript: **score = 5 − ABS(R − I)**, summed over the 5 criteria (max 25), highest total wins.

**Worst-case rule applied:** where v2 gives a band (e.g. "Low to very low" = 2→1), I took the endpoint *farthest* from SkyLink's actual rating — i.e. the lowest fit score that option could possibly claim.

## SkyLink — scores per strategic option (v2, worst case)

| Criterion | R | Continue | Graduate | Spin out | Sell | Discontinue |
|---|---|---|---|---|---|---|
| Technical risk remaining | 2 | I=1 → **4** | I=4 → **3** | I=5 → **2** | I=4 → **3** | I=3 → **4** |
| Strategic alignment | 5 | I=3 → **3** | I=5 → **5** | I=1 → **1** | I=1 → **1** | I=4 → **4** |
| Commercial viability | 2 | I=5 → **2** | I=5 → **2** | I=1 → **4** | I=3 → **4** | I=3 → **4** |
| Capital & op. intensity | 3 | I=1 → **3** | I=4 → **4** | I=5 → **3** | I=1 → **3** | I=3 → **5** |
| Feasibility of ext. ownership | 3 | I=1 → **3** | I=5 → **3** | I=4 → **4** | I=2 → **4** | I=1 → **3** |
| **TOTAL (of 25)** | | **15** | **17** | **14** | **15** | **20** |
| Rank | | 3 | 2 | 5 | 4 | **1** |

**Recommended path: DISCONTINUE — 20/25.** Ranking: Discontinue (20) > Graduate (17) > Continue internally (15) = Sell (15) > Spin out (14).

**Robustness:** Discontinue still wins under a mid-point band reading (21/25), a best-case reading (22/25) and a "lowest number in the band" reading (21/25) — so the call isn't an artefact of the worst-case choice.

**This flips the prior answer:** v1 scored SkyLink **Sell = 21** (Spin out 20, Continue 18). Under v2, Sell collapses to 15 because v2 defines the "Sell" ideal as low technical risk, *very low* strategic alignment and low capital intensity — none of which match SkyLink's v2 ratings.

**One flag worth raising:** the v2 "Discontinue" profile (very high strategic alignment, low technical risk, medium viability, moderate intensity) is effectively a *keeper* profile, and it only wins because the v2 rating row gives SkyLink strategic alignment 5 and technical risk 2 — which contradicts the qualitative evidence in the SkyLink charter/deliverables (TRL 6, non-core adjacency, ~$0.8B/yr burn, <$10B TAM) that drove the earlier "Sell" recommendation. I'd sanity-check that rating row before issuing the recommendation.

**Portfolio cross-check (same method):** SolisOne → Discontinue (22), SkyLink → Discontinue (20), AmensaMech → Discontinue (21), AmensaDrive → Graduate (20). Three of four BUs flip to Discontinue, which is another signal that the v2 framework's "Discontinue" column is under-penalised (three of its five descriptors are single points, so worst-case = best-case there).

## File produced
`SkyLink_Strategic_Option_Scores_v2.xlsx` — 3 tabs: **SkyLink scores (v2 worst)** (full calculation grid + recommendation, sensitivity, v1-vs-v2 delta, caveat), **Method & band mapping** (step-by-step + every descriptor → endpoint → worst-case I → score), **All BUs (v2 worst case)** (portfolio cross-check vs v1 recommendations).