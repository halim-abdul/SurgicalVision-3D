from __future__ import annotations

import numpy as np


def shifted_pair(height: int = 160, width: int = 240, shift: int = 8, seed: int = 7) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    left = (rng.random((height, width)) * 255).astype(np.uint8)
    right = np.zeros_like(left)
    right[:, :-shift] = left[:, shift:]
    return left, right
