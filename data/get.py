# Daniel Holmes
# 2019/07/22
# get.py
# function for getting data with train test split, specific features and label


import os
import pandas as pd
from sklearn.model_selection import train_test_split

directory = os.path.dirname(__file__)
csv = os.path.join(directory, 'data.csv')


def pipeline(features, label, data_points, test_size):
    """ get data from csv """

    df = pd.read_csv(csv, index_col=0)[:data_points]
    X = df[features]
    y = df[label]

    return train_test_split(X, y, test_size=test_size, shuffle=False)