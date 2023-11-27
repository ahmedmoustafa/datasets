# The Obesity Dataset

![](https://media.gettyimages.com/id/85074748/photo/obese-man-with-72-inch-waist.jpg?s=2048x2048&w=gi&k=20&c=hZZhDirAK0xGSHg8R7TGCrpGDbU_cRLsEGtVaxic7dE=)


## Overview
The dataset reports on obesity levels in individuals from Mexico, Peru, and Colombia. The dataset focuses on individuals aged between 14 and 61, covering a wide range of eating habits and physical conditions. It is a valuable resource for understanding obesity patterns in these populations through a comprehensive collection of data points relating to individual health metrics, dietary habits, and lifestyle choices. The dataset is aimed at facilitating research and analysis to understand the factors contributing to different levels of obesity.

## Description
The dataset consists of various features that include both lifestyle attributes and physical measurements. The dataset is structured as follows:

| Column Number | Column Name                      | Description                                      | Type (Abstract) | Possible Values/Range |
|---------------|----------------------------------|--------------------------------------------------|-----------------|-----------------------|
| 1             | Gender                           | Gender of the individual                         | Categorical     | [Female, Male]        |
| 2             | Age                              | Age of the individual in years                   | Numerical       | 14.0 - 61.0           |
| 3             | Height                           | Height of the individual in meters               | Numerical       | 1.45 - 1.98           |
| 4             | Weight                           | Weight of the individual in kilograms            | Numerical       | 39.0 - 173.0          |
| 5             | family_history_with_overweight   | Whether the individual has a family history of overweight | Categorical | [yes, no]         |
| 6             | FAVC                             | Frequent consumption of high caloric food        | Categorical     | [no, yes]             |
| 7             | FCVC                             | Frequency of consumption of vegetables           | Numerical       | 1.0 - 3.0             |
| 8             | NCP                              | Number of main meals                             | Numerical       | 1.0 - 4.0             |
| 9             | CAEC                             | Consumption of food between meals                | Categorical     | [Sometimes, Frequently, Always, no] |
| 10            | SMOKE                            | Smoking status                                   | Categorical     | [no, yes]             |
| 11            | CH2O                             | Consumption of water daily (liters)              | Numerical       | 1.0 - 3.0             |
| 12            | SCC                              | Calories consumption monitoring                  | Categorical     | [no, yes]             |
| 13            | FAF                              | Physical activity frequency                      | Numerical       | 0.0 - 3.0             |
| 14            | TUE                              | Time using technology devices (hours)            | Numerical       | 0.0 - 2.0             |
| 15            | CALC                             | Alcohol consumption                              | Categorical     | [no, Sometimes, Frequently, Always] |
| 16            | MTRANS                           | Most frequent transportation mode                | Categorical     | [Public_Transportation, Walking, Automobile, Motorbike, Bike] |
| 17            | NObeyesdad                       | Obesity level                                    | Categorical     | [Normal_Weight, Overweight_Level_I, Overweight_Level_II, Obesity_Type_I, Obesity_Type_II, Obesity_Type_III, Insufficient_Weight] |

## Potential Applications
- Obesity research focusing on dietary habits and physical activity.
- Statistical analysis for healthcare studies.
- Educational use in data science, particularly in health-related analytics.
- Development of predictive models in public health.

## Disclaimer
The dataset is provided "as is" without warranty of any kind.

## Contact Information
For questions or more information about the dataset, please see [dataset provider's page](https://www.kaggle.com/datasets/aravindpcoder/obesity-or-cvd-risk-classifyregressorcluster).

