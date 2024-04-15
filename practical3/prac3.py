import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Iris dataset from Seaborn
iris = sns.load_dataset('iris')

# Display the first few rows of the dataset to understand its structure
print(iris.head())

# Visualize data distributions with a box plot
sns.boxplot(data=iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])
plt.title('Box Plot of Iris Dataset')
plt.show()
plt.pause(1)

# Scatter Plot
sns.scatterplot(x='sepal_length', y='petal_width', data=iris, hue='species', palette='Set2')
plt.title('Scatter Plot of Sepal Length vs Petal Width in Iris Dataset')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Width')
plt.show()
plt.pause(1)

# Identify outliers using a box plot
sns.boxplot(data=iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])
plt.title('Box Plot to Identify Outliers in Iris Dataset')
plt.show()
plt.pause(1)

# Histogram
iris['sepal_length'].plot(kind='hist', bins=20, edgecolor='black')
plt.title('Histogram of Sepal Length in Iris Dataset')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()
plt.pause(1)

# Bar Chart
iris['species'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Bar Chart of Iris Species')
plt.xlabel('Species')
plt.ylabel('Count')
plt.show()
plt.pause(1)

# Pie Chart
species_counts = iris['species'].value_counts()
plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart of Iris Species Distribution')
plt.axis('equal')
plt.show()
plt.pause(1)
