import pandas as pd
from config import DATA_PATH, START_SEASON

def load_data():
    # Read CSVs, ensure consistent dtypes and avoid low memory warnings
    players = pd.read_csv(DATA_PATH + "PlayerStatistics.csv", low_memory=False)
    games = pd.read_csv(DATA_PATH + "Games.csv", low_memory=False)
    adv = pd.read_csv(DATA_PATH + "PlayerStatisticsAdvanced.csv", low_memory=False)
    teams = pd.read_csv(DATA_PATH + "TeamStatistics.csv", low_memory=False)

    # Add a season column if missing in players
    if "season" not in players.columns:
        players["season"] = pd.to_datetime(players["gameDateTimeEst"]).dt.year

    if "season" not in games.columns:
        games["season"] = pd.to_datetime(games["gameDateTimeEst"]).dt.year

    # Filter for seasons we care about
    players = players[players["season"] >= START_SEASON]
    games = games[games["season"] >= START_SEASON]

    return players, games, adv, teams