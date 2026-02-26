from kelly import fractional_kelly

class PaperTrader:
    def __init__(self, bankroll):
        self.bankroll = bankroll
        self.positions = []

    def place_trade(self, prob, market_prob, odds):
        edge = prob - market_prob
        if edge <= 0:
            return 0
        size = fractional_kelly(prob, odds)
        bet_amount = self.bankroll * size
        self.bankroll -= bet_amount
        self.positions.append(bet_amount)
        return bet_amount