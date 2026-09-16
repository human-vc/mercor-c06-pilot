**Answer (2025E, REIT scenario, 5.5% industry cap rate)**

- Inflation-adjusted enterprise value: **$44,544 million**
- Inflation-adjusted target share price: **$139.68**

**How the numbers are built** (all inputs from `Financials/Golden_Everest_REIT_Analysis.xlsx`)

| Step | Value |
|---|---|
| 2024A Services share of revenue = share of opex (895 / 5,420) | 16.51% |
| 2025E revenue (model) | $5,826.5mm |
| 2025E EBITDA (model, 43.0% margin) | $2,505.4mm |
| 2025E operating expenses excl. D&A (revenue less EBITDA) | $3,321.1mm |
| 2% inflation on opex | +$66.4mm |
| of which passed through to Services revenue (16.51%) | +$11.0mm |
| of which absorbed (non-Services, 83.49%) | -$55.5mm |
| Inflation-adjusted 2025E EBITDA (NOI proxy) | $2,449.9mm |
| Enterprise value = 2,449.9 / 5.5% | **$44,544mm** |
| Less net debt (model) | -$4,737mm |
| Equity value | $39,807mm |
| Shares outstanding | 285mm |
| Target share price | **$139.68** |

**Context and judgment calls**

- Inflation was applied to cash operating expenses (revenue minus EBITDA), not D&A, since D&A is a historical-cost charge and the cap rate capitalizes EBITDA/NOI. If D&A were included in the inflated base and the full absorbed increase pushed through EBITDA, the result would be EV $44,341mm and $138.96/share, so the conclusion is not sensitive to that choice.
- The 5.5% cap rate is more generous than the model's own mid case (16.4x EBITDA, roughly a 6.1% implied rate, giving $41,038mm and $127.37), so even after the $55mm inflation hit to EBITDA the cap-rate valuation lands about $3.5bn above the deck's headline REIT value. The two figures reconcile through multiple (5.5% is equivalent to 18.2x, the REIT peer median the model reserves for its high case), not through the inflation adjustment.
- The cap rate was not in any file in the folder (model, three decks, Elliott/Iron Mountain deck, peer filings); it was supplied by the client on request.

**Files produced**

- `/private/tmp/c06w/pgbtb_dt/work/Golden_Everest_Inflation_Adjusted_Valuation_2025.xlsx` (the step-by-step calculation above)
- `/private/tmp/c06w/pgbtb_dt/work/CLIENT_QUESTION.md` (the cap-rate question, now answered)