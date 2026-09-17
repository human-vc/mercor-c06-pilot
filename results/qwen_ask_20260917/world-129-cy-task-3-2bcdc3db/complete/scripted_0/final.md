Here are the results, using the midpoint of the Company Size range as the user count.

**Primary answers (rounded to 0.01%)**

| Metric | Business | Growth |
|---|---|---|
| Average discount % (user-count weighted) | **18.60%** | **19.01%** |
| % variance vs. average policy threshold | **+22.87%** | **+25.34%** |

**How I got there**

1. **Latest pricing version = v4.2** (Brightpath_Historical_Pricing_Versions_ChangeLog.xlsx, effective 1 Apr 2024, no end date): Business $32/user/mo, Growth $58/user/mo.
2. **Discount logs** = Brightpath_Discount_Approval_Logs_v1.0.xlsx, 800 rows (the "(1)" duplicate is byte-for-byte identical in data). 214 Business and 176 Growth deals; I used **Final_Approved_Discount_%** and each deal's **Policy_Threshold_%**.
3. **Company Size ranges / midpoints** = Brightpath_Revenue_by_Segment.xlsx → ARR_by_Company_Size: 10–50 (30), 51–250 (150.5), 251–500 (375.5). Since the logs carry no size field, implied users = Initial_List_Price ÷ (v4.2 price × 12), then each deal is placed in the band its implied user count falls in and weighted by that band's midpoint. Deals implying >500 users (mostly Business, list prices up to ~$294K) sit in the top band at 375.5.
4. **Averages:** Business weighted discount 18.5959% vs weighted threshold 15.1346% → (18.5959−15.1346)/15.1346 = +22.87%. Growth weighted discount 19.0131% vs weighted threshold 15.1692% → +25.34%.

**Sensitivity (in case you want the unweighted read):** a straight deal-count average gives Business 18.70% (+23.68% vs its 15.12% average threshold) and Growth 18.57% (+26.42% vs its 14.69% average threshold). The weighting only shifts things ~0.1–0.5 pt, so the conclusion is stable: both tiers are running roughly **23–26% above their approved discount ceiling**, i.e. ~3.5 pts (Business) and ~3.8 pts (Growth) of discount leakage off list.

**File produced:** `Business_Growth_Discount_vs_Threshold_Analysis.xlsx` — a "Deal_Level_Detail" tab (all 390 Business/Growth log deals with implied users, band, midpoint weight, discount and threshold) and a "Summary" tab with the weighted/unweighted averages and variance calculations, plus method and source notes.