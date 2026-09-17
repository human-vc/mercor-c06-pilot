## Answer

**Primary result** (average of the tier's deals in the discount log; per your instruction the size-range midpoints are applied only to the Company Size segment rows):

| | Business | Growth |
|---|---|---|
| **Average discount** | **18.70%** | **18.57%** |
| Average policy threshold | 15.12% | 14.69% |
| **% variance vs. average threshold** | **+23.68%** | **+26.42%** |

**Sensitivity — if each log deal is weighted by the segment user count (band midpoint):**

| | Business | Growth |
|---|---|---|
| User-weighted average discount | 18.60% | 19.01% |
| User-weighted average threshold | 15.13% | 15.17% |
| % variance | +22.87% | +25.34% |

Both tiers are discounting roughly a quarter above their own policy thresholds — i.e., ~3.6 pts (Business) and ~3.9 pts (Growth) of leakage per deal.

### Inputs used
- **Latest pricing version:** v4.2, effective 2024-04-01 (`Brightpath_Historical_Pricing_Versions_ChangeLog.xlsx`) — Business $32/user/mo, Growth $58/user/mo (Team $15, Enterprise $110 base).
- **Revenue by segment:** `Brightpath_Revenue_by_Segment.xlsx` → `ARR_by_Company_Size`: Small Practice 10–50 (midpoint 30), Mid-Market 51–250 (150.5), Upper Mid-Market 251–500 (375.5); 3,983 customers → ≈321,840 users.
- **Discount approval logs:** `Brightpath_Discount_Approval_Logs_v1.0.xlsx`, 800 rows, all 2024 (the duplicate "(1)" copy is byte-for-byte identical in data — 0 differing rows). Business = 214 deals, Growth = 176. Discounts = `Final_Approved_Discount_%`; thresholds = mean of `Policy_Threshold_%` (which varies 10/15/20 by deal).
- **Variance formula:** (avg discount − avg threshold) ÷ avg threshold. Using `Discount_Requested_%` instead of the approved figure would give +31.72% (Business) and +34.62% (Growth).

### Caveats worth flagging
1. The discount logs contain **no company-size field**, so a true midpoint-weighted tier average requires mapping each deal to a size band via implied users = `Initial_List_Price ÷ (v4.2 price × 12)`. That mapping is imperfect: 75 of 214 Business deals imply >500 users (out of range), so I capped them in the top band. Deal-level `Pricing_Tier` also disagrees with the log's tier for ~75% of matching Deal_IDs, and the `Customer_Size_Segment` in the transaction file is randomly distributed across tiers — so I did not use it as the primary weighting.
2. Tier assignment in the logs is not corroborated by the transaction data; if the tier labels are unreliable, the per-tier splits carry that uncertainty (the all-tier average discount is 18.0%, consistent with the 18.01% quoted in the exec deck).
3. `Brightpath_NRR_ARR_by_Tier_v1.0.xlsx` shows 1,200 Business and 1,500 Growth customers, which cannot be reconciled with the 3,983-customer / company-size view in the revenue file — a data-quality item to raise with the client.

### File produced
- **`Discount_vs_Threshold_Analysis.xlsx`** — 4 tabs: `Summary` (primary, cross-check and sensitivity figures with source/method notes), `Deal_detail_weighting` (all 390 Business+Growth log rows with implied users, size band, midpoint weight), `Band_counts` (per-tier/per-band weighted averages), `Revenue_by_Segment_users` (midpoint → user-count build-up).