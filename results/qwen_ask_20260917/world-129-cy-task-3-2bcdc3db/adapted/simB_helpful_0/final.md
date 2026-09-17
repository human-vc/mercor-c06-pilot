## Answer

| Metric | Business | Growth |
|---|---|---|
| **Average discount %** | **18.70%** | **18.57%** |
| **% variance vs. average policy threshold** | **+23.68%** | **+26.42%** |

(Unrounded: Business 18.696262% discount vs 15.116822% threshold → +23.678516%; Growth 18.568182% vs 14.687500% → +26.421663%)

### How I got there
- **Latest pricing version** = **v4.2** (effective 2024‑04‑01, open‑ended) in `Brightpath_Historical_Pricing_Versions_ChangeLog.xlsx` — Team $15 / Business $32 / Growth $58 / Enterprise $110 per user/month.
- **Discounts** = simple mean of `Final_Approved_Discount_%` in `Brightpath_Discount_Approval_Logs_v1.0.xlsx` (214 Business rows, 176 Growth rows; all 800 rows are dated 2024, so they all sit inside the v4.2 era). I verified the second copy, `..._v1.0(1).xlsx`, is row‑for‑row identical, so it makes no difference.
- **Threshold** = simple mean of `Policy_Threshold_%` over the same rows (values are a mix of 10/15/20% per deal).
- **Variance** = (avg discount − avg threshold) ÷ avg threshold × 100.
- **Revenue by segment**: used the **midpoint of each Company Size range** as the user count per row, as instructed (Mid‑Market 51–250 → 150.5 users × 1,080 customers = 162,540 users / $45.6M ARR; Upper Mid‑Market 251–500 → 375.5 × 209 = 78,480 users / $20.4M ARR). Because each tier maps to a single size band, the ARR weight is constant within a tier and collapses to the simple mean — the result is unchanged.

### Sensitivities worth knowing
- Restricting to approvals on/after 2024‑04‑01 (strict v4.2 window): Business 18.52% / +22.67%, Growth 18.32% / +24.71%.
- Weighting by deal `Initial_List_Price`: Business 18.77% / +22.42%, Growth 19.13% / +25.48%.
- Using `Discount_Requested_%` rather than the approved discount: Business +31.72%, Growth +34.62%.

### Read‑through
Growth is the bigger policy breach **relative to its threshold (+26.42% vs +23.68%)** despite a slightly lower absolute discount (18.57% vs 18.70%), because Growth's policy threshold is tighter (14.69% vs 15.12%). The absolute overage is also larger for Growth (+3.88 pp vs +3.58 pp).

**File produced:** `1. Analysis/Discount_vs_Policy_Threshold_by_Tier.md` (sources, method, headline table, sensitivities).