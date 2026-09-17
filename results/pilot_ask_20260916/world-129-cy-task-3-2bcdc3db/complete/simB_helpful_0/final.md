To determine the average discount percentages and their variances relative to policy thresholds, the following datasets were analyzed in accordance with the specified instructions:

1. **Latest Pricing Version (v4.2 from the Historical Pricing Change Log):**
   * **Business Tier:** $\$32\text{ / user / month} = \$384\text{ / user / year}$
   * **Growth Tier:** $\$58\text{ / user / month} = \$696\text{ / user / year}$

2. **Revenue Data by Segment (`Revenue_by_Segment_Detail`):**
   * **Business Tier** aligns with **Mid-Market (51–250 employees)**:
     * Exact arithmetic midpoint: $(51 + 250) / 2 = \mathbf{150.5}\text{ users}$ *(span midpoint: $150.0\text{ users}$)*
     * List price per customer: $150.5 \times \$384 = \$57,792\text{ / year}$
     * Actual ARPU across segment rows averages $\$42,317.12$ (unweighted mean) / $\$42,222.22$ (revenue-weighted).
   * **Growth Tier** aligns with **Upper Mid-Market (251–500 employees)**:
     * Exact arithmetic midpoint: $(251 + 500) / 2 = \mathbf{375.5}\text{ users}$ *(span midpoint: $375.0\text{ users}$)*
     * List price per customer: $375.5 \times \$696 = \$261,348\text{ / year}$
     * Actual ARPU across segment rows averages $\$100,742.68$ (unweighted mean) / $\$97,607.66$ (revenue-weighted).

3. **Discount Approval Logs Policy Thresholds (`Policy_Threshold_%`):**
   * **Business Tier Average Policy Threshold:** **15.12%** ($15.1168\%$)
   * **Growth Tier Average Policy Threshold:** **14.69%** ($14.6875\%$)

---

### **Primary Results (Standard Segment Row Mean & Exact Midpoints)**

* **Business discount:** **26.78%**
* **Growth discount:** **61.45%**
* **Business threshold-relative variance:** **77.13%**
* **Growth threshold-relative variance:** **318.40%**

*(Variance calculated as relative percentage difference: $\frac{\text{Discount} - \text{Policy Threshold}}{\text{Policy Threshold}} \times 100$)*

---

### **Summary of Alternative Standard Conventions**

For complete analytical transparency across standard methodologies:

| Methodology / Convention | Business Discount | Growth Discount | Business Relative Variance | Growth Relative Variance | Business Percentage-Point Diff | Growth Percentage-Point Diff |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Exact Midpoints (150.5 / 375.5) — Simple Row Mean** | **26.78%** | **61.45%** | **77.13%** | **318.40%** | +11.66% | +46.77% |
| **Exact Midpoints (150.5 / 375.5) — Aggregate / Weighted** | **26.94%** | **62.65%** | **78.22%** | **326.57%** | +11.82% | +47.96% |
| **Span Midpoints (150 / 375) — Simple Row Mean** | **26.53%** | **61.40%** | **75.52%** | **318.05%** | +11.42% | +46.71% |
| **Span Midpoints (150 / 375) — Aggregate / Weighted** | **26.70%** | **62.60%** | **76.61%** | **326.23%** | +11.58% | +47.91% |
| **Directly from Discount Logs (`Final_Approved_Discount_%`)** | **18.70%** | **18.57%** | **23.68%** | **26.42%** | +3.58% | +3.88% |