# World Happiness: Annual Data, 2005–2023

This teaching collection contains annual country-level well-being measures. Unlike the 2019 teaching table elsewhere in this repository, these columns are annual measures, not ladder-point decomposition contributions.

## Files and setup

- [happiness_original.tsv](happiness_original.tsv): 2,363 rows and 11 columns, with missing values preserved in the local source copy.
- [happiness.tsv](happiness.tsv): 2,362 rows and 11 columns, after undocumented local imputation and one exclusion.
- [countries.tsv](countries.tsv): 191 rows and five columns of supplementary labels, with no documented source or reference date.
- [Python notebook](happiness.ipynb): loads all three tables, flags local imputations, reports the excluded record, and joins metadata without losing rows. Setup requires pandas; add a plotting library when answering the exercises.

The notebook uses fixed Git LFS payload URLs beginning with `https://media.githubusercontent.com/media/ahmedmoustafa/datasets/4f2478a00774897b3a3cfce99466bc97a620eb5a/happiness/`. Ordinary raw GitHub URLs may return LFS pointers. After cloning, run `git lfs pull --include="happiness/*.tsv"` from the repository root.

## Variables

| Column | Meaning and interpretation |
| --- | --- |
| `country` | Country or region label; pair with year to identify a record. |
| `year` | Observation year, 2005–2023. Coverage differs across countries. |
| `life_ladder` | Mean Cantril life evaluation on a 0–10 scale. |
| `log_gdp_per_capita` | Natural log of GDP per capita. This is not a dollar amount; the exact PPP/base-year vintage needs the source release documentation. |
| `social_support` | Average response about having someone to rely on. |
| `healthy_life_expectancy_at_birth` | Healthy life expectancy in years, which can include upstream estimates. |
| `freedom_to_make_life_choices` | Average reported satisfaction with freedom of choice. |
| `generosity` | Donation-related residual adjusted for GDP, not donation amounts or a raw proportion. |
| `perceptions_of_corruption` | Summary of perceived corruption in government/business. |
| `positive_affect` | Summary of positive experiences; consult the release-specific questionnaire for the exact components. |
| `negative_affect` | Summary of negative experiences; consult the release-specific questionnaire for the exact components. |

The lookup adds `continent`, `region`, `economic_status`, and `political_system`. These undated labels do not establish a country's classification in each observation year. Do not use them as verified historical measures.

## What changed during local preprocessing

The previous README described random-forest imputation, but no script, model settings, predictors, seed, or environment was retained. The estimates cannot currently be regenerated. The notebook instead provides a reproducible comparison of the two stored tables.

| Variable | Previously missing cells filled in retained rows |
| --- | ---: |
| log_gdp_per_capita | 28 |
| social_support | 13 |
| healthy_life_expectancy_at_birth | 63 |
| freedom_to_make_life_choices | 36 |
| generosity | 80 |
| perceptions_of_corruption | 124 |
| positive_affect | 24 |
| negative_affect | 16 |
| **Total** | **384** |

No originally observed value in the retained rows changed. Egypt–2005 is absent from the processed table; the reason was not recorded. It remains in the original file. The correction made here preserves all three data files and does not invent a reason for the exclusion or a replacement imputation method.

`imputed_mask` marks each locally filled value by country, year, and variable. `excluded_records` retains the omitted row. These flags do not identify estimates or imputations already present in the upstream source. Use the original table for an observed-value sensitivity analysis. For prediction, fit any new imputation method on training data only; this existing complete table is not evidence of leakage-free preprocessing.

## Country-name matching

A direct name join misses 11 labels and 152 processed rows. The notebook applies six explicit aliases:

| Data label | Lookup label |
| --- | --- |
| Congo (Brazzaville) | Congo, Republic of the |
| Congo (Kinshasa) | Congo, Democratic Republic of the |
| Czechia | Czech Republic |
| South Korea | Korea, South |
| Taiwan Province of China | Taiwan |
| Türkiye | Turkey |

Hong Kong S.A.R. of China, Ivory Coast, North Macedonia, Somaliland region, and State of Palestine have no corresponding entry in this lookup. They account for 61 rows that remain unmatched; none is assigned another country's metadata. The left join preserves all 2,362 processed records and reports the remaining unmatched counts. It validates that lookup keys are unique. Name matching is not an assertion about sovereignty or a validation of the lookup classifications.

## Analysis limits

Specify a year, a common time interval, and an averaging rule before comparing countries. Repeated years from the same country are not independent observations. An unweighted mean across country-years gives more influence to countries with more observed years. Report missingness, imputation, and unmatched metadata; do not silently drop them. Correlations do not establish causal effects, and national averages do not describe individual relationships.

## Exercises

1. For a selected year, summarize life_ladder across countries. State whether the summary weights each country equally; it is not a population-weighted average.
2. For a selected year, compare life_ladder across available lookup regions. Report unmatched countries separately and state the lookup limitations.
3. What is the range of `log_gdp_per_capita` values, and which countries have the highest and lowest GDP per capita?
4. How has the `life_ladder` score changed over time in a specific country?
5. Choose common start and end years. Which countries have the largest change in life_ladder? Include only countries observed in both years and report exclusions.
6. Are there noticeable trends in `healthy_life_expectancy_at_birth` over time across regions or continents?
7. What is the relationship between `log_gdp_per_capita` and `life_ladder`? Do countries with higher GDP per capita tend to have higher happiness scores?
8. How does `social_support` correlate with `life_ladder`? Do countries with higher social support report higher happiness?
9. Is there a relationship between `freedom_to_make_life_choices` and `life_ladder`?
10. How do `positive_affect` and `negative_affect` differ across countries? Are there countries with high positive affect and low negative affect, or vice versa?
11. Is there a correlation between `life_ladder` and `positive_affect`? What about `life_ladder` and `negative_affect`?
12. What association appears between perceptions_of_corruption and life_ladder? Explain why this comparison does not establish a causal effect.
13. How does the `generosity` measure correlate with `log_gdp_per_capita`? Are wealthier countries generally more or less generous?
14. How do different regions or continents compare in terms of `life_ladder`, `social_support`, and `freedom_to_make_life_choices`?
15. Explore healthy life expectancy by the recorded economic labels. Explain why the undated lookup cannot establish historical economic status.
16. Create a time-series chart showing `life_ladder` over time for a selected group of countries.
17. Use scatter plots to explore relationships between `log_gdp_per_capita` and `life_ladder`, color-coded by continent or region.
18. Compare an analysis using original observed values with one using the processed table. Report which variables and country-years were imputed, the excluded record, and whether your conclusion changes.

## Source, citation, and reuse

The earlier documentation attributes these measures to the Gallup World Poll, World Development Indicators, WHO, and Penn World Table, and references the [World Happiness Report 2024](https://www.worldhappiness.report/ed/2024/). The exact source file/version and local extraction process have not been established. The original-named file is a preserved local input, not a verified unmodified upstream release.

Report citation: Helliwell, J. F., Layard, R., Sachs, J. D., De Neve, J.-E., Aknin, L. B., and Wang, S. (Eds.). (2024). *World Happiness Report 2024*. University of Oxford: Wellbeing Research Centre.

The source license, redistribution terms, and lookup provenance still need verification. The repository's CC0 notice does not establish rights over third-party data. Consult the providers before further redistribution or publication, and cite the source release and repository version used. The previous external decorative image was removed because its reuse permission was not documented.
