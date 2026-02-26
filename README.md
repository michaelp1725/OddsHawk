# OddsHawk - NBA Polymarket Paper Trading Bot

Quantitative NBA player prop modeling for prediction market paper trading. OddsHawk simulates trades on Polymarket by analyzing player performance, computing probabilities, and using risk management techniques like the fractional Kelly criterion and correlated parlay Monte Carlo simulations.

---

## Features

- Logistic Regression baseline model
- XGBoost gradient boosted trees
- Probability calibration for improved model confidence
- Historical NBA data support (2005–present)
- Correlated parlay Monte Carlo simulations via PyTorch
- Fractional Kelly position sizing for bankroll management
- Polymarket CLOB API integration for live orderbook data
- Polymarket Subgraph queries for historical market data
- Paper trading only — no real money execution

---

## Data

The project is trained on historical NBA statistics from the following CSVs:

- `Games.csv`
- `PlayerStatistics.csv`
- `PlayerStatisticsAdvanced.csv`
- `TeamStatistics.csv`

**Source:** [NBA statistics Kaggle dataset](https://www.kaggle.com/datasets/nathanlauga/nba-games) (publicly available).

> Place all CSVs in `data/raw/`. Do **not** commit them to Git if they are large. `.gitignore` is already set up to exclude `data/raw/*`.

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd OddsHawk

# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate on Mac/Linux
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate

# Install Project Dependencies
pip install -r requirements.txt

# Confirm the environment is active and dependencies are installed
python3 -m pip list