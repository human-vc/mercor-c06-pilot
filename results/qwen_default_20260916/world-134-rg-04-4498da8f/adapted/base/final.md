## Console output

```
=====================================================================
 COMPLISURE | TrainIQ share-loss scenarios — 2025 (market size fixed)
=====================================================================
 SOURCE INPUTS
   Latest 5-yr forecast (Management_Forecast_v8.xlsx, "5yr forecast"):
     2025 base-case market size ........... $422.998M   (held constant)
     2025 CompliSure base-case share ...... 11.75%
     2025 CompliSure base-case revenue .... $49.71M
   Expanded financial dataset (Financial dataset_2016-25B expanded.xlsx):
     2025B TrainIQ revenue ................ $78.77M
     => TrainIQ 2025 base share (78.77/422.998) = 18.62%

 TRAINIQ REPORT — estimated share loss by research firm (bars, 2025)
     Firm A = 7%   Firm B = 12%   Firm C = 18%   (of TrainIQ's share)

 METHOD: freed share = TrainIQ share x loss% ; all of it captured by
         CompliSure; new revenue = new share x unchanged market size.
         (equivalently: base revenue + TrainIQ revenue x loss%)
---------------------------------------------------------------------
 SCENARIO  Share lost (pp)  CompliSure 2025   CompliSure 2025
                          MARKET SHARE      REVENUE ($M)
   Base        --              11.75%          49.71
   Firm A      1.30            13.05%          55.22
   Firm B      2.23            13.99%          59.16
   Firm C      3.35            15.10%          63.88
---------------------------------------------------------------------
 SENSITIVITY — if "latest 5-yr forecast" = 5yr_forecast_v5.xlsx
   (2025 share 9.75%, revenue $41.25M, same $422.998M market):
   Firm A: 11.05% / $46.76M   Firm B: 11.99% / $50.70M   Firm C: 13.10% / $55.43M
 SENSITIVITY — if the 7 / 12 / 18 figures are percentage POINTS (not % of share):
   Firm A: 18.75% / $79.31M   Firm B: 23.75% / $100.46M  Firm C: 29.75% / $125.84M
=====================================================================
```

## Conclusions

**Primary answer (base case = Management_Forecast_v8, the highest/latest version of the 5-year forecast; TrainIQ's share taken from the expanded financial dataset; 2025 market size held at $422.998M):**

| Scenario | CompliSure 2025 market share | CompliSure 2025 revenue |
|---|---|---|
| Firm A | **13.05%** | **$55.22M** |
| Firm B | **13.99%** | **$59.16M** |
| Firm C | **15.10%** | **$63.88M** |

(Base case for reference: 11.75% / $49.71M.)

**Two caveats you should confirm before this goes into the deck:**

1. **The TrainIQ report is an image-only PDF** (a single embedded JPEG, no text layer), and no OCR library is available in this environment. I recovered the content by pixel analysis: title "TrainIQ – Projected Market Share Loss", subtitle "2025", three bars labelled **Firm A / Firm B / Firm C** whose tops sit exactly on the 7th, 12th and 18th gridlines of a 0–~19/20 gridline axis. The axis tick labels were not legible, so I interpreted 7/12/18 as **percent of TrainIQ's share lost** (consistent with "lose a *portion* of its market share"). The percentage-point and forecast-version alternatives are shown above so you can swap in the intended reading in seconds.
2. **Which forecast is "latest" is ambiguous** — the folder holds `5yr_forecast_v5.xlsx`, `Management_Forecast_v7b.xlsx` and `Management_Forecast_v8.xlsx` (all with identical timestamps). v8 and v7b are the same model with different share trajectories (v8: 11.75%→20% by 2030, matching the "Base (Mgmt)" 0.20 share-capture assumption in *Key Assumptions.xlsx*; v5: 9.75%→8%, which looks like the downside case). I used v8; the v5 alternative is in the sensitivity block.

**Files produced:** `trainiq_report.png` (the image extracted from the PDF), plus intermediate crops `rotated_cw.png` / `rotated_ccw.png` used to attempt reading the rotated vertical text on the chart's left edge.