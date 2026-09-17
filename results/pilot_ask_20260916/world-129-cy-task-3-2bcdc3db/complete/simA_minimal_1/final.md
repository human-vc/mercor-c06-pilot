To determine the average discount percentage for the **Business** and **Growth** tiers and calculate their threshold-relative variances, we integrate the three referenced data sources:

1. **Latest Pricing Version (v4.2)** from `Brightpath_Historical_Pricing_Versions_ChangeLog.xlsx`:
   - **Business Tier:** $\$32.00$ / user / month ($\$384.00$ / user / year)
   - **Growth Tier:** $\$58.00$ / user / month ($\$696.00$ / user / year)

2. **Revenue Data by Segment** from `Brightpath_Revenue_by_Segment.xlsx` (`Revenue_by_Segment_Detail`):
   - **Business Tier $\rightarrow$ Mid-Market ($51$–$250$ employees):**
     - User Count (Midpoint): $\frac{51 + 250}{2} = 150.5$ users *(or $150.0$ integer midpoint)*
     - List Annual Value per Customer: $150.5 \times \$384.00 = \$57,792.00$ *(or $150.0 \times \$384.00 = \$57,600.00$)*
     - Actual Total ARR: $\$45,600,000$ across $1,080$ customers ($\text{ARPU} = \$42,222.22$)
     - Implied List Total ARR: $1,080 \times \$57,792.00 = \$62,415,360.00$
   - **Growth Tier $\rightarrow$ Upper Mid-Market ($251$–$500$ employees):**
     - User Count (Midpoint): $\frac{251 + 500}{2} = 375.5$ users *(or $375.0$ integer midpoint)*
     - List Annual Value per Customer: $375.5 \times \$696.00 = \$261,348.00$ *(or $375.0 \times \$696.00 = \$261,000.00$)*
     - Actual Total ARR: $\$20,400,000$ across $209$ customers ($\text{ARPU} = \$97,607.66$)
     - Implied List Total ARR: $209 \times \$261,348.00 = \$54,621,732.00$

3. **Discount Approval Logs** from `Brightpath_Discount_Approval_Logs_v1.0.xlsx`:
   - **Business Tier Average Policy Threshold:** $15.12\%$ ($15.1168\%$)
   - **Growth Tier Average Policy Threshold:** $14.69\%$ ($14.6875\%$)

---

### **Primary Results (Weighted Aggregate ARR, Exact Midpoint)**

* **Business Discount:** **26.94%** (unrounded: $26.9411\%$)
* **Growth Discount:** **62.65%** (unrounded: $62.6522\%$)
* **Business Threshold-Relative Variance:** **78.22%** (unrounded: $78.2191\%$; absolute: $+11.82$ percentage points)
* **Growth Threshold-Relative Variance:** **326.57%** (unrounded: $326.5684\%$; absolute: $+47.96$ percentage points)

$$\text{Threshold-Relative Variance} = \frac{\text{Discount} - \text{Policy Threshold}}{\text{Policy Threshold}} \times 100$$

---

### **Methodological Variations Breakdown**

Depending on whether midpoints are exact vs. rounded integers, or aggregated across total ARR vs. averaged across segment rows:

| Metric | Primary (Exact Midpoint, Weighted ARR) | Variant B (Exact Midpoint, Row-Level Mean) | Variant C (Integer Midpoint, Weighted ARR) | Variant D (Integer Midpoint, Row-Level Mean) | Variant E (Direct from Discount Logs) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Business Discount** | **26.94%** | **26.78%** | **26.70%** | **26.53%** | **18.70%** |
| **Growth Discount** | **62.65%** | **61.45%** | **62.60%** | **61.40%** | **18.57%** |
| **Business Threshold-Relative Variance** | **78.22%** | **77.13%** | **76.61%** | **75.52%** | **23.68%** |
| **Growth Threshold-Relative Variance** | **326.57%** | **318.40%** | **326.23%** | **318.05%** | **26.42%** |

*(Note: If calculated as absolute percentage point differences from policy thresholds, the variances are $+11.82\%$ for Business and $+47.96\%$ for Growth under the primary model, or $+3.58\%$ and $+3.88\%$ under Variant E).*