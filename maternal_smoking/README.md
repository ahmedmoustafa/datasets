# Maternal Smoking and Birth Weight

This historical teaching table has 610 rows and 20 columns. The repository identifies it as a subset of the Child Health and Development Studies (CHDS). Its selection and recoding script is not available, so do not treat it as the complete study or a representative population sample.

## Download and start

[Browse the table](maternal_smoking.tsv) or [download this fixed data version](https://media.githubusercontent.com/media/ahmedmoustafa/datasets/4f2478a00774897b3a3cfce99466bc97a620eb5a/maternal_smoking/maternal_smoking.tsv). The TSV is stored with Git LFS; a regular raw GitHub link can return a pointer instead of data. After cloning, run `git lfs pull --include="maternal_smoking/maternal_smoking.tsv"` from the repository root.

- [Python notebook](maternal_smoking_py.ipynb): requires pandas.
- [R notebook](maternal_smoking_r.ipynb): requires tidyverse.

Both notebooks check the 610 × 20 shape and all column names. Run the setup cells first, then complete the blank answer cells. The data values are unchanged by this documentation update. The TSV under `smoking/` is an identical legacy copy; use this directory for the lesson.

## Data dictionary

Definitions are based on the [original Berkeley Stat Labs codebook](https://www.stat.berkeley.edu/users/statlabs/data/babies.readme) and the values in this local table. Unresolved items are labeled below.

| Column | Meaning |
| --- | --- |
| `id` | Record identifier. All 610 values are distinct. |
| `date` | Encoded birth date. The source defines 1096 as January 1, 1961; this is not a Unix timestamp. |
| `gestation` | Pregnancy duration in days. |
| `weight` | Birth weight in ounces; source code 999 means unknown. |
| `parity` | Number of previous pregnancies, including fetal deaths and stillbirths; 0 means none. Source code 99 means unknown. |
| `mom.race` | Historical maternal race/ethnicity labels: asian, black, mexican, mixed, white. |
| `mom.age` | Maternal age in years at the end of pregnancy. |
| `mom.edu` | Education code; see below. |
| `mom.height` | Maternal height in inches. |
| `mom.weight` | Maternal prepregnancy weight in pounds. |
| `dad.race` | Historical paternal race/ethnicity labels; same labels as `mom.race`. |
| `dad.age` | Paternal age in years. |
| `dad.edu` | Paternal education; same source coding as maternal education. |
| `dad.height` | Paternal height in inches. |
| `dad.weight` | Paternal weight in pounds. |
| `marital` | 1 married, 2 legally separated, 3 divorced, 4 widowed, 5 never married. Local code 0 is undocumented. |
| `income` | Historical annual family income category. Keep codes 0–9 categorical; see the source inconsistency below. |
| `smoke` | `never`: never smoked; `now`: smokes now; `until_pregnancy`: smoked until the current pregnancy; `once_not_now`: former smoker. |
| `quit.time` | Coded smoking/cessation history; see below. |
| `cigs` | Cigarette-use range for past/current smokers; see below. |

Education: 0 = below eighth grade; 1 = eighth–twelfth grade without graduation; 2 = high school graduate; 3 = high school plus trade school; 4 = high school plus some college; 5 = college graduate; 6/7 = trade school with high school completion unclear; 9 = unknown. Maternal codes present are 0–5; paternal codes are 0–7.

Cessation (`quit.time`): 0 = never smoked; 1 = still smokes; 2 = during the current pregnancy; 3 = within one year; 4 = one to two years ago; 5 = two to three; 6 = three to four; 7 = five to nine; 8 = ten or more; 9 = quit, timing unknown. Source codes 98/99 mean unknown/not asked. The source does not provide a clear four-to-five-year category; do not invent one.

Cigarette use (`cigs`): 0 = never; 1 = 1–4; 2 = 5–9; 3 = 10–14; 4 = 15–19; 5 = 20–29; 6 = 30–39; 7 = 40–60; 8 = 60 or more; 9 = smoked, quantity unknown. Source codes 98/99 mean unknown/not asked. These codes are not cigarette counts. The source ranges overlap at 60; code 8 is absent from this table. Six records have code 9 and need separate treatment.

The income codebook claims $2,500 increments but also assigns code 8 to $12,500–14,999 and code 9 to $15,000 or more. These statements do not define a consistent scale. Do not convert the codes to dollar amounts or calculate their arithmetic mean until the mapping is resolved.

## Missing values and interpretation

There are no blank cells in this snapshot, but that does not mean every value is known. Two records have the undocumented `marital = 0`; six have unknown cigarette quantity. Keep these distinct from known categories. The source also uses 99 for unknown parental age/height, 999 for unknown parental weight, and 9 for unknown education; those parental codes are absent here.

Check unusual measurements before analysis, including gestation values from 148 to 338 days. Preserve the original table and document any exclusions in your analysis. The historical race labels mix social categories and do not establish biological explanations. Smoking status is recorded at a point in the study; `now` does not establish uninterrupted smoking throughout pregnancy. These observational data support association exercises, not causal conclusions from group differences alone.

## Questions

Answer visually and numerically where appropriate. Include group sizes, units, handling of unknown values, and limitations.

- **Q1.** How many distinct values appear in `mom.race` and `smoke`? Show counts for each category.
- **Q2.** What are the average ages of mothers and fathers? Report the number of observations used.
- **Q3.** What percentage of mothers belong to each of the four smoking categories? Include former smokers (`once_not_now`).
- **Q4.** Among mothers recorded as smoking now (`now`), what percentage falls in each cigarette-use category? Report unknown use separately. Explain why the exact mean number of cigarettes cannot be calculated from these ranges.
- **Q5.** Show the distribution of birth weight in ounces. Describe unusual values without removing them automatically.
- **Q6.** How does birth weight differ across the recorded smoking categories? Report group sizes and describe associations, not causal effects.
- **Q7.** How does birth weight vary across the historical maternal race categories? Discuss possible confounding and why these categories do not establish biological causes.
- **Q8.** What is the correlation between maternal prepregnancy weight and birth weight? Include a scatterplot.
- **Q9.** What is the correlation between paternal weight and birth weight? Include a scatterplot.
- **Q10.** Compare the correlations in Q8 and Q9 using the same complete records. Which has the greater absolute value? Does that difference alone establish statistical significance?
- **Q11.** What is the correlation between maternal and paternal weight?
- **Q12.** How does average maternal prepregnancy weight vary across the recorded race categories? Report group sizes and limitations.
- **Q13.** How do smoking-category proportions vary by maternal education? Treat education codes as categories.
- **Q14.** How do smoking-category proportions vary by recorded family income code? Treat the codes as categories; their dollar mapping is unresolved.
- **Q15.** What association appears between the recorded maternal and paternal race categories? Use a contingency table and discuss the limits of interpretation.

## Source and reuse status

The source documentation is in Deborah Nolan and Terry Speed's *Stat Labs: Mathematical Statistics Through Applications* and the [Berkeley data page](https://www.stat.berkeley.edu/users/statlabs/labs.html). These references explain the historical study and coding; they do not establish the exact selection process for this 610-row copy.

The source data's redistribution license and the local transformation history have not been verified. The repository's CC0 notice does not establish rights over third-party source data. Confirm the source terms before further redistribution or research publication; do not describe this dataset as verified public-domain data. This update preserves the existing records and makes the unresolved provenance explicit.

## Learning resources

Use the publishers' current resources:

- [pandas user guide](https://pandas.pydata.org/docs/user_guide/)
- [Matplotlib cheat sheets](https://matplotlib.org/cheatsheets/)
- [Seaborn tutorial](https://seaborn.pydata.org/tutorial.html)
- [Posit cheat sheets for R](https://posit.co/resources/cheatsheets/)
- [Financial Times Visual Vocabulary](https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary)

The previously bundled reference PDFs and decorative images have been removed. Their publishers retain their own rights and license terms; these links do not place the materials under the repository's license.
