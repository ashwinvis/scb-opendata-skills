# /// script
# dependencies = [
#   "scb_opendata_mcp",
#   "pandas",
#   "seaborn",
#   "matplotlib"
# ]
# ///

import asyncio

from scb_opendata_mcp.server import get_table_data
from scb_opendata_mcp.models import Dataset

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


async def generate_regional_dashboard():
    # Initialize catgeory map - we'll use it to translate the category labels
    category_map = {}

    # Fetch data for multiple indicators
    indicators = {"business": "TAB6017", "health": "TAB5055", "housing": "TAB513"}

    results = {}
    for indicator_name, table_id in indicators.items():
        try:
            raw_data = await get_table_data(table_id)

            # Validate data structure
            try:
                dataset = Dataset.model_validate(raw_data)
            except Exception as e:
                print(f"Data validation failed for {table_id}: {e}")
                continue

            # Extract region data from each dataset
            print(dataset.dimension)
            if "ContentsCode" in dataset.dimension:
                # content_label = dataset.dimension["ContentsCode"]["label"]
                # cat_index = dataset.dimension['ContentsCode']['category']['index']
                categories = dataset.dimension["ContentsCode"]["category"]["label"]

                # Accumulate category_map from categories:
                category_map.update(categories)

                # For this simplified example, we'll just take the first value for each category
                # In a real implementation, you'd need to handle the multi-dimensional data properly
                values = dataset.value

                # Create a simple DataFrame with categories and values
                # Note: This is simplified - real data would need proper reshaping based on dimensions
                df = pd.DataFrame(
                    {
                        "category": list(categories.keys()),
                        # Take first N values matching number of categories
                        "value": values[: len(categories.keys())],
                    }
                )
                results[indicator_name] = df

        except Exception as e:
            print(f"Error processing {table_id}: {e}")
            continue

    # Create multi-panel visualization
    fig, axes = plt.subplots(3, 1, figsize=(12, 15))

    # Business statistics by region
    if "business" in results:
        sns.barplot(data=results["business"], x="category", y="value", ax=axes[0])
        axes[0].set_title("Business Statistics by Category")
        axes[0].set_xticklabels(
            [category_map.get(r, r) for r in results["business"]["category"]],
            rotation=45,
        )

    # Health expenditure by region
    if "health" in results:
        sns.barplot(data=results["health"], x="category", y="value", ax=axes[1])
        axes[1].set_title("Health Expenditure by Category")
        axes[1].set_xticklabels(
            [category_map.get(r, r) for r in results["health"]["category"]], rotation=45
        )

    # Housing construction by region
    if "housing" in results:
        sns.barplot(data=results["housing"], x="category", y="value", ax=axes[2])
        axes[2].set_title("Housing Construction by Category")
        axes[2].set_xticklabels(
            [category_map.get(r, r) for r in results["housing"]["category"]],
            rotation=45,
        )

    plt.tight_layout()
    plt.savefig("regional_dashboard.png")
    print("Regional dashboard saved as regional_dashboard.png")


if __name__ == "__main__":
    asyncio.run(generate_regional_dashboard())
