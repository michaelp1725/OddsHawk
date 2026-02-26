# live_signals.py
import numpy as np
from data_loader import load_data
from features import create_features
from models import train_models
from monte_carlo import simulate_parlay
from kelly import fractional_kelly
from paper_trader import PaperTrader
from clob_client import get_orderbook
from subgraph_client import query_subgraph
from config import BANKROLL

def fetch_market_ids():
    # Minimal example: fetch 5 markets
    query = """
    {
      markets(first: 5) {
        id
        question
      }
    }
    """
    res = query_subgraph(query)
    return [m["id"] for m in res.get("data", {}).get("markets", [])]

def get_market_price(market_id):
    orderbook = get_orderbook(market_id)
    bids = orderbook.get("bids", [])
    asks = orderbook.get("asks", [])
    if bids and asks:
        return (float(bids[0]["price"]) + float(asks[0]["price"])) / 2
    return 0.5

def run_live_signals():
    # Load data & features
    players, games, adv, teams = load_data()
    players = create_features(players)

    # Train models
    log_model, xgb_model = train_models(players, "points")

    # Initialize trader
    trader = PaperTrader(BANKROLL)

    # Select top 3 recent players for demo parlay
    top_players = players.groupby("personId").tail(1)
    player_ids = top_players["personId"].tolist()[:3]
    features = [c for c in players.columns if "rolling" in c]
    probs = log_model.predict_proba(top_players[features])[:, 1]

    # Monte Carlo joint probability
    corr_matrix = np.identity(len(probs))
    joint_prob = simulate_parlay(probs, corr_matrix)

    # Fetch markets & calculate signals
    market_ids = fetch_market_ids()
    for market_id in market_ids:
        market_price = get_market_price(market_id)
        implied_prob = market_price

        ev = joint_prob - implied_prob
        action = "BUY YES" if ev > 0 else "BUY NO"

        odds = 1 / implied_prob if implied_prob > 0 else 2
        bet_fraction = fractional_kelly(joint_prob, odds)
        bet_amount = trader.bankroll * bet_fraction
        trader.bankroll -= bet_amount

        print(f"Market {market_id}: {action}")
        print(f"EV: {ev:.3f}, Kelly fraction: {bet_fraction:.3f}, Bet: ${bet_amount:.2f}")
        print(f"Remaining bankroll: ${trader.bankroll:.2f}\n")

if __name__ == "__main__":
    run_live_signals()