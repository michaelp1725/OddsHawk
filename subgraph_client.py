import requests
from config import POLYMARKET_SUBGRAPH_URL

def query_subgraph(query):
    response = requests.post(
        POLYMARKET_SUBGRAPH_URL,
        json={"query": query}
    )
    return response.json()