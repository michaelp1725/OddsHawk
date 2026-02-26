import requests

def fetch_markets(market_ids):
    """
    Fetch market info from Polymarket for the given market IDs.
    """
    markets = []
    for market_id in market_ids:
        try:
            url = f"https://api.polymarket.com/markets/{market_id}"
            resp = requests.get(url)
            resp.raise_for_status()
            markets.append(resp.json())
        except requests.HTTPError as e:
            print(f"[CLOB] Failed to fetch market {market_id}: {e}")
    return markets