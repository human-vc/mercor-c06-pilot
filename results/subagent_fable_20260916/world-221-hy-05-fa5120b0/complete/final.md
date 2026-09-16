Nothing further is needed: the workbook's live formulas reproduce the script's figures exactly, and the merger model recalculation at the 9M TTM 2025 account was verified against a formula engine (the 2024 baseline reproduced the file's cached values before I switched the account cell).

**The five values (merger model set to 9M TTM 2025, medians of the nine comps: P/NAV 0.7182x, P/E 10.17x, P/S 9.11x)**

1. Scenario 1 to 2 (run-rate synergies): **+4.64%**
2. Scenario 2 to 3 (TPVG NAV contribution, pre-dilution): **+22.04%**
3. Scenario 3 to 4 (pro forma, after dilution): **-15.53%**
4. Pro Forma Implied Equity Value after dilution: **USD 1,660,990 thousand**
5. Total value creation vs standalone: **+7.87%**

**Bridge (USD '000)**

| Scenario | Implied equity value |
|---|---|
| 1. BBDC standalone (LTM NAV 1,166,795; LTM NII 119,328; LTM Sales 281,866) | 1,539,792 |
| 2. + run-rate synergies of 21,085 (7.5% of combined TTM EBIT) | 1,611,271 |
| 3. + TPVG standalone NAV of 355,053 | 1,966,324 |
| 4. PF NAV 1,413,233 / PF NII 185,372 / PF Sales 376,005 through the same multiples, then times legacy BBDC ownership of 78.77% (105,159 / 133,494 PF shares) | 1,660,990 |

**How it was built**

- Implied equity value in scenarios 1, 2 and 4 is the simple average of the three multiple methods. Synergies enter through NII (the P/E method); NAV and Sales are unchanged in scenario 2.
- Scenario 3 adds TPVG's NAV at book, before any new shares. Scenario 4 applies the ownership adjustment, the same convention the merger model uses for "BBDC Equity Value Post-Bid". The gross pro forma implied equity value before that adjustment is 2,108,549.
- Switching Merger Analysis!F18 to the TTM account also removes the new debt draw: 50% of BBDC's 9M 2025 cash covers cash consideration plus fees, so the PF NAV adjustment is share consideration less TPVG NAV less fees, or (108,615).
- Comp medians are over the nine numbered comps in the file (its own median row). The "Others: Above $1 Billion Market Cap" block (TSLX, GBDC, TRIN) sits outside the peer set and was excluded. For reference, including those three would move the medians to 0.7726x / 9.855x / 8.59x.

**File produced**

/private/tmp/c06w/v1r5xugx/work/BBDC_TPVG_Value_Creation_Bridge.xlsx (one sheet: sourced inputs with cell references, the bridge with live formulas, and the assumption notes above). Your vF models were not modified; the account switch was run on a recalculated copy.