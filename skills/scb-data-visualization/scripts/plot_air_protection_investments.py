# /// script
# dependencies = [
#   "scb_opendata_mcp",
#   "pandas",
#   "matplotlib",
#   "pydantic",
#   "rich"
# ]
# ///

import asyncio
from scb_opendata_mcp.server import get_table_data
from scb_opendata_mcp.models import Dataset
import pandas as pd
import matplotlib.pyplot as plt
from rich import print

async def validated_data_plot():
    # Fetch data with validation
    table_id = "TAB2844"  # Investment data
    raw_data = await get_table_data(table_id)

    # Validate data structure
    try:
        ds = Dataset.model_validate(raw_data)
        print("Data validation successful")
    except Exception as e:
        print(f"Data validation failed: {e}")
        return

    print(ds)
    # print(f"{ds.dimension = }")
    # print(f"{ds.note = }")

    # Transform validated data
    # TAB2844 has dimensions: ContentsCode, Tid (year), SNI2007 (industry), Miljoomrade (environmental area)
    years = ds.dimension["Tid"]["category"]["label"]
    environmental_areas = ds.dimension["Miljoomrade"]["category"]["label"]

    # Create DataFrame - this is simplified, real code would need proper reshaping
    # The data structure is [SNI2007, ContentsCode, Tid, Miljoomrade] with size [20, 1, 1, 7]
    # We need to reshape the data properly
    df = pd.DataFrame(
        {
            "year": list(years.keys())
            * len(environmental_areas.keys())
            * 20,  # Repeat years for each combination
            "environmental_area": list(environmental_areas.keys())
            * 20,  # Repeat environmental areas for each industry
            "investment": ds.value,
        }
    )

    # Filter for a specific environmental area
    air_protection_df = df[df["environmental_area"] == "LUFT"].copy()

    # Create investment visualization
    plt.figure(figsize=(10, 6))
    plt.bar(air_protection_df["year"], air_protection_df["investment"], color="skyblue")
    plt.title("Investments in Air Protection (TAB2844)")
    plt.xlabel("Year")
    plt.ylabel("Investment (SEK million)")
    plt.grid(True, axis="y")
    plt.savefig("air_protection_investments.png")
    print("Investment visualization saved as air_protection_investments.png")


if __name__ == "__main__":
    asyncio.run(validated_data_plot())
