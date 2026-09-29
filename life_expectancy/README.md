# Life Expectancy Dataset


## Description
This teaching table contains 2,864 country-year records: 179 countries with one record per year from 2000 through 2015. There are 20 columns. It is a processed compilation from Kaggle, not an unmodified WHO release. The data values are preserved in this correction.

**`Measles` is first-dose measles vaccination coverage (%), not a case count.** No blank cells remain, but the publisher filled missing values. A complete table does not mean every value was observed.

## Start here

- [Data](life_expectancy.csv)
- [R starter notebook](life_expectancy_r_notebook.ipynb), using base R.
- [Questions](life_expectancy_r_questions.md)

The notebook uses a fixed public data version and verifies column names, country-year keys, coverage, and vaccination percentage bounds. Run its setup before completing the blank answer cells.

## Columns

| Column Name                   | Data Type | Description                                                |
|-------------------------------|-----------|------------------------------------------------------------|
| `Country`                     | String    | Name of the country.                                       |
| `Region`                      | String    | Geographical region to which the country belongs.          |
| `Year`                        | Integer   | Year of the record.                                        |
| `Infant_deaths`               | Float     | Infant mortality: probability of death before age 1, per 1,000 live births.               |
| `Under_five_deaths`           | Float     | Under-five mortality: probability of death before age 5, per 1,000 live births.|
| `Adult_mortality`             | Float     | Probability of dying between ages 15 and 60, per 1,000 people who reach age 15.                  |
| `Alcohol_consumption`         | Float     | Recorded alcohol consumption, liters of pure alcohol per person age 15 or older.|
| `Hepatitis_B`                 | Integer   | Third-dose hepatitis B (HepB3) coverage among 1-year-olds (%).|
| `Measles`                     | Integer   | First-dose measles-containing vaccine (MCV1) coverage among 1-year-olds (%).                          |
| `BMI`                         | Float     | Reported population mean BMI (kg/m²); age/standardization details need source verification.                 |
| `Polio`                       | Integer   | Polio (Pol3) immunization coverage among 1-year-olds (%).  |
| `Diphtheria`                  | Integer   | Diphtheria tetanus toxoid and pertussis (DTP3) immunization coverage among 1-year-olds (%).|
| `Incidents_HIV`               | Float     | New HIV infections per 1,000 uninfected people ages 15–49.|
| `GDP_per_capita`              | Integer   | Gross Domestic Product per capita in current prices (USD). |
| `Population_mln`              | Float     | Total population in millions.                              |
| `Thinness_ten_nineteen_years` | Float     | Prevalence of thinness among children and adolescents aged 10-19 years (%).|
| `Thinness_five_nine_years`    | Float     | Prevalence of thinness among children aged 5-9 years (%).  |
| `Schooling`                   | Float     | Mean years of formal education among people age 25 or older, according to the publisher.                              |
| `Economy_status`              | String    | Publisher grouping (`Developed` or `Developing`); not a verified annual classification.|
| `Life_expectancy`             | Float     | Average life expectancy at birth, total (years).           |

## Measurement sources and limits

The dictionary follows the [publisher's documentation](https://www.kaggle.com/datasets/lashagoch/life-expectancy-who-updated/) and standard indicator definitions: [WHO infant mortality](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/infant-mortality-rate-%28probability-of-dying-between-birth-and-age-1-per-1000-live-births%29), [WHO under-five mortality](https://data.who.int/indicators/i/E3CAF2B/2322814), [World Bank adult mortality](https://datahelpdesk.worldbank.org/knowledgebase/articles/114956-what-is-the-definition-of-adult-mortality), and [World Bank HIV incidence](https://data.worldbank.org/indicator/SH.HIV.INCD.ZS). These references clarify the intended indicators; they do not establish a row-by-row match to current provider releases.

The exact BMI age group and standardization, the original series for childhood thinness, and the annual classification rules need better source records. Do not apply individual BMI thresholds to national means to estimate obesity prevalence or diagnose a population. Historical labels in `Region` and `Economy_status` are the publisher's grouping, not a verified classification for every year.

## Upstream preprocessing

The publisher reports replacing missing values with nearby three-year averages, or regional averages when a country lacks values across all years. Countries missing more than four columns were excluded. Therefore, absence of blank cells reflects preprocessing and selection as well as data availability.

The local repository does not include the original missing-value mask, a record of affected cells, or a reproducible preprocessing script. We cannot reliably label individual cells as observed or imputed, recreate the estimates, or quantify their uncertainty from this CSV alone. Do not manufacture imputation flags. Retain these limits in any analysis report.

Repeated years from a country are related observations. Specify a year or averaging period, handle that dependence in inferential work, and distinguish country averages from population-weighted summaries. For forecasting, nearby-year imputation may use information from later years; this table does not establish a leakage-free evaluation. Associations between national indicators do not establish causal or individual-level relationships.

## Source, citation, and reuse

Source: Lasha (`lashagoch`), *Life Expectancy (WHO) Fixed*, Kaggle, version 1, March 30, 2023. [Dataset and methods](https://www.kaggle.com/datasets/lashagoch/life-expectancy-who-updated/).

The publisher attributes indicators to WHO, World Bank, and Our World in Data and labels the compilation CC0. That is the publisher's license statement; it does not independently resolve the terms of every underlying series. Preserve the source/version citation and verify provider terms for your intended redistribution or publication. The local table has 20 columns, while the publisher describes 21; the exact local transformation is not recorded.

This correction changes documentation and the starter notebook, not the data. The former third-party image was removed because its reuse permission was not documented.
