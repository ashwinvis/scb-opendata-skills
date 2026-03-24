---
name: scb-population
description: Workflows and use cases for SCB Population tables covering demographics, births, deaths, and population projections
---

# SCB Population Tables

This skill provides workflows for accessing Statistics Sweden's population data, including demographic statistics, birth and death records, population projections, migrations, and household compositions.

## Common Table IDs and Keywords

- **Population Statistics**: TAB6008, TAB698, TAB4161 (keywords: "population", "befolkning", "demographics")
- **Births**: TAB5959, TAB694 (keywords: "births", "födda", "natality")
- **Deaths**: TAB5958, TAB694 (keywords: "deaths", "döda", "mortality")
- **Population Projections**: TAB5974, TAB698 (keywords: "population projections", "befolkningsframskrivningar")
- **Migrations**: TAB698, TAB694 (keywords: "migrations", "flyttningar", "immigration")
- **Households**: TAB4374, TAB1533, TAB1531 (keywords: "households", "hushåll", "family composition")

## Use Cases & Examples

### Retrieve Population Projections for Planning
```
1. scb_opendata_mcp_search_tables(query="population projections", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB5974")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB5974")
4. scb_opendata_mcp_get_table_data(table_id="TAB5974", selection=[
    {"variableCode": "scenario", "valueCodes": ["huvud"]},
    {"variableCode": "år", "valueCodes": ["2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032", "2033", "2034", "2035", "2036", "2037", "2038", "2039", "2040", "2041", "2042", "2043", "2044", "2045", "2046", "2047", "2048", "2049", "2050"]}
])
```

### Analyze Migration Patterns
```
1. scb_opendata_mcp_search_tables(query="migrations", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB698")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB698")
4. scb_opendata_mcp_get_table_data(table_id="TAB698", selection=[
    {"variableCode": "flyttningstyp", "valueCodes": ["inflyttning"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```