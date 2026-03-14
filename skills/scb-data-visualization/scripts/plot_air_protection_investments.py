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
    # TAB2844 has dimensions: ContentsCode, Tid (year), SNI2007 (industry), Miljömiljöområde (environmental area)
    years = validated_data.dimension['Tid']['category']['label']
    environmental_areas = validated_data.dimension['Miljömiljöområde']['category']['label']
    
    # Create DataFrame - this is simplified, real code would need proper reshaping
    df = pd.DataFrame({
        'year': list(years.keys()),
        'environmental_area': list(environmental_areas.keys()),
        'investment': validated_data.value
    })
    
    # Filter for a specific environmental area
    air_protection_df = df[df['environmental_area'] == 'LUFT'].copy()
    
    # Create investment visualization
    plt.figure(figsize=(10, 6))
    plt.bar(air_protection_df['year'], air_protection_df['investment'], color='skyblue')
    plt.title('Investments in Air Protection (TAB2844)')
    plt.xlabel('Year')
    plt.ylabel('Investment (SEK million)')
    plt.grid(True, axis='y')
    plt.savefig('air_protection_investments.png')
    print("Investment visualization saved as air_protection_investments.png")

if __name__ == "__main__":
    asyncio.run(validated_data_plot())
