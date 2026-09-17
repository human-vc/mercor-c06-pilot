### **1. Executive Summary & Key Results**

Based on the **REIT model (`Financials/Golden_Everest_REIT_Analysis.xlsx`)**, incorporating a **2% inflation rate** on operational expenses with pass-through capability restricted to **Services revenues**, the updated 2025 financial and valuation metrics for Golden Everest are summarized below.

The valuation is evaluated across the primary REIT valuation benchmarks established in the model:
1. **REIT Industry Benchmark (Median Peer Multiple: 18.20x / Cap Rate: ~5.49%)**: The benchmark valuation multiple derived directly from the Data Center REIT comparable peer group.
2. **REIT Model Base Case (Applied Mid-Case Multiple: 16.38x / Cap Rate: ~6.11%)**: The model’s target multiple ($18.20\text{x} \times 0.90$) utilized in the *Valuation Summary*, *Executive Summary*, and the *Board Presentation* (Project Titan) to derive the pre-inflation base target share price of $127.37.

---

### **Summary of Inflation-Adjusted Valuation (2025E)**

| Metric | Pre-Inflation Base Model | Inflation-Adjusted (REIT Industry Median: 18.20x) | Inflation-Adjusted (REIT Model Mid Applied: 16.38x) |
| :--- | :---: | :---: | :---: |
| **Total Revenue ($mm)** | $5,827 | **$5,837** | **$5,837** |
| **Cash Operational Expenses ($mm)** | $3,321 | **$3,388** | **$3,388** |
| **Adjusted EBITDA ($mm)** | $2,505 | **$2,450** | **$2,450** |
| **Enterprise Value ($mm)** | $41,038 *(at 16.38x)* / $45,598 *(at 18.20x)* | **$44,589** | **$40,130** |
| **Less: Net Debt ($mm)** | ($4,737) | **($4,737)** | **($4,737)** |
| **Equity Value ($mm)** | $36,301 *(at 16.38x)* / $40,861 *(at 18.20x)* | **$39,852** | **$35,393** |
| **Shares Outstanding (mm)** | 285.0 | **285.0** | **285.0** |
| **Target Share Price ($)** | $127.37 *(at 16.38x)* / $143.37 *(at 18.20x)* | **$139.83** | **$124.19** |

*Note: Per prompt instructions, monetary values are rounded to the nearest whole $ million, and share prices to 2 decimal places.*

---

### **2. Detailed Step-by-Step Methodology & Calculations**

#### **Step 1: Service Revenue Proportion in 2024**
From the `Historicals` sheet (Row 8 & 10):
- **2024A Service Revenue**: $\$895.0\text{ million}$
- **2024A Total Revenue**: $\$5,420.0\text{ million}$
- **Proportion of Total Revenue deriving from Services ($p$)**:
  $$p = \frac{\$895.0\text{ mm}}{\$5,420.0\text{ mm}} = \frac{179}{1084} \approx 16.512915\%$$

#### **Step 2: Base 2025E Operational Expenses**
From the `Projections (C-Corp)` sheet (Rows 16 & 19):
- **2025E Forecast Revenue**: $\$5,826.50\text{ million}$
- **2025E EBITDA Margin**: $43.00\%$
- **2025E EBITDA**: $\$5,826.50\text{ mm} \times 43.0\% = \$2,505.395\text{ million}$
- **2025E Forecast Operational Expenses (Cash OpEx)**:
  $$\text{Base OpEx} = \text{Revenue} - \text{EBITDA} = \$5,826.50 - \$2,505.395 = \$3,321.105\text{ million}$$

#### **Step 3: Inflation Impact & Revenue Pass-Through**
- **Inflation Rate**: $2.0\%$
- **Total Operational Expense Increase**:
  $$\Delta \text{OpEx}_{\text{total}} = \$3,321.105\text{ mm} \times 2.0\% = +\$66.4221\text{ million}$$

Per the prompt, the proportion of operational expenses deriving from Service revenue equals $p \approx 16.5129\%$:
- **OpEx Deriving from Service Revenue**:
  $$\text{OpEx}_{\text{Service}} = \$3,321.105\text{ mm} \times 16.512915\% = \$548.41125\text{ million}$$
- **Increase in Service OpEx (Passed through to Customers)**:
  $$\Delta \text{Revenue} = \Delta \text{OpEx}_{\text{Service}} = \$548.41125\text{ mm} \times 2.0\% = +\$10.968225\text{ million}$$
