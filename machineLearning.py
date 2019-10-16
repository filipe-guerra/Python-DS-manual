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


# MEAN ABSOLUTE ERROR
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)


# SPLITING DATA TO TRAINING
from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))

# UNDERFITTING AND OVERFITTING