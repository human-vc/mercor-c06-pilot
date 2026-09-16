Both source-file reads and the scenario math check out (e.g. Firm A: 41.25 + 0.07 × 78.77 = 46.76; 46.76 / 423.00 = 11.05%). Nothing else is outstanding.

## Final answers (printed to console above)

**Inputs (2025)**
- Market size: $423.00M (`5yr_forecast_v5.xlsx`, 2025 column; held constant)
- CompliSure base case: revenue $41.25M, market share 9.75%
- TrainIQ 2025B revenue: $78.77M (`Financial dataset_2016-25B expanded.xlsx`) = 18.62% share

**Scenarios (TrainIQ loses the stated % of its share; all of it flows to CompliSure)**

| Scenario | TrainIQ share loss | Share transferred | CompliSure 2025 share | CompliSure 2025 revenue |
|---|---|---|---|---|
| Firm A | 7% | 1.30 pp | **11.05%** | **$46.76M** |
| Firm B | 12% | 2.23 pp | **11.99%** | **$50.70M** |
| Firm C | 18% | 3.35 pp | **13.10%** | **$55.42M** |

**Assumptions worth flagging**
- The report PDF is image-only; the three bars were read as 7%, 12%, 18% and confirmed by pixel measurement against the gridlines (6.94%, 11.95%, 17.91%).
- "Estimated % Share Loss" is treated as a relative loss (a portion of TrainIQ's own share), consistent with "lose a portion of its market share." If the firms meant absolute percentage points, CompliSure's share would instead be 16.75% / 21.75% / 27.75%, with revenue $70.86M / $92.01M / $117.38M.
- "Our latest 5-year forecast" is taken as `5yr_forecast_v5.xlsx` (the only series with Market size / Market share rows; its 2024A market of $367.82M equals the four competitors' 2024 revenue plus CompliSure's). `Management_Forecast_v8.xlsx` is management's plan, not ours.
- The forecast's 2025 market ($423.00M, 2024A × 1.15) is the denominator for both companies. Note the expanded dataset's 2025B competitor budgets plus CompliSure would sum to $433.62M; the forecast's figure was used because the question starts from the forecast's base-case outlook.

**File produced**
- `trainiq_share_scenarios.py` reads both source workbooks, applies the three scenarios, and prints the table above.
