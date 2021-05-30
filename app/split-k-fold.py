#!/usr/bin/env python3
from sklearn.model_selection import KFold
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
import pandas as pd
import sys


# command line input
input_file = sys.argv[1]
k = sys.argv[2]

# data import
df = pd.read_csv(input_file)


# data preprocessing
df.columns = df.columns.str.replace(" ", "")
oh_enc = OneHotEncoder()
ord_enc = OrdinalEncoder()

## Nominal to OneHotEncoded
df[df.columns[-1:]]
## Nominal to Ordinal

kf = KFold(n_splits=int(k))

i = 1

for train_index, test_index in kf.split(df):
    train_data = df.loc[train_index]
    test_data = df.loc[test_index]
    test_file_name = str(i) + "_test.csv"
    train_file_name = str(i) + "_train.csv"
    i += 1
    train_data.to_csv(train_file_name, index=False)
    test_data.to_csv(test_file_name, index=False)
