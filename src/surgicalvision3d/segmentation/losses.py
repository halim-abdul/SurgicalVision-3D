from __future__ import annotations

import torch
from torch import nn
import torch.nn.functional as F


class DiceCrossEntropyLoss(nn.Module):
    def __init__(self, dice_weight: float = 0.5, eps: float = 1e-6) -> None:
        super().__init__()
        self.dice_weight = dice_weight
        self.eps = eps

    def forward(self, logits: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
        ce = F.cross_entropy(logits, target)
        probs = logits.softmax(1)
        one_hot = F.one_hot(target, logits.shape[1]).permute(0, 3, 1, 2).float()
        dims = (0, 2, 3)
        intersect = (probs * one_hot).sum(dims)
        denom = probs.sum(dims) + one_hot.sum(dims)
        dice_loss = 1.0 - ((2 * intersect + self.eps) / (denom + self.eps)).mean()
        return (1 - self.dice_weight) * ce + self.dice_weight * dice_loss
