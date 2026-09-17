### **Executive Summary**

Based on the Golden Everest REIT model, applying a **2% inflation rate** to operational expenses with a pass-through mechanism applicable solely to **Services revenues**, and valuing the business using the **REIT industry capitalization rate of 5.5%**, the results for 2025E are:

* **Inflation-Adjusted Enterprise Value:** **$44,544 million**
* **Target Share Price:** **$139.68** *(or **$139.67** based on rounded equity value of $39,807 million)*

---

### **Detailed Step-by-Step Methodology & Calculation**

#### **1. Baseline 2024 Revenue Proportions**
From the Historical Financials (`Historicals` sheet):
* **Storage & Data Center Revenue (2024A):** $4,453.0 million
* **Service Revenue (2024A):** $895.0 million
* **Other Revenue (2024A):** $72.0 million
* **Total Revenue (2024A):** **$5,420.0 million**

$$\text{Service Revenue Proportion (2024A)} = \frac{\$895.0\text{ mm}}{\$5,420.0\text{ mm}} \approx 16.5129\% \quad \left(\frac{179}{1,084}\right)$$

---

#### **2. 2025E Forecast Operational Expenses (Pre-Inflation)**
From the REIT Financial Projections (`Projections (C-Corp)` and `REIT Conversion` sheets):
* **2025E Total Revenue:** $5,826.500 million
* **2025E EBITDA (43.0% margin):** $2,505.395 million
* **2025E Operational Expenses ($\text{Revenue} - \text{EBITDA}$):** 
  $$\$5,826.500\text{ mm} - \$2,505.395\text{ mm} = \$3,321.105\text{ million}$$

---

#### **3. Operational Expenses Deriving from Service Revenue**
Per the prompt's assumption, the proportion of forecast operating expenses deriving from Service revenue is equal to the 2024 Service revenue share ($16.5129\%$):
* **Service-Derived OpEx:** 
  $$\$3,321.105\text{ mm} \times 16.5129\% = \$548.411\text{ million}$$
* **Non-Service OpEx (Storage, Data Center & Other):** 
  $$\$3,321.105\text{ mm} \times (1 - 0.165129) = \$3,321.105\text{ mm} \times 83.4871\% = \$2,772.694\text{ million}$$

---

#### **4. Impact of 2% Inflation & Revenue Pass-Through**
* **Total OpEx Inflation Increase (+2.0%):**
  $$\Delta \text{OpEx}_{\text{total}} = \$3,321.105\text{ mm} \times 2.0\% = +\$66.4221\text{ million}$$
* **Increase in Service-Derived OpEx:**
  $$\Delta \text{OpEx}_{\text{service}} = \$548.411\text{ mm} \times 2.0\% = +\$10.9682\text{ million}$$
* **Increase in Non-Service OpEx:**
  $$\Delta \text{OpEx}_{\text{non-service}} = \$2,772.694\text{ mm} \times 2.0\% = +\$55.4539\text{ million}$$

**Pass-Through Mechanism:**
* Because cost increases can be passed on **only for Services revenues**, Service revenue increases by the **$10.9682 million** cost increase, neutralizing the inflation impact on services.
* The non-service cost increase of **$55.4539 million** cannot be passed on and must be absorbed.

**Net Impact on 2025E EBITDA (NOI):**
$$\Delta \text{EBITDA} = \Delta \text{Revenue} - \Delta \text{OpEx}_{\text{total}} = +\$10.9682\text{ mm} - \$66.4221\text{ mm} = -\$55.4539\text{ million}$$

$$\text{Adjusted 2025E EBITDA} = \$2,505.395\text{ mm} - \$55.4539\text{ mm} = \mathbf{\$2,449.941\text{ million}}$$

---

#### **5. Valuation at 5.5% Capitalization Rate**
Using the standard REIT industry valuation formula ($\text{Enterprise Value} = \frac{\text{NOI / EBITDA}}{\text{Cap Rate}}$):

* **REIT Capitalization Rate:** $5.5\%$ ($0.055$)
* **Inflation-Adjusted Enterprise Value:**
  $$\text{Enterprise Value} = \frac{\$2,449.9411\text{ mm}}{0.055} = \mathbf{\$44,544.38\text{ million}} \longrightarrow \mathbf{\$44,544\text{ million}}$$

---

#### **6. Bridge to Target Share Price**
* **Enterprise Value:** $44,544.38 million
* **Less Net Debt:** $-\$4,737.00$ million *(Total Debt of $7,350M less Cash of $675M at conversion baseline; row 34 of Valuation Summary)*
* **Inflation-Adjusted Equity Value:**
  $$\text{Equity Value} = \$44,544.38\text{ mm} - \$4,737.00\text{ mm} = \mathbf{\$39,807.38\text{ million}} \longrightarrow \mathbf{\$39,807\text{ million}}$$
* **Diluted Shares Outstanding:** $285.0$ million

$$\text{Target Share Price} = \frac{\$39,807.384\text{ mm}}{285.0\text{ mm shares}} = \mathbf{\$139.68\text{ per share}}$$
*(Using rounded Equity Value of $39,807M: $\frac{\$39,807\text{ mm}}{285.0\text{ mm}} = \mathbf{\$139.67\text{ per share}}$)*

---

### **Summary Table: Pre-Inflation vs. Post-Inflation REIT Valuation**

| Metric | Pre-Inflation Base (5.5% Cap Rate) | Inflation Impact (2% OpEx, Pass-Through on Services) | Post-Inflation Adjusted |
| :--- | :---: | :---: | :---: |
| **Total Revenue ($mm)** | $5,827 | +$11 | $5,837 |
| **Operational Expenses ($mm)** | $3,321 | +$66 | $3,388 |
| **2025E EBITDA / NOI ($mm)** | $2,505 | -$55 | **$2,450** |
| **Capitalization Rate** | 5.50% | — | **5.50%** |
| **Enterprise Value ($mm)** | **$45,553** | -$1,008 | **$44,544** |
| **Less: Net Debt ($mm)** | ($4,737) | — | ($4,737) |
| **Equity Value ($mm)** | **$40,816** | -$1,008 | **$39,807** |
| **Shares Outstanding (mm)** | 285.0 | — | 285.0 |
| **Target Share Price ($)** | **$143.21** | -$3.53 | **$139.68** |

---

### **Sensitivity & Methodological Notes**

1. **Base EBITDA Rounding ($2,504mm vs. $2,505.4mm):**
   * If using the rounded base EBITDA of $2,504.0 million (from row 4 of `Sensitivity Analysis`):
     * Adjusted EBITDA = $2,448.52 million
     * Enterprise Value = **$44,519 million**
     * Target Share Price = **$139.58**
2. **Multiple Equivalence (18.2x Multiple):**
   * In the model's peer comparison sheet, the median data center REIT multiple is 18.2x ($\approx \frac{1}{5.495\%}$). If valued directly at 18.2x adjusted EBITDA rather than $\frac{1}{0.055}$:
     * Enterprise Value = **$44,589 million**
     * Target Share Price = **$139.83**
3. **Total OpEx Including D&A ($3,991.1mm):**
   * If inflation were applied to operating expenses including non-cash D&A ($670mm):
     * Adjusted EBITDA = $2,438.75 million
     * Enterprise Value = **$44,341 million**
     * Target Share Price = **$138.96**