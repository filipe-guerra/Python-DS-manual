import pandas as pd

# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)

#Selecting The Prediction Target
y = melbourne_data.Price

#Choosing "Features"
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

# Building Your Model
# The steps to building and using a model are:

# Define: What type of model will it be? A decision tree? Some other type of model? Some other parameters of the model type are specified too.
# Fit: Capture patterns from provided data. This is the heart of modeling.
# Predict: Just what it sounds like
# Evaluate: Determine how accurate the model's predictions are.

from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)

# Predictions
print("The predictions are")
print(melbourne_model.predict(X.head()))