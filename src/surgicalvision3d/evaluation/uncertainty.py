from __future__ import annotations

import torch


def predictive_entropy(probabilities: torch.Tensor, eps: float = 1e-8) -> torch.Tensor:
    p = probabilities.clamp_min(eps)
    return -(p * p.log()).sum(dim=-1)


def variation_ratio(probabilities: torch.Tensor) -> torch.Tensor:
    return 1.0 - probabilities.max(dim=-1).values
