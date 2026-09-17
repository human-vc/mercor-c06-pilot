I decoded the chart image in the report (the PDF page is a scanned image, so I read it pixel-by-pixel) and ran the analysis. Final answers are printed to the console above.

## What the report says
"Train IQ Market Share Loss Estimates" — a bar chart with a **0–20% y-axis (5% gridlines)** showing how much of its market share TrainIQ is expected to lose, by research firm:
- **Research Firm A ≈ 7%** (bar top at y=436px → 7.05%)
- **Research Firm B ≈ 12%** (y=312px → 12.12%)
- **Research Firm C ≈ 18%** (y=164px → 18.18%)

(Because market size is held constant, "7/12/18% of TrainIQ's share" and the same % of TrainIQ's revenue are mathematically identical, so the result is unaffected by that wording.)

## Base case inputs used
| Item | Value | Source |
|---|---|---|
| 2025 market size (unchanged) | $423.00M | latest 5-yr forecast market row (`Management_Forecast_v7b`/`v8` lineage) |
| CompliSure 2025 revenue | $49.71M | **`Management_Forecast_v8.xlsx`** (latest 5-year forecast), Total Revenue 2025 |
| CompliSure 2025 share | 11.75% | 49.71 / 423.00 |
| TrainIQ 2025 revenue | $78.77M | **`Financial dataset_2016-25B expanded.xlsx`**, row 2025B / TrainIQ |
| TrainIQ 2025 share | 18.62% | 78.77 / 423.00 |

## Results (all TrainIQ share lost is captured by CompliSure; other competitors and market size unchanged)

| Scenario | TQ share lost | Revenue shifted | **CompliSure 2025 revenue** | **CompliSure 2025 share** |
|---|---|---|---|---|
| Base case | – | – | $49.71M | 11.75% |
| **Firm A** | 7.00% | +$5.51M | **$55.22M** | **13.05%** |
| **Firm B** | 12.00% | +$9.45M | **$59.16M** | **13.99%** |
| **Firm C** | 18.00% | +$14.18M | **$63.88M** | **15.10%** |

(Using the un-rounded pixel readings 7.05/12.12/18.18% gives $55.26M/13.07%, $59.25M/14.02%, $64.03M/15.14% — i.e. essentially the same.)

## File produced
- `CompliSure_2025_TrainIQ_share_scenarios.xlsx` — inputs, sources, assumptions and the three-scenario calculation with the resulting 2025 revenue and market share.