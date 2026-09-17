## Answers

| Metric | Business | Growth |
|---|---|---|
| **Average discount %** | **18.70%** | **18.57%** |
| **% variance vs. average policy threshold** | **+23.68%** | **+26.42%** |

**Supporting detail**

- Business: avg approved discount 18.6963% (n = 214 deals) vs. avg policy threshold 15.1168% → gap +3.58 pp → **+23.68%** variance
- Growth: avg approved discount 18.5682% (n = 176 deals) vs. avg policy threshold 14.6875% → gap +3.88 pp → **+26.42%** variance

**Sources & method (per the defaults you confirmed)**
- Pricing version: **v4.2** (effective 2024‑04‑01, open‑ended) from `Brightpath_Historical_Pricing_Versions_ChangeLog.xlsx` — Business $32/user/mo, Growth $58/user/mo.
- Discounts: `Brightpath_Discount_Approval_Logs_v1.0.xlsx`, `Final_Approved_Discount_%`, simple unweighted mean per tier, all 800 rows (all dated 2024). The duplicate `(1)` file is byte-identical in data, so it changes nothing.
- Variance = (tier avg discount − tier avg `Policy_Threshold_%`) / tier avg threshold × 100. Thresholds in the log vary deal-by-deal (10/15/20%), so the tier average threshold is the correct denominator.

**Sensitivities (do not change the headline answer)**
- Restricted to the v4.2 window only (approvals ≥ 2024‑04‑01; n = 161 / 130): Business 18.52% vs 15.09% → **+22.67%**; Growth 18.32% vs 14.69% → **+24.71%**.
- List-price-value-weighted: Business **+22.42%**, Growth **+25.48%**.
- Using *requested* rather than approved discounts: Business **+31.72%**, Growth **+34.62%** — i.e., requests run ~1.2× the policy ceiling and approvers only claw back about a third of the excess.

**On the Revenue by Segment file (midpoint user counts applied as instructed)**
`Brightpath_Revenue_by_Segment.xlsx` carries no tier field, so it cannot reweight the tier discounts; I used the size-band midpoints (30 / 150.5 / 375.5 users per customer) to map segments to tiers as a cross-check. That yields ~80,820 implied Team seats, 162,540 Business and 78,480 Growth seats, and ARR per implied user of $668 (Small), $281 (Mid‑Market) and $260 (Upper Mid‑Market) against v4.2 annual list of $180/$384/$696 — confirming the ARR file is not reconcilable to v4.2 seat pricing and that the log-level means above are the right basis.

**Read-through:** both tiers are running roughly a quarter above their own policy ceiling, and Growth is the worse offender (26.42% vs 23.68%) despite a lower average threshold — ~61% of approved deals in each tier breach their stated threshold, so this is a systemic approval-discipline issue rather than a few outliers.

**File produced:** `Brightpath_Tier_Discount_vs_Policy_Analysis.xlsx` (per-tier averages, thresholds, gaps, variances and the three sensitivities).