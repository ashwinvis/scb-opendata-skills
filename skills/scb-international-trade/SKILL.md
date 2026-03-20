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

### Retrieve Current Import Statistics
```
1. scb_opendata_mcp_search_tables(query="imports", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB5440")
3. scb_opendata_mcp_get_table_data(table_id="TAB5440", selection=[
    {"variableCode": "varugrupp", "valueCodes": ["maskiner", "kemikalier"]},
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

### Examine Trade Balance Statistics
```
1. scb_opendata_mcp_search_tables(query="trade balance", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB5440")
3. scb_opendata_mcp_get_table_data(table_id="TAB5440", selection=[
    {"variableCode": "sektor", "valueCodes": ["total"]},
    {"variableCode": "år", "valueCodes": ["2024"]},
    {"variableCode": "kvartal", "valueCodes": ["K1", "K2", "K3", "K4"]}
])
```

### Retrieve Commodity-Specific Trade Data
```
1. scb_opendata_mcp_search_tables(query="commodity trade", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB1630")
3. scb_opendata_mcp_get_table_data(table_id="TAB1630", selection=[
    {"variableCode": "vara", "valueCodes": ["elektronik"]},
    {"variableCode": "handelstyp", "valueCodes": ["import", "export"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

### Analyze Service Trade Patterns
```
1. scb_opendata_mcp_search_tables(query="service trade", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB6695")
3. scb_opendata_mcp_get_table_data(table_id="TAB6695", selection=[
    {"variableCode": "tjänstetyp", "valueCodes": ["transport", "finansiell", "turism"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

### Examine Foreign Direct Investment Flows
```
1. scb_opendata_mcp_search_tables(query="foreign investment", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB2844")
3. scb_opendata_mcp_get_table_data(table_id="TAB2844", selection=[
    {"variableCode": "investeringstyp", "valueCodes": ["inflöde", "utflöde"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

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

### Compare Trade Performance Across Commodity Groups
```
1. scb_opendata_mcp_search_tables(query="imports", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB5440")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB5440")
4. scb_opendata_mcp_get_table_data(table_id="TAB5440", selection=[
    {"variableCode": "varugrupp", "valueCodes": ["jordbruk", "tillverkning"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```