**Answers (Business and Growth tiers, unweighted tier averages per your option C):**

| Metric | Business | Growth |
|---|---|---|
| Average discount | **18.70%** (18.6963%) | **18.57%** (18.5682%) |
| Average policy threshold (for reference) | 15.12% (15.1168%) | 14.69% (14.6875%) |
| % variance vs. its average threshold | **+23.68%** | **+26.42%** |

**How I got there**

- **Latest pricing version:** v4.2 (effective 2024‑04‑01, no end date) in `Brightpath_Historical_Pricing_Versions_ChangeLog.xlsx` — Team $15, Business $32, Growth $58, Enterprise $110 per user/month.
- **Revenue by segment:** `Brightpath_Revenue_by_Segment.xlsx` → `ARR_by_Company_Size` supplies the Company Size bands (10–50, 51–250, 251–500 → midpoints 30 / 150.5 / 375.5 users). Per your clarification, these midpoints are used only for rows where Company Size is already stated; no deal-level user weighting or band assignment was applied to the logs.
- **Discount logs:** `Brightpath_Discount_Approval_Logs_v1.0.xlsx` (800 rows; the "(1)" duplicate has identical values) — 214 Business and 176 Growth deals. Discount = mean of `Final_Approved_Discount_%`; threshold = mean of `Policy_Threshold_%` (which varies deal-to-deal at 10/15/20%).
- **Variance formula used** (no further instruction given, so flagging my choice): (avg discount − avg threshold) ÷ avg threshold × 100, i.e., relative variance. In absolute terms the gaps are +3.58 pp (Business) and +3.88 pp (Growth).
- **Discount column used:** `Final_Approved_Discount_%`. If you instead want the *requested* discount, the figures would be Business 19.91% / +31.72% and Growth 19.77% / +34.62%.

**Takeaway:** both tiers systematically exceed their own policy thresholds — Business carries the higher absolute discount (18.70%), Growth the larger relative breach (+26.42%) — evidencing the discount-leakage problem noted in the pricing model and exec deck.

**File produced:** `Discount_vs_Threshold_Calc.md` (sources, calculations, and sensitivity notes).