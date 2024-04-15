import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_iris
# Load the Iris dataset 
iris = load_iris()
# Convert the dataset into a Pandas dataframe with feature names
df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],columns=['sepal
_length', 'sepal_width', 'petal_length', 'petal_width', 'target'])
# Split the dataset into predictors (X) and target (y)
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
# Create a linear regression model
model = LinearRegression()
# Fit the model to the data
model.fit(X, y)
# Print the coefficients of the model
print('Coefficients: \n', model.coef_)
# Predict the target variable for a new observation
new_observation = [[5.1, 3.5, 1.4, 0.2]]
print('Predicted target value for new observation:',model.predict(new_obser
vation))