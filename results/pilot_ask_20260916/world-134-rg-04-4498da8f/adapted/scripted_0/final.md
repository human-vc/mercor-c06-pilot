### Executive Summary & Scenario Analysis

Based on the **latest 5-year forecast** (`Management_Forecast_v8.xlsx` / `v7b.xlsx` incorporating the `Key Assumptions.xlsx` Base Management Case), the **expanded financial dataset** (`Financial dataset_2016-25B expanded.xlsx`), and the research firm estimates from the attached report (`Train IQ market share report (1).pdf`), here is the market share and revenue analysis for CompliSure in 2025.

Per confirmation, **any market share lost by TrainIQ is assumed to be fully captured by CompliSure**, and the **overall market size in 2025 remains unchanged** at **$423.00M** ($422,997.78K).

---

### Key Baseline Data (2025)

* **Overall 2025 Market Size:** **$423.00M** ($422,997.78K, based on 15.0% CAGR over 2024A market size of $367.82M)
* **CompliSure 2025 Base-Case Outlook:**
  * **Market Share:** **11.75%** (11.7509%)
  * **Revenue:** **$49.71M** ($49,705.996K)
* **TrainIQ 2025 Base-Case Outlook:**
  * **Revenue:** **$78.77M** (from the expanded financial dataset)
  * **Market Share:** **18.62%** ($78.77M / $423.00M = 18.6218%)

---

### Research Firm Estimates (TrainIQ % Share Loss)
From `Train IQ market share report (1).pdf`:
* **Firm A:** **7.00%** loss
* **Firm B:** **12.00%** loss
* **Firm C:** **18.00%** loss

---

### Final Answers

#### Primary Model: Relative Loss of TrainIQ Market Share
*(Standard market research convention: TrainIQ loses 7%, 12%, and 18% of its projected market share/revenue, with CompliSure capturing 100% of the lost volume)*

| Scenario | TrainIQ Share Loss (%) | Market Share Transferred (%) | Dollar Value Captured ($M) | CompliSure 2025 Market Share (%) | CompliSure 2025 Revenue ($M) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **2025 Base Case** | — | — | — | **11.75%** | **$49.71M** |
| **Scenario A (Firm A)** | **7.00%** | +1.30% | +$5.51M | **13.05%** | **$55.22M** |
| **Scenario B (Firm B)** | **12.00%** | +2.23% | +$9.45M | **13.99%** | **$59.16M** |
| **Scenario C (Firm C)** | **18.00%** | +3.35% | +$14.18M | **15.10%** | **$63.88M** |

---

### Console Output Summary

```text
========================================================================================
COMPLISURE 2025 MARKET SHARE & REVENUE SCENARIO ANALYSIS
========================================================================================
Market Size (2025): $423.00M ($422,997.78K)
CompliSure Base Case: Market Share = 11.75% | Revenue = $49.71M ($49,705.996K)
TrainIQ Base Case:    Market Share = 18.62% | Revenue = $78.77M

----------------------------------------------------------------------------------------
PRIMARY SCENARIO RESULTS (Relative Share Loss: 7% / 12% / 18% of TrainIQ):
----------------------------------------------------------------------------------------
Scenario A (Firm A - 7.00% loss):
  - TrainIQ Lost Volume:      1.30% market share ($5.51M revenue)
  - CompliSure Market Share:  13.05%
  - CompliSure Revenue:       $55.22M

Scenario B (Firm B - 12.00% loss):
  - TrainIQ Lost Volume:      2.23% market share ($9.45M revenue)
  - CompliSure Market Share:  13.99%
  - CompliSure Revenue:       $59.16M

Scenario C (Firm C - 18.00% loss):
  - TrainIQ Lost Volume:      3.35% market share ($14.18M revenue)
  - CompliSure Market Share:  15.10%
  - CompliSure Revenue:       $63.88M
========================================================================================
```

---

### Alternative Sensitivities

For completeness, two alternative modeling variants:

1. **Absolute Percentage Point Loss** *(if 7%, 12%, 18% were treated as absolute percentage points of the total market rather than relative to TrainIQ)*:
   * **Scenario A (+7.00 pp):** Market Share = **18.75%** | Revenue = **$79.32M**
   * **Scenario B (+12.00 pp):** Market Share = **23.75%** | Revenue = **$100.47M**
   * **Scenario C (+18.00 pp):** Market Share = **29.75%** | Revenue = **$125.85M**

2. **Downside Base Forecast Variant** *(`5yr_forecast_v5.xlsx` base: 9.75% share / $41.25M revenue)*:
   * **Scenario A (7.00% relative loss):** Market Share = **11.05%** | Revenue = **$46.76M**
   * **Scenario B (12.00% relative loss):** Market Share = **11.99%** | Revenue = **$50.70M**
   * **Scenario C (18.00% relative loss):** Market Share = **13.10%** | Revenue = **$55.42M**