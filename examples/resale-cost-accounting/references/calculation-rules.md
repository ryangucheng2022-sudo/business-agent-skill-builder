# Calculation Rules (example)

- Landed unit cost = purchase_cost (converted) + freight − rebate.
- Line cost = landed unit cost × quantity.
- Margin amount = (selling_price − landed unit cost) × quantity.
- Margin % = margin amount ÷ (selling_price × quantity).
- Currency conversion uses the invoice-date rate from the rate table;
  record the rate used on each row.
- Round money to 2 decimals at line level; totals are sums of rounded
  lines (state this convention in the output notes).
- Tax-inclusive prices are converted to tax-exclusive before margin is
  computed, using the tax flag in the field dictionary.
- Abnormal margin: margin % < 0 or above the team's review threshold
  (example: 60%) → route to the exception list, never silently keep.
