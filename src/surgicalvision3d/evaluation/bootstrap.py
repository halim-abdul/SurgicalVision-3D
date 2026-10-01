from __future__ import annotations

import numpy as np


def bootstrap_mean_ci(values: np.ndarray, samples: int = 2000, confidence: float = 0.95, seed: int = 11711) -> tuple[float, float, float]:
    arr = np.asarray(values, dtype=float)
    rng = np.random.default_rng(seed)
    means = np.array([rng.choice(arr, len(arr), replace=True).mean() for _ in range(samples)])
    alpha = (1.0 - confidence) / 2.0
    return float(arr.mean()), float(np.quantile(means, alpha)), float(np.quantile(means, 1 - alpha))
