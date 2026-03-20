---
name: scb-business-economy
description: Workflows and use cases for SCB Business Economy tables covering industry statistics, IT usage, and economic performance
---

# SCB Business Economy Tables

This skill provides workflows for accessing Statistics Sweden's business and economic data, including industry statistics, IT usage in businesses, economic performance indicators, and various business-related metrics.

## Common Table IDs and Keywords

- **Business Register**: TAB6017, TAB6062, TAB6262 (keywords: "business register", "företagsregister", "company statistics")
- **Industry Statistics**: TAB6343, TAB6382 (keywords: "industry statistics", "näringsgren", "sector performance")
- **IT Usage in Business**: TAB4672, TAB4673 (keywords: "IT usage", "IT-användning", "digitalization")
- **Business Demographics**: TAB6017, TAB6062 (keywords: "business demographics", "företagsdemografi", "company age")
- **Innovation Statistics**: TAB3780, TAB3775 (keywords: "innovation", "innovation", "R&D statistics")
- **E-commerce**: TAB6695, TAB6696 (keywords: "e-commerce", "e-handel", "online sales")
- **Business Investments**: TAB2844, TAB2843 (keywords: "business investments", "företagsinvesteringar", "capital expenditures")

## Use Cases & Examples

### Retrieve Current Business Register Statistics
```
1. scb_opendata_mcp_search_tables(query="business register", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB6017")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB6017")
4. scb_opendata_mcp_get_table_data(table_id="TAB6017", selection=[
    {"variableCode": "näringsgren", "valueCodes": ["C", "D", "E"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

### Analyze Industry Performance by Sector
```
1. scb_opendata_mcp_search_tables(query="industry statistics", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB6343")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB6343")
4. scb_opendata_mcp_get_table_data(table_id="TAB6343", selection=[
    {"variableCode": "sektor", "valueCodes": ["tillverkning", "tjänster"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

### Examine IT Usage in Businesses
```
1. scb_opendata_mcp_search_tables(query="IT usage", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB4672")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB4672")
4. scb_opendata_mcp_get_table_data(table_id="TAB4672", selection=[
    {"variableCode": "näringsgren", "valueCodes": ["alla"]},
    {"variableCode": "it_användning", "valueCodes": ["moln", "ai", "stordata"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

### Retrieve Business Demographics and Company Age
```
1. scb_opendata_mcp_search_tables(query="business demographics", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB6017")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB6017")
4. scb_opendata_mcp_get_table_data(table_id="TAB6017", selection=[
    {"variableCode": "företagsålder", "valueCodes": ["0-2", "3-5", "10+"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

### Analyze Innovation Statistics and R&D
```
1. scb_opendata_mcp_search_tables(query="innovation", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB3780")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB3780")
4. scb_opendata_mcp_get_table_data(table_id="TAB3780", selection=[
    {"variableCode": "innovationstyp", "valueCodes": ["produkt", "process"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

### Examine E-commerce Trends
```
1. scb_opendata_mcp_search_tables(query="e-commerce", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB6695")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB6695")
4. scb_opendata_mcp_get_table_data(table_id="TAB6695", selection=[
    {"variableCode": "sektor", "valueCodes": ["detaljhandel", "partihandel"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

### Retrieve Business Investment Statistics
```
1. scb_opendata_mcp_search_tables(query="business investments", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB2844")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB2844")
4. scb_opendata_mcp_get_table_data(table_id="TAB2844", selection=[
    {"variableCode": "investeringstyp", "valueCodes": ["maskiner", "mjukvara"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

### Compare Business Performance Across Regions
```
1. scb_opendata_mcp_search_tables(query="business register", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB6017")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB6017")
4. scb_opendata_mcp_get_table_data(table_id="TAB6017", selection=[
    {"variableCode": "region", "valueCodes": ["01", "02", "03"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```