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
        'health': 'TAB5055',
        'housing': 'TAB513'
    }
    
    results = {}
    for indicator_name, table_id in indicators.items():
        dataset = await get_table_data(table_id)
        # Extract region data from each dataset
        if 'Region' in dataset.dimension:
            regions = dataset.dimension['Region']['category']['label']
            values = dataset.value
            df = pd.DataFrame({
                'region': list(regions.keys()),
                'value': values
            })
            results[indicator_name] = df
    
    # Create multi-panel visualization
    fig, axes = plt.subplots(3, 1, figsize=(12, 15))
    
    # Business statistics by region
    if 'business' in results:
        sns.barplot(data=results['business'], x='region', y='value', ax=axes[0])
        axes[0].set_title('Business Statistics by Region')
        axes[0].set_xticklabels([region_map.get(r, r) for r in results['business']['region']], rotation=45)
    
    # Health expenditure by region
    if 'health' in results:
        sns.barplot(data=results['health'], x='region', y='value', ax=axes[1])
        axes[1].set_title('Health Expenditure by Region')
        axes[1].set_xticklabels([region_map.get(r, r) for r in results['health']['region']], rotation=45)
    
    # Housing construction by region
    if 'housing' in results:
        sns.barplot(data=results['housing'], x='region', y='value', ax=axes[2])
        axes[2].set_title('Housing Construction by Region')
        axes[2].set_xticklabels([region_map.get(r, r) for r in results['housing']['region']], rotation=45)
    
    plt.tight_layout()
    plt.savefig('regional_dashboard.png')
    print("Regional dashboard saved as regional_dashboard.png")

if __name__ == "__main__":
    asyncio.run(generate_regional_dashboard())
