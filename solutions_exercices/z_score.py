# -*- coding: utf-8 -*-

# Two possible function for z_score

import numpy as np
import operator
import pandas as pd


def z_score_1(X):
    # zero mean and unit variance
    mean = np.mean(X, axis=0)
    std_dev = np.std(X, axis=0)
    z = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
    return z, mean, std_dev

#  or


def z_score_2(X):
    if isinstance(X, pd.DataFrame):
        X = X.to_numpy()

    def _mean(data):
        return float(sum(data) / len(data))

    def _variance(data):
        mu = _mean(data)
        return _mean([(x - mu) ** 2 for x in data])

    def _stddev(data):
        return (_variance(data)) ** 0.5

    def _zscore(data):
        num = [x - _mean(data) for x in data]
        return [x / _stddev(data) for x in num]

    mean = [_mean(x) for x in zip(*X)]
    std_dev = [_stddev(x) for x in zip(*X)]
    z = [_zscore(x) for x in zip(*X)]

    return z, mean, std_dev


x_train_standardize, mean, std_dev = z_score_1(x_train) # or use z_score_2
x_test_standardize = ((x_test - mean) / std_dev)
# Yes, on the test set, you need to apply the value find in the train set!

