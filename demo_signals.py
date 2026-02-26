from clob_client import fetch_markets
from monte_carlo import simulate_parlay
from kelly import fractional_kelly

# === MANUAL MARKET IDS ===
# Paste the Polymarket market IDs you want to track
MARKET_IDS = [
    "slug_or_id_1",
    "slug_or_id_2",
    "slug_or_id_3"
]

print("Fetching live Polymarket markets...")
markets = fetch_markets(MARKET_IDS)

if not markets:
    print("No live markets found.")
else:
    for market in markets:
        name = market.get("name", "Unnamed Market")
        yes_price = market.get("yesPrice", 2.0)
        no_price = market.get("noPrice", 2.0)

        # Example: run Monte Carlo simulation & Kelly calculation
        joint_prob = simulate_parlay([yes_price])  # simplified for demo
        kelly_fraction = fractional_kelly(joint_prob, yes_price)

        print(f"Market: {name}")
        print(f"  Market odds: {yes_price}, EV: {joint_prob}")
        print(f"  Fractional Kelly bet fraction: {kelly_fraction:.3f}")
        print("-" * 40)