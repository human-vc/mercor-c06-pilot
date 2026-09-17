Based on the client data room files—specifically the **Discount Approval Logs** (`Brightpath_Discount_Approval_Logs_v1.0.xlsx`), along with the context from the **Latest Pricing Version** (`v4.2`) and the **Revenue Data by Segment**—here are the calculations and results:

---

### **Summary of Results**

* **Business Discount:** **18.70%**
* **Growth Discount:** **18.57%**
* **Business Threshold-Relative Variance:** **23.68%**
* **Growth Threshold-Relative Variance:** **26.42%** *(or **26.41%** if calculated from rounded intermediate figures)*

---

### **Detailed Calculation Breakdown**

#### **1. Business Tier**
* **Sample Size ($N$):** 214 approved deals
* **Final Approved Discount:**
  * Sum = $4,001\%$
  * Average Discount = $\frac{4,001}{214} \approx 18.69626\% \rightarrow$ **18.70%**
* **Policy Threshold:**
  * Sum = $3,235\%$
  * Average Policy Threshold = $\frac{3,235}{214} \approx 15.11682\% \rightarrow$ **15.12%**
* **Threshold-Relative % Variance:**
  $$\% \text{Variance} = \frac{\text{Average Discount} - \text{Average Policy Threshold}}{\text{Average Policy Threshold}} \times 100$$
  * Exact calculation: $\frac{4,001 - 3,235}{3,235} = \frac{766}{3,235} \approx 23.67852\% \rightarrow$ **23.68%**
  * Using rounded inputs: $\frac{18.70\% - 15.12\%}{15.12\%} \approx 23.67725\% \rightarrow$ **23.68%**

---

#### **2. Growth Tier**
* **Sample Size ($N$):** 176 approved deals
* **Final Approved Discount:**
  * Sum = $3,268\%$
  * Average Discount = $\frac{3,268}{176} \approx 18.56818\% \rightarrow$ **18.57%**
* **Policy Threshold:**
  * Sum = $2,585\%$
  * Average Policy Threshold = $\frac{2,585}{176} = 14.68750\% \rightarrow$ **14.69%**
* **Threshold-Relative % Variance:**
  $$\% \text{Variance} = \frac{\text{Average Discount} - \text{Average Policy Threshold}}{\text{Average Policy Threshold}} \times 100$$
  * Exact calculation: $\frac{3,268 - 2,585}{2,585} = \frac{683}{2,585} \approx 26.42166\% \rightarrow$ **26.42%**
  * Using rounded inputs: $\frac{18.57\% - 14.69\%}{14.69\%} \approx 26.41253\% \rightarrow$ **26.41%**

---

### **Additional Analytical Context & Alternatives**

1. **Absolute Percentage-Point Spread:**
   * **Business:** $18.70\% - 15.12\% = +\mathbf{3.58\%}$ (percentage points above policy threshold)
   * **Growth:** $18.57\% - 14.69\% = +\mathbf{3.88\%}$ (percentage points above policy threshold)

2. **Deals Effective Under Pricing Version v4.2 Only (Post April 1, 2024):**
   * **Business ($N=161$):** Average Discount = **18.52%**, Average Policy Threshold = **15.09%**, Threshold-Relative Variance = **22.67%**
   * **Growth ($N=130$):** Average Discount = **18.32%**, Average Policy Threshold = **14.69%**, Threshold-Relative Variance = **24.71%**

3. **Discount Requested vs. Policy Threshold:**
   * **Business:** Average Requested Discount = **19.91%**, Relative Variance = **31.72%**
   * **Growth:** Average Requested Discount = **19.77%**, Relative Variance = **34.62%**