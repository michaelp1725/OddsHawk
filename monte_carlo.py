import torch
from config import MONTE_CARLO_SIMS

def simulate_parlay(probs, corr_matrix):
    dist = torch.distributions.MultivariateNormal(
        torch.zeros(len(probs)),
        torch.tensor(corr_matrix, dtype=torch.float32)
    )
    sims = dist.sample((MONTE_CARLO_SIMS,))
    sims = torch.sigmoid(sims)
    outcomes = (sims < torch.tensor(probs)).float()
    joint_prob = outcomes.prod(dim=1).mean().item()
    return joint_prob