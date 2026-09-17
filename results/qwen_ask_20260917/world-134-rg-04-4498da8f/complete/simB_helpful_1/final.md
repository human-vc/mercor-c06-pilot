## What I did

**Sources used**
- **Latest 5‑year forecast:** `5. Forecast model/Management_Forecast_v8.xlsx` (2025 total revenue **$49,705,996**) together with the driver lines of the same latest model (`Management_Forecast_v7b.xlsx`): 2025 market size **$422,997.784K** and CompliSure 2025 share **11.75088807%**. Cross‑check: 11.75088807% × $422.998M = $49.71M = v8 revenue exactly (v8 carries the same revenue block as v7b, so v8/v7b is the latest model — not v5, which shows the older 9.7509% / $41.25M case).
- **Expanded financial dataset:** `Financial dataset_2016-25B expanded.xlsx` → TrainIQ 2025B revenue **US$78.77M** → TrainIQ 2025 share = 78.77 / 422.998 = **18.62%**.
- **Report:** `Train IQ market share report (1).pdf` is an **image‑only PDF** (no text layer, no OCR engine available in this environment). I decoded the embedded chart pixel‑by‑pixel: y‑axis "Percentage" scaled 0–18, and the three bars (Research Firm A / B / C) measure 6.94 / 11.96 / 17.96 on that scale → **A = 7%, B = 12%, C = 18%**.

**Assumptions:** 2025 market size fixed at $423.00M; 100% of TrainIQ's lost share goes to CompliSure; no other competitor affected. Since the bars are labelled as TrainIQ *market share* estimates, I treat them as each firm's estimate of TrainIQ's **resulting** 2025 share (loss = 18.62% − bar). The percentage‑point‑loss reading is shown as an alternative.

## Console output (primary reading — bars = TrainIQ's resulting 2025 share)

```
CompliSure BASE CASE 2025 : share 11.75%  |  revenue $49.71M
TrainIQ BASE CASE 2025    : share 18.62%  (rev $78.77M)

Scenario   TrainIQ 2025   Share loss   CompliSure share   CompliSure revenue   vs base
Firm A          7.00%       11.62pp           23.37%              $98.87M     +$49.16M
Firm B         12.00%        6.62pp           18.37%              $77.72M     +$28.01M
Firm C         18.00%        0.62pp           12.37%              $52.34M      +$2.63M
```

**Alternative reading (if the bars are percentage‑point losses):**
```
Firm A : loss  7.00pp -> share 18.75%  |  revenue $79.32M
Firm B : loss 12.00pp -> share 23.75%  |  revenue $100.47M
Firm C : loss 18.00pp -> share 29.75%  |  revenue $125.85M
```

**Caveat worth flagging:** the bar values (7/12/18%) were recovered by decoding the chart image, since the PDF has no extractable text and no OCR tool is available here — please sanity‑check them against the original report. Under the primary reading, Firm C's 18% is essentially TrainIQ's current 18.62% share, i.e. almost no loss.

**File produced:** `TrainIQ_share_loss_scenarios.py` (self‑contained script that prints the table above).