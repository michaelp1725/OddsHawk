import pandas as pd
from config import ROLLING_WINDOW

def create_features(players):
    # Sort by player and game date
    players = players.sort_values(["personId", "gameDateTimeEst"])

    # Compute rolling averages for key stats
    stats = ["points", "reboundsTotal", "assists"]

    for stat in stats:
        if stat in players.columns:
            players[f"{stat}_rolling"] = (
                players.groupby("personId")[stat]
                .rolling(ROLLING_WINDOW)
                .mean()
                .reset_index(0, drop=True)
            )

    # Drop rows where rolling stats couldn't be computed
    players.dropna(subset=[f"{s}_rolling" for s in stats if s in players.columns], inplace=True)

    return players