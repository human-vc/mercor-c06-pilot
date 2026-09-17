**Answer (headline = revenue-weighted using the company‑size midpoint as the user count, per your instruction)**

| Metric | Business | Growth |
|---|---|---|
| Average discount % | **19.37%** | **18.58%** |
| Average policy threshold % | 15.25% | 14.79% |
| **% variance vs. its average threshold** | **+27.01%** | **+25.59%** |

**How this was built**
- **Latest pricing version:** v4.2 in `Brightpath_Historical_Pricing_Versions_ChangeLog.xlsx` (effective 2024‑04‑01, no end date) → Business $32/user/mo, Growth $58/user/mo.
- **Discounts:** `Brightpath_Discount_Approval_Logs_v1.0.xlsx` — 800 rows, all dated 2024; Business n = 214, Growth n = 176 (by `Pricing_Tier`). The second copy `…v1.0(1).xlsx` is data‑identical, so it made no difference. Discount measured = `Final_Approved_Discount_%`; threshold = `Policy_Threshold_%` on the same deals.
- **Revenue weighting:** `Brightpath_Revenue_by_Segment.xlsx` company‑size ranges → midpoint users: Small Practice (10–50) = 30, Mid‑Market (51–250) = 150.5, Upper Mid‑Market (251–500) = 375.5. Each log deal was matched by `Deal_ID` to its size segment in `Brightpath_Deal_Transactions_v1.0.xlsx`, and weighted by midpoint users × v4.2 list price × 12 (within a tier this is equivalent to weighting by users, since the list price is constant).
- **Variance:** (avg discount − avg threshold) ÷ avg threshold × 100.

**Sensitivity (if you want a straight deal average instead of a revenue‑weighted one)**
- Business: discount 18.70%, threshold 15.12%, variance **+23.68%**
- Growth: discount 18.57%, threshold 14.69%, variance **+26.42%**
- On the v4.2 window only (approvals on/after 2024‑04‑01, n = 161/130), the unweighted variances are +22.67% (Business) and +24.71% (Growth).
- For reference, requested discounts (pre‑negotiation) run higher: 20.72% Business and 19.84% Growth ARR‑weighted.

**Read‑through:** both tiers are landing roughly 3.8–4.1 percentage points above their own policy ceiling — Business is the bigger offender in relative terms (+27.0% vs. +25.6%), and the leakage is concentrated in deals whose threshold was 10% but which closed at 20–30%+, mostly at VP/CFO approval levels.

**File produced:** `Tier_Discount_vs_Policy_Threshold_Analysis.xlsx` (tabs: `Summary`, `Deal_Detail` with per‑deal weights, `Method_Notes`).