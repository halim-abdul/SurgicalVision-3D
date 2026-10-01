from __future__ import annotations

import torch
from torch import nn


class SpectralReconstructor(nn.Module):
    """Simple RGB-to-spectral baseline for controlled reconstruction experiments."""

    def __init__(self, bands: int = 31) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(3, 64, 3, padding=1), nn.GELU(),
            nn.Conv2d(64, 128, 3, padding=1), nn.GELU(),
            nn.Conv2d(128, bands, 1),
        )

    def forward(self, rgb: torch.Tensor) -> torch.Tensor:
        return self.net(rgb)
