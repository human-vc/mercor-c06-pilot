To determine the average discount percentage and threshold-relative variance for the **Business** and **Growth** tiers, we integrate data from the three specified sources:
1. **Latest Pricing Version (v4.2)** (`Brightpath_Historical_Pricing_Versions_ChangeLog.xlsx`):
   - **Business tier**: $\$32/\text{user/month}$ ($\$384/\text{user/year}$) — target segment: Mid-Market firms.
   - **Growth tier**: $\$58/\text{user/month}$ ($\$696/\text{user/year}$) — target segment: Upper Mid-Market firms.
2. **Revenue Data by Segment** (`Brightpath_Revenue_by_Segment.xlsx`):
   - **Mid-Market (51–250 employees)**: Midpoint user count $= \frac{51 + 250}{2} = 150.5$ users (or $150$ users). Total ARR $= \$45,600,000$ across $1,080$ customers ($\text{ARPU} = \$42,222.22$).
   - **Upper Mid-Market (251–500 employees)**: Midpoint user count $= \frac{251 + 500}{2} = 375.5$ users (or $375$ users). Total ARR $= \$20,400,000$ across $209$ customers ($\text{ARPU} = \$97,607.66$).
3. **Discount Approval Logs** (`Brightpath_Discount_Approval_Logs_v1.0.xlsx`):
   - **Business Tier Policy Threshold**: Average $= 15.12\%$ ($15.1168\%$).
   - **Growth Tier Policy Threshold**: Average $= 14.69\%$ ($14.6875\%$).

---

### **Primary Results**
*(Using segment-specific mapping, exact range midpoints, and weighted total ARR vs. list ARR)*:

- **Business discount**: **26.94%**
- **Growth discount**: **62.65%**
- **Business threshold-relative variance**: **78.22%**
- **Growth threshold-relative variance**: **326.57%**

---

### **Detailed Breakdown & Methodology**

#### 1. List Price per Customer
- **Business Tier** (Mid-Market: 51–250 employees):
  $$\text{List ARR per Customer} = 150.5 \text{ users} \times \$32/\text{mo} \times 12\text{ mos} = \$57,792.00$$
  $$\text{Total List ARR} = 1,080 \text{ customers} \times \$57,792.00 = \$62,415,360.00$$
  $$\text{Discount \%} = \frac{\$62,415,360.00 - \$45,600,000.00}{\$62,415,360.00} = \mathbf{26.94\%} \quad (26.9411\%)$$

- **Growth Tier** (Upper Mid-Market: 251–500 employees):
  $$\text{List ARR per Customer} = 375.5 \text{ users} \times \$58/\text{mo} \times 12\text{ mos} = \$261,348.00$$
  $$\text{Total List ARR} = 209 \text{ customers} \times \$261,348.00 = \$54,621,732.00$$
  $$\text{Discount \%} = \frac{\$54,621,732.00 - \$20,400,000.00}{\$54,621,732.00} = \mathbf{62.65\%} \quad (62.6522\%)$$

#### 2. Threshold-Relative Variance
Calculated as the relative percentage variance from each tier's average policy threshold:
$$\text{\% Variance} = \frac{\text{Discount \%} - \text{Policy Threshold \%}}{\text{Policy Threshold \%}} \times 100$$
- **Business**: $\frac{26.9411\% - 15.1168\%}{15.1168\%} \times 100 = \mathbf{78.22\%}$ (or $+11.82\text{ pp}$ absolute difference)
- **Growth**: $\frac{62.6522\% - 14.6875\%}{14.6875\%} \times 100 = \mathbf{326.57\%}$ (or $+47.96\text{ pp}$ absolute difference)

---

### **Alternative Calculation Variations**

For complete reference depending on the aggregation standard:

1. **Simple Arithmetic Mean of Segment Row Discounts (Exact Midpoints: 150.5 & 375.5)**:
   - Business discount: **26.78%** | Threshold-relative variance: **77.13%**
   - Growth discount: **61.45%** | Threshold-relative variance: **318.40%**

2. **Rounded/Integer Midpoints (150 & 375)**:
   - *Weighted*:
     - Business discount: **26.70%** | Threshold-relative variance: **76.61%**
     - Growth discount: **62.60%** | Threshold-relative variance: **326.23%**
   - *Simple Mean of Rows*:
     - Business discount: **26.53%** | Threshold-relative variance: **75.52%**
     - Growth discount: **61.40%** | Threshold-relative variance: **318.05%**

3. **Directly from `Final_Approved_Discount_%` in the Discount Approval Logs**:
   - Business discount: **18.70%** (18.6963%) | Threshold-relative variance: **23.68%** (or $+3.58\text{ pp}$)
   - Growth discount: **18.57%** (18.5682%) | Threshold-relative variance: **26.42%** (or $+3.88\text{ pp}$)