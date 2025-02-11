# -*- coding: utf-8 -*-

from sklearn.model_selection import KFold
import numpy as np
import pandas as pd


def cross_validation(X, y, model, num_folds=5):
    if isinstance(X, pd.DataFrame):
        X = X.to_numpy()
    if isinstance(y, pd.DataFrame):
        y = y.to_numpy()

    cv = KFold(n_splits=num_folds, random_state=123, shuffle=True)
    results_train, results_test = [], []
    for train_index, test_index in cv.split(X):
        X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]
        clf = model.fit(X_train, y_train)
        accuracy_train = clf.score(X=X_train, y=y_train)
        accuracy_test = clf.score(X=X_test, y=y_test)  # Return the mean accuracy
        results_train.append(accuracy_train)
        results_test.append(accuracy_test)
    return results_train, results_test
