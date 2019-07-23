# Daniel Holmes
# 2019/04/11
# process.py
# calculates stats from results.csv saved as data.csv

import pandas as pd
from data.functions import get_player_stats
from data.COLUMNS import p1_columns, p2_columns, columns, d_columns

df = pd.read_csv('data/results.csv')
df_stats = pd.DataFrame(columns=columns)

r = 0

for row in df.index[:20000]:
    print(row)
    
    # Get labels
    winner_score = df.at[row, 'winner_score']
    loser_score = df.at[row, 'loser_score']

    # Make sure the score were entered
    if pd.isnull(winner_score) or pd.isnull(loser_score):
        continue

    label = loser_score - winner_score

    # Required information to determine stats
    match_id = df.at[row, 'result_id']
    winner_id = df.at[row, 'winner_id']
    loser_id = df.at[row, 'loser_id']

    # Stats for each player
    winner = get_player_stats(df, row, match_id, winner_id, loser_id)
    loser = get_player_stats(df, row, match_id, loser_id, winner_id)

    # Winner's perspective
    for stat, column in zip(winner, p1_columns):
        df_stats.at[r, column] = stat

    for stat, column in zip(loser, p2_columns):
        df_stats.at[r, column] = stat

    for stat1, stat2, column in zip(winner, loser, d_columns):
        df_stats.at[r, column] = stat2 - stat1

    df_stats.at[r, 'outcome'] = 1
    df_stats.at[r, 'score'] = label
    r += 1

    # Loser's perspective
    for stat, column in zip(loser, p1_columns):
        df_stats.at[r, column] = stat

    for stat, column in zip(winner, p2_columns):
        df_stats.at[r, column] = stat

    for stat1, stat2, column in zip(loser, winner, d_columns):
        df_stats.at[r, column] = stat2 - stat1

    df_stats.at[r, 'outcome'] = -1
    df_stats.at[r, 'score'] = -label
    r += 1

df_stats.to_csv('data/data.csv')


