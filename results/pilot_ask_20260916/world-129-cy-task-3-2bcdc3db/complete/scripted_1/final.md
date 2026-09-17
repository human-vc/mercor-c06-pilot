To determine the average discount percentages and threshold-relative variances for the **Business** and **Growth** tiers, we synthesize the relevant data across the three referenced files:

1. **Latest Pricing Version (v4.2)** (*`Brightpath_Historical_Pricing_Versions_ChangeLog.xlsx`*):
   - **Business Tier:** **$32.00 / user / month** ($384.00 / user / year)
   - **Growth Tier:** **$58.00 / user / month** ($696.00 / user / year)

2. **Revenue Data by Segment** (*`Brightpath_Revenue_by_Segment.xlsx`*):
   - **Business Tier** aligns with **Mid-Market (51–250 employees)**:
     - **Company Size Range:** 51 to 250 employees $\rightarrow$ Midpoint user count = **150.5** (or integer midpoint **150**)
     - **List Price per Account:** $150.5 \times \$384.00 = \mathbf{\$57,792.00}$ (or $150 \times \$384.00 = \$57,600.00$)
     - **Actual Realized ARPU:** Total ARR / Total Customers = $\$45,600,000 / 1,080 = \mathbf{\$42,222.22}$ (unweighted/table ARPU = $\$42,317.12$)
     - **Discount Percentage:** 
       - Using Weighted ARPU & exact midpoint (150.5): $1 - \frac{\$42,222.22}{\$57,792.00} = \mathbf{26.94\%}$
       - Using Integer midpoint (150): $1 - \frac{\$42,222.22}{\$57,600.00} = \mathbf{26.70\%}$
       - Using Simple/Sheet ARPU ($42,317.12): **26.78%** (midpoint 150.5) or **26.53%** (midpoint 150)
   - **Growth Tier** aligns with **Upper Mid-Market (251–500 employees)**:
     - **Company Size Range:** 251 to 500 employees $\rightarrow$ Midpoint user count = **375.5** (or integer midpoint **375**)
     - **List Price per Account:** $375.5 \times \$696.00 = \mathbf{\$261,348.00}$ (or $375 \times \$696.00 = \$261,000.00$)
     - **Actual Realized ARPU:** Total ARR / Total Customers = $\$20,400,000 / 209 = \mathbf{\$97,607.66}$ (unweighted/table ARPU = $\$100,742.68$)
     - **Discount Percentage:**
       - Using Weighted ARPU & exact midpoint (375.5): $1 - \frac{\$97,607.66}{\$261,348.00} = \mathbf{62.65\%}$
       - Using Integer midpoint (375): $1 - \frac{\$97,607.66}{\$261,000.00} = \mathbf{62.60\%}$
       - Using Simple/Sheet ARPU ($100,742.68): **61.45%** (midpoint 375.5) or **61.40%** (midpoint 375)

3. **Discount Approval Logs** (*`Brightpath_Discount_Approval_Logs_v1.0.xlsx`*):
   - **Average Policy Thresholds:**
     - **Business:** **15.12%** ($15.1168\%$)
     - **Growth:** **14.69%** ($14.6875\%$)
   - *(Note: If average discount is taken directly from `Final_Approved_Discount_%` in the approval logs: Business = **18.70%**, Growth = **18.57%**)*

---

### Primary Results (Calculated via Revenue by Segment & Latest Pricing Model)
Using the exact midpoint of each tier's company size range (150.5 and 375.5) and weighted ARPU:

* **Business discount:** **26.94%** *(or **26.70%** using integer midpoint 150; **26.78%** using simple ARPU)*
* **Growth discount:** **62.65%** *(or **62.60%** using integer midpoint 375; **61.45%** using simple ARPU)*
* **Business threshold-relative variance:** **+78.22%** *(relative variance vs. 15.12% threshold; absolute difference is **+11.82%**)*
* **Growth threshold-relative variance:** **+326.57%** *(relative variance vs. 14.69% threshold; absolute difference is **+47.96%**)*

---

### Alternative Interpretation (Directly from Discount Approval Logs)
If using the historical approved discount rates directly logged in the discount approval records:

* **Business discount:** **18.70%**
* **Growth discount:** **18.57%**
* **Business threshold-relative variance:** **+23.68%** *(absolute difference: **+3.58%**)*
* **Growth threshold-relative variance:** **+26.42%** *(absolute difference: **+3.88%**)*