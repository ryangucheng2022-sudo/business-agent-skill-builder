---
name: resale-cost-accounting
description: Calculate resale (buy-and-resell) cost and margin from exported order and purchase files. Use when the user asks to compute resale cost, check margins on resale orders, or reconcile selling prices against purchase costs, freight, tax and rebates.
---

# Resale Cost Accounting (worked example)

> A miniature skill built with the business-agent-skill-builder method.
> Numbers and thresholds are illustrative — replace them with your own
> policies before real use.

## Overview

Use this skill to turn exported sales orders and purchase records into a
validated cost/margin table with an exception list. Prioritize
traceability: every cost figure must trace to a source row.

## Required Inputs

- Sales order export: order id, customer, part number, quantity, selling
  price, currency.
- Purchase cost source: part number, purchase cost, currency, effective
  date.
- Optional: freight table, rebate terms, exchange-rate table.

If the purchase cost for any part is missing, still produce the table and
list those rows under Exceptions as `Needs confirmation`.

## Workflow

1. Inspect the exports: confirm dates, currencies and column meanings
   against `references/field-dictionary.md`.
2. Validate required fields; flag duplicates and missing costs.
3. Apply `references/calculation-rules.md` (cost composition, currency
   conversion, rounding, margin).
4. Route abnormal rows through `references/exception-cases.md`.
5. Produce the output below; summarize sources, assumptions and
   exceptions.

## Source Priority

1. Finance-controlled purchase cost master data.
2. Latest official purchase export.
3. Supplier quotation attached to the order.
4. User-provided note (label results `Assumed`).

## Output Requirements

- Cleaned calculation table: one row per order line with landed cost,
  margin amount and margin %.
- Exception list with reason per row.
- Margin summary by customer and by part.
- Source and assumption notes; figures labeled Confirmed / Calculated /
  Assumed / Needs confirmation.

## Escalation

Ask for confirmation before:
- Using a fallback exchange rate or an expired purchase cost.
- Reporting a negative-margin order as final.
- Sending the table outside the team.
