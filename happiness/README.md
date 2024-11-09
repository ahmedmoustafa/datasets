# World Happiness Report

![Smile](https://www.futurity.org/wp/wp-content/uploads/2024/02/happiness-wealth-survey-1600.jpg)

This dataset provides country-level data on subjective well-being (happiness) and associated economic, health, and social metrics. The data spans multiple years, capturing trends in well-being, economic conditions, health expectancy, and social perceptions globally.

## Files in Dataset

- [**`happiness.tsv`**](happiness.tsv): Contains yearly data on happiness and associated metrics for each country.
- [**`countries.tsv`**](countries.tsv): A supplementary lookup table with metadata for each country, including geographical and political information.

## Data Sources and Variables

### Columns in [`happiness.tsv`](happiness.tsv)

| Column                        | Description                                                                                                  |
|-------------------------------|--------------------------------------------------------------------------------------------------------------|
| `country`                     | The name of the country                                                                                      |
| `year`                        | The year of data collection                                                                                  |
| `life_ladder`                 | Subjective well-being, measured by [Gallup's Cantril life ladder](https://news.gallup.com/poll/122453/understanding-gallup-uses-cantril-scale.aspx) survey                                       |
| `log_gdp_per_capita`          | Gross domestic product (GDP) per capita (logged) in dollars                      |
| `social_support`              | Average response indicating if individuals have someone to rely on in times of trouble                       |
| `healthy_life_expectancy_at_birth` | Expected years of healthy life at birth, interpolated/extrapolated as needed                        |
| `freedom_to_make_life_choices`| Average satisfaction level regarding freedom of choice                                                       |
| `generosity`                  | Residual measure of generosity based on responses about recent charitable donations, adjusted for GDP        |
| `perceptions_of_corruption`   | Average perception of corruption in government and business sectors                                         |
| `positive_affect`             | Average score of positive experiences (laughter, enjoyment, interesting activities)                          |
| `negative_affect`             | Average score of negative emotions (worry, sadness, anger)                                                  |

### Columns in [`countries.tsv`](countries.tsv) (Lookup Table)

| Column            | Description                                        |
|-------------------|----------------------------------------------------|
| `country`         | The name of the country                            |
| `continent`       | The continent where the country is located         |
| `region`          | Specific region within the continent               |
| `economic_status` | The economic classification of the country         |
| `political_system`| Type of political system governing the country     |

The `countries.tsv` file serves as a lookup table to provide supplementary metadata for each country, allowing for deeper analysis based on geographical and political characteristics.

## Usage Notes

1. **Time Coverage**: Happiness scores and other metrics are available across multiple years, enabling trend analysis.
2. **GDP Forecasting**: Values for `log_gdp_per_capita` in 2023 are forecasted where actual data was unavailable.
3. **Binary and Averaged Measures**: Measures such as `social_support` and `perceptions_of_corruption` are based on binary responses, while `positive_affect` and `negative_affect` are averages of related emotions.

## Suggested Questions for Data Exploration

   - What are the average, minimum, and maximum values of `life_ladder` (happiness scores) across all countries?
   - How does `life_ladder` vary across different continents or regions?
   - What is the range of `log_gdp_per_capita` values, and which countries have the highest and lowest GDP per capita?
   - How has the `life_ladder` score changed over time in a specific country?
   - Which countries have seen the largest increase or decrease in happiness scores over the years?
   - Are there noticeable trends in `healthy_life_expectancy_at_birth` over time across regions or continents?
   - What is the relationship between `log_gdp_per_capita` and `life_ladder`? Do countries with higher GDP per capita tend to have higher happiness scores?
   - How does `social_support` correlate with `life_ladder`? Do countries with higher social support report higher happiness?
   - Is there a relationship between `freedom_to_make_life_choices` and `life_ladder`?
   - How do `positive_affect` and `negative_affect` differ across countries? Are there countries with high positive affect and low negative affect, or vice versa?
   - Is there a correlation between `life_ladder` and `positive_affect`? What about `life_ladder` and `negative_affect`?
   - Does `perceptions_of_corruption` influence `life_ladder`? Do countries with lower perceived corruption have higher happiness scores?
   - How does the `generosity` measure correlate with `log_gdp_per_capita`? Are wealthier countries generally more or less generous?
   - How do different regions or continents compare in terms of `life_ladder`, `social_support`, and `freedom_to_make_life_choices`?
   - Are there differences in `healthy_life_expectancy_at_birth` between countries in different economic classifications?
   - Create a time-series chart showing `life_ladder` over time for a selected group of countries.
   - Use scatter plots to explore relationships between `log_gdp_per_capita` and `life_ladder`, color-coded by continent or region.

---

- To start loading the data in `Python`, copy [this notebook](happiness.ipynb) into your Colaboratory on Google Drive.

---

## Source and License

- This data is sourced from the Gallup World Poll, World Development Indicators, WHO, and Penn World Table.
- Some missing values in [the original dataset](happiness_original.tsv) were imputed using a Random Forest imputation approach.
- Additional insights on global happiness trends can be found in the **World Happiness Report**:

  > Helliwell, J. F., Layard, R., & Sachs, J. (Eds.). (2024). *World Happiness Report 2024*. Sustainable Development Solutions Network. Retrieved from [https://worldhappiness.report/](https://worldhappiness.report/).

- Please adhere to the licensing terms specified by the data providers.
