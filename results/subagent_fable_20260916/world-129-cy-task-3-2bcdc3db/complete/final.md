No more inputs are needed; every source is in hand and the computation is done. Here is the answer.

**Results (rounded to 0.01%)**

- Business tier discount: **26.78%**
- Growth tier discount: **61.45%**
- Business variance vs. its average policy threshold: **+77.13%**
- Growth variance vs. its average policy threshold: **+318.40%**

**How these were derived**

Inputs
- Latest pricing version: v4.2 in `5. Client Data Room/09 Optional datasets/Brightpath_Historical_Pricing_Versions_ChangeLog.xlsx` (effective 2024-04-01, no end date). Business = $32/user/month, Growth = $58/user/month.
- Revenue by segment: `Brightpath_Revenue_by_Segment.xlsx`, sheet ARR_by_Company_Size. Mid-Market (51-250 employees) ARPU $42,317.12; Upper Mid-Market (251-500 employees) ARPU $100,742.68.
- Discount approval logs: `Brightpath_Discount_Approval_Logs_v1.0.xlsx` (the "(1)" copy is byte-for-byte identical, 800 deals). Average Policy_Threshold_%: Business 15.1168% (n=214), Growth 14.6875% (n=176).

Tier-to-segment mapping (no explicit table exists in the folder, so this follows the tier positioning text in the pricing changelog and the Current Pricing Tiers doc): Business is the "core package for mid-market workflow teams" with "strong adoption among 50–200 seat firms," so it maps to Mid-Market (51-250). Growth is for "scaling firms with cross-department collaborations," so it maps to Upper Mid-Market (251-500).

Calculation
- Business: users = (51+250)/2 = 150.5; annual list = 150.5 × $32 × 12 = $57,792.00; discount = 1 − 42,317.12 / 57,792.00 = 26.78%; variance = (26.78 − 15.12) / 15.12 = +77.13%.
- Growth: users = (251+500)/2 = 375.5; annual list = 375.5 × $58 × 12 = $261,348.00; discount = 1 − 100,742.68 / 261,348.00 = 61.45%; variance = (61.45 − 14.69) / 14.69 = +318.40%.

Notes
- The ARPU column in ARR_by_Company_Size is the simple mean of the 15 industry-by-region rows for each size band, and averaging the row-level discounts gives the same result (26.78% and 61.45%), so it is consistent with an "average discount" reading. If you instead use ARR ÷ Customer_Count (weighted ARPU: $42,222.22 and $97,607.66), the figures become Business 26.94% / +78.22% and Growth 62.65% / +326.57%.
- In percentage-point terms the gaps are Business +11.66 pp and Growth +46.77 pp above threshold.
- For reference, the logs themselves show approved discounts of 18.70% (Business) and 18.57% (Growth); the segment-derived figures above are far higher because realized ARPU sits well below list at the size-band midpoint, especially for Growth.

No files were produced; the answer is contained in this reply.
