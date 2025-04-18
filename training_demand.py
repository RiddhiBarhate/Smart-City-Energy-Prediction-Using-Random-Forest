import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from joblib import dump, load

# Load the dataset
data = pd.read_csv("E:/project 2023/ME Projects/Electricity demand forcasting/Electricity demand forcasting/Book1.csv")

# Perform any necessary preprocessing steps, such as handling missing values, scaling features, etc.

# Split the dataset into features (X) and target (y)
X = data.drop(columns=["Peak Demand (kW)"])  # Features
y = data["Peak Demand (kW)"]  # Target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)

# Evaluate the model
train_loss = mean_squared_error(y_train, train_predictions)
test_loss = mean_squared_error(y_test, test_predictions)

print("Train Loss:", train_loss)
print("Test Loss:", test_loss)

# Save the trained model
dump(model, "linear_regression_model.joblib")

# Load the model for inference later
loaded_model = load("linear_regression_model.joblib")

# Example usage:
# prediction = loaded_model.predict(new_data)
