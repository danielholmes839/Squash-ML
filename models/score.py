# Daniel Holmes
# 2019/07/22
# score.py
# functions for scoring a models predictions against test set

import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, f1_score, matthews_corrcoef, accuracy_score, recall_score, precision_score


def confusion_matrix_df(y_test, y_pred, classes):
    """ Create a confusion matrix as a data frame """
    cm = confusion_matrix(y_test, y_pred)
    cm = cm / cm.astype(np.float).sum(axis=1)
    return pd.DataFrame(columns=classes, index=classes, data=cm)


def percent_scores(y_test, y_pred):
    """ Score predictions """
    return {
        'accuracy': accuracy_score(y_test, y_pred),
        'recall': recall_score(y_test, y_pred, average='weighted'),
        'precision': precision_score(y_test, y_pred, average='weighted'),
        'f1': f1_score(y_test, y_pred, average='weighted'),
        'matthew coefficient': matthews_corrcoef(y_test, y_pred)
    }