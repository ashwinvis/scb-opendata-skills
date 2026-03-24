---
name: scb-energy-electricity
description: Workflows and use cases for SCB Energy and Electricity tables covering energy consumption, production, and electricity statistics
---

# SCB Energy and Electricity Tables

This skill provides workflows for accessing Statistics Sweden's energy and electricity data, including energy consumption, production, electricity statistics, and related metrics.

## Common Table IDs and Keywords

- **Energy Consumption**: TAB3571, TAB3819, TAB6399, TAB991 (keywords: "energy", "energi", "energy consumption")
- **Electricity Production**: TAB3571, TAB3819, TAB5644, TAB1010, TAB1011 (keywords: "electricity", "el", "electricity production")
- **Energy Sources**: TAB3571, TAB3819, TAB1010, TAB1011 (keywords: "energy sources", "energikälla", "renewable energy")
- **Electricity Prices**: TAB3819, TAB3950, TAB4310, TAB4311 (keywords: "electricity prices", "elpriser")
- **Electricity Contracts**: TAB3571, TAB3584, TAB4480 (keywords: "electricity contracts", "elavtal")

## Use Cases & Examples

### Analyze Energy Consumption by Source

```
1. scb_opendata_mcp_search_tables(query="energy", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB6399")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB6399")
4. scb_opendata_mcp_get_table_data(table_id="TAB6399", selection=[
    {"variableCode": "AnvOmrade", "valueCodes": ["Tot", "Exp"]},
    {"variableCode": "Tid", "valueCodes": ["2025M01"]}
])
```

### Examine Electricity Production Statistics

```
1. scb_opendata_mcp_search_tables(query="electricity", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB5644")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB5644")
4. scb_opendata_mcp_get_table_data(table_id="TAB5644", selection=[
    {"variableCode": "Produktionsslag", "valueCodes": ["Total", "Vattenkraft", "Vindkraft"]},
    {"variableCode": "Tid", "valueCodes": ["2025M01"]}
])
```

### Compare Energy Consumption Across Sectors

```
1. scb_opendata_mcp_search_tables(query="energy", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB6399")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB6399")
4. scb_opendata_mcp_get_table_data(table_id="TAB6399", selection=[
    {"variableCode": "AnvOmrade", "valueCodes": ["ElGasVärm", "JärnSpårBuss", "Bosts"]},
    {"variableCode": "Tid", "valueCodes": ["2025M01"]}
])
```

### Analyze Renewable Energy Trends

```
1. scb_opendata_mcp_search_tables(query="renewable energy", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB1010")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB1010")
4. scb_opendata_mcp_get_table_data(table_id="TAB1010", selection=[
    {"variableCode": "Prodslag", "valueCodes": ["Vattenkraft", "Vind", "sol"]},
    {"variableCode": "Tid", "valueCodes": ["2020", "2021", "2022", "2023", "2024"]}
])
```

### Examine Energy Production by Region

```
1. scb_opendata_mcp_search_tables(query="energy", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB1010")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB1010")
4. scb_opendata_mcp_get_table_data(table_id="TAB1010", selection=[
    {"variableCode": "Prodslag", "valueCodes": ["Tot", "Vattenkraft", "Karnkraft"]},
    {"variableCode": "Tid", "valueCodes": ["2024"]}
])
```

### Compare Fossil vs Renewable Energy Consumption

```
1. scb_opendata_mcp_search_tables(query="energy", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB6399")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB6399")
4. scb_opendata_mcp_get_table_data(table_id="TAB6399", selection=[
    {"variableCode": "AnvOmrade", "valueCodes": ["ElGasVärm", "JärnSpårBuss", "Bosts"]},
    {"variableCode": "Tid", "valueCodes": ["2025M01", "2025M02", "2025M03"]}
])
```