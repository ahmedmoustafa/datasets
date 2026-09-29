# The Obesity Dataset



## Overview

This table has 2,111 records and 17 columns. **UCI reports that 77% of the records were generated with SMOTE and 23% came from web respondents.** The source respondents were from Mexico, Peru, and Colombia. These rows are not 2,111 independent observed participants, and the class proportions are not population prevalence estimates.

The local CSV matches the table in the UCI archive. It contains no blank cells and 24 repeated rows beyond their first occurrence. This update preserves the data, including those duplicates. The file does not identify which records are synthetic or which source records generated them.

## Start here

- [Data](obesity.csv)
- [Worked R notebook](obesity_r_notebook.ipynb), using ggplot2, reshape2, and corrplot.
- [Additional questions](questions.md)

The notebook downloads a fixed data version and checks its shape, columns, missingness, and duplicate count. It preserves the original activity values when adding rounded groups. Run all cells in order; package installation requires internet access if dependencies are missing.

## Description
The dataset consists of various features that include both lifestyle attributes and physical measurements. The dataset is structured as follows:

| Column Number | Column Name                      | Description                                      | Type            | Possible Values/Range |
|---------------|----------------------------------|--------------------------------------------------|-----------------|-----------------------|
| 1             | Gender                           | Gender of the individual                         | Categorical     | [Female, Male]        |
| 2             | Age                              | Age of the individual in years                   | Numerical       | 14.0 - 61.0           |
| 3             | Height                           | Height of the individual in meters               | Numerical       | 1.45 - 1.98           |
| 4             | Weight                           | Weight of the individual in kilograms            | Numerical       | 39.0 - 173.0          |
| 5             | family_history_with_overweight   | Whether the individual has a family history of overweight | Categorical | [yes, no]         |
| 6             | FAVC                             | Frequent consumption of high caloric food        | Categorical     | [no, yes]             |
| 7             | FCVC                             | Vegetable-frequency questionnaire code           | Numerical       | 1.0 - 3.0             |
| 8             | NCP                              | Main-meal questionnaire code                             | Numerical       | 1.0 - 4.0             |
| 9             | CAEC                             | Consumption of food between meals                | Categorical     | [Sometimes, Frequently, Always, no] |
| 10            | SMOKE                            | Smoking status                                   | Categorical     | [no, yes]             |
| 11            | CH2O                             | Water-intake questionnaire code, not exact liters              | Numerical       | 1.0 - 3.0             |
| 12            | SCC                              | Calories consumption monitoring                  | Categorical     | [no, yes]             |
| 13            | FAF                              | Activity-frequency questionnaire code                      | Numerical       | 0.0 - 3.0             |
| 14            | TUE                              | Technology-use questionnaire code, not exact hours            | Numerical       | 0.0 - 2.0             |
| 15            | CALC                             | Alcohol consumption                              | Categorical     | [no, Sometimes, Frequently, Always] |
| 16            | MTRANS                           | Most frequent transportation mode                | Categorical     | [Public_Transportation, Walking, Automobile, Motorbike, Bike] |
| 17            | NObeyesdad                       | Obesity level                                    | Categorical     | [Normal_Weight, Overweight_Level_I, Overweight_Level_II, Obesity_Type_I, Obesity_Type_II, Obesity_Type_III, Insufficient_Weight] |

## Measurement and analysis limits

Several survey responses were categorical before synthetic interpolation. Fractional values in FCVC, NCP, CH2O, FAF, and TUE are not precise observed frequencies, meal counts, liters, days, or hours. Consult the [source paper's questionnaire](https://pmc.ncbi.nlm.nih.gov/articles/PMC6710633/) for response categories. Do not infer an exact measurement from a code or assume rounding reconstructs the original survey answer.

The source labeling process used BMI, calculated from weight and height. Predicting the class with these same inputs partly reconstructs the label definition. State that clearly when designing a modeling exercise. The supplied labels are not a clinical diagnosis or a basis for individual medical decisions.

Use the table for learning descriptive analysis and model mechanics. It does not support population prevalence estimates or causal claims about lifestyle. A random split can place duplicates or related synthetic records on both sides. Keeping identical rows together only addresses exact duplicates; the synthetic lineage is unavailable. Strong claims about generalization need independent observed validation data. Any new oversampling should be fitted on training data only.

The notebook's rounded activity bins are an optional visualization. It keeps the original FAF column for continuous summaries and correlations. Pearson correlations of interpolated codes require caution because category spacing is a modeling assumption.

## Source, citation, and license

Mendoza Palechor, F., and de la Hoz Manotas, A. (2019). *Dataset for estimation of obesity levels based on eating habits and physical condition in individuals from Colombia, Peru and Mexico*. Data in Brief, 25, 104344. [doi:10.1016/j.dib.2019.104344](https://doi.org/10.1016/j.dib.2019.104344).

Dataset: [UCI Machine Learning Repository, doi:10.24432/C5H31Z](https://doi.org/10.24432/C5H31Z). UCI distributes it under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). Retain source attribution, the license link, and a description of modifications when redistributing it. The repository's general CC0 notice does not replace the source data's license.

This correction changes documentation and the worked example, not the CSV. The previously embedded third-party image was removed because its reuse permission was not documented.
