---
name: scb-housing-construction
description: Workflows and use cases for SCB Housing and Construction tables covering real estate, building permits, and construction statistics
---

# SCB Housing and Construction Tables

This skill provides workflows for accessing Statistics Sweden's housing and construction data, including real estate transactions, building permits, construction costs, property taxes, and housing market indicators.

## Common Table IDs and Keywords

- **Building Permits**: TAB513, TAB2534, TAB796 (keywords: "building permits", "bygglov", "construction permits")
- **Housing Starts**: TAB513, TAB2534 (keywords: "housing starts", "påbörjade bostäder", "new constructions")
- **Housing Completions**: TAB4384, TAB4385 (keywords: "housing completions", "färdigställda bostäder", "completed housing")
- **Real Estate Prices**: TAB4711, TAB4712, TAB1143 (keywords: "real estate prices", "bostadspriser", "property prices")
- **Construction Costs**: TAB4410, TAB1368 (keywords: "construction costs", "byggkostnader", "building costs")
- **Property Taxes**: TAB4711, TAB4712 (keywords: "property taxes", "fastighetsskatt", "real estate taxes")

## Use Cases & Examples

### Analyze Construction Cost Trends
```
1. scb_opendata_mcp_search_tables(query="construction costs", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB4410")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB4410")
4. scb_opendata_mcp_get_table_data(table_id="TAB4410", selection=[
    {"variableCode": "byggnadstyp", "valueCodes": ["bostadshus"]},
    {"variableCode": "år", "valueCodes": ["2020", "2021", "2022", "2023", "2024"]}
])
```

### Analyze Construction Activity by Building Type
```
1. scb_opendata_mcp_search_tables(query="building permits", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB513")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB513")
4. scb_opendata_mcp_get_table_data(table_id="TAB513", selection=[
    {"variableCode": "byggnadstyp", "valueCodes": ["bostadshus", "icke-bostadshus"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```