#!/usr/bin/env python3
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import sys
input_path = sys.argv[1]

data = pd.read_csv(input_path)
data.columns = data.columns.str.replace(" ", "")

# column descriptions
numeric_columns = data._get_numeric_data().columns
ordinal_columns = ["checking_status", "savings_status", "employment", "job"]
binary_columns = ["class", "own_telephone", "foreign_worker"]
categorical_columns = list(
    set(data.columns) - set(numeric_columns) - set(binary_columns)
)
nominal_columns = list(set(categorical_columns) - set(ordinal_columns))

# categorical data stripping and one-hot encoding
for c in categorical_columns:
    data[c] = data[c].str.strip()

preprocessed_categorical_data = pd.get_dummies(data[nominal_columns])

# ordinal data preprocessing and ordinal encoding
## checking status
scale_mapper = {
    "<0": 0,
    "0<=X<200": 1,
    ">=200": 2,
    "no checking": 3,
}
data["checking_status"] = data["checking_status"].replace(scale_mapper)
## savings status
scale_mapper = {
    "<100": 0,
    "100<=X<500": 1,
    "500<=X<1000": 2,
    ">=1000": 3,
    "no known savings": 4,
}
data["savings_status"] = data["savings_status"].replace(scale_mapper)
## employment
scale_mapper = {
    "unemployed": 0,
    "<1": 1,
    "1<=X<4": 2,
    "4<=X<7": 3,
    ">=7": 4,
}
data["employment"] = data["employment"].replace(scale_mapper)
## job
scale_mapper = {
    "unemp/unskilled non res": 0,
    "unskilled resident": 1,
    "skilled": 2,
    "high qualif/self emp/mgmt": 3,
}
data["job"] = data["job"].replace(scale_mapper)

# boolean data encoding
le = LabelEncoder()
for c in binary_columns:
    data[c] = le.fit_transform(data[c])

df = pd.concat(
    [
        preprocessed_categorical_data,
        data[ordinal_columns],
        data[numeric_columns],
        data[binary_columns],
    ],
    axis=1,
)

df.to_csv("preprocessed_data.csv", index=False)
