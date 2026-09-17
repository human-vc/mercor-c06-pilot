I ran the numbers off the discount approval logs (all 800 rows, dated 2024 — the duplicate `..._v1.0(1).xlsx` is data-identical), anchored to the latest pricing version **v4.2** (effective 2024‑04‑01, open‑ended: Team $15, Business $32, Growth $58, Enterprise $110 per user/month).

## Headline answer (unweighted tier averages, as logged)

| Metric | Business | Growth |
|---|---|---|
| Avg approved discount | **18.70%** (18.6963, n=214) | **18.57%** (18.5682, n=176) |
| Avg policy threshold | 15.12% | 14.69% |
| **% variance vs threshold** | **+23.68%** | **+26.42%** |
| Gap in percentage points | +3.58 pp | +3.88 pp |

Variance = (tier avg discount − tier avg Policy_Threshold_%) / tier avg threshold × 100, computed on unrounded values.

## Cross-checks (same direction, so the conclusion is robust)

- **Deal-value / user-weighted** (list price ÷ v4.2 per‑user price = implied users; within a tier this equals list-price weighting since $/user is constant): Business 18.77% vs 15.33% threshold → **+22.42%**; Growth 19.13% vs 15.25% → **+25.48%**.
- **Restricted to the v4.2 window** (approvals on/after 2024‑04‑01): Business 18.52% vs 15.09% → **+22.67%** (n=161); Growth 18.32% vs 14.69% → **+24.71%** (n=130).
- Requested (pre-negotiation) discounts run higher: Business 19.91%, Growth 19.77% — i.e. approvers give back only ~1.2 pp on average, so over-threshold behaviour is systemic, not a rounding artefact.
- Context: full-log blended average approved discount is 18.01%, matching the "Average Discount Rate: 18.01%" cited on slide 4 of *Brightpath Software Pricing Strategy_vF.pptx* — confirming the log is the right source.

## On the revenue-by-segment input
Per your instruction I used company-size midpoints as user counts: Small Practice (10–50) = 30.0 → 80,820 users / $54.0M ARR; Mid-Market (51–250) = 150.5 → 162,540 users / $45.6M ARR; Upper Mid-Market (251–500) = 375.5 → 78,479.5 users / $20.4M ARR (total 321,839.5 users, $120M ARR). That file contains **no pricing-tier field**, so it cannot re-weight the Business/Growth log averages — it only corroborates scale (e.g. the Business tier's logged deals imply ~84.5k users at $32/user/mo, consistent with the Mid-Market user base). If you want the tier mapping formalised (Team→Small Practice, Business→Mid-Market, Growth→Upper Mid-Market), the user-weighted blended discount across those three tiers is 18.43%.

## Read-through
Growth is the worse offender relative to policy (+26.42% vs +23.68%), despite the two tiers discounting at nearly identical absolute rates — because Growth's average threshold is the lowest of any tier (14.69% vs Business 15.12%). For comparison, Team is +18.51% and Enterprise +14.71% over threshold. Tightening Growth's approval discipline (or resetting its threshold) is where the margin leakage is concentrated.

**File produced:** `Business_Growth_Discount_vs_Threshold_Analysis.xlsx` — all four tiers with simple and weighted discounts, thresholds, variances, implied users at v4.2 pricing, and a Notes tab documenting method, sources and sensitivities.