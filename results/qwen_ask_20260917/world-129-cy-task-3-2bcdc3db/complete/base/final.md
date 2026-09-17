Thanks — I have everything I need except one weighting detail. Facts I've locked in: latest pricing = v4.2 (Business $32/user/mo, Growth $58/user/mo, from Brightpath_Historical_Pricing_Versions_ChangeLog); discount logs = Brightpath_Discount_Approval_Logs_v1.0 (800 rows; both copies are identical) using Final_Approved_Discount_% and the mean of Policy_Threshold_% per tier; company-size bands = Revenue_by_Segment (10–50, 51–250, 251–500 → midpoints 30 / 150.5 / 375.5).

The logs have no company-size column, only Initial_List_Price, so how should the "midpoint as user count" weighting be applied?

A) Implied users = Initial_List_Price ÷ (v4.2 price × 12) → map to the band it falls in → weight that deal's discount by the band midpoint (30/150.5/375.5). [75 of 214 Business deals imply >500 users — cap them at 375.5, or drop them?]
B) Same, but weight each deal by its raw implied user count (no banding).
C) No weighting: simple average discount per tier (Business 18.70%, Growth 18.57%) vs average threshold (Business 15.12%, Growth 14.69%).
D) Something else (e.g., join the logs to the deal-transaction file's Customer_Size_Segment, or weight by ARR from Revenue_by_Segment).

For reference, results are: C → Business 18.70% / +23.68%, Growth 18.57% / +26.42%; A (capped) → Business 18.60% / +22.87%, Growth 19.01% / +25.34%; B → Business 18.77% / +22.42%, Growth 19.13% / +25.48%. Also please confirm: use Final_Approved_Discount_% (not Discount_Requested_%) and variance = (avg discount − avg threshold) ÷ avg threshold.