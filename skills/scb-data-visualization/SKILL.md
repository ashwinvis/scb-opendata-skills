---
name: scb-data-visualization
description: Generate Python scripts for fetching SCB table data and creating visualizations using matplotlib and seaborn
---

# SCB Data Visualization Script Generation

This skill generates Python scripts that fetch data from Statistics Sweden (SCB) tables and create visualizations. The scripts use the scb_opendata_mcp API to retrieve data, transform it with pandas, and visualize it using matplotlib or seaborn.

## Sample Table IDs for demonstrating visualization

- **Environment**: TAB2844 (environmental protection investments indicators)

## Available Scripts

The following example Python scripts are available in the `scripts/` directory:

- **`scripts/plot_environmental_protection_investments.py`** — Script plotting bar chart based on data on environmental investments using TAB2844

## Workflow

Each script follows the same pattern:
1. Fetch data using `get_table_data()` with hardcoded table IDs
2. Extract dimensions and values from the Dataset structure
3. Transform data into pandas DataFrames
4. Create visualizations using matplotlib or seaborn
5. Save output as PNG files

## Running the Scripts

All generated scripts include the required dependency declarations and can be run using:

```bash
# Preferred method - using uv
uv run scripts/script_name.py

# Alternative methods
pipx run scripts/script_name.py

# Fallback: Using python directly (after installing dependencies in a venv)
python3 scripts/script_name.py
```

**Note**: `uv run` is the preferred method as it provides better performance and dependency management.

**P.S**: If this is not possible and the fallback option is chosen, read this [packaging guide] on how to install using venvs:

[packaging guide]: https://raw.githubusercontent.com/pypa/packaging.python.org/refs/heads/main/source/guides/installing-using-pip-and-virtual-environments.rst

### Installing `uv`

If `uv` is missing you can install it by running:

macOS / Linux:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows:

```pwsh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Guidelines

- **Hardcode Table IDs only, not raw table data**: Scripts use hardcoded table IDs but fetch live data. Avoid embedding raw data in the scripts.
- **API Integration**: Uses scb_opendata_mcp server tools for data retrieval
- **Data Validation**: Optional validation using Pydantic models
- **Dependency Management**: Clear dependency declarations for easy execution in the top of the script.
