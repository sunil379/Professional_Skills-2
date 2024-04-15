import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, 
classification_report
# Load the dataset
url = "https://stats.idre.ucla.edu/stat/data/binary.csv"
admissions_data = pd.read_csv(url)
# Preprocess the data
# For simplicity, we'll assume there are no missing values and the data is 
clean
# Define predictor (X) and target (y) variables
X = admissions_data[['gre', 'gpa', 'rank']]
y = admissions_data['admit']
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, 
random_state=42)
# Perform logistic regression
# Add intercept term
X_train = sm.add_constant(X_train)
X_test = sm.add_constant(X_test)
# Fit logistic regression model
logit_model = sm.Logit(y_train, X_train)
result = logit_model.fit()
# Print summary of the model
print(result.summary())
# Evaluate the model
# Predict on test set
y_pred = result.predict(X_test)
y_pred_class = np.where(y_pred > 0.5, 1, 0) # Convert predicted 
probabilities to binary classes
# Model accuracy
accuracy = accuracy_score(y_test, y_pred_class)
print("\nAccuracy:", accuracy)
# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred_class)
print("\nConfusion Matrix:")
print(conf_matrix)
# Classification report
class_report = classification_report(y_test, y_pred_class)
print("\nClassification Report:")
print(class_report)