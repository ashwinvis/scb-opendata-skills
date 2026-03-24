---
name: scb-opendata-mcp-workflows
description: Use cases and workflows to show how to invoke a tool, or chain multiple tools. Tools are available when connected to the MCP server scb_opendata_mcp. This skill helps with finding statistical data, comparing data across regions, saving and retrieving common queries, exploring available codelists, getting detailed metadata for a table, searching and retrieving data with pagination, and aggregating data using codelists.
---

# SCB Open-data MCP server

MCP server which provides tool calls to interface with Statistics Sweden's API.

## Use Cases & Examples

### Find Statistical Data for a Specific Region

```
1. scb_opendata_mcp_search_tables(query="employment", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB4707")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB4707")
4. scb_opendata_mcp_get_table_data(table_id="TAB4707", selection=[
    {"variableCode": "region", "valueCodes": ["01"]},
    {"variableCode": "age", "valueCodes": ["15-64"]}
])
```

### Compare Statistical Data Across Regions

```
1. scb_opendata_mcp_search_tables(query="employment", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB4707")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB4707")
4. scb_opendata_mcp_get_table_data(table_id="TAB4707", selection=[
    {"variableCode": "region", "valueCodes": ["01"]},
    {"variableCode": "age", "valueCodes": ["15-64"]}
])
5. scb_opendata_mcp_get_table_data(table_id="TAB4707", selection=[
    {"variableCode": "region", "valueCodes": ["02"]},
    {"variableCode": "age", "valueCodes": ["15-64"]}
])
```

### Save and Retrieve a Common Query

```
1. scb_opendata_mcp_save_query(table_id="TAB2844", selection=[
    {"variableCode": "SNI2007", "valueCodes": ["7-33+35-36"]},
    {"variableCode": "Miljoomrade", "valueCodes": ["000", "100", "200", "300", "400"]},
    {"variableCode": "ContentsCode", "valueCodes": ["MI1302AC"]},
    {"variableCode": "Tid", "valueCodes": ["from(2001)"]}
])
2. scb_opendata_mcp_get_saved_query(query_id="501779")
3. scb_opendata_mcp_get_saved_query_data(query_id="501779")
4. scb_opendata_mcp_get_saved_query_selection(query_id="501779")
```

### Explore Available Codelists

```
1. scb_opendata_mcp_list_codelists(table_id="TAB4707")
2. scb_opendata_mcp_get_codelist(codelist_id="Region")
3. scb_opendata_mcp_get_codelist(codelist_id="Age")
```

### Get Detailed Metadata for a Table

```
1. scb_opendata_mcp_get_table_metadata(table_id="TAB4707")
2. scb_opendata_mcp_get_table_default_selection(table_id="TAB4707")
```

### Search and Retrieve Statistical Data with Pagination

```
1. scb_opendata_mcp_search_tables(query="wage", lang="en", page_size=20)
2. scb_opendata_mcp_get_table_metadata(table_id="TAB6047")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB6047")
4. scb_opendata_mcp_get_table_data(table_id="TAB6047", selection=[
    {"variableCode": "age", "valueCodes": ["15-64"]}
])
```

### Retrieve Statistical Data by Age and Sex

```
1. scb_opendata_mcp_search_tables(query="population", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB6008")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB6008")
4. scb_opendata_mcp_get_table_data(table_id="TAB6008", selection=[
    {"variableCode": "age", "valueCodes": ["15-64"]},
    {"variableCode": "sex", "valueCodes": ["1"]}
])
```

### Analyze Statistical Data Across Different Sectors

```
1. scb_opendata_mcp_search_tables(query="labor cost", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB68")
3. scb_opendata_mcp_get_table_default_selection(table_id="TAB68")
4. scb_opendata_mcp_get_table_data(table_id="TAB68", selection=[
    {"variableCode": "sector", "valueCodes": ["private"]},
    {"variableCode": "year", "valueCodes": ["2023"]}
])
```

### Aggregate Data Using Codelists

```
1. scb_opendata_mcp_search_tables(query="population", lang="en")
2. scb_opendata_mcp_get_table_metadata(table_id="TAB4562")
3. scb_opendata_mcp_list_codelists(table_id="TAB4562")
4. scb_opendata_mcp_get_table_data(table_id="TAB4562", selection=[
    {"variableCode": "Region", "codelist": "agg_RegionNUTS2_2008", "valueCodes": ["*"]},
    {"variableCode": "Vattenanslutning", "valueCodes": ["10"]},
    {"variableCode": "ContentsCode", "valueCodes": ["000000VP"]},
    {"variableCode": "Tid", "valueCodes": ["2023"]}
])
```
