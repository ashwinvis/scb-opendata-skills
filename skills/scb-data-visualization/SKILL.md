---
name: scb-data-visualization
description: Generate Python scripts for fetching SCB table data and creating visualizations using matplotlib and seaborn
---

# SCB Data Visualization Script Generation

This skill generates Python scripts that fetch data from Statistics Sweden (SCB) tables and create visualizations. The scripts use the scb_opendata_mcp API to retrieve data, transform it with pandas, and visualize it using matplotlib or seaborn.

## Common Table IDs for Visualization

- **Business Economy**: TAB6017 (business statistics), TAB2844 (investments), TAB3780 (innovation)
- **Environment**: TAB5055 (environmental indicators), TAB3571 (energy), TAB2496 (children's working environment)
- **Housing**: TAB513 (construction), TAB4384 (housing types), TAB4196 (completed dwellings)
- **Education**: TAB4879 (life tables by education), TAB1302 (students), TAB5798 (research)
- **International Trade**: TAB5440 (trade), TAB1630 (electronics), TAB6695 (services)

## Script Generation Examples

### Basic Script Template

```python
# /// script
# dependencies = [
#   "scb_opendata_mcp",
#   "pandas",
#   "matplotlib"
# ]
# ///

import asyncio
from scb_opendata_mcp.server import get_table_data
import pandas as pd
import matplotlib.pyplot as plt

async def main():
    # Fetch data from SCB table
    table_id = "TAB6017"  # Business statistics
    data = await get_table_data(table_id)
    
    # Transform data to pandas DataFrame
    df = pd.DataFrame(data['values'])
    
    # Create visualization
    plt.figure(figsize=(10, 6))
    plt.plot(df['year'], df['population'])
    plt.title('Population Trend in Stockholm (15-64 years)')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.grid(True)
    plt.savefig('population_trend.png')
    print("Visualization saved as population_trend.png")

if __name__ == "__main__":
    asyncio.run(main())
```

### Advanced Script with Multiple Data Sources

```python
# /// script
# dependencies = [
#   "scb_opendata_mcp",
#   "pandas",
#   "seaborn"
# ]
# ///

import asyncio
from scb_opendata_mcp.server import get_table_data, get_table_metadata
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

async def fetch_and_plot_comparison():
    # Fetch employment data for multiple regions
    regions = ["01", "03", "14"]  # Stockholm, Uppsala, Västra Götaland
    employment_data = []
    
    for region in regions:
        data = await get_table_data("TAB5055")
        df = pd.DataFrame(data['values'])
        df['region'] = region
        employment_data.append(df)
    
    # Combine data
    combined_df = pd.concat(employment_data)
    
    # Create comparison plot
    plt.figure(figsize=(12, 8))
    sns.lineplot(data=combined_df, x='year', y='employment_rate', hue='region', marker='o')
    plt.title('Employment Rate Comparison: Stockholm vs Uppsala vs Västra Götaland')
    plt.xlabel('Year')
    plt.ylabel('Employment Rate (%)')
    plt.legend(title='Region')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('employment_comparison.png')
    print("Comparison visualization saved as employment_comparison.png")

if __name__ == "__main__":
    asyncio.run(fetch_and_plot_comparison())
```

### Script with Data Validation

```python
# /// script
# dependencies = [
#   "scb_opendata_mcp",
#   "pandas",
#   "matplotlib",
#   "pydantic"
# ]
# ///

import asyncio
from scb_opendata_mcp.server import get_table_data
from scb_opendata_mcp.models import Dataset
import pandas as pd
import matplotlib.pyplot as plt

async def validated_data_plot():
    # Fetch data with validation
    table_id = "TAB2844"  # Investment data
    raw_data = await get_table_data(table_id)
    
    # Validate data structure
    try:
        validated_data = Dataset(**raw_data)
        print("Data validation successful")
    except Exception as e:
        print(f"Data validation failed: {e}")
        return
    
    # Transform validated data
    df = pd.DataFrame({
        'year': validated_data.dimension['tid']['category']['index'],
        'gdp': validated_data.value
    })
    
    # Create GDP growth visualization
    df['gdp_growth'] = df['gdp'].pct_change() * 100
    
    plt.figure(figsize=(10, 6))
    plt.bar(df['year'], df['gdp_growth'], color='skyblue')
    plt.title('Sweden GDP Annual Growth Rate')
    plt.xlabel('Year')
    plt.ylabel('GDP Growth (%)')
    plt.axhline(0, color='red', linestyle='--', linewidth=1)
    plt.grid(True, axis='y')
    plt.savefig('gdp_growth.png')
    print("GDP growth visualization saved as gdp_growth.png")

if __name__ == "__main__":
    asyncio.run(validated_data_plot())
```

## Use Cases & Examples

### Generate Population Pyramid Script

```python
# /// script
# dependencies = [
#   "scb_opendata_mcp",
#   "pandas",
#   "matplotlib"
# ]
# ///

import asyncio
from scb_opendata_mcp.server import get_table_data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

async def generate_population_pyramid():
    # Fetch housing data by type
    data1 = await get_table_data("TAB4384")
    data2 = await get_table_data("TAB4196")
    
    # Process data
    male_df = pd.DataFrame(male_data['values'])
    female_df = pd.DataFrame(female_data['values'])
    
    # Create population pyramid
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Male population (left side)
    ax.barh(male_df['age_group'], male_df['population'] / -1000, color='blue', label='Male')
    
    # Female population (right side)
    ax.barh(female_df['age_group'], female_df['population'] / 1000, color='pink', label='Female')
    
    ax.set_title('Sweden Population Pyramid (2023)')
    ax.set_xlabel('Population (thousands)')
    ax.set_ylabel('Age Group')
    ax.legend()
    ax.grid(True, axis='y')
    
    plt.tight_layout()
    plt.savefig('population_pyramid.png')
    print("Population pyramid saved as population_pyramid.png")

if __name__ == "__main__":
    asyncio.run(generate_population_pyramid())
```

### Generate Regional Comparison Dashboard

```python
# /// script
# dependencies = [
#   "scb_opendata_mcp",
#   "pandas",
#   "seaborn",
#   "matplotlib"
# ]
# ///

import asyncio
from scb_opendata_mcp.server import get_table_data, get_codelist
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

async def generate_regional_dashboard():
    # Get region codelist for labels
    regions_codelist = await get_codelist("Region")
    region_map = {code['code']: code['label'] for code in regions_codelist['codes']}
    
    # Fetch data for multiple indicators
    indicators = {
        'business': 'TAB6017',
        'environment': 'TAB5055',
        'housing': 'TAB513'
    }
    
    results = {}
    for indicator_name, table_id in indicators.items():
        data = await get_table_data(table_id)
        df = pd.DataFrame(data['values'])
        results[indicator_name] = df
    
    # Create multi-panel visualization
    fig, axes = plt.subplots(3, 1, figsize=(12, 15))
    
    # Employment by region
    sns.barplot(data=results['employment'], x='region', y='employment_rate', ax=axes[0])
    axes[0].set_title('Employment Rate by Region')
    axes[0].set_xticklabels([region_map.get(r, r) for r in results['employment']['region']], rotation=45)
    
    # GDP by region
    sns.barplot(data=results['gdp'], x='region', y='gdp_per_capita', ax=axes[1])
    axes[1].set_title('GDP per Capita by Region')
    axes[1].set_xticklabels([region_map.get(r, r) for r in results['gdp']['region']], rotation=45)
    
    # Population by region
    sns.barplot(data=results['population'], x='region', y='population', ax=axes[2])
    axes[2].set_title('Population by Region')
    axes[2].set_xticklabels([region_map.get(r, r) for r in results['population']['region']], rotation=45)
    
    plt.tight_layout()
    plt.savefig('regional_dashboard.png')
    print("Regional dashboard saved as regional_dashboard.png")

if __name__ == "__main__":
    asyncio.run(generate_regional_dashboard())
```

## Running the Scripts

All generated scripts include the required dependency declarations and can be run using:

```bash
# Preferred method - using uv
uv run script_name.py

# Alternative methods
pipx run script_name.py

# Using python directly (after installing dependencies)
python script_name.py
```

**Note**: `uv run` is the preferred method as it provides better performance and dependency management.

## Key Features

- **Table ID Hardcoding**: Scripts use hardcoded table IDs but fetch live data
- **API Integration**: Uses scb_opendata_mcp server tools for data retrieval
- **Data Validation**: Optional validation using Pydantic models
- **Pandas Integration**: Data transformation and analysis
- **Visualization**: Matplotlib and Seaborn for professional charts
- **Dependency Management**: Clear dependency declarations for easy execution