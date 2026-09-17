Based on the Golden Everest REIT model (`Financials/Golden_Everest_REIT_Analysis.xlsx`), here is the step-by-step calculation of the inflation-adjusted enterprise value and target share price for 2025.

---

### **1. Key Inputs from the Model**

* **2024 Revenue Breakdown** (`Historicals` sheet):
  * Storage & Data Center Revenue: **$4,453.0 million**
  * Service Revenue: **$895.0 million**
  * Other Revenue: **$72.0 million**
  * **Total Revenue (2024):** **$5,420.0 million**
  * **Proportion of Service Revenue ($p$):** $\frac{\$895.0}{\$5,420.0} \approx \mathbf{16.5129\%}$
  * **Non-Service Revenue Proportion ($1 - p$):** $\mathbf{83.4871\%}$

* **2025 Forecast Base Case** (`Projections (C-Corp)` & `REIT Conversion` sheets):
  * **Forecast Revenue (2025E):** **$5,826.50 million**
  * **EBITDA Margin:** **43.0%**
  * **Forecast EBITDA (2025E):** $5,826.50 \times 43.0\% = \mathbf{\$2,505.395 \text{ million}}$
  * **Forecast Operational Expenses (excl. D&A):** $\$5,826.50 - \$2,505.395 = \mathbf{\$3,321.105 \text{ million}}$
  * **Net Debt:** **$4,737.0 million**
  * **Shares Outstanding:** **285.0 million**
  * **REIT Industry Capitalization Rate:** **5.5%** ($0.055$)

---

### **2. Inflation Adjustment to Operational Expenses & EBITDA**

1. **Total Inflation Impact on Operational Expenses (2%):**
   $$\Delta \text{OpEx}_{\text{total}} = 2\% \times \$3,321.105 \text{ million} = \mathbf{\$66.422 \text{ million}}$$

2. **Allocation by Revenue Proportion:**
   * **Service-derived OpEx increase (passed on to clients):**
     $$\Delta \text{OpEx}_{\text{service}} = 16.5129\% \times \$66.422 \text{ million} = \mathbf{\$10.968 \text{ million}}$$
     *(Because this increase is fully passed on via Services revenues, it is offset dollar-for-dollar by a corresponding revenue increase and has a net zero impact on EBITDA.)*
   * **Non-Service-derived OpEx increase (cannot be passed on):**
     $$\Delta \text{OpEx}_{\text{other}} = (1 - 16.5129\%) \times \$66.422 \text{ million} = \mathbf{\$55.454 \text{ million}}$$

3. **Inflation-Adjusted 2025E EBITDA:**
   $$\text{EBITDA}_{\text{adj}} = \$2,505.395 \text{ million} - \$55.454 \text{ million} = \mathbf{\$2,449.941 \text{ million}}$$

---

### **3. Valuation Based on 5.5% Capitalization Rate**

1. **Inflation-Adjusted Enterprise Value:**
   $$\text{Enterprise Value} = \frac{\text{Adjusted EBITDA}}{\text{Cap Rate}} = \frac{\$2,449.941 \text{ million}}{0.055} = \mathbf{\$44,544.38 \text{ million}}$$
   * Rounded to the nearest whole number: **$44,544 million**

2. **Inflation-Adjusted Equity Value:**
   $$\text{Equity Value} = \text{Enterprise Value} - \text{Net Debt} = \$44,544.38 \text{ million} - \$4,737.0 \text{ million} = \mathbf{\$39,807.38 \text{ million}}$$
   * Rounded to the nearest whole number: **$39,807 million**

3. **Target Share Price:**
   $$\text{Target Share Price} = \frac{\$39,807.38 \text{ million}}{285.0 \text{ million shares}} = \mathbf{\$139.68}$$

---

### **Summary of Results**

* **Inflation-Adjusted 2025E EBITDA:** **$2,450 million**
* **Inflation-Adjusted Enterprise Value:** **$44,544 million**
* **Target Share Price (2025):** **$139.68**

*(Note: If using the unrounded base EBITDA of $2,504.0 million present in select sensitivity tables, the adjusted EV is **$44,519 million** with a target share price of **$139.58**; if total operating expenses include D&A of $670 million, the adjusted EV is **$44,341 million** with a target share price of **$138.96**).*