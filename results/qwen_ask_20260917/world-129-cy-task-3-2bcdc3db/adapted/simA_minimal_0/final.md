## Answer

| Metric | Business | Growth |
|---|---|---|
| **Average discount %** (mean of `Final_Approved_Discount_%`) | **18.70%** | **18.57%** |
| **% variance vs. average policy threshold** | **+23.68%** | **+26.42%** |

Supporting detail: Business = 214 approval-log deals, average `Policy_Threshold_%` of 15.12% (gap of +3.58 pts); Growth = 176 deals, average threshold of 14.69% (gap of +3.88 pts). Variance = (tier avg discount − tier avg threshold) ÷ tier avg threshold.

### How I got there
- **Latest pricing version:** `Brightpath_Historical_Pricing_Versions_ChangeLog.xlsx` → **v4.2** (effective 2024‑04‑01, no end date): Business $32/user/mo, Growth $58/user/mo. The whole discount log is dated 2024, so it is the v4.2‑era book of business.
- **Discount logs:** `Brightpath_Discount_Approval_Logs_v1.0.xlsx` (800 rows). The duplicate copy `…v1.0(1).xlsx` is identical row‑for‑row, so there is no version conflict. Thresholds are not a single tier constant — they vary deal‑by‑deal (10/15/20%), so each tier's "average policy threshold" is the mean of its own rows.
- **Revenue by segment:** `Brightpath_Revenue_by_Segment.xlsx` carries no tier field, so it cannot drive the tier averages directly; per your instruction I used the **midpoint of each Company‑Size range as the user count** (Small Practice 30, Mid‑Market 150.5, Upper Mid‑Market 375.5) to build a size‑weighted sensitivity (joined to deal size via `Deal_ID` in `Brightpath_Deal_Transactions_v1.0.xlsx`).

### Sensitivities (in case a different convention was intended)

| Method | Business disc. | Business var. | Growth disc. | Growth var. |
|---|---|---|---|---|
| Simple mean, all 800 log rows (**headline**) | 18.70% | +23.68% | 18.57% | +26.42% |
| Restricted to v4.2 window (approved ≥ 2024‑04‑01) | 18.52% | +22.67% | 18.32% | +24.71% |
| Weighted by `Initial_List_Price` | 18.77% | +22.42% | 19.13% | +25.48% |
| Weighted by size‑range midpoint (users) | 19.37% | +27.01% | 18.58% | +25.59% |
| Weighted by deal ARR | 19.15% | +29.20% | 18.64% | +24.03% |
| Using `Discount_Requested_%` instead of approved | 19.91% | +31.72% | 19.77% | +34.62% |

### Read‑through
Both tiers are running materially **out of policy** — roughly 24–26% above their allowed threshold — and **Growth is the worse offender in relative terms** (+26.42% vs. +23.68%) even though its absolute discount is slightly lower, because Growth's average threshold is 0.43 pts tighter. If requested discounts were granted as asked, the overage would balloon to ~+32% (Business) and ~+35% (Growth).

No files were created; the analysis is reproducible from the discount log, the pricing changelog (v4.2), the deal‑transaction file, and the revenue‑by‑segment file.