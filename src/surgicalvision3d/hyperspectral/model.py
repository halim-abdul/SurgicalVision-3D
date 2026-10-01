from __future__ import annotations

import torch
from torch import nn


class SpectralSpatialNet(nn.Module):
    """3D spectral-spatial CNN for patch-wise tissue classification.

    Input shape: [B, 1, bands, H, W].
    """

    def __init__(self, num_classes: int, channels: int = 24) -> None:
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv3d(1, channels, kernel_size=(7, 3, 3), padding=(3, 1, 1)), nn.BatchNorm3d(channels), nn.GELU(),
            nn.Conv3d(channels, channels * 2, kernel_size=(5, 3, 3), padding=(2, 1, 1)), nn.BatchNorm3d(channels * 2), nn.GELU(),
            nn.AdaptiveAvgPool3d(1),
        )
        self.head = nn.Linear(channels * 2, num_classes)

    def forward(self, cube: torch.Tensor) -> torch.Tensor:
        return self.head(self.features(cube).flatten(1))
