# Daniel Holmes
# 8/4/2019
# functions.py
# functions to get player stats from the results.csv
# some functions are really gross

from datetime import datetime, timedelta


def get_matches(df, player_id):
    """ Get all games played by player """
    return df[(df.winner_id == player_id) | (df.loser_id == player_id)].reset_index()


def get_match_index(matches_df, match_id):
    """ Get match index in df from ID """
    for i in matches_df.index:                                                      # for every game
        if matches_df.at[i, 'result_id'] == match_id:                               # if the game id's are the same
            return i                                                                # return the index


def get_trend(matches_df, match_index, player_id, n):
    """
        Get player trend over the last n games
        trend is the sum of the player's rating adjustment
    """
    trend = 0
    n_added = 0
    previous_match_index = match_index + 1

    if previous_match_index == matches_df.shape[0]:
        return 0

    for i in range(previous_match_index, matches_df.shape[0]):

        if matches_df.at[i, 'winner_id'] == player_id:          # player won
            if matches_df.at[i, 'winner_adjust'] != 0:          # player adjustment wasn't 0

                trend += matches_df.at[i, 'winner_adjust']      # add to trend
                n_added += 1                                    # increment

        else:                                                   # player lost
            if matches_df.at[i, 'loser_adjust'] != 0:
                trend += matches_df.at[i, 'winner_adjust']
                n_added += 1

        if n_added == n:                                        # stop once n matches have been added
            break

    return trend


def get_avg_adjustment(matches_df, match_index, player_id, n):
    """ get player average adjustment similar to trend """

    adjustment = 0
    n_added = 0
    previous_match_index = match_index + 1

    if previous_match_index == matches_df.shape[0]:
        return 0

    for i in range(previous_match_index, matches_df.shape[0]):

        if matches_df.at[i, 'winner_id'] == player_id:               # player won
            if matches_df.at[i, 'winner_adjust'] != 0:               # player adjustment wasn't 0

                adjustment += matches_df.at[i, 'winner_adjust']      # add to trend
                n_added += 1                                         # increment

        else:                                                        # player lost
            if matches_df.at[i, 'loser_adjust'] != 0:
                adjustment += matches_df.at[i, 'winner_adjust']
                n_added += 1

        if n_added == n:                                             # stop once n matches have been added
            break

    if n_added == 0:
        return 0

    return adjustment/n_added


def get_win_streak(matches_df, match_index, player_id):
    """ Get player win streak """

    previous_match_index = match_index + 1
    win_streak = 0

    if previous_match_index == matches_df.shape[0]:
        return 0

    if matches_df.at[previous_match_index, 'winner_id'] == player_id == player_id:
        on_win_streak = True
    else:
        on_win_streak = False

    for i in range(previous_match_index, matches_df.shape[0]):
        if on_win_streak and matches_df.at[i, 'winner_id'] == player_id:
            win_streak += 1

        elif not on_win_streak and matches_df.at[i, 'loser_id'] == player_id:
            win_streak -= 1

        else:
            break

    return win_streak


def get_win_rate(matches_df, match_index, player_id, n):
    """ get player win rate over the last n games """

    total = 0
    wins = 0

    previous_match_index = match_index + 1

    if previous_match_index == matches_df.shape[0]:
        return 50

    for i in range(previous_match_index, matches_df.shape[0]):
        if matches_df.at[i, 'winner_id'] == player_id:
            wins += 1

        total += 1

        if total == n:
            break

    if total == 0:
        return 50

    return int((wins/total) * 100)


def get_head_to_head(matches_df, match_index, opponent_id):
    """ gets a player win percentage against another player """

    n_games = len(matches_df)
    n_games_head_to_head = 0
    n_wins = 0
    previous_game_index = match_index + 1

    if previous_game_index == matches_df.shape[0]:
        return 50

    for i in range(previous_game_index, n_games):               # for every previous game played by the player
        if matches_df.at[i, 'loser_id'] == opponent_id:         # if the loser was the opponent
            n_wins += 1                                         # add a win
            n_games_head_to_head += 1                           # add a game to the total number of games

        elif matches_df.at[i, 'winner_id'] == opponent_id:      # if the winner was the opponent
            n_games_head_to_head += 1                           # only add a game to the total number of games

    if n_games_head_to_head == 0:                               # if they haven't played a game before
        return 50                                               # return 50%

    return round((n_wins/n_games_head_to_head)*100)             # return as a percent


