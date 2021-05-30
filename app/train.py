#!/usr/bin/env python3
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score, accuracy_score, roc_curve
import pandas as pd
import sys

train_path = str(sys.argv[1])
train_data = pd.read_csv(train_path)
test_path = str(sys.argv[2])
test_data = pd.read_csv(test_path)

# print(train_data[:-1])
# print(train_data[-1:])

mlp = MLPClassifier()
rfc = RandomForestClassifier()
dtree = DecisionTreeClassifier()
model = rfc


model.fit(
    train_data.loc[:, train_data.columns != "class"],
    train_data["class"],
)

auc = roc_auc_score(
        test_data["class"],
        model.predict(test_data.loc[:, test_data.columns != "class"]),        
    )
accuracy = accuracy_score(
        test_data["class"],
        model.predict(test_data.loc[:, test_data.columns != "class"]),
    )
print("Model " + train_path.split("_")[0].split('/')[-1] + ";accuracy=" + str(accuracy) + ";auc="+str(auc))
