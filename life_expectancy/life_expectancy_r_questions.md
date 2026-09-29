# Questions on the Life Expectancy Dataset

Read the [dataset notes](README.md) before starting. The table contains upstream imputation and repeated country observations. Use descriptive language and report selection, units, and limitations.

1. Explore the table with head(), summary(), and str(). Confirm that Country and Year identify one row and explain why no blank cells does not mean all values were observed.

2. For 2015, calculate the mean and median Life_expectancy across countries. State that these are unweighted country summaries, not a population-weighted average.

3. For Region = "Asia" in 2015, calculate the unweighted mean GDP_per_capita and report the number of countries. Use the recorded Region labels; they do not include every country commonly described as Asian.

4. Plot a histogram of Life_expectancy for 2015 using hist(). Label the units and describe the distribution.

5. Find the minimum Life_expectancy and maximum GDP_per_capita in the full table. Report every tied country-year, not just the first row.

6. For 2015, create a flag indicating whether a country's mean BMI is above the median country mean in that year. Explain why this relative flag does not classify individuals or estimate obesity prevalence.

7. Plot Life_expectancy by year for Egypt after sorting by Year. Describe the pattern and explain how upstream imputation could affect it.

8. For 2015, calculate the correlation between Adult_mortality and Life_expectancy. Explain their shared mortality basis and why the association does not identify a causal effect.

9. For 2015, explore Life_expectancy, Schooling, and Alcohol_consumption with scatterplots. State the units and explain the limits of country-level comparisons.

10. For 2015, sort countries by Adult_mortality. Also list the five highest mean BMI values and five lowest Schooling values. State how you handle ties.

11. Rank GDP_per_capita from highest to lowest in 2015 and report Japan's rank. Use the same rank for ties and state the ranking method.

12. Find every country tied for the highest mean BMI in 2000. This ranks country means, not obesity prevalence.

13. For 2005, calculate mean Alcohol_consumption among rows labeled Developed and report the country count. Explain that the grouping is not verified as a historical classification.

14. Rank Schooling from highest to lowest in 2010 and report India's rank. State the ranking method and how ties are handled.

15. For Region = "Africa", calculate the unweighted mean and median Life_expectancy for each year, then plot both. Report country counts per year and distinguish these summaries from the life expectancy of a pooled regional population.
