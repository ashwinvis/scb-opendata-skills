---
name: scb-education-research
description: Workflows and use cases for SCB Education and Research tables covering schools, universities, and R&D statistics
---

# SCB Education and Research Tables

This skill provides workflows for accessing Statistics Sweden's education and research data, including school statistics, university enrollment, R&D expenditures, innovation metrics, and educational outcomes.

## Common Table IDs and Keywords

- **School Statistics**: TAB2107, TAB372 (keywords: "schools", "skolor", "primary education")
- **University Statistics**: TAB1302, TAB1312 (keywords: "universities", "universitet", "higher education")
- **R&D Statistics**: TAB5798, TAB5794 (keywords: "R&D", "FoU", "research and development")
- **Innovation Statistics**: TAB3780, TAB3775 (keywords: "innovation", "innovation", "business innovation")
- **Adult Education**: TAB325, TAB3834 (keywords: "adult education", "vuxenutbildning", "continuing education")
- **Educational Outcomes**: TAB2107, TAB372 (keywords: "educational outcomes", "utbildningsresultat", "graduation rates")
- **International Students**: TAB1302, TAB1312 (keywords: "international students", "utbytesstudenter", "foreign students")

## Use Cases & Examples

### Retrieve Primary School Statistics
```
1. scb_opendata_mcp_search_tables(query="schools", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB2107")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB2107")
4. scb_opendata_mcp_get_table_data(table_id="TAB2107", selection=[
    {"variableCode": "skoltyp", "valueCodes": ["grundskola"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

### Analyze University Enrollment Trends
```
1. scb_opendata_mcp_search_tables(query="universities", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB1302")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB1302")
4. scb_opendata_mcp_get_table_data(table_id="TAB1302", selection=[
    {"variableCode": "utbildningsområde", "valueCodes": ["STEM", "humaniora"]},
    {"variableCode": "år", "valueCodes": ["2020", "2021", "2022", "2023", "2024"]}
])
```

### Examine R&D Expenditures by Sector
```
1. scb_opendata_mcp_search_tables(query="R&D", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB5798")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB5798")
4. scb_opendata_mcp_get_table_data(table_id="TAB5798", selection=[
    {"variableCode": "sektor", "valueCodes": ["företag", "högskola", "stat"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

### Retrieve Innovation Statistics for Business Sector
```
1. scb_opendata_mcp_search_tables(query="innovation", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB3780")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB3780")
4. scb_opendata_mcp_get_table_data(table_id="TAB3780", selection=[
    {"variableCode": "näringsgren", "valueCodes": ["tillverkning", "tjänster"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

### Analyze Adult Education Participation
```
1. scb_opendata_mcp_search_tables(query="adult education", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB325")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB325")
4. scb_opendata_mcp_get_table_data(table_id="TAB325", selection=[
    {"variableCode": "åldersgrupp", "valueCodes": ["25-44", "45-64"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

### Examine Educational Outcomes and Graduation Rates
```
1. scb_opendata_mcp_search_tables(query="schools", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB2107")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB2107")
4. scb_opendata_mcp_get_table_data(table_id="TAB2107", selection=[
    {"variableCode": "utbildningsnivå", "valueCodes": ["sekundär", "tertiär"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

### Retrieve International Student Statistics
```
1. scb_opendata_mcp_search_tables(query="universities", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB1302")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB1302")
4. scb_opendata_mcp_get_table_data(table_id="TAB1302", selection=[
    {"variableCode": "ursprungsland", "valueCodes": ["EU", "icke-EU"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```

### Compare Education Performance Across Regions
```
1. scb_opendata_mcp_search_tables(query="schools", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB2107")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB2107")
4. scb_opendata_mcp_get_table_data(table_id="TAB2107", selection=[
    {"variableCode": "region", "valueCodes": ["01", "02", "03"]},
    {"variableCode": "år", "valueCodes": ["2024"]}
])
```