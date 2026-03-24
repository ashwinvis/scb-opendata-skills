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