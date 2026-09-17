## Answer

**Latest pricing version = v4.2** (effective 1‑Apr‑2024 → current: Team $15 / Business $32 / Growth $58 / Enterprise $75–110 per user/month, per `Brightpath_Historical_Pricing_Versions_ChangeLog.xlsx`).

Using the FY2024 discount approval logs (Business n = 214, Growth n = 176; `Final_Approved_Discount_%` vs `Policy_Threshold_%`), with each deal's user count set to the **midpoint of its Company Size range** (Small Practice 10–50 → 30; Mid‑Market 51–250 → 150.5; Upper Mid‑Market 251–500 → 375.5, from `Brightpath_Revenue_by_Segment.xlsx`, joined to the logs via `Customer_Size_Segment` in `Brightpath_Deal_Transactions_v1.0.xlsx` on Deal_ID — all 800 IDs matched):

| Metric | Business | Growth |
|---|---|---|
| **Average discount (user‑count weighted)** | **19.37%** | **18.58%** |
| Average policy threshold (user‑count weighted) | 15.25% | 14.79% |
| **% variance vs. threshold** | **+27.01%** | **+25.59%** |

Total users behind the weights: Business 39,956; Growth 30,765.

**Sensitivity, in case you want the unweighted read:** simple (per‑deal) means give Business 18.70% discount / +23.68% variance and Growth 18.57% discount / +26.42% variance. Restricting approvals to the v4.2 window only (≥1‑Apr‑2024) gives Business 19.06% / +25.63% and Growth 18.16% / +22.58%. The conclusion is stable either way: **both mid‑tiers are approving discounts ~25–27% above their own policy thresholds**, so thresholds are routinely overridden (or set unrealistically low) in Business and Growth.

Note: the two copies of the approval log (`v1.0` and `v1.0(1)`) are identical, so no version choice was needed there.

**Files produced**
- `Deliverables/Discount_Variance_Methodology.md` — inputs, method, headline results and sensitivity table
- `Deliverables/Discount_Variance_Calculation.csv` — the underlying computed values for all four scope/weighting variants