# Field Dictionary (example)

| Field | Meaning | Notes |
|---|---|---|
| order_id | Sales order identifier | Must be unique per export |
| customer | Customer name | Use the master-data spelling |
| part_number | Resold part / SKU | Join key to purchase cost |
| quantity | Units sold | > 0 |
| selling_price | Unit price charged to the customer | In order currency |
| purchase_cost | Unit purchase cost | In purchase currency; check effective date |
| tax | Tax treatment flag | Whether prices are tax-inclusive |
| freight | Allocated freight per unit | From the freight table when present |
| rebate | Expected supplier rebate per unit | Only when contractually confirmed |
| exchange_rate | Purchase→order currency conversion | Invoice-date rate unless policy says otherwise |
