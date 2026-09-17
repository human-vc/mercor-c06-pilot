## Answer

**Sources / version checks first**
- **Latest pricing version = v4.2** (effective 2024‑04‑01, no end date) in `Brightpath_Historical_Pricing_Versions_ChangeLog.xlsx`: Team $15, **Business $32**, **Growth $58**, Enterprise $110 per user/month.
- **Discount logs**: `Brightpath_Discount_Approval_Logs_v1.0.xlsx` (800 deals, all CY2024 approvals). The second copy, `...v1.0(1).xlsx`, is identical on all 801 rows, so there is no version conflict.
- **Revenue by segment** (`Brightpath_Revenue_by_Segment.xlsx`, $120M ARR) contains no tier field, so it was used as context/weighting cross‑check; the per‑deal revenue weight comes from `Initial_List_Price` in the logs.
- Average discount = mean of `Final_Approved_Discount_%`; average policy threshold = mean of `Policy_Threshold_%` for the same deals (thresholds are deal‑level: 10/15/20%); variance = (avg discount ÷ avg threshold − 1).

| | **Business** | **Growth** |
|---|---|---|
| Deals (n) | 214 | 176 |
| **Average discount** | **18.70%** (18.6963%) | **18.57%** (18.5682%) |
| Average policy threshold | 15.12% | 14.69% |
| **% variance vs threshold** | **+23.68%** (+23.6785%) | **+26.42%** (+26.4217%) |
| Variance in points | +3.58 pts | +3.88 pts |
| Deals approved above their own threshold | 60.8% (130/214) | 60.8% (107/176) |

**Key takeaways**
- Growth's variance is larger *not* because it discounts more aggressively (the two tiers are within 0.13 pts of each other) but because Growth's average policy threshold is lower (14.69% vs 15.12%).
- Revenue/list‑price‑weighted (the "revenue‑weighted" read): Business 18.77% discount → **+22.42%** variance; Growth 19.13% → **+25.48%** variance. Same conclusion.
- On requested (pre‑negotiation) discounts the gap is wider: Business 19.91% (+31.72%), Growth 19.77% (+34.62%) — approvers claw back only ~1.2 pts on average.
- Sensitivity: restricting to the v4.2 pricing window only (approvals ≥ 2024‑04‑01, 600 deals) gives Business 18.52% / +22.67% and Growth 18.32% / +24.71%.
- Materiality: ~3.6–3.9 pts of policy leakage on the $25M Business and $35M Growth ARR bases ≈ $0.9M and $1.4M of annual give‑back versus policy.

**File produced:** `Discount_vs_Policy_Threshold_Calc.md` (method, full table, and sensitivities).