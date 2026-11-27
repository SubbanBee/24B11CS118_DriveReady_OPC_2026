# Day 4 – Tools, Structured Output and Google Sheets

## Project
Sweet Crumbs Home Bakery – AI Agent

## Objective
Build an AI agent using LangChain and Groq that can use Python tools, validate structured order data, and record practice orders in Google Sheets.

## Tools Implemented
1. `get_price` – Retrieves cake prices.
2. `is_open` – Handles business-hours enquiries without inventing unknown hours.
3. `log_order` – Validates and records practice orders in Google Sheets.

## Structured Output
Created a Pydantic `Order` model with:
- Customer name
- Cake item
- Quantity
- Required date
- Eggless preference

## Available Menu
- Chocolate Cake – Rs. 650
- Plum Cake – Rs. 500

Both cakes have eggless versions available.

## Testing Results
- Unknown cake validation – Passed
- Missing required date – Passed
- Zero quantity validation – Passed
- Tool execution trace – Verified
- Google Sheets connection – Successful

## Final Result
Successfully created a Sweet Crumbs AI Agent that uses tools, validates order details, and stores practice orders in Google Sheets.

**Note:** All recorded orders are practice records only, not real bakery bookings.
