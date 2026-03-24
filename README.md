# SCB Open Data Skills

SCB Open Data Skills are definitions for accessing Statistics Sweden's comprehensive statistical data through the SCB Open Data MCP server. These skills are interoperable with major coding agent tools and provide standardized workflows for retrieving, analyzing, and working with Swedish official statistics.

The skills in this repository follow the standardized Agent Skills format and are designed to work with the [SCB Open Data MCP Server].

[SCB Open Data MCP Server]: https://github.com/ashwinvis/scb-opendata-mcp

## How do Skills work?

Skills are self-contained folders that package instructions, workflows, and resources for AI agents to access specific SCB statistical domains. Each folder includes a `SKILL.md` file with YAML frontmatter (name and description) followed by detailed guidance on table IDs, keywords, and use case examples.

## Installation

SCB Open Data skills are compatible with various coding agent frameworks that support the Agent Skills standard.

### Generic instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/ashwinvis/scb-opendata-skills.git
   ```

2. Symlink or copy skill folders to your agent's skills directory
3. Ensure your agent is configured to connect to the [SCB Open Data MCP Server].


## Skills

This repository contains skills organized by statistical domain, covering all major areas of Statistics Sweden's open data offerings.

### Available Skills

<!-- This table is auto-generated. Do not edit manually. -->
<!-- BEGIN_SKILLS_TABLE -->
| Name | Description | Documentation |
|------|-------------|---------------|
| `scb-business-economy` | Workflows for business and economic data including industry statistics, IT usage, and economic performance | [SKILL.md](skills/scb-business-economy/SKILL.md) |
| `scb-data-visualization` | Generate Python scripts for fetching SCB table data and creating visualizations using matplotlib and seaborn | [SKILL.md](skills/scb-data-visualization/SKILL.md) |
| `scb-education-research` | Workflows for education and research data covering schools, universities, and R&D statistics | [SKILL.md](skills/scb-education-research/SKILL.md) |
| `scb-environment` | Workflows for environmental data including climate indicators, energy consumption, and sustainability metrics | [SKILL.md](skills/scb-environment/SKILL.md) |
| `scb-housing-construction` | Workflows for housing and construction data covering real estate, building permits, and construction statistics | [SKILL.md](skills/scb-housing-construction/SKILL.md) |
| `scb-international-trade` | Workflows for international trade data including import/export statistics and trade balances | [SKILL.md](skills/scb-international-trade/SKILL.md) |
| `scb-labor-market` | Workflows for labor market data covering employment, wages, working hours, and labor costs | [SKILL.md](skills/scb-labor-market/SKILL.md) |
| `scb-living-conditions` | Workflows for living conditions data including income, education, health, and social statistics | [SKILL.md](skills/scb-living-conditions/SKILL.md) |
| `scb-opendata-mcp-workflows` | Core workflows and use cases for the SCB Open Data MCP server interface | [SKILL.md](skills/scb-opendata-mcp-workflows/SKILL.md) |
| `scb-population` | Workflows for population data including demographics, births, deaths, and population projections | [SKILL.md](skills/scb-population/SKILL.md) |
| `scb-energy-electricity` | Workflows and use cases for SCB Energy and Electricity tables covering energy consumption, production, and electricity statistics | [SKILL.md](skills/scb-energy-electricity/SKILL.md) |
| `scb-macro-economics` | Workflows and use cases for SCB Macroeconomics tables covering GDP, inflation (CPI), and economic indicators | [SKILL.md](skills/scb-macro-economics/SKILL.md) |
<!-- END_SKILLS_TABLE -->

### Using Skills in Your Coding Agent

Once a skill is installed, reference it directly when giving instructions to your coding agent:

- "Use the SCB business economy skill to retrieve current industry statistics for manufacturing sectors"
- "Use the SCB population skill to analyze demographic trends in Stockholm region"
- "Use the SCB labor market skill to compare wage data across public and private sectors"
- "Use the SCB international trade skill to examine export trends for Swedish manufacturing"

Your coding agent will automatically load the corresponding `SKILL.md` instructions and workflow patterns while completing the statistical data retrieval task.

### Contribute or Customize a Skill

1. Copy one of the existing skill folders and rename it
2. Update the new folder's `SKILL.md` frontmatter:
   ```markdown
   ---
   name: scb-new-skill-name
   description: Describe what statistical domain this skill covers and when to use it
   ---

   # Skill Title
   
   Extended description.
   
   ## Common Table IDs and Keywords
   
   Use scripts in https://github.com/ashwinvis/scb-opendata-mcp/tree/main/docs to fetch tables
   
   ## Use Cases & Examples
   
   In particular, show workflows with scb_opendata_mcp_* tools
   ```
3. Add or edit supporting documentation and examples
4. Test your skill with the SCB Open Data MCP Server
5. Submit a pull request to contribute back to the repository

### Skill Structure

Each skill follows a consistent structure:
- **Common Table IDs and Keywords**: Lists the most relevant SCB table IDs and search keywords
- **Use Cases & Examples**: Provides step-by-step workflows for common statistical analysis tasks
- **MCP Server Integration**: Shows how to chain multiple tool calls for complex queries

## SCB Open Data MCP Server

This skills repository is designed to work with the [SCB Open Data MCP Server](https://github.com/ashwinvis/scb-opendata-mcp), which provides the underlying tool calls and API interface to Statistics Sweden's data.

- [SCB Open Data MCP Server Repository](https://github.com/ashwinvis/scb-opendata-mcp)
- [Statistics Sweden (SCB) Official Website](https://www.scb.se/)
- [SCB Open Data API Documentation](https://www.scb.se/en/services/open-data-api/)
- [Agent Skills Specification](https://agentskills.io/specification)

## License

This repository and its skills are licensed under the MIT License. The statistical data accessed through these skills is subject to Statistics Sweden's terms of use.

## Disclaimer

This is an unofficial prototype. The workflows were generated using AI while using official documents and a sampling of tables fetched from SCB's open data as context.
A thorough rigorous verification test is recommended before using it in any serious application.
