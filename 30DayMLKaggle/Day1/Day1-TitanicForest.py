import numpy as np # linear algebra
import pandas as pd # data process

import matplotlib as mpl
import matplotlib.pyplot as plt

train_data = pd.read_csv("Day1/train.csv")
print(train_data.head())

test_data = pd.read_csv("Day1/test.csv")
print(test_data.head())

FF = train_data.Fare
FFnm = FF.to_numpy()

QQ = plt.plot(FFnm)
# plt.pause(0)

women = train_data.loc[train_data.Sex=='female']["Survived"]
rate_women = sum(women)/len(women)

men = train_data.loc[train_data.Sex=='male']["Survived"]
rate_men = sum(men)/len(men)

print(" %.2f%% of women who survived:" % (rate_women))
print(" %.2f%% of men who survived:" % (rate_men))

from sklearn.ensemble import RandomForestClassifier

y = train_data["Survived"]

features = ["Pclass","Sex","SibSp","Parch"]

X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

# This is what happens when using get dummies
print(X)

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X,y)
predictions = model.predict(X_test)

print(predictions)