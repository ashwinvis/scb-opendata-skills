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
    # Fetch health care expenditure data
    dataset = await get_table_data("TAB5055")
    
    # Extract data from dataset structure
    # TAB5055 has dimensions: ContentsCode, Tid (year), HC (health care function)
    years = dataset.dimension['Tid']['category']['label']
    health_functions = dataset.dimension['HC']['category']['label']
    values = dataset.value
    
    # Create DataFrame
    df = pd.DataFrame({
        'year': list(years.keys()),
        'health_function': list(health_functions.keys()),
        'expenditure': values
    })
    
    # Filter for specific health functions and years for comparison
    # This is a simplified example - real code would need proper filtering
    comparison_df = df[df['health_function'].isin(['HC1', 'HC2', 'HC3'])]
    
    # Create comparison plot
    plt.figure(figsize=(12, 8))
    sns.lineplot(data=comparison_df, x='year', y='expenditure', hue='health_function', marker='o')
    plt.title('Health Care Expenditure by Function (TAB5055)')
    plt.xlabel('Year')
    plt.ylabel('Expenditure')
    plt.legend(title='Health Function')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('health_expenditure_comparison.png')
    print("Comparison visualization saved as health_expenditure_comparison.png")

if __name__ == "__main__":
    asyncio.run(fetch_and_plot_comparison())
