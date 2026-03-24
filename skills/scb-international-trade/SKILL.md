---
name: scb-international-trade
description: Workflows and use cases for SCB International Trade tables covering imports, exports, and foreign trade statistics
---

# SCB International Trade Tables

This skill provides workflows for accessing Statistics Sweden's international trade data, including import/export statistics, trade balances, commodity flows, and foreign trade indicators.

## Common Table IDs and Keywords

- **Import Statistics**: TAB5440, TAB1630, TAB1631 (keywords: "imports", "import", "import statistics")
- **Export Statistics**: TAB5440, TAB1630, TAB1631 (keywords: "exports", "export", "export statistics")
- **Trade Balance**: TAB5440 (keywords: "trade balance", "handelsbalans", "net trade")
- **Commodity Trade**: TAB1630, TAB1631 (keywords: "commodity trade", "varuhandel", "goods trade")
- **Service Trade**: TAB6695, TAB6696 (keywords: "service trade", "tjänstehandel", "services trade")
- **Foreign Direct Investment**: TAB2844, TAB2843 (keywords: "FDI", "foreign investment", "utländska investeringar")
- **Trade by Country**: TAB5440 (keywords: "trade by country", "handel per land", "country-specific trade")

## Use Cases & Examples

### Retrieve Country-Specific Trade Statistics
```
1. scb_opendata_mcp_search_tables(query="trade by country", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB5440")
3. scb_opendata_mcp_get_table_data(table_id="TAB5440", selection=[
    {"variableCode": "land", "valueCodes": ["DE", "US", "CN"]},
    {"variableCode": "handelstyp", "valueCodes": ["export"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

### Analyze Export Trends by Commodity
```
1. scb_opendata_mcp_search_tables(query="exports", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB5440")
3. scb_opendata_mcp_get_table_data(table_id="TAB5440", selection=[
    {"variableCode": "vara", "valueCodes": ["trä", "stål", "fordon"]},
    {"variableCode": "år", "valueCodes": ["2020", "2021", "2022", "2023", "2024"]}
])
```