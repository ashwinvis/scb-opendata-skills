---
name: scb-environment
description: Workflows and use cases for SCB Environment tables covering climate, energy, waste, and environmental indicators
---

# SCB Environment Tables

This skill provides workflows for accessing Statistics Sweden's environmental data, including climate indicators, energy consumption, waste management, environmental protection, and sustainability metrics.

## Common Table IDs and Keywords

- **Climate Indicators**: TAB5055, TAB5057 (keywords: "climate", "klimat", "greenhouse gases")
- **Energy Consumption**: TAB3571, TAB3819 (keywords: "energy", "energi", "energy consumption")
- **Waste Management**: TAB5058, TAB5059 (keywords: "waste", "avfall", "waste management")
- **Environmental Protection**: TAB2844, TAB2843 (keywords: "environmental protection", "miljövård", "protection expenditures")
- **Water Resources**: TAB5055, TAB5057 (keywords: "water", "vatten", "water consumption")
- **Air Quality**: TAB6489, TAB6490 (keywords: "air quality", "luftkvalitet", "emissions")
- **Sustainability Indicators**: TAB5055, TAB5057 (keywords: "sustainability", "hållbarhet", "SDG indicators")

## Use Cases & Examples

### Retrieve Sustainability Development Goals Indicators
```
1. scb_opendata_mcp_search_tables(query="sustainability", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB5055")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB5055")
4. scb_opendata_mcp_get_table_data(table_id="TAB5055", selection=[
    {"variableCode": "sdg_mål", "valueCodes": ["7", "11", "12", "13"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

### Examine Air Quality Indicators
```
1. scb_opendata_mcp_search_tables(query="air quality", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB6489")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB6489")
4. scb_opendata_mcp_get_table_data(table_id="TAB6489", selection=[
    {"variableCode": "förorening", "valueCodes": ["NO2", "PM10", "SO2"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```