# Daniel Holmes
# 11/4/2019
# COLUMNS.py
# groups of columns. Used mainly in process.py to put player data into the df systematically


p1_columns = ['p1_rating',                      # Columns for player 1 data
              'p1_win_streak',
              'p1_win_rate_S',
              'p1_win_rate_M',
              'p1_win_rate_L',
              'p1_trend_S',
              'p1_trend_M',
              'p1_trend_L',
              'p1_avg_adjustment_S',
              'p1_avg_adjustment_M',
              'p1_avg_adjustment_L',
              'p1_avg_opponent_rating_S',
              'p1_avg_opponent_rating_M',
              'p1_avg_opponent_rating_L',
              'p1_avg_opponent_rating_win',
              'p1_avg_opponent_rating_loss',
              'p1_hh',
              'p1_rust',
              'p1_games_week1',
              'p1_games_week2',
              'p1_upsets_made',
              'p1_times_upset']

p2_columns = ['p2_rating',                      # Columns for player 2 data
              'p2_win_streak',
              'p2_win_rate_S',
              'p2_win_rate_M',
              'p2_win_rate_L',
              'p2_trend_S',
              'p2_trend_M',
              'p2_trend_L',
              'p2_avg_adjustment_S',
              'p2_avg_adjustment_M',
              'p2_avg_adjustment_L',
              'p2_avg_opponent_rating_S',
              'p2_avg_opponent_rating_M',
              'p2_avg_opponent_rating_L',
              'p2_avg_opponent_rating_win',
              'p2_avg_opponent_rating_loss',
              'p2_hh',
              'p2_rust',
              'p2_games_week1',
              'p2_games_week2',
              'p2_upsets_made',
              'p2_times_upset'
              ]

d_columns = ['d_rating',                        # Columns with the delta in player stats, player 2 - player 1
             'd_win_streak',
             'd_win_rate_S',
             'd_win_rate_M',
             'd_win_rate_L',
             'd_trend_S',
             'd_trend_M',
             'd_trend_L',
             'd_avg_adjustment_S',
             'd_avg_adjustment_M',
             'd_avg_adjustment_L',
             'd_avg_opponent_rating_S',
             'd_avg_opponent_rating_M',
             'd_avg_opponent_rating_L',
             'd_avg_opponent_rating_win',
             'd_avg_opponent_rating_loss',
             'd_hh',
             'd_rust',
             'd_games_week1',
             'd_games_week2',
             'd_upsets_made',
             'd_times_upset'
             ]

labels = [                                      # Label columns
    'score',
    'outcome'
]

# All columns in data.csv
columns = p1_columns + p2_columns + d_columns + labels