- **OpEx Deriving from Non-Service Revenue (Storage & Data Center)**:
  $$\text{OpEx}_{\text{Non-Service}} = \$3,321.105\text{ mm} \times (1 - 0.16512915) = \$2,772.69375\text{ million}$$
- **Unrecoverable Expense Increase**:
  $$\Delta \text{OpEx}_{\text{unrecoverable}} = \$2,772.69375\text{ mm} \times 2.0\% = +\$55.453875\text{ million}$$

#### **Step 4: Inflation-Adjusted 2025E EBITDA**
$$\Delta \text{EBITDA} = \Delta \text{Revenue} - \Delta \text{OpEx}_{\text{total}} = +\$10.968225 - \$66.422100 = -\$55.453875\text{ million}$$
$$\text{Adjusted EBITDA} = \$2,505.395 - \$55.453875 = \mathbf{\$2,449.941125\text{ million}} \approx \mathbf{\$2,450\text{ million}}$$

---

### **3. Valuation Based on REIT Capitalization Rates**

In corporate REIT valuation, the property capitalization rate ($\text{Cap Rate} = \frac{\text{NOI}}{\text{EV}}$) is the direct inverse of the EV/EBITDA multiple ($\text{EV} = \frac{\text{EBITDA}}{\text{Cap Rate}} = \text{EBITDA} \times \text{Multiple}$).

From the model's `Comparable Companies` and `Valuation Summary` sheets:
- **Net Debt**: $\$4,737.0\text{ million}$
- **Diluted Shares Outstanding**: $285.0\text{ million}$

#### **A. REIT Industry Benchmark (Median Multiple: 18.20x | Cap Rate: 5.4945%)**
From `Comparable Companies` (Row 15 & Row 49) / `Valuation Summary` (Row 31 High):
- **Enterprise Value**:
  $$\text{EV} = \$2,449.941125\text{ mm} \times 18.20 = \$44,588.9285\text{ mm} \rightarrow \mathbf{\$44,589\text{ million}}$$
- **Equity Value**:
  $$\text{Equity Value} = \$44,588.9285\text{ mm} - \$4,737.00\text{ mm} = \$39,851.9285\text{ mm} \rightarrow \mathbf{\$39,852\text{ million}}$$
- **Target Share Price**:
  $$\text{Share Price} = \frac{\$39,851.9285\text{ mm}}{285.0\text{ mm shares}} = \mathbf{\$139.83}$$

#### **B. REIT Model Applied Case (Target Mid Multiple: 16.38x | Cap Rate: 6.1050%)**
From `Valuation Summary` (Row 31 Mid: $18.20\text{x} \times 0.90$) / `Executive Summary` (Row 16 & 21):
- **Enterprise Value**:
  $$\text{EV} = \$2,449.941125\text{ mm} \times 16.38 = \$40,130.0356\text{ mm} \rightarrow \mathbf{\$40,130\text{ million}}$$
- **Equity Value**:
  $$\text{Equity Value} = \$40,130.0356\text{ mm} - \$4,737.00\text{ mm} = \$35,393.0356\text{ mm} \rightarrow \mathbf{\$35,393\text{ million}}$$
- **Target Share Price**:
  $$\text{Share Price} = \frac{\$35,393.0356\text{ mm}}{285.0\text{ mm shares}} = \mathbf{\$124.19}$$

---

### **4. Sensitivity Matrix Across Valuation Multiples**

| Scenario / Valuation Basis | EV/EBITDA Multiple | Implied Cap Rate | Enterprise Value ($mm) | Equity Value ($mm) | Target Share Price ($) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Model Applied Low Case** | 15.47x | 6.46% | **$37,901** | **$33,164** | **$116.36** |
| **Model Target / Applied Mid Case** | **16.38x** | **6.11%** | **$40,130** | **$35,393** | **$124.19** |
| **REIT Industry Median Benchmark** | **18.20x** | **5.49%** | **$44,589** | **$39,852** | **$139.83** |
| **REIT Industry Peer Mean** | 18.60x | 5.38% | **$45,569** | **$40,832** | **$143.27** |
| *Size-Adjusted Comp Reference* | 8.30x | 12.05% | **$20,335** | **$15,598** | **$54.73** |