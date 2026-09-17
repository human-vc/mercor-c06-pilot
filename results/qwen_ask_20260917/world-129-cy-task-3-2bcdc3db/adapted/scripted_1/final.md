## Answer

Using the latest pricing version (**v4.2**, effective 2024‑04‑01, open‑ended: Business $32 and Growth $58 per user/month), the segment revenue/company‑size data, and the discount approval logs (800 rows, all 2024; the two v1.0 log copies are identical), and weighting each deal by the **midpoint of its company‑size range** as the user count (Small Practice 10–50 → 30; Mid‑Market 51–250 → 150.5; Upper Mid‑Market 251–500 → 375.5), with discount = `Final_Approved_Discount_%`:

| Metric | Business | Growth |
|---|---|---|
| Average discount % | **19.37%** | **18.58%** |
| Average policy threshold % | 15.25% | 14.79% |
| % variance vs threshold | **+27.01%** | **+25.59%** |

- Business discount: **19.37%** (19.3673%)
- Growth discount: **18.58%** (18.5811%)
- Business threshold‑relative variance: **+27.01%** (27.0149%) — i.e. approved Business discounts run ~27% above the policy allowance
- Growth threshold‑relative variance: **+25.59%** (25.5916%)

Variance formula: (tier avg discount − tier avg `Policy_Threshold_%`) ÷ tier avg `Policy_Threshold_%` × 100.

### Sensitivity (if you prefer a plain per‑deal average, unweighted)
| | Business | Growth |
|---|---|---|
| Avg discount | 18.70% | 18.57% |
| Avg threshold | 15.12% | 14.69% |
| % variance | +23.68% | +26.42% |

Restricting to approvals inside the v4.2 window only (on/after 2024‑04‑01, n=161/130) gives weighted variances of +25.63% (Business) and +22.58% (Growth).

### Notes / caveats
- The approval log carries three different `Policy_Threshold_%` values (10/15/20%) per tier with no tier‑level policy table anywhere in the data room, so the "average policy threshold" had to be computed from the log itself (same weighting basis as the discounts).
- `Revenue_by_Segment.xlsx` has no tier field, so it cannot drive tier averages directly; tier/segment linkage came from the deal‑level transaction file (`Customer_Size_Segment` per `Deal_ID`), and the v4.2 per‑user price converts user counts into revenue‑proportional weights (identical ranking to pure user weighting within a tier).
- Because the client reply specified the midpoint‑of‑company‑size user count, that weighting is used for the headline figures above; the unweighted figures are provided as the alternative.

**File produced:** `Deliverables_Discount_Variance_Analysis.xlsx` (Detail tab with per‑deal user counts, revenue base, discounts and thresholds; Results tab with headline and sensitivity figures).