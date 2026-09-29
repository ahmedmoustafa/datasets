# Questions for Analyzing the Obesity Dataset
Read the [dataset notes](README.md) first. About 77% of the records are synthetic. Describe the released table; do not present its summaries as population estimates.

## Univariate Analysis
- How is gender distributed in the dataset? Use a bar plot to visualize the distribution.
- What are the mean, median, and standard deviation of the age across the records? Use descriptive statistics functions.
- Create a histogram to analyze the distribution of weight in the dataset. Add appropriate bin sizes and titles.
- What is the proportion of each obesity level in the dataset?

## Bivariate Analysis
- Is there a correlation between weight and height?
- How does weight distribution differ between genders?
- Compare the original activity code (FAF) with an optional rounded grouping. Preserve the original values and discuss whether rounding changes your interpretation.

## Multivariate Analysis
- Create a heatmap to visualize the correlations between all numerical variables in the dataset.
- Standardize the numerical variables before PCA and explain how you handle interpolated questionnaire codes. How much variance is explained by the first two principal components?

## Loops and Conditions
- Divide the dataset into age groups (e.g., <20, 20-40, >40). For each group, calculate the average main-meal code (NCP), noting that it is not an exact meal count. Use loops and conditions for this analysis.
- Count records with weight below Q1 - 1.5 × IQR or above Q3 + 1.5 × IQR. These flags do not establish data errors; do not remove records automatically.

## Modeling
- Build a linear regression model to predict weight based on height, age, and gender. Report training and held-out $R^2$ separately. Keep exact duplicate records in the same split and explain why unknown synthetic lineage still limits the evaluation.
