# Life Expectancy Dataset

![](https://media.gettyimages.com/id/529363167/photo/multi-generation-family-relaxing-on-retaining-wall.jpg?s=2048x2048&w=gi&k=20&c=g18hPHzWyEKlCoIt9jNzeSvaDv1wJBIt-JvHe8-Wv48=)

## Description
This dataset, [`life_expectancy.csv`](life_expectancy.csv), contains information related to life expectancy and various health, economic, and social indicators for different countries and regions.

## Columns

| Column Name                   | Data Type | Description                                                |
|-------------------------------|-----------|------------------------------------------------------------|
| `Country`                     | String    | Name of the country.                                       |
| `Region`                      | String    | Geographical region to which the country belongs.          |
| `Year`                        | Integer   | Year of the record.                                        |
| `Infant_deaths`               | Float     | Number of infant deaths per 1000 population.               |
| `Under_five_deaths`           | Float     | Number of deaths under five years of age per 1000 population.|
| `Adult_mortality`             | Float     | Adult mortality rate per 1000 population.                  |
| `Alcohol_consumption`         | Float     | Alcohol consumption measured as liters of pure alcohol consumed per capita.|
| `Hepatitis_B`                 | Integer   | Hepatitis B (HepB) immunization coverage among 1-year-olds (%).|
| `Measles`                     | Integer   | Number of reported measles cases.                          |
| `BMI`                         | Float     | Average Body Mass Index of the population.                 |
| `Polio`                       | Integer   | Polio (Pol3) immunization coverage among 1-year-olds (%).  |
| `Diphtheria`                  | Integer   | Diphtheria tetanus toxoid and pertussis (DTP3) immunization coverage among 1-year-olds (%).|
| `Incidents_HIV`               | Float     | Number of new HIV infections per 1000 uninfected population.|
| `GDP_per_capita`              | Integer   | Gross Domestic Product per capita in current prices (USD). |
| `Population_mln`              | Float     | Total population in millions.                              |
| `Thinness_ten_nineteen_years` | Float     | Prevalence of thinness among children and adolescents aged 10-19 years (%).|
| `Thinness_five_nine_years`    | Float     | Prevalence of thinness among children aged 5-9 years (%).  |
| `Schooling`                   | Float     | Number of years of Schooling.                              |
| `Economy_status`              | String    | Economic status of the country, categorized as either `Developed` or `Developing`.|
| `Life_expectancy`             | Float     | Average life expectancy at birth, total (years).           |

## Usage
This dataset can be used for various analytical purposes such as studying the factors affecting life expectancy, understanding the relationships between different health indicators, and assessing the impact of economic status on life expectancy.

- [R questions](life_expectancy_r_questions.md), [R notebook](life_expectancy_r_notebook.ipynb)

## Citation
This dataset was obtained from Kaggle, and it is available [here](https://www.kaggle.com/datasets/lashagoch/life-expectancy-who-updated/).
