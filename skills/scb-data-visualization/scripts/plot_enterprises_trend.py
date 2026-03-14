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
    dataset = await get_table_data(table_id)
    
    # Extract data from dataset structure
    # Dataset has dimensions: ContentsCode (metrics), Tid (year), SNI2007 (industry)
    years = dataset.dimension['Tid']['category']['label']
    metrics = dataset.dimension['ContentsCode']['category']['label']
    values = dataset.value
    
    # Create DataFrame - reshape the data for plotting
    # This is a simplified example - real code would need proper reshaping
    df = pd.DataFrame({
        'year': list(years.keys()),
        'metric': list(metrics.keys()),
        'value': values
    })
    
    # Filter for a specific metric (e.g., number of enterprises)
    enterprises_df = df[df['metric'] == '000007DX'].copy()
    
    # Create visualization
    plt.figure(figsize=(10, 6))
    plt.bar(enterprises_df['year'], enterprises_df['value'])
    plt.title('Number of Enterprises by Year (TAB6017)')
    plt.xlabel('Year')
    plt.ylabel('Number of Enterprises')
    plt.grid(True)
    plt.savefig('enterprises_trend.png')
    print("Visualization saved as enterprises_trend.png")

if __name__ == "__main__":
    asyncio.run(main())
