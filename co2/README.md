# Global CO<sub>2</sub> Emissions from Fossil Fuels

Annual global carbon dioxide emissions from fossil fuels and cement production, from 1750 through 2024.

The data comes from the [Global Carbon Project](https://globalcarbonproject.org/)'s annual Global Carbon Budget release, redistributed here from the [datahub.io](https://datahub.io/core/co2-fossil-global) packaging of it.

The columns included in [`co2.csv`](co2.csv) are described in the table below. All emission figures are in **million metric tonnes of carbon** (MtC), not tonnes of CO<sub>2</sub>. Early years carry blanks where a fuel category was not yet recorded.

| Column | Description |
| -- | -- |
| `Year` | Calendar year, 1750 to 2024 |
| `Total` | Total emissions from all sources |
| `Gas Fuel` | Emissions from gas fuel consumption |
| `Liquid Fuel` | Emissions from liquid fuel consumption |
| `Solid Fuel` | Emissions from solid fuel consumption |
| `Cement` | Emissions from cement production |
| `Gas Flaring` | Emissions from gas flaring |
| `Per Capita` | Emissions per person, in metric tonnes of carbon |

Here are a few questions:

1. How have total emissions changed since 1750, and when does the curve begin to bend upward?
2. Which fuel category contributes most to the total, and has that changed over time?
3. Per capita emissions and total emissions tell different stories. Where do they diverge, and why?
4. Cement and gas flaring are small contributors. How do their trends compare with the fuel categories?

## Source and license

- **Source:** Andrew, R. M., & Peters, G. P. (2025). *The Global Carbon Project's fossil CO2 emissions dataset* (2025v15). Zenodo. <https://doi.org/10.5281/zenodo.17417124>
- **Upstream packaging:** <https://github.com/datasets/co2-fossil-global>
- **License:** Open Data Commons Public Domain Dedication and License ([ODC-PDDL-1.0](http://opendatacommons.org/licenses/pddl/))

The upstream dataset is refreshed each December after the Global Carbon Project release. This copy is a point-in-time mirror taken in September 2026, kept here so that teaching material does not depend on a third-party URL that may move.
