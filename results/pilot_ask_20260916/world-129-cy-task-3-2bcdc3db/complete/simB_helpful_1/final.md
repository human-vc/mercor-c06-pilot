To determine the average discount percentages and their variances relative to policy thresholds, we integrate data from the three specified sources:
1. **Latest Pricing Version (`v4.2`):**
   - **Business Tier:** $\$32.00$ / user / month ($\$384.00$ / user / year)
   - **Growth Tier:** $\$58.00$ / user / month ($\$696.00$ / user / year)
2. **Revenue Data by Segment (`Brightpath_Revenue_by_Segment.xlsx`):**
   - **Business Tier (Mid-Market: 51–250 employees):** Exact range midpoint $= \frac{51 + 250}{2} = 150.5$ users. List ARR per customer $= 150.5 \times \$32 \times 12 = \$57,792.00$.
   - **Growth Tier (Upper Mid-Market: 251–500 employees):** Exact range midpoint $= \frac{251 + 500}{2} = 375.5$ users. List ARR per customer $= 375.5 \times \$58 \times 12 = \$261,348.00$.
   - Segment row discounts are calculated as $\text{Discount} = \frac{\text{List ARPU} - \text{Actual ARPU}}{\text{List ARPU}}$.
3. **Discount Approval Logs (`Brightpath_Discount_Approval_Logs_v1.0.xlsx`):**
   - **Business Tier Average Policy Threshold:** $15.12\%$ ($15.1168\%$)
   - **Growth Tier Average Policy Threshold:** $14.69\%$ ($14.6875\%$)

---

### **Primary Results (Standard Row-Level Segment Analysis with Exact Midpoints)**

* **Business Discount:** **26.78%** (26.7769%)
* **Growth Discount:** **61.45%** (61.4527%)
* **Business Threshold-Relative Variance:** **77.13%** (relative variance: $\frac{26.7769\% - 15.1168\%}{15.1168\%}$)
* **Growth Threshold-Relative Variance:** **318.40%** (relative variance: $\frac{61.4527\% - 14.6875\%}{14.6875\%}$)

---

### **Alternative Analytical Conventions**

Depending on specific rounding, weighting, or variance conventions used, the figures evaluate as follows:

1. **Rounded / Span Midpoints (150 users for Business, 375 users for Growth):**
   * **Business Discount:** **26.53%** (26.5328%)
   * **Growth Discount:** **61.40%** (61.4013%)
   * **Business Threshold-Relative Variance:** **75.52%**
   * **Growth Threshold-Relative Variance:** **318.05%**

2. **Overall Aggregate ARR-Weighted Basis (Total Actual ARR vs. Total List ARR):**
   * *Exact Midpoints (150.5 / 375.5):*
     * **Business Discount:** **26.94%** | **Variance:** **78.22%**
     * **Growth Discount:** **62.65%** | **Variance:** **326.57%**
   * *Rounded Midpoints (150 / 375):*
     * **Business Discount:** **26.70%** | **Variance:** **76.61%**
     * **Growth Discount:** **62.60%** | **Variance:** **326.23%**

3. **Absolute Percentage-Point Difference ($\text{Discount} - \text{Threshold}$):**
   * **Business Variance:** **+11.66%** ($26.78\% - 15.12\%$)
   * **Growth Variance:** **+46.77%** ($61.45\% - 14.69\%$)

4. **Direct Discount Approval Logs (`Final_Approved_Discount_%` in Logs):**
   * **Business Discount:** **18.70%** (18.6963%) | **Relative Variance:** **+23.68%** | **Absolute Variance:** **+3.58%**
   * **Growth Discount:** **18.57%** (18.5682%) | **Relative Variance:** **+26.42%** | **Absolute Variance:** **+3.88%**