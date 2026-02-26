def fractional_kelly(prob, odds, fraction=0.25):
    """
    Compute fractional Kelly bet size.

    prob: probability of winning (0-1)
    odds: decimal odds
    fraction: fraction of Kelly to use (default 0.25)
    """
    b = odds - 1
    kelly = (prob * b - (1 - prob)) / b
    return max(kelly * fraction, 0)