# Questions on Life Expectancy Dataset

## Data Exploration and Descriptive Statistics
1. **Explore the Dataset:**
   - Load the dataset and use functions like `head()`, `summary()`, and `str()` to explore the first few rows, summary statistics, and structure of the dataset.
   
2. **Calculate Descriptive Statistics:**
   - Calculate the mean and median of `Life_expectancy` for all countries.

## Data Filtering and Basic Plotting
3. **Filter Data and Calculate Average:**
   - Extract and display data for a specific region, say "Asia", and calculate the average `GDP_per_capita` for this region.

4. **Visualize Data Distribution:**
   - Create a basic histogram of `Life_expectancy` to visualize its distribution.

## Identifying Specific Data Points
5. **Find Specific Data Points:**
   - Identify the row where `Life_expectancy` is minimum and extract the corresponding country.
   - Identify the row where `GDP_per_capita` is maximum and extract the corresponding year.

## Data Transformation and Trend Analysis
6. **Create New Variable:**
   - Create a new column `BMI_category` which categorizes countries as either "Underweight", "Normal weight", "Overweight", or "Obese" based on the `BMI` column values.

7. **Analyze Trends:**
   - Plot the trend of `Life_expectancy` over the years for a specific country or region and analyze any visible trends.

## Correlation and Multivariate Analysis
8. **Correlation Analysis:**
   - Calculate and interpret the correlation between `Adult_mortality` and `Life_expectancy`.

9. **Explore Multivariate Relationships:**
   - Explore the relationship between `Life_expectancy`, `Schooling`, and `Alcohol_consumption` using appropriate visualizations such as scatter plots.

## Sorting and Ordering Data
10. **Sort and Order Data:**
   - Use the `sort` function to list the countries in ascending/descending order of `Adult_mortality`.
   - Use the `order` function to list the top 5 countries based on `BMI` and the bottom 5 countries based on `Schooling`.

## Advanced Visualization and Aggregation
11. **Facetted Visualization:**
   - Create a facetted scatter plot comparing `Life_expectancy` vs. `GDP_per_capita` for different `Economy_status` categories.

12. **Aggregate Data:**
    - Calculate the average `Life_expectancy`, `Schooling`, and `Alcohol_consumption` for each combination of `Region` and `Economy_status`.

## Hypothesis Testing and Predictive Modeling
13. **Test Hypothesis:**
    - Conduct a hypothesis test to compare the `Life_expectancy` between "Developed" and "Developing" countries.

14. **Build a Simple Model:**
    - Build a simple linear regression model to predict `Life_expectancy` based on variables like `Adult_mortality`, `BMI`, and `Schooling`.
