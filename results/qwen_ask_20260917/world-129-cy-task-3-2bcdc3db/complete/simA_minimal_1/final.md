I've completed the analysis. Here are the results.

## Answer

| Metric | Business | Growth |
|---|---|---|
| **Average discount %** | **18.70%** | **18.57%** |
| **% variance vs. avg policy threshold** | **+23.68%** | **+26.42%** |

(Average policy threshold: Business 15.12%, Growth 14.69% → gaps of +3.58 pp and +3.88 pp respectively.)

## Inputs and method

- **Latest pricing version:** v4.2 (effective 2024‑04‑01, still open) in `Brightpath_Historical_Pricing_Versions_ChangeLog.xlsx` — Team $15, **Business $32**, **Growth $58**, Enterprise $110/user/month. v4.2 notes map Business to "50–200 seat firms" (Mid‑Market band) and Growth to scaling cross‑department firms (Upper Mid‑Market band).
- **Revenue data by segment:** `Brightpath_Revenue_by_Segment.xlsx` → Company Size bands 10–50 / 51–250 / 251–500, giving midpoints **30 / 150.5 / 375.5 users**, and ARR/customer counts (Mid‑Market: $45.6M / 1,080 customers; Upper Mid‑Market: $20.4M / 209 customers). Per your instruction, the midpoints are applied **only to the segment rows** (i.e., to convert revenue-segment data into user counts), not as weights on the discount logs.
- **Discount approval logs:** `Brightpath_Discount_Approval_Logs_v1.0.xlsx` — 800 rows; the duplicate copy `...v1.0(1).xlsx` is byte-for-byte identical in content, so either yields the same result. Averages use **Final_Approved_Discount_%** vs. the mean of **Policy_Threshold_%** per tier (thresholds are only 10/15/20 in the file). n = 214 Business, 176 Growth.
- **Variance formula:** (tier avg discount − tier avg threshold) ÷ tier avg threshold.

## Sensitivity (if you want the tier averages weighted by size instead)

Because the logs carry no company-size field, weighting each deal by the band midpoint implied by its `Initial_List_Price` at v4.2 rates gives: Business 18.60% / +22.87%, Growth 19.01% / +25.34%. Weighting by raw implied users (equivalently, by list price) gives Business 18.77% / +22.42%, Growth 19.13% / +25.48%. The conclusion is unchanged either way: **both tiers run roughly a quarter above their policy threshold, and Growth overshoots proportionally more than Business even though its absolute discount is slightly lower.** Notably, ~61% of Business and Growth deals were approved above their own stated threshold.

## File produced

- `Tier_discount_vs_policy_threshold.xlsx` — Sheet 1: tier results, thresholds, gaps, mapped bands/midpoints and ARR inputs with sources; Sheet 2: the weighting sensitivity table above.