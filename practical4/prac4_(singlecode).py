import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway

# Load the Iris dataset from Seaborn
iris_data = sns.load_dataset('iris')

# a. Find the correlation matrix:
# Exclude the 'species' column for correlation calculation
correlation_matrix = iris_data.drop('species', axis=1).corr()
print("Correlation Matrix:")
print(correlation_matrix)
print("\n")

# b. Plot the correlation plot on the dataset:
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5)
plt.title("Correlation Plot of Iris Dataset")
plt.show()

# c. Analysis of Covariance (ANOVA) if data have categorical variables:
# Assuming 'species' is a categorical variable (replace with your actual column name)
categories = iris_data['species'].unique()

# Perform ANOVA for each feature based on the categorical variable
for feature in iris_data.columns[:-1]:  # Exclude the last column (assuming it's the categorical variable)
    groups = [iris_data[iris_data['species'] == category][feature] for category in categories]
    f_statistic, p_value = f_oneway(*groups)
    
    print(f"ANOVA for {feature}: F-statistic = {f_statistic}, p-value = {p_value}")
