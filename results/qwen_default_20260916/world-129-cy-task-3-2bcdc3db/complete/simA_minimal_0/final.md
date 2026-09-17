## Answer

Using the latest pricing version (**v4.2**, effective 1‑Apr‑2024 → current: Business $32, Growth $58/user/mo), the FY2024 discount approval log (800 approved deals; Business n=214, Growth n=176), and the Company Size bands in the revenue‑by‑segment file (Small Practice 10–50 → **30** users, Mid‑Market 51–250 → **150.5**, Upper Mid‑Market 251–500 → **375.5** midpoints), with each approved deal weighted by its segment's user count:

| Metric | Business | Growth |
|---|---|---|
| **Average discount** | **19.37%** | **18.58%** |
| **% variance vs. average policy threshold** | **+27.01%** | **+25.59%** |

(Unweighted averages: Business discount 19.37% vs. threshold 15.25%; Growth 18.58% vs. 14.79%. If you prefer a straight per‑deal average with no user weighting, the figures are Business 18.70% / +23.68% and Growth 18.57% / +26.42%.)

**Interpretation:** both tiers are running roughly a quarter to more than a quarter **above** their approved discount guardrails — discounts are being systematically approved beyond policy — and Business and Growth have converged at ~19% and ~18.6% despite Growth being the premium tier, which erodes the $32 → $58 price ladder.

**Key caveats found in the data**
- `Policy_Threshold_%` is not a single published number per tier (Business rows carry 10/15/20%, Growth rows carry 10/15/20%), so the tier threshold had to be averaged from the log itself.
- The two discount‑log files (`v1.0` and `v1.0(1)`) are identical in content (0 differing rows), so no version reconciliation was required.
- The discount log has no company‑size field, so I joined each `Deal_ID` to `Brightpath_Deal_Transactions_v1.0.xlsx` to obtain the Customer Size Segment for the midpoint user count. Note that the log's tier/discount values do not reconcile with the transaction file for the same Deal_ID (only 200/800 tier matches), so the transaction file was used solely as the size bridge.
- Restricting to approvals on/after the v4.2 effective date would give Business 19.06% / +25.63% and Growth 18.16% / +22.58% — the same conclusion.

**Files produced**
- `Discount_Variance_Methodology.md` — sources, user‑count derivation, formulas, results, sensitivity table and caveats.
- `Discount_Variance_Business_Growth.csv` — the computed averages, thresholds and variances under both the user‑weighted and simple bases.