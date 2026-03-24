---
name: scb-macro-economics
description: Workflows and use cases for SCB Macroeconomics tables covering GDP, inflation (CPI), and economic indicators
---

# SCB Macroeconomics Tables

This skill provides workflows for accessing Statistics Sweden's macroeconomics data, including GDP, inflation (CPI), and economic indicators.

## Common Table IDs and Keywords

- **GDP**: TAB3100, TAB3610, TAB676 (keywords: "GDP", "national accounts")
- **Inflation**: TAB3936, TAB2085 (keywords: "inflation", "CPI")
- **Economic Indicators**: TAB3100, TAB3610 (keywords: "economic indicators", "national accounts")

## Use Cases & Examples

### Analyze GDP Growth

```
1. scb_opendata_mcp_search_tables(query="GDP", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB3100")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB3100")
4. scb_opendata_mcp_get_table_data(table_id="TAB3100", selection=[
    {"variableCode": "EkoIndikator", "valueCodes": ["BNP10"]},
    {"variableCode": "ContentsCode", "valueCodes": ["NR0103A!"]},
    {"variableCode": "Tid", "valueCodes": ["2025K1", "2025K2", "2025K3", "2025K4"]}
])
```

### Examine Inflation Trends

```
1. scb_opendata_mcp_search_tables(query="inflation", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB3936")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB3936")
4. scb_opendata_mcp_get_table_data(table_id="TAB3936", selection=[
    {"variableCode": "ContentsCode", "valueCodes": ["PR0101C2"]},
    {"variableCode": "Tid", "valueCodes": ["2007M01", "2007M02", "2007M03"]}
])
```

### Compare Economic Indicators

```
1. scb_opendata_mcp_search_tables(query="economic indicators", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB3610")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB3610")
4. scb_opendata_mcp_get_table_data(table_id="TAB3610", selection=[
    {"variableCode": "Anvandningstyp", "valueCodes": ["BNPM"]},
    {"variableCode": "ContentsCode", "valueCodes": ["000000RQ"]},
    {"variableCode": "Tid", "valueCodes": ["2020", "2021", "2022", "2023"]}
])
```