## Console output (printed above) and conclusions

**Note on the attached report:** `Train IQ market share report (1).pdf` contains **no text layer** — it is a single flattened screenshot of a bar chart ("TrainIQ Market Share", y-axis = *Percentage*, x-axis = *Research Firm A / B / C*). I extracted the embedded JPEG and measured the bars pixel-precisely against the gridlines (0–18 scale): **Firm A ≈ 6.94 → 7%, Firm B ≈ 11.96 → 12%, Firm C ≈ 17.96 → 18%**. As you confirmed, I ran both possible readings of those three values.

**Base case (latest 5-year forecast = `Management_Forecast_v8.xlsx`, whose 2025 revenue ties exactly to the market drivers in `Management_Forecast_v7b.xlsx`):**
- 2025 market size = **$423.00M** (held constant in all scenarios)
- CompliSure 2025 share = **11.75%**; CompliSure 2025 revenue = **$49.71M**
- TrainIQ 2025B revenue = **$78.77M** (`Financial dataset_2016-25B expanded.xlsx`) → TrainIQ 2025 share = 78.77 / 423.00 = **18.62%**

### Primary answer — bars = percentage-point share **lost** by TrainIQ (share = 11.75% + loss)
| Scenario | TQ loss | CompliSure share 2025 | CompliSure revenue 2025 | Uplift vs base |
|---|---|---|---|---|
| Firm A | 7.00 pp | **18.75%** | **$79.32M** | +$29.61M |
| Firm B | 12.00 pp | **23.75%** | **$100.47M** | +$50.76M |
| Firm C | 18.00 pp | **29.75%** | **$125.85M** | +$76.14M |

*Feasibility flag:* TrainIQ only holds 18.62% of the 2025 market, so the maximum transferable loss is 18.62 pp → CompliSure ceiling of **30.37% / $128.48M**. Firm C's 18.00 pp sits just inside that limit (Firms A–C all require TrainIQ to shed 38%–97% of its current share).

### Alternative answer — bars = TrainIQ's **resulting** 2025 share (loss = 18.62% − bar)
| Scenario | TQ share | TQ loss | CompliSure share 2025 | CompliSure revenue 2025 |
|---|---|---|---|---|
| Firm A | 7.00% | 11.62 pp | **23.37%** | **$98.87M** |
| Firm B | 12.00% | 6.62 pp | **18.37%** | **$77.72M** |
| Firm C | 18.00% | 0.62 pp | **12.37%** | **$52.34M** |

Method: new share = base share + TrainIQ's loss; revenue = new share × fixed $422.9978M market size; no share reallocated to other competitors. All figures rounded to 2 dp / $0.01M.

**Files produced:** `TrainIQ_share_loss_2025_results.txt` (the printed results table) and `trainiq_report.jpg` (the chart image extracted from the PDF for verification).