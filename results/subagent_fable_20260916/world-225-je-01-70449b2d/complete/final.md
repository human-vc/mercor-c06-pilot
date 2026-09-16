All results are in hand and the workbook's formula references check out, so nothing further is needed.

**Answer**

Inflation-adjusted 2025E valuation for Golden Everest at a 5.5% REIT cap rate:

- **Enterprise value: $44,544 million**
- **Target share price: $139.68**

**How it was derived (all figures from `Golden_Everest_REIT_Analysis.xlsx`)**

| Step | $mm |
|---|---|
| 2025E revenue (Projections C16) | 5,826.5 |
| 2025E EBITDA, base case (Projections C19, 43% margin) | 2,505.4 |
| 2025E operating expenses excl. D&A = revenue − EBITDA | 3,321.1 |
| 2% inflation on operating expenses | 66.4 |
| Service revenue share of 2024 total revenue (895 / 5,420) | 16.5% |
| Increase passed through via Services revenue (16.5% × 66.4) | 11.0 |
| Unrecovered increase absorbed in EBITDA | 55.5 |
| Inflation-adjusted 2025E EBITDA (NOI proxy) | 2,449.9 |
| Enterprise value = 2,449.9 / 5.5% | **44,544** |
| Less: net debt (per model, $4,737mm) | (4,737) |
| Equity value | 39,807 |
| ÷ 285mm shares → target price | **$139.68** |

**Assumptions worth flagging**

- The model carries no NOI line, so 2025E EBITDA is used as the income measure capitalized at 5.5%. D&A is non-cash and sits below EBITDA, so whether or not it is treated as "operating expense" does not change the result.
- Net debt of $4,737mm and 285mm shares are the figures the model and all three decks use consistently (Historicals shows a different $6,675mm balance-sheet net debt, but the valuation spine uses $4,737mm, so I kept it).
- For reference, the same cap rate with no inflation hit gives EV of $45,553mm and $143.21/share; the inflation drag is $1,008mm of EV and $3.54/share. The implied EV/EBITDA is 18.2x, in line with the REIT comp median in the model.

**File produced**

- `Financials/Golden_Everest_Inflation_CapRate_Valuation.xlsx` — one-sheet live-formula walk from the model inputs to the EV and price above, with source cell references.
