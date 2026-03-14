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

async def generate_housing_comparison():
    # Fetch housing data by type and region
    dataset1 = await get_table_data("TAB4384")
    dataset2 = await get_table_data("TAB4196")
    
    # Extract data from TAB4384 (Costs and price in newly constructed buildings)
    # Dimensions: ContentsCode, Region, Investor, Rooms
    regions1 = dataset1.dimension['Region']['category']['label']
    investors1 = dataset1.dimension['Investor']['category']['label']
    values1 = dataset1.value
    
    # Extract data from TAB4196 (Completed dwellings in special housing)
    # Dimensions: ContentsCode, Region, SpecialHousingType
    regions2 = dataset2.dimension['Region']['category']['label']
    housing_types2 = dataset2.dimension['SpecialHousingType']['category']['label']
    values2 = dataset2.value
    
    # Create DataFrames (simplified - real code would need proper reshaping)
    df1 = pd.DataFrame({
        'region': list(regions1.keys()),
        'investor': list(investors1.keys()),
        'cost': values1
    })
    
    df2 = pd.DataFrame({
        'region': list(regions2.keys()),
        'housing_type': list(housing_types2.keys()),
        'completed': values2
    })
    
    # Filter for specific regions (e.g., Stockholm region "01")
    stockholm_df1 = df1[df1['region'] == '01'].copy()
    stockholm_df2 = df2[df2['region'] == '01'].copy()
    
    # Create comparison visualization
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot 1: Construction costs by investor type
    plt.sca(axes[0])
    plt.bar(stockholm_df1['investor'], stockholm_df1['cost'])
    axes[0].set_title('Construction Costs by Investor Type (Stockholm)')
    axes[0].set_xlabel('Investor Type')
    axes[0].set_ylabel('Cost')
    axes[0].tick_params(axis='x', rotation=45)
    
    # Plot 2: Completed dwellings by housing type
    plt.sca(axes[1])
    plt.bar(stockholm_df2['housing_type'], stockholm_df2['completed'])
    axes[1].set_title('Completed Dwellings by Housing Type (Stockholm)')
    axes[1].set_xlabel('Housing Type')
    axes[1].set_ylabel('Number Completed')
    axes[1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('stockholm_housing_comparison.png')
    print("Housing comparison saved as stockholm_housing_comparison.png")

if __name__ == "__main__":
    asyncio.run(generate_housing_comparison())
