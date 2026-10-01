from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import cv2
import numpy as np
import torch
from torch.utils.data import Dataset


@dataclass(frozen=True)
class PhaseFrame:
    path: Path
    label: int


class PhaseClipDataset(Dataset):
    """Create fixed-length temporal clips from ordered frame metadata."""

    def __init__(self, frames: Sequence[PhaseFrame], clip_length: int = 16, size: tuple[int, int] = (224, 224)) -> None:
        self.frames = list(frames)
        self.clip_length = clip_length
        self.size = size

    def __len__(self) -> int:
        return max(0, len(self.frames) - self.clip_length + 1)

    def _load(self, path: Path) -> torch.Tensor:
        image = cv2.imread(str(path), cv2.IMREAD_COLOR)
        if image is None:
            raise FileNotFoundError(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, self.size[::-1], interpolation=cv2.INTER_AREA)
        arr = image.astype(np.float32) / 255.0
        return torch.from_numpy(arr).permute(2, 0, 1)

    def __getitem__(self, index: int) -> tuple[torch.Tensor, torch.Tensor]:
        clip = self.frames[index:index + self.clip_length]
        x = torch.stack([self._load(f.path) for f in clip])
        y = torch.tensor([f.label for f in clip], dtype=torch.long)
        return x, y
