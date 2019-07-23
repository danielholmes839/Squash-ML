# Ottawa Squash Match Predictions #
I created a machine learning web application which can be used to predict the score of amateur squash matches in Ottawa. 
This repository contains all the code I used to generate the model and clean the data. 
See the website [here](https://odsa-genius.herokuapp.com/). 
See the full source code [here](https://github.com/danielholmes839/Squash-App).
Squash players in Ottawa use a website called [Rankenstein](https://www.rankenstein.ca/index.pl) which has kept track of squash matches since 2005. 
I trained my model using 15,000 games played in Ottawa with wide variety of stats from 1000+ players.

# Data Visualization

High dimensional data of wins/losses visualization by TSNE:

![TSNE visualization of wins and losses ](/visualization/TSNE_graph_outcome.png){:height="50%" width="50%"}


# Features
SHapley Additive exPlanations (SHAP) summary plot visualizes feature importance

![Feature Importance](/visualization/summary_plot_outcome.png){:height="50%" width="50%"}

I've tried many features including:
- Rating
- Win streak
- Win rate vs. opponent
- Trend (increase in rating over time)
- Upset rate
- Time since last played
