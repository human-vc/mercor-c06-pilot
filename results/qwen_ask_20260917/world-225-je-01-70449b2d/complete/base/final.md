## Answer

**Method** (all inputs from `Financials/Golden_Everest_REIT_Analysis.xlsx`)

| Step | Item | Value |
|---|---|---|
| 1 | 2024A Service Revenue ÷ Total Revenue = $895 ÷ $5,420 (pass-through share) | **16.51%** |
| 2 | 2025E Revenue (5,420 × 1.075) | $5,826.5 |
| | 2025E EBITDA (43.0% margin, pre‑inflation) | $2,505.4 |
| | 2025E forecast cash OpEx (Revenue − EBITDA = 57% of revenue) | $3,321.1 |
| 3 | OpEx increase at 2% inflation | $66.4 |
| | Less: recoverable via Services (16.51%) | ($11.0) |
| | **Unrecovered cost absorbed in margin** | **$55.5** |
| | **2025E inflation‑adjusted EBITDA** (margin 42.05%) | **$2,449.9** |
| 4 | Cap rate 5.5% → implied multiple 1 ÷ 5.5% = 18.18x | |
| | **Inflation‑adjusted Enterprise Value** = 2,449.9 ÷ 0.055 | **$44,544 mm** |
| | Less: Net Debt | ($4,737) mm |
| | **Inflation‑adjusted Equity Value** | **$39,807 mm** |
| | ÷ Shares outstanding (285 mm) | |
| | **Target Share Price, 2025E** | **$139.68** |

**Headline results**
- **Inflation‑adjusted Enterprise Value (2025E): ≈ $44,544 million**
- **Inflation‑adjusted Equity Value: ≈ $39,807 million**
- **Target share price (REIT, 2025E): $139.68**

**Context:** without the inflation drag the same 5.5% cap rate gives EV of $45,553 mm and $159.94… precisely, $143.21/share, so unrecovered 2% inflation destroys ~$1,009 mm of enterprise value (~$3.54/share). The 2% cost shock is only 16.5% offset, so EBITDA margin compresses 95bps from 43.0% to 42.05%. The resulting $139.68 target is +228.6% vs. the $42.50 trading price and +198.8% vs. the $46.75 strategic offer, and it exceeds the model's mid‑case REIT value of $127.37/share (16.4x EBITDA) because a 5.5% cap rate implies a richer 18.2x multiple.

**Assumptions flagged:** (i) "operating expenses" = cash OpEx excluding D&A (Cost of Services $1,844 + SG&A $651 = $2,495 in 2024, i.e. Revenue − EBITDA), since D&A is not inflation‑priced; (ii) net debt held at the model's $4,737 mm used in all three valuation scenarios (note the Historicals tab shows 2024A net debt of $6,675 mm — using that instead gives $132.88/share); (iii) revenue growth/margin base case unchanged apart from the inflation drag.

**File produced:** `Financials/Golden_Everest_Inflation_Adjusted_REIT_Valuation.xlsx` — a live, formula‑driven build‑up of the four steps above (with memo comparisons and sensitivities).