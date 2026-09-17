## Answer

**Latest pricing version = v4.2** (effective 2024‑04‑01, still current): Team $15 / **Business $32** / **Growth $58** / Enterprise $75–110 per user per month (from `Brightpath_Historical_Pricing_Versions_ChangeLog.xlsx`).

**Company Size midpoints used as user counts** (`Brightpath_Revenue_by_Segment.xlsx` → ARR_by_Company_Size): Small Practice 10–50 → **30**; Mid‑Market 51–250 → **150.5**; Upper Mid‑Market 251–500 → **375.5**. Each approval record's Deal_ID was joined to `Brightpath_Deal_Transactions_v1.0.xlsx` to get its size band, and the midpoint user count was used to weight the tier averages. Discounts = `Final_Approved_Discount_%`, thresholds = `Policy_Threshold_%` from `Brightpath_Discount_Approval_Logs_v1.0.xlsx` (800 FY2024 records; the duplicate `v1.0(1)` file is identical).

| | Business | Growth |
|---|---|---|
| Avg. discount (user‑weighted) | **19.37%** | **18.58%** |
| Avg. policy threshold (user‑weighted) | 15.25% | 14.79% |
| **% variance vs. threshold** | **+27.01%** | **+25.59%** |

- Business discount: **19.37%** — threshold‑relative variance: **+27.01%**
- Growth discount: **18.58%** — threshold‑relative variance: **+25.59%**

Both tiers are approving discounts roughly a quarter above their policy ceilings (Business 214 deals / 39,956 weighted users; Growth 176 deals / 30,765 weighted users), i.e. systematic threshold leakage rather than isolated outliers.

For transparency, if the tiers are averaged *unweighted* (simple deal average) instead of by user count, the results are Business 18.70% / +23.68% and Growth 18.57% / +26.42%; a list‑price‑weighted cut gives 18.77% / +24.19% and 19.13% / +30.26%. Restricting to approvals on/after the v4.2 effective date gives 19.06% / +25.63% and 18.16% / +22.58%.

**File produced:** `1. Analysis/Tier_Discount_vs_Threshold_Calc.md` (methodology, per‑band detail, and sensitivity table).