## Answer

| Metric | Value |
|---|---|
| **Business tier – average discount** | **18.60%** (18.5959%) |
| **Growth tier – average discount** | **19.01%** (19.0131%) |
| **Business – %variance vs. its average policy threshold (15.13%)** | **+22.87%** |
| **Growth – %variance vs. its average policy threshold (15.17%)** | **+25.34%** |

### How I got there
- **Latest pricing = v4.2** (effective 2024‑04‑01, open‑ended end date) from `Brightpath_Historical_Pricing_Versions_ChangeLog.xlsx`: Business **$32**/user/mo, Growth **$58**/user/mo.
- **Company-size midpoints** from `Brightpath_Revenue_by_Segment.xlsx` → `ARR_by_Company_Size`: Small Practice 10–50 → **30**, Mid‑Market 51–250 → **150.5**, Upper Mid‑Market 251–500 → **375.5** users.
- **Discount logs** = `Brightpath_Discount_Approval_Logs_v1.0.xlsx` (800 rows; the `(1)` duplicate is data‑identical, so no reconciliation issue). Since the logs carry no size field, each deal's band was derived from its contract size at current list price (implied users = `Initial_List_Price ÷ (tier price × 12)`), then the band's midpoint was used as the user count weighting `Final_Approved_Discount_%` and `Policy_Threshold_%` within each tier.
- **Variance** = (avg discount − avg threshold) ÷ avg threshold. Band mix: Business 2/64/148 (n=214), Growth 13/87/76 (n=176).

**Read‑across:** both tiers are discounting ~a quarter above their approved ceilings, with Growth leaking slightly more (+25.34% vs +22.87%) — evidence that the discount-approval guardrails are not binding, which supports the pricing‑model recommendation to cut average discounting via feature/outcome bundling.

**Sensitivity (in case you want the unweighted view):** simple average discounts are Business 18.70% (+23.68% vs threshold) and Growth 18.57% (+26.42% vs threshold); weighting by raw implied users instead of band midpoints gives Business 18.77% (+22.42%) and Growth 19.13% (+25.48%). Using `Discount_Requested_%` rather than final approved would push both tiers to ~+34–36%.

**File produced:** `Discount_vs_Threshold_Calc.md` — sources, method, results, and the sensitivity table.