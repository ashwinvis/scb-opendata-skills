# /// script
# dependencies = [
#   "scb_opendata_mcp",
#   "pandas",
#   "matplotlib"
# ]
# ///

import asyncio
from scb_opendata_mcp.server import get_table_data
from scb_opendata_mcp.models import Dataset
import pandas as pd
import matplotlib.pyplot as plt


async def generate_housing_comparison():
    # Fetch housing data by type and region
    raw_data1 = await get_table_data("TAB4384")
    raw_data2 = await get_table_data("TAB4196")

    # Validate data structure
    try:
        dataset1 = Dataset(**raw_data1)
        dataset2 = Dataset(**raw_data2)
        print("Data validation successful")
    except Exception as e:
        print(f"Data validation failed: {e}")
        return

    # Extract data from TAB4384 (Costs and price in newly constructed buildings)
    # Dimensions: ContentsCode, Region, AntalRum (number of rooms), Tid
    regions1 = dataset1.dimension["Region"]["category"]["label"]
    rooms1 = dataset1.dimension["AntalRum"]["category"]["label"]
    values1 = dataset1.value

    # Extract data from TAB4196 (Completed dwellings in special housing)
    # Dimensions: ContentsCode, Region, TypAvSpecialbostad (type of special housing)
    regions2 = dataset2.dimension["Region"]["category"]["label"]
    housing_types2 = dataset2.dimension["TypAvSpecialbostad"]["category"]["label"]
    values2 = dataset2.value

    # Create DataFrames (simplified - real code would need proper reshaping)
    # The data structure is [AntalRum, ContentsCode, Tid, Region] with size [6, 1, 1, 1]
    df1 = pd.DataFrame(
        {
            "region": list(regions1.keys())
            * len(rooms1.keys()),  # Repeat region for each room count
            "rooms": list(rooms1.keys()),  # List of room counts
            "cost": values1,
        }
    )

    # The data structure is [Region, ContentsCode, Tid, TypAvSpecialbostad] with size [21, 1, 1, 3]
    df2 = pd.DataFrame(
        {
            "region": list(regions2.keys())
            * len(housing_types2.keys()),  # Repeat region for each housing type
            "housing_type": list(housing_types2.keys())
            * 21,  # Repeat housing types for each region
            "completed": values2,
        }
    )

    # Filter for specific regions (e.g., Stockholm region "01")
    stockholm_df1 = df1[df1["region"] == "01"].copy()
    stockholm_df2 = df2[df2["region"] == "01"].copy()

    # Create comparison visualization
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Plot 1: Construction costs by number of rooms
    plt.sca(axes[0])
    plt.bar(stockholm_df1["rooms"], stockholm_df1["cost"])
    axes[0].set_title("Construction Costs by Number of Rooms (Stockholm)")
    axes[0].set_xlabel("Number of Rooms")
    axes[0].set_ylabel("Cost")
    axes[0].tick_params(axis="x", rotation=45)

    # Plot 2: Completed dwellings by housing type
    plt.sca(axes[1])
    plt.bar(stockholm_df2["housing_type"], stockholm_df2["completed"])
    axes[1].set_title("Completed Dwellings by Housing Type (Stockholm)")
    axes[1].set_xlabel("Housing Type")
    axes[1].set_ylabel("Number Completed")
    axes[1].tick_params(axis="x", rotation=45)

    plt.tight_layout()
    plt.savefig("stockholm_housing_comparison.png")
    print("Housing comparison saved as stockholm_housing_comparison.png")


if __name__ == "__main__":
    asyncio.run(generate_housing_comparison())
