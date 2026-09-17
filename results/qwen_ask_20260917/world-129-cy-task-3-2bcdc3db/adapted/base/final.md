Thanks — I've located the sources. Two quick confirmations before I lock the numbers (I can only ask once, so I'll state my default if you don't correct me):

1) Which discount column should count as "the average discount percentage"?
   - Default: Final_Approved_Discount_% (the discount actually granted), simple (unweighted) mean per tier.
   - Alternatives: Discount_Requested_% , or a deal-value-weighted mean using Initial_List_Price.

2) "Using the latest pricing version" (v4.2, effective 2024-04-01, no end date in the changelog): should I restrict the approval-log rows to deals approved on/after 2024-04-01 (v4.2 window, n=161 Business / 130 Growth), or use all 800 log rows (all dated 2024)?
   - Default: all 2024 log rows for the tier averages, with the v4.2 window reported as a sensitivity.

3) Variance definition: % variance = (tier avg discount − tier avg Policy_Threshold_%) / tier avg Policy_Threshold_% × 100. Confirm you want relative %, not percentage-point gap.

FYI, the two copies of the discount log (…_v1.0.xlsx and …_v1.0(1).xlsx) are byte-for-byte identical in data, and the Revenue by Segment file has no tier field, so it can't drive the tier averages — I'll use it only for context/weighting if you want ARR weighting instead.