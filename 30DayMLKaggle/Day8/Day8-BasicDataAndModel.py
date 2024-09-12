import pandas as pd

melbourne_data = pd.read_csv("Day8/melb_data.csv/melb_data.csv")
DS = melbourne_data.describe()
print(DS)
print(DS.Rooms.loc["mean"])

print(melbourne_data.columns)

melbourne_data = melbourne_data.dropna(axis=0)

# Select the prediction target
y = melbourne_data.Price

# choose features
melbourne_feature = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

X = melbourne_data[melbourne_feature]

print(X.describe())

from sklearn.tree import DecisionTreeClassifier

melbourne_model = DecisionTreeClassifier(random_state=1)
# specify a random-state ensures getting the same results each run
melbourne_model.fit(X,y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))