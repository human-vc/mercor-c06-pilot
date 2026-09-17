## What I did

**1. The attached report is an image‑only PDF** (`Train IQ market share report (1).pdf` – 1 page, no text layer, one embedded 1200×742 raster). I extracted the image and decoded it pixel‑by‑pixel (glyph‑by‑glyph) to recover the chart:

- Title: **"TrainIQ – Market Share Outlook"**; three grey bars, legend **"FIRM A / FIRM B / FIRM C"** (legend groups centred at x≈360/660/960 align exactly with the three bars).
- Y‑axis ticks read **0%, 5%, 10%, 15%** (baseline y=607 px, 24.73 px per pp).
- Bar tops at y=436 / 312 / 164 px → **6.91 / 11.93 / 17.91 pp**, i.e. (allowing the uniform ~0.1 px‑gridline bias) **7%, 12% and 18%** projected share loss for TrainIQ.

**2. Base case (latest 5‑yr forecast – `Management_Forecast_v8.xlsx`, whose 2025 revenue $49,705.996K ties exactly to `v7b`, the last version carrying the market rows):**
- 2025 market size = **$422.9978M** (unchanged in all scenarios)
- CompliSure 2025 share = **11.75%**; revenue = **$49.71M**

**3. TrainIQ's 2025 base share (from `Financial dataset_2016-25B expanded.xlsx`, 2025B revenue $78.77M):** 78.77 / 422.9978 = **18.62%**. Its lost share is redistributed to CompliSure (market size fixed, 100% capture).

## Console output

```
Base case 2025:  Market size $422.9978M | CompliSure share 11.75% | revenue $49.71M
TrainIQ 2025B:   revenue $78.77M -> share 18.62%

Scenario        TrainIQ share loss   CompliSure share   CompliSure revenue
Firm A                   7.00%              13.05%            $55.22M
Firm B                  12.00%              13.99%            $59.16M
Firm C                  18.00%              15.10%            $63.88M
```

**Answers (2 dp):** Firm A – 13.05% / $55.22M; Firm B – 13.99% / $59.16M; Firm C – 15.10% / $63.88M.

## Caveats you should confirm

- I read the three bar values as **relative (% of TrainIQ's own share) losses**, since an 18 *percentage‑point* loss would erase TrainIQ's entire 18.62% share. If the report actually means percentage‑point losses, the answers would instead be 18.75%/$79.32M (A), 23.75%/$100.47M (B), 29.75%/$125.85M (C).
- The bar values are derived from pixel geometry (7/12/18%); the chart's printed data labels and axis title were not legibly recoverable, so please sanity‑check them against the original source.
- I assumed CompliSure captures **all** of TrainIQ's released share; if it leaks to Syncore/Velocity/UpSkill, the uplift should be scaled by CompliSure's capture rate.
- I used `Management_Forecast_v8/v7b` (market size $422.998M, share 11.75%). Note `5yr_forecast_v5` is a downside variant (share 9.75%, revenue $41.25M) — under that base the answers would be 11.05%/$46.76M, 11.99%/$50.70M, 13.10%/$55.43M.

**Files produced:** none delivered; only a working extraction of the report image (`trainiq_img.png`) was written to the folder while decoding the PDF.