def get_avg_opponent_rating(matches_df, match_index, player_id, n):
    """ gets a player average opponent rating over n games  """

    sum_opponent_rating = 0
    matches = 0

    previous_match_index = match_index + 1

    # not enough data
    if previous_match_index == matches_df.shape[0]:
        if matches_df.at[match_index, 'winner_id'] == player_id:
            return matches_df.at[match_index, 'winner_rating']
        else:
            return matches_df.at[match_index, 'loser_rating']

    # normal
    for i in range(previous_match_index, matches_df.shape[0]):               # for every previous game played by the player
        if matches_df.at[i, 'winner_id'] == player_id:
            sum_opponent_rating += matches_df.at[i, 'loser_rating']

        else:
            sum_opponent_rating += matches_df.at[i, 'winner_rating']

        matches += 1

        if matches == n:
            break

    # found 0 matches
    if matches == 0:
        if matches_df.at[match_index, 'winner_id'] == player_id:
            return matches_df.at[match_index, 'winner_rating']
        else:
            return matches_df.at[match_index, 'loser_rating']

    return int(sum_opponent_rating/matches)


def get_avg_opponent_rating_wl(matches_df, match_index, player_id, n, wins_only):
    """ gets a player average opponent rating over n games where they lose or win """

    sum_opponent_rating = 0
    wl = 0
    matches = 0

    previous_match_index = match_index + 1

    # not enough data
    if previous_match_index == matches_df.shape[0]:
        if matches_df.at[match_index, 'winner_id'] == player_id:
            return matches_df.at[match_index, 'winner_rating']
        else:
            return matches_df.at[match_index, 'loser_rating']

    # normal
    for i in range(previous_match_index, matches_df.shape[0]):               # for every previous game played by the player
        if wins_only:
            if matches_df.at[i, 'winner_id'] == player_id:
                sum_opponent_rating += matches_df.at[i, 'loser_rating']
                wl += 1

        else:
            if matches_df.at[i, 'loser_id'] == player_id:
                sum_opponent_rating += matches_df.at[i, 'winner_rating']
                wl += 1

        matches += 1
        if matches == n:
            break

    # found 0 matches
    if wl == 0:
        if matches_df.at[match_index, 'winner_id'] == player_id:
            return matches_df.at[match_index, 'winner_rating']
        else:
            return matches_df.at[match_index, 'loser_rating']

    return int(sum_opponent_rating/wl)


def get_time_since_played(matches_df, match_index):
    """ time since a player last played """
    if match_index + 1 == matches_df.shape[0]:
        return 3

    format = '%Y-%m-%d'

    present = matches_df.at[match_index, 'result_date']
    present = datetime.strptime(present, format)

    past = matches_df.at[match_index + 1, 'result_date']
    past = datetime.strptime(past, format)

    return (present - past).days


def get_games_played_since(matches_df, match_index, n):
    """ time since a player last played """
    if match_index + 1 == matches_df.shape[0]:
        return 1

    format = '%Y-%m-%d'

    present = matches_df.at[match_index, 'result_date']
    present = datetime.strptime(present, format)

    previous_match_index = match_index + 1

    matches = 0
    stop = present - timedelta(days=n)

    for i in range(previous_match_index, matches_df.shape[0]):
        date = datetime.strptime(matches_df.at[i, 'result_date'], format)

        if date >= stop:
            matches += 1

        else:
            break

    return matches


def get_upsets_made(matches_df, match_index, player_id, n):
    """ Get the number of times the player has made an upset in the last n games """
    upsets = 0
    n_checked = 0

    previous_match_index = match_index + 1
    if previous_match_index == matches_df.shape[0]:
        return 0

    for i in range(previous_match_index, matches_df.shape[0]):
        if matches_df.at[i, 'winner_id'] == player_id:
            if matches_df.at[i, 'winner_rating'] < matches_df.at[i, 'loser_rating']:
                upsets += 1

        n_checked += 1
        if n_checked == n:
            break

    return upsets


