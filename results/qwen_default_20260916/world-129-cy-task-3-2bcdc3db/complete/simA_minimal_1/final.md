## Results

**Method locked in** (per your confirmation): latest pricing version = **v4.2** (effective 2024‑04‑01 → current: Team $15 / Business $32 / Growth $58 / Enterprise $75–110 per user/mo, from `Brightpath_Historical_Pricing_Versions_ChangeLog.xlsx`); discounts and thresholds from `Brightpath_Discount_Approval_Logs_v1.0.xlsx` (800 FY2024 rows; Business n=214, Growth n=176; discount = `Final_Approved_Discount_%`, threshold = `Policy_Threshold_%`); user count = midpoint of each Company Size band from `Brightpath_Revenue_by_Segment.xlsx` → **Small Practice 10–50 = 30, Mid‑Market 51–250 = 150.5, Upper Mid‑Market 251–500 = 375.5**, joined to each Deal_ID via `Customer_Size_Segment` in `Brightpath_Deal_Transactions_v1.0.xlsx` and used as the weight for both the discount and its threshold.

| | Business | Growth |
|---|---|---|
| Deals / total users (weight) | 214 / 39,956 | 176 / 30,765 |
| **Average discount % (user‑weighted)** | **19.37%** (19.3673) | **18.58%** (18.5811) |
| Average policy threshold % (user‑weighted) | 15.25% | 14.79% |
| **% variance vs threshold** (disc ÷ thr − 1) | **+27.01%** | **+25.59%** |
| Variance in percentage points | +4.12 pts | +3.79 pts |

**Answer in one line:** Business discount **19.37%**, Growth discount **18.58%**, Business threshold‑relative variance **+27.01%**, Growth threshold‑relative variance **+25.59%** — both tiers are running roughly a quarter above their approved policy ceilings.

Sensitivity (since the weighting choice was left to me):
- Unweighted simple means: Business 18.70% disc / 15.12% thr → **+23.68%**; Growth 18.57% / 14.69% → **+26.42%**. Weighting barely moves Growth but lifts Business ~3.3 pts, because Business's largest discounts sit in the 251–500 employee band (19.73% avg vs 17.56% for Small Practice).
- Restricting to approvals on/after the v4.2 effective date (Apr 1, 2024): Business 19.06% / +25.63%; Growth 18.16% / +22.58%. I used all FY2024 approvals for the headline numbers, as the log contains no pre‑v4.2 pricing tiers other than these four.
- Note: the two discount‑log files (`v1.0` and `v1.0(1)`) are byte‑identical in content (800 rows, zero differences), and the deal‑level transaction file's `Discount_Percentage` does **not** reconcile with the approval log for the same Deal_ID (only 23/800 match), so the approval log was treated as the authoritative discount source per your instruction.

**File produced:** `Tier_Discount_vs_Threshold_Analysis.xlsx` — per‑tier calculation with sources, midpoints, weights, both weighted and unweighted variants.