Based on the data in the **Discount Approval Logs** (`Brightpath_Discount_Approval_Logs_v1.0.xlsx`), along with reference to the **Latest Pricing Version** (v4.2, effective April 1, 2024 from `Brightpath_Historical_Pricing_Versions_ChangeLog.xlsx`) and the **Revenue by Segment** data (`Brightpath_Revenue_by_Segment.xlsx`), here are the calculated metrics:

---

### **Primary Results (Full Approval Logs Dataset, N = 800 deals)**

* **Business Discount:** **18.70%** *(exact: 18.6963%)*
* **Growth Discount:** **18.57%** *(exact: 18.5682%)*
* **Business Threshold-Relative Variance:** **+23.68%** *(exact: +23.6785%)*
* **Growth Threshold-Relative Variance:** **+26.42%** *(exact: +26.4217%)*

---

### **Detailed Breakdown & Methodology**

1. **Business Tier (214 deals):**
   * **Average Final Approved Discount:** $\frac{\sum \text{Final Approved Discount \%}}{214} = \mathbf{18.70\%}$ ($18.696262\%$)
   * **Average Policy Threshold:** $\frac{\sum \text{Policy Threshold \%}}{214} = \mathbf{15.12\%}$ ($15.116822\%$)
   * **Threshold-Relative Variance:** 
     $$\frac{18.696262\% - 15.116822\%}{15.116822\%} \times 100 = \mathbf{+23.68\%}$$
     *(Note: Using pre-rounded inputs $(18.70 - 15.12) / 15.12 \times 100 = +23.68\%$; absolute difference is $+3.58\%$ percentage points).*

2. **Growth Tier (176 deals):**
   * **Average Final Approved Discount:** $\frac{\sum \text{Final Approved Discount \%}}{176} = \mathbf{18.57\%}$ ($18.568182\%$)
   * **Average Policy Threshold:** $\frac{\sum \text{Policy Threshold \%}}{176} = \mathbf{14.69\%}$ ($14.687500\%$)
   * **Threshold-Relative Variance:** 
     $$\frac{18.568182\% - 14.687500\%}{14.687500\%} \times 100 = \mathbf{+26.42\%}$$
     *(Note: Using pre-rounded inputs $(18.57 - 14.69) / 14.69 \times 100 = +26.41\%$; absolute difference is $+3.88\%$ percentage points).*

---

### **Alternative: Filtered for Deals under the Latest Pricing Version (v4.2, $\ge$ April 1, 2024)**

If the logs are filtered to the effective window of the latest pricing version (v4.2, effective April 1, 2024):
* **Business Tier (161 deals):**
  * Average Discount: **18.52%** *(Policy Threshold: 15.09%)*
  * Threshold-Relative Variance: **+22.67%** *(from unrounded) / **+22.73%** (from rounded)*
* **Growth Tier (130 deals):**
  * Average Discount: **18.32%** *(Policy Threshold: 14.69%)*
  * Threshold-Relative Variance: **+24.71%** *(from unrounded and rounded)*