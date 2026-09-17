Final answers are printed to the console above. Summary:

**Inputs used**
- Latest 5‑year forecast: `5. Forecast model/Management_Forecast_v8.xlsx` (2025 P&L; market drivers carried in v7b) → 2025 market size **$423.00M**, CompliSure base share **11.75%**, base revenue **$49.71M**.
- Expanded financial dataset: `2. Competitive analysis/Financial dataset_2016-25B expanded.xlsx` → TrainIQ 2025B revenue **$78.77M** ⇒ TrainIQ base share **18.62%**.
- Research report: `Train IQ market share report (1).pdf` is an **image‑only PDF** (no text layer, no OCR engine available in this environment), so I read the bar chart pixel‑by‑pixel against its 0–18 gridline axis: **Firm A = 7%, Firm B = 12%, Firm C = 18%** (y‑axis label "Percentage", x labels "Research Firm A/B/C").

**Results (market size held constant; 100% of TrainIQ's lost share captured by CompliSure)**

| Scenario | TrainIQ 2025 share | Share lost (pp) | CompliSure share | CompliSure revenue |
|---|---|---|---|---|
| Base (no shift) | 18.62% | – | 11.75% | $49.71M |
| A | 7.00% | 11.62 | **23.37%** | **$98.87M** |
| B | 12.00% | 6.62 | **18.37%** | **$77.72M** |
| C | 18.00% | 0.62 | **12.37%** | **$52.34M** |

**Caveat you should be aware of:** the report doesn't state whether 7/12/18% is TrainIQ's *resulting* share (the reading I used — the bars sit exactly on gridlines, consistent with a "share after the loss" chart, and Firm C ≈ today's 18.62% = the "no change" case). If instead those numbers are the *amount* of share lost, the answers are: A 18.75% / $79.32M, B 23.75% / $100.47M, C 29.75% / $125.85M (both sets printed to the console). Also note the base case implies CompliSure revenue of $49.71M vs. ~$40M ARR cited in the SOW — I used the forecast file as instructed.

**Files produced:** `trainiq_report.jpg` (the chart image extracted from the PDF, used to read the values). No other deliverables were requested.