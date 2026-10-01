from __future__ import annotations

import numpy as np
from scipy.spatial import cKDTree


def chamfer_distance(a: np.ndarray, b: np.ndarray) -> float:
    if len(a) == 0 or len(b) == 0:
        return float("nan")
    da, _ = cKDTree(b).query(a, k=1)
    db, _ = cKDTree(a).query(b, k=1)
    return float(np.mean(da ** 2) + np.mean(db ** 2))


def hausdorff95(a: np.ndarray, b: np.ndarray) -> float:
    if len(a) == 0 or len(b) == 0:
        return float("nan")
    da, _ = cKDTree(b).query(a, k=1)
    db, _ = cKDTree(a).query(b, k=1)
    return float(max(np.percentile(da, 95), np.percentile(db, 95)))
