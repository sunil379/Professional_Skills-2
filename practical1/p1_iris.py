import pandas as pd

iris = pd.read_csv('iris.csv')

#  Use subset() function to select only rows where Sepal.Width > 3
setosa_subset = iris[iris['sepal_width'] >= 3.9]
print("1] Subset of Iris dataset with only rows where Sepal.Width > 3.9 :\n")
print(setosa_subset)

#  Use aggregate() function to calculate mean sepal length for each species
aggregate_result = iris.groupby('species').mean()
print("\n2] Aggregate result - Mean sepal length and sepal width for each species:\n")
print(aggregate_result)