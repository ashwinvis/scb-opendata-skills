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

### Retrieve Current Population Statistics by Region
```
1. scb_opendata_mcp_search_tables(query="population", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB6008")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB6008")
4. scb_opendata_mcp_get_table_data(table_id="TAB6008", selection=[
    {"variableCode": "region", "valueCodes": ["01"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

### Analyze Birth Trends Over Time
```
1. scb_opendata_mcp_search_tables(query="births", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB5959")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB5959")
4. scb_opendata_mcp_get_table_data(table_id="TAB5959", selection=[
    {"variableCode": "år", "valueCodes": ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024"]},
    {"variableCode": "månad", "valueCodes": ["M01", "M02", "M03", "M04", "M05", "M06", "M07", "M08", "M09", "M10", "M11", "M12"]}
])
```

### Examine Mortality Rates by Age Group
```
1. scb_opendata_mcp_search_tables(query="deaths", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB5958")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB5958")
4. scb_opendata_mcp_get_table_data(table_id="TAB5958", selection=[
    {"variableCode": "ålder", "valueCodes": ["0-14"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
5. scb_opendata_mcp_get_table_data(table_id="TAB5958", selection=[
    {"variableCode": "ålder", "valueCodes": ["65+"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

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

### Examine Household Composition Statistics
```
1. scb_opendata_mcp_search_tables(query="households", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB4374")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB4374")
4. scb_opendata_mcp_get_table_data(table_id="TAB4374", selection=[
    {"variableCode": "hushållstyp", "valueCodes": ["ensam"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

### Compare Population Trends Across Regions
```
1. scb_opendata_mcp_search_tables(query="population", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB6008")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB6008")
4. scb_opendata_mcp_get_table_data(table_id="TAB6008", selection=[
    {"variableCode": "region", "valueCodes": ["01"]},
    {"variableCode": "år", "valueCodes": ["2020", "2024"]}
])
5. scb_opendata_mcp_get_table_data(table_id="TAB6008", selection=[
    {"variableCode": "region", "valueCodes": ["02"]},
    {"variableCode": "år", "valueCodes": ["2020", "2024"]}
])
```

### Analyze Demographic Changes Over Time
```
1. scb_opendata_mcp_search_tables(query="population", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB698")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB698")
4. scb_opendata_mcp_get_table_data(table_id="TAB698", selection=[
    {"variableCode": "år", "valueCodes": ["1990", "2000", "2010", "2020"]},
    {"variableCode": "ålder", "valueCodes": ["0-14", "15-64", "65+"]}
])
```