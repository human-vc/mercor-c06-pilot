Question on methodology before I finalize the four numbers.

What I have locked in:
• Latest pricing version = v4.2 (effective Apr 1, 2024 → current): Team $15, Business $32, Growth $58, Enterprise $75–110/user/mo (Brightpath_Historical_Pricing_Versions_ChangeLog.xlsx).
• Discount source = Brightpath_Discount_Approval_Logs_v1.0.xlsx (800 rows, all FY2024): Business n=214, Growth n=176; discount = Final_Approved_Discount_%, threshold = Policy_Threshold_%.
• Company Size ranges (Brightpath_Revenue_by_Segment.xlsx → ARR_by_Company_Size): Small Practice 10–50 → midpoint 30 users (2,694 customers), Mid-Market 51–250 → 150.5 (1,080), Upper Mid-Market 251–500 → 375.5 (209).

What I need you to confirm is how the user count should be applied, because the discount log has no company-size field:
(A) Join each Deal_ID to Brightpath_Deal_Transactions_v1.0.xlsx to get Customer_Size_Segment, assign the band midpoint as that deal's user count, and compute user-weighted average discount AND user-weighted average threshold per tier; or
(B) Simple unweighted mean of Final_Approved_Discount_% and Policy_Threshold_% per tier (user count not used as a weight); or
(C) Weight each tier's per-band average discount by the band's total users (midpoint × customer count from the revenue file).

Also: should the discount population be limited to deals approved on/after Apr 1, 2024 (v4.2 effective date), or use all of FY2024? My default if I don't hear back is (A) with all FY2024 approvals.