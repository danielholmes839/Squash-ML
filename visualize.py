from data.COLUMNS import d_columns
from visualization.summary_plot import shap_summary_plot
from visualization.tsne import TSNE_graph


shap_summary_plot(d_columns, 'score')
shap_summary_plot(d_columns, 'outcome')


# Create TSNE plots
score_colours = {
    3: [[1, 0, 0, 0.5]],
    2: [[1, 0, .25, .5]],
    1: [[1, 0, .5, 1]],
    -1: [[.5, 0, 1, 1]],
    -2: [[.25, 0, 1, .5]],
    -3: [[0, 0, 1, 0.5]]
}

outcome_colours = {
    1: [[1, 0, 0]],
    -1: [[0, 0, 1]]
}


TSNE_graph(d_columns, 'score', score_colours)
TSNE_graph(d_columns, 'outcome', outcome_colours)