## Answer

**Primary results (user-count weighted on the segment-row basis, all 800 FY2024 approvals):**

| Metric | Business | Growth |
|---|---|---|
| Average discount | **18.71%** | **18.64%** |
| Average policy threshold (for reference) | 15.04% | 14.72% |
| % variance vs. own threshold | **+24.38%** | **+26.61%** |

So: **Business discount = 18.71%, Growth discount = 18.64%, Business threshold-relative variance = +24.38%, Growth threshold-relative variance = +26.61%.**

### How I got there
- **Latest pricing version:** v4.2 (effective 2024‑04‑01, no end date) in `Brightpath_Historical_Pricing_Versions_ChangeLog.xlsx` — Team $15 / **Business $32** / **Growth $58** / Enterprise $75–110 per user/month. This is the version whose tier names match the `Pricing_Tier` values in the logs.
- **User counts:** midpoints of the Company Size ranges in `Brightpath_Revenue_by_Segment.xlsx` → `ARR_by_Company_Size` (ties exactly to the detail sheet): Small Practice 10–50 → 30 users, Mid‑Market 51–250 → 150.5, Upper Mid‑Market 251–500 → 375.5. Weighted by each segment row's customer count: 30×2,694 = 80,820; 150.5×1,080 = 162,540; 375.5×209 = 78,479.5.
- **Discounts:** `Final_Approved_Discount_%` and `Policy_Threshold_%` from `Brightpath_Discount_Approval_Logs_v1.0.xlsx` (Business n=214, Growth n=176; the "(1)" duplicate file is content-identical). Each approval was placed in a company-size band via `Deal_ID` → `Customer_Size_Segment` in `Brightpath_Deal_Transactions_v1.0.xlsx` (all 800 IDs matched) — the midpoint was used only as the band-level weight, per your instruction, not assigned deal-by-deal.
- Averaged discount and threshold within each band, then rolled the band averages up with the user-count weights; variance = (weighted discount ÷ weighted threshold − 1).

### Sensitivities (conclusion unchanged either way)
- Unweighted deal means: Business 18.70% → +23.68%; Growth 18.57% → +26.42%.
- Restricted to approvals on/after the v4.2 effective date (2024‑04‑01): Business 18.55% → +23.35%; Growth 18.50% → +24.93%. (No instruction was available on the date filter, so the full FY2024 population is the primary figure.)

**Interpretation:** both tiers are discounting roughly a quarter above their own approved policy ceilings, and Growth is the worse of the two relative to policy (≈+26.6% vs ≈+24.4%) even though its absolute average discount is marginally lower — its policy thresholds are set tighter.

**File produced:** `1. Analysis/Discount_vs_Threshold_by_Tier_workings.md` (sources, band-level detail, weights, results and sensitivities).