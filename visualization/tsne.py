# Daniel Holmes
# 2019/07/22
# tsne.py
# visualize high dimensional data using TSNE


import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from data.get import pipeline


def TSNE_graph(features, label, colours):
    """ TSNE graph of matches played coloured by label """
    X_train, X_test, y_train, y_test = pipeline(features, label, 4000, 0.0001)
    X_embedded = TSNE(n_components=2, random_state=2).fit_transform(X_train, y_train)

    for X, y in zip(X_embedded, y_train):
        plt.scatter(X[0], X[1], c=colours[y])

    plt.savefig(f'visualization/TSNE_graph_{label}.png')