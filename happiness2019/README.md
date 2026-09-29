# World Happiness Report 2019: Teaching Dataset

This CSV contains 155 countries or regions and nine columns. It is a local teaching copy associated with the 2019 report. The data values and column names are preserved so existing code continues to work.

## Start here

[Browse the CSV](happiness2019.csv) or [download the fixed data version](https://raw.githubusercontent.com/ahmedmoustafa/datasets/4f2478a00774897b3a3cfce99466bc97a620eb5a/happiness2019/happiness2019.csv).

- [R notebook](happiness.ipynb): uses base R.
- [Python notebook](happiness_py.ipynb): requires pandas for the setup cells. Install a plotting library when you need one for your answers.

The notebooks load the same fixed version and check column names, dimensions, country uniqueness, and score bounds. Copy a notebook into your own Colab workspace and run its setup cells before answering the questions.

## What the numbers mean

The 2019 report ranks average life evaluations for 2016–2018 on the 0–10 Cantril ladder. The endpoints refer to the worst and best possible life, not momentary happiness. The six explanatory columns in this copy are modeled contributions in ladder points. They are not the underlying measurements. See [Chapter 2 of the 2019 report](https://www.worldhappiness.report/ed/2019/changing-world-happiness/) and the [report FAQ](https://www.worldhappiness.report/faq/).

| Column | Meaning in this file |
| --- | --- |
| `country` | Country or region label; 155 distinct values. |
| `category` | Local grouping label with an unverified source and date. |
| `score` | Average life-evaluation score on the 0–10 ladder. |
| `gdp_per_capita` | Contribution associated with GDP per capita, in ladder points; not currency. |
| `social_support` | Social-support contribution, in ladder points; not a survey proportion. |
| `healthy_life_expectancy` | Health-related contribution, in ladder points; not years of life. |
| `freedom_to_make_life_choices` | Freedom-related contribution, in ladder points; not a survey proportion. |
| `generosity` | Generosity-related contribution, in ladder points; not a donation amount. |
| `perceptions_of_corruption` | Corruption-related contribution, in ladder points; not a corruption rate. |

The six contributions alone do not sum to the score. The report's decomposition also includes a reference component and residual, which are not separate columns here. A zero contribution does not imply zero income, zero life expectancy, or the complete absence of the underlying factor.

## Local limitations

The file has no blank cells. Scores range from 2.853 to 7.769. This does not establish that the source measurements are complete or error-free.

The recorded categories are Developed (37 rows), Developing (65), Transitioning (14), and Underdeveloped (39). Their source, assignment rules, and reference year are not documented. They are retained as existing teaching labels, not certified UN classifications. Avoid treating them as a natural ranking or using them for substantive conclusions without a documented classification source.

The exact source download, selection process, and category-join script for this 155-row copy are unavailable. Do not describe it as a verified complete reproduction of the official ranking. There are no survey weights, individual responses, or uncertainty estimates in this file. Country-level associations cannot establish individual-level relationships or causal effects.

## Questions

Use descriptive statistics and suitable plots. Include units, group sizes, and limitations. The notebooks repeat these questions and provide blank answer cells.

1. Compare score distributions across the four recorded categories. Report the number of countries or regions in each group and explain the limits of these undocumented category labels.
2. Plot the GDP contribution against the score and calculate their correlation. Explain why this is not a relationship between income in dollars and happiness.
3. Compare the healthy-life-expectancy contribution across categories using plots and descriptive summaries. Keep the units in ladder points, not years.
4. What association appears between the social-support and freedom contributions? Include a scatterplot and correlation.
5. How does the corruption-related contribution vary across categories? Explain why it is not a measured corruption percentage.
6. Calculate the unweighted mean score in each category. Explain why this is a mean across countries or regions, not a population-weighted mean across people.
7. For an arithmetic exercise, define scenario_score = score + freedom_to_make_life_choices. This doubles only the recorded freedom contribution while holding all other terms fixed. Rank the five largest increases, state how you handle ties, and explain why the result is not a causal prediction or an observed score.
8. Compare the GDP and social-support contributions directly. If you also calculate their ratio, report zero denominators as undefined and explain why the ratio is not an economic measure.
9. Among countries or regions below the median score, describe the association between generosity and GDP contributions. Explain why this subset comparison does not establish a trend over time or a causal effect.

## Source and reuse

Reference: Helliwell, J. F., Huang, H., and Wang, S. (2019), “Changing World Happiness,” Chapter 2 of the *World Happiness Report 2019*. Cite the original report and identify this repository's data version when describing your analysis.

The applicable redistribution terms for this particular data copy have not been verified. The repository's CC0 notice does not establish rights to third-party source data. Confirm the source terms before further redistribution or publication. The grouping labels and local extraction history also need a traceable source.

## Learning resources

- [pandas user guide](https://pandas.pydata.org/docs/user_guide/)
- [Matplotlib cheat sheets](https://matplotlib.org/cheatsheets/)
- [Seaborn tutorial](https://seaborn.pydata.org/tutorial.html)
- [Financial Times Visual Vocabulary](https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary)

These public publisher links replace the previous private-course links. The decorative third-party image has been removed from the page because its reuse permission was not documented.
