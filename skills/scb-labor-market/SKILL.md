---
name: scb-labor-market
description: Workflows and use cases for SCB Labor Market tables covering employment, wages, working hours, and labor costs
---

# SCB Labor Market Tables

This skill provides workflows for accessing Statistics Sweden's comprehensive labor market data, including employment statistics, wage information, working hours, labor costs, and related economic indicators.

## Common Table IDs and Keywords

- **Employment Statistics**: TAB4707, TAB4714, TAB4718, TAB4723 (keywords: "employment", "anställningar", "ongoing employments")
- **Wage Data**: TAB6047, TAB6048 (keywords: "wages", "lönesummor", "salary sums")
- **Working Hours**: TAB5191, TAB6650 (keywords: "working hours", "arbetad tid", "hours worked")
- **Labor Costs**: TAB68, TAB72 (keywords: "labor costs", "arbetskostnadsindex", "labor cost index")
- **Sickness Absence**: TAB6458, TAB6467, TAB6468 (keywords: "sickness absence", "sjukfrånvaro")
- **Employment Flow**: TAB6012, TAB6016 (keywords: "employment flow", "flöde anställningar")

## Use Cases & Examples

### Find Current Employment Statistics by Sector
```
1. scb_opendata_mcp_search_tables(query="employment", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB4707")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB4707")
4. scb_opendata_mcp_get_table_data(table_id="TAB4707", selection=[
    {"variableCode": "sektor", "valueCodes": ["privat"]},
    {"variableCode": "månad", "valueCodes": ["2025M12"]}
])
```

### Compare Wages Across Public and Private Sectors
```
1. scb_opendata_mcp_search_tables(query="wages", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB6047")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB6047")
4. scb_opendata_mcp_get_table_data(table_id="TAB6047", selection=[
    {"variableCode": "sektor", "valueCodes": ["privat"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
5. scb_opendata_mcp_get_table_data(table_id="TAB6047", selection=[
    {"variableCode": "sektor", "valueCodes": ["offentlig"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

### Analyze Working Hours Trends by Industry
```
1. scb_opendata_mcp_search_tables(query="working hours", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB5191")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB5191")
4. scb_opendata_mcp_get_table_data(table_id="TAB5191", selection=[
    {"variableCode": "sektor", "valueCodes": ["privat"]},
    {"variableCode": "näringsgren", "valueCodes": ["C"]},
    {"variableCode": "kvartal", "valueCodes": ["2024K4"]}
])
```

### Retrieve Labor Cost Index for Economic Analysis
```
1. scb_opendata_mcp_search_tables(query="labor cost", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB68")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB68")
4. scb_opendata_mcp_get_table_data(table_id="TAB68", selection=[
    {"variableCode": "år", "valueCodes": ["2024"]},
    {"variableCode": "kvartal", "valueCodes": ["K4"]}
])
```

### Compare Employment by Gender and Region
```
1. scb_opendata_mcp_search_tables(query="employment", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB4718")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB4718")
4. scb_opendata_mcp_get_table_data(table_id="TAB4718", selection=[
    {"variableCode": "kön", "valueCodes": ["1"]},
    {"variableCode": "region", "valueCodes": ["01"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
5. scb_opendata_mcp_get_table_data(table_id="TAB4718", selection=[
    {"variableCode": "kön", "valueCodes": ["2"]},
    {"variableCode": "region", "valueCodes": ["01"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

### Analyze Sickness Absence Trends by Sector
```
1. scb_opendata_mcp_search_tables(query="sickness absence", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB6458")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB6458")
4. scb_opendata_mcp_get_table_data(table_id="TAB6458", selection=[
    {"variableCode": "sektor", "valueCodes": ["privat"]},
    {"variableCode": "år", "valueCodes": ["2024"]},
    {"variableCode": "kvartal", "valueCodes": ["K1", "K2", "K3", "K4"]}
])
```

### Examine Employment Flow Statistics
```
1. scb_opendata_mcp_search_tables(query="employment flow", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB6012")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB6012")
4. scb_opendata_mcp_get_table_data(table_id="TAB6012", selection=[
    {"variableCode": "kön", "valueCodes": ["1+2"]},
    {"variableCode": "storleksklass", "valueCodes": ["10-49"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

### Analyze Employment Trends by Industry
```
1. scb_opendata_mcp_search_tables(query="employment", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB4723")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB4723")
4. scb_opendata_mcp_get_table_data(table_id="TAB4723", selection=[
    {"variableCode": "näringsgren", "valueCodes": ["C"]},
    {"variableCode": "år", "valueCodes": ["2024"]},
    {"variableCode": "månad", "valueCodes": ["M12"]}
])
```