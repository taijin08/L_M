import pandas as pd

melbourne_data = pd.read_csv("Day8/melb_data.csv/melb_data.csv")

melbourne_data = melbourne_data.dropna(axis=0)

# Select the prediction target
y = melbourne_data.Price

# choose features
melbourne_feature = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

X = melbourne_data[melbourne_feature]

from sklearn.tree import DecisionTreeRegressor

melbourne_model = DecisionTreeRegressor(random_state=1)
# specify a random-state ensures getting the same results each run
melbourne_model.fit(X,y)

# Calculate mean absolute error
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)

# insample score
print(mean_absolute_error(y,predicted_home_prices))


from sklearn.model_selection import train_test_split

train_X, val_X, train_y, val_y = train_test_split(X,y,random_state=0)
melbourne_model2 = DecisionTreeRegressor()
melbourne_model2.fit(train_X,train_y)
val_predictions = melbourne_model2.predict(val_X)
print(mean_absolute_error(val_y,val_predictions))