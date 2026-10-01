from __future__ import annotations

import torch
from torch import nn


class FrameEncoder(nn.Module):
    """Compact CNN encoder suitable for research fixtures and ablations."""

    def __init__(self, out_dim: int = 256) -> None:
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, 3, stride=2, padding=1), nn.BatchNorm2d(32), nn.GELU(),
            nn.Conv2d(32, 64, 3, stride=2, padding=1), nn.BatchNorm2d(64), nn.GELU(),
            nn.Conv2d(64, 128, 3, stride=2, padding=1), nn.BatchNorm2d(128), nn.GELU(),
            nn.AdaptiveAvgPool2d(1),
        )
        self.proj = nn.Linear(128, out_dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.proj(self.features(x).flatten(1))


class PhaseRecognitionModel(nn.Module):
    """Frame encoder + bidirectional GRU temporal classifier.

    Input shape: ``[batch, time, 3, height, width]``.
    Output shape: ``[batch, time, num_phases]``.
    """

    def __init__(self, num_phases: int, feature_dim: int = 256, hidden_dim: int = 192) -> None:
        super().__init__()
        self.encoder = FrameEncoder(feature_dim)
        self.temporal = nn.GRU(feature_dim, hidden_dim, batch_first=True, bidirectional=True)
        self.head = nn.Sequential(nn.LayerNorm(hidden_dim * 2), nn.Dropout(0.2), nn.Linear(hidden_dim * 2, num_phases))

    def forward(self, clips: torch.Tensor) -> torch.Tensor:
        b, t, c, h, w = clips.shape
        z = self.encoder(clips.reshape(b * t, c, h, w)).reshape(b, t, -1)
        y, _ = self.temporal(z)
        return self.head(y)
