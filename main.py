from data_loader import load_data
from features import create_features
from models import train_models
from config import BANKROLL
from paper_trader import PaperTrader

def main():
    # Load CSV data
    players, games, adv, teams = load_data()

    # Compute rolling features
    players = create_features(players)

    # Train models on points
    log_model, xgb_model = train_models(players, "points")

    # Initialize paper trader
    trader = PaperTrader(BANKROLL)

    print("System initialized successfully.")
    print("Example rolling stats:")
    print(players[["personId", "points_rolling", "assists_rolling", "reboundsTotal_rolling"]].head())

if __name__ == "__main__":
    main()