**Results (user-count weighted per your segment-row basis, method C):**

| Metric | Business | Growth |
|---|---|---|
| Average discount | **18.71%** | **18.64%** |
| Average policy threshold | 15.04% | 14.72% |
| % variance vs threshold | **+24.38%** | **+26.61%** |

**How this was built**
- **Latest pricing version:** v4.2 (effective 1 Apr 2024 → present) in `Brightpath_Historical_Pricing_Versions_ChangeLog.xlsx` — Team $15, Business $32, Growth $58, Enterprise $75–110 per user/month. This confirms the tier names in the discount log (Business/Growth) are the current, as-sold tiers, so all 800 FY2024 approval rows are on the current tier structure.
- **Discounts:** `Brightpath_Discount_Approval_Logs_v1.0.xlsx`, `Final_Approved_Discount_%` and `Policy_Threshold_%` (Business n=214, Growth n=176; the "(1)" copy is data-identical).
- **User counts:** Company Size range midpoints from `Brightpath_Revenue_by_Segment.xlsx` → ARR_by_Company_Size: Small Practice (10–50) = 30, Mid-Market (51–250) = 150.5, Upper Mid-Market (251–500) = 375.5, each × that segment row's customer count (2,694 / 1,080 / 209) → weights 80,820 / 162,540 / 78,479.5 users.
- **Segment averages → weighted up:** the log carries no size field, so each Deal_ID was joined to `Brightpath_Deal_Transactions_v1.0.xlsx` (`Customer_Size_Segment`) only to place it in a size band; the band average discount/threshold was then weighted by the segment-row user count.
  - Business: Small 17.56%/15.07%, Mid 18.80%/14.86%, Upper-Mid 19.73%/15.41% → 18.71% vs 15.04%
  - Growth: Small 18.21%/14.38%, Mid 18.97%/14.86%, Upper-Mid 18.39%/14.80% → 18.64% vs 14.72%

**Sensitivity (for transparency):** on a simple unweighted deal basis the answers are Business 18.70% / +23.68% and Growth 18.57% / +26.42%; restricting to approvals on/after 1 Apr 2024 gives Business 18.52% / +22.67% and Growth 18.32% / +24.71% (unweighted basis). No date filter was applied in the headline numbers.

**Takeaway:** both tiers are discounting roughly a quarter above their approved policy ceilings, with Growth running hotter (+26.61%) than Business (+24.38%) despite a slightly lower average threshold — i.e., threshold discipline is weakest in Growth.

**File produced:** `Business_Growth_Discount_vs_Threshold_Analysis.xlsx` (tabs: Segment detail, Results, Notes).