# Daniel Holmes
# 2019/07/22
# summary_plot.py
# creates summary plots of features using shap library


import shap
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from data.get import pipeline


def shap_summary_plot(features, label):
    """ Create a shap summary plot"""

    # Get data and train the model
    X_train, X_test, y_train, y_test = pipeline(features, label, 4000, .25)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Create the shap summary plot
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_test)
    shap.summary_plot(shap_values, X_test, show=False)
    plt.figure(figsize=(12, 12))
    plt.savefig(f'visualization/summary_plot_{label}.png', )
    plt.clf()


