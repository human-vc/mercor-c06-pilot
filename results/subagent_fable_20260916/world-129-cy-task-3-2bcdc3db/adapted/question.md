# Client question: method confirmation for tier discount averages

I have the three inputs open:

- Pricing changelog: latest version is v4.2, effective 1 Apr 2024 (Business $32, Growth $58).
- Discount approval logs (v1.0; the "(1)" copy is identical): 800 deals approved 1 Jan to 31 Dec 2024, with Final_Approved_Discount_% and Policy_Threshold_% per deal. 200 of the 800 deals were approved before 1 Apr 2024.
- Revenue by segment: ARR by industry, region, and company size. It has no tier, customer, or deal key that joins to the discount logs, so it cannot be used to weight the tier averages.

My default method, unless you tell me otherwise:

1. Restrict the discount logs to deals approved on or after 1 Apr 2024 (the v4.2 effective window).
2. Average discount per tier = simple (unweighted) mean of Final_Approved_Discount_% for Business and for Growth.
3. Average policy threshold per tier = simple mean of Policy_Threshold_% for that tier over the same deals.
4. Threshold-relative variance = (average discount - average threshold) / average threshold.

Question: Is that the intended method, or do you want (a) all 2024 deals with no date restriction, and/or (b) a weighted average (for example, weighted by Initial_List_Price) rather than a simple mean?