def get_times_upset(matches_df, match_index, player_id, n):
    """ Get the number of times a player has been upset in the last n games """
    upsets = 0
    n_checked = 0

    previous_match_index = match_index + 1
    if previous_match_index == matches_df.shape[0]:
        return 0

    for i in range(previous_match_index, matches_df.shape[0]):
        if matches_df.at[i, 'loser_id'] == player_id:
            if matches_df.at[i, 'winner_rating'] < matches_df.at[i, 'loser_rating']:
                upsets += 1

        n_checked += 1
        if n_checked == n:
            break

    return upsets


def get_player_stats(df, r, match_id, p1_id, p2_id):
    """ Get player information before the match """
    S = 4   # short term
    M = 8   # medium term
    L = 12  # long term

    p1_matches = get_matches(df, p1_id)  # list of p1 matches
    p1_match_index = get_match_index(p1_matches, match_id)  # index of match in the df of the p1's matches

    if df.at[r, 'winner_id'] == p1_id:
        p1_rating = df.at[r, 'winner_rating']
    else:
        p1_rating = df.at[r, 'loser_rating']

    p1_win_streak = get_win_streak(p1_matches, p1_match_index, p1_id)       # win streak

    p1_win_rate_S = get_win_rate(p1_matches, p1_match_index, p1_id, S)      # win rate short term
    p1_win_rate_M = get_win_rate(p1_matches, p1_match_index, p1_id, M)      # win rate medium term
    p1_win_rate_L = get_win_rate(p1_matches, p1_match_index, p1_id, L)      # win rate long term

    p1_trend_S = get_trend(p1_matches, p1_match_index, p1_id, S)            # trend short term
    p1_trend_M = get_trend(p1_matches, p1_match_index, p1_id, M)            # trend medium term
    p1_trend_L = get_trend(p1_matches, p1_match_index, p1_id, L)            # trend long term

    p1_avg_adjustment_S = get_avg_adjustment(p1_matches, p1_match_index, p1_id, S)             # average adjustment short term
    p1_avg_adjustment_M = get_avg_adjustment(p1_matches, p1_match_index, p1_id, M)             # average adjustment medium term
    p1_avg_adjustment_L = get_avg_adjustment(p1_matches, p1_match_index, p1_id, L)             # average adjustment long term

    p1_avg_opponent_rating_S = get_avg_opponent_rating(p1_matches, p1_match_index, p1_id, S)   # avg opponent rating short term
    p1_avg_opponent_rating_M = get_avg_opponent_rating(p1_matches, p1_match_index, p1_id, M)   # avg opponent rating medium term
    p1_avg_opponent_rating_L = get_avg_opponent_rating(p1_matches, p1_match_index, p1_id, L)   # avg opponent rating long term

    p1_avg_opponent_rating_win = get_avg_opponent_rating_wl(p1_matches, p1_match_index, p1_id, L, True)     # avg opponent rating in wins
    p1_avg_opponent_rating_loss = get_avg_opponent_rating_wl(p1_matches, p1_match_index, p1_id, L, False)   # avg opponent rating in losses

    p1_hh = get_head_to_head(p1_matches, p1_match_index, p2_id)                     # win percentage vs opponent

    p1_rust = get_time_since_played(p1_matches, p1_match_index)                     # time since last played
    p1_games_week1 = get_games_played_since(p1_matches, p1_match_index, 7)          # games played in the past week
    p1_games_week2 = get_games_played_since(p1_matches, p1_match_index, 14)         # games played in the past 2 weeks

    p1_upsets_made = get_upsets_made(p1_matches, p1_match_index, p1_id, L)
    p1_times_upset = get_times_upset(p1_matches, p1_match_index, p1_id, L)

    # MUST CORRESPOND TO COLUMNS IN COLUMNS.py
    return [p1_rating,

            p1_win_streak,

            p1_win_rate_S,
            p1_win_rate_M,
            p1_win_rate_L,

            p1_trend_S,
            p1_trend_M,
            p1_trend_L,

            p1_avg_adjustment_S,
            p1_avg_adjustment_M,
            p1_avg_adjustment_L,

            p1_avg_opponent_rating_S,
            p1_avg_opponent_rating_M,
            p1_avg_opponent_rating_L,

            p1_avg_opponent_rating_win,
            p1_avg_opponent_rating_loss,

            p1_hh,
            p1_rust,
            p1_games_week1,
            p1_games_week2,

            p1_upsets_made,
            p1_times_upset]

