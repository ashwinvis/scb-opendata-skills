# /// script
# dependencies = [
#   "scb_opendata_mcp",
#   "pyjstat",
#   "pandas",
#   "matplotlib",
#   "seaborn",
#   "pydantic",
#   "rich"
# ]
# ///

import asyncio
from pyjstat import pyjstat
from scb_opendata_mcp.server import get_table_data
from scb_opendata_mcp.models import Dataset
import matplotlib.pyplot as plt
import seaborn as sns
from rich import print

async def validated_data_plot():
    # Fetch data with validation
    table_id = "TAB2844"  # Investment data
    raw_data = await get_table_data(
        table_id,
        selection= [
              {"variableCode": "SNI2007", "valueCodes": ["7-33+35-36"]},  # Total industry
              {"variableCode": "Miljoomrade", "valueCodes": ["100", "200"]},  # Air and Water protection
              {"variableCode": "ContentsCode", "valueCodes": ["MI1302AC"]},  # Investment values
              {"variableCode": "Tid", "valueCodes": ["from(2001)"]}
        ]
    )

    # Validate data structure
    try:
        ds = Dataset.model_validate(raw_data)
        print("Data validation successful")
    except Exception as e:
        print(f"Data validation failed: {e}")
        return

    # print(ds)
    # print(f"{ds.dimension = }")
    # print(f"{ds.note = }")

    # Transform validated data
    # TAB2844 has dimensions: ContentsCode, Tid (year), SNI2007 (industry), Miljoomrade (environmental area)
    years = ds.dimension["Tid"]["category"]["label"]
    environmental_areas = ds.dimension["Miljoomrade"]["category"]["label"]

    # Transform validated data using pyjstat
    dfs = pyjstat.from_json_stat(raw_data)
    df = dfs[0]
    print(df.columns)
    print(df.head())
    
    # Now we have both Air and Water protection data
    print(df)
    
    # Create investment visualization using seaborn
    plt.figure(figsize=(12, 8))
    sns.set_style("whitegrid")
    
    # Create bar plot with hue for different environmental areas
    ax = sns.barplot(
        data=df, 
        x="year", 
        y="value", 
        hue="environmental area ",
        palette="viridis",
        dodge=True  # Place bars side by side
    )
    
    plt.title("Investments in Environmental Protection: Air vs Water (TAB2844)", fontsize=16)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Investment (SEK million)", fontsize=12)
    plt.legend(title="Environmental Area", title_fontsize=12, fontsize=11)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("environmental_protection_investments.png")
    print("Investment visualization saved as environmental_protection_investments.png")


if __name__ == "__main__":
    asyncio.run(validated_data_plot())
