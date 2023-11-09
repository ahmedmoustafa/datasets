import numpy as np
import pandas as pd

# Set a random seed for reproducibility
np.random.seed(123)

# Number of individuals
n = 1000

# Generate sex randomly
sex = np.random.choice(['Male', 'Female'], size=n)

# Generate height based on sex
height = np.where(sex == 'Male', np.random.normal(175, 7, n), np.random.normal(162, 6, n))

# Generate weight based on height and sex using adjusted linear models
weight = np.where(
    sex == 'Male',
    0.7 * height - 58 + np.random.normal(0, 5, n),
    0.6 * height - 45 + np.random.normal(0, 5, n)
)

# Create a DataFrame
data = pd.DataFrame({'Sex': sex, 'Height_cm': height, 'Weight_kg': weight})

# Save the dataset to a TSV file
file_path = 'height_weight_sex.tsv'
data.to_csv(file_path, sep='\t', index=False)
