from __future__ import annotations

import numpy as np


def reject_depth_outliers(points: np.ndarray, z_limits: tuple[float, float] = (0.02, 2.0)) -> np.ndarray:
    lo, hi = z_limits
    keep = np.isfinite(points).all(1) & (points[:, 2] >= lo) & (points[:, 2] <= hi)
    return points[keep]


def voxel_downsample_numpy(points: np.ndarray, voxel: float = 0.002) -> np.ndarray:
    if len(points) == 0:
        return points
    keys = np.floor(points / voxel).astype(np.int64)
    _, idx = np.unique(keys, axis=0, return_index=True)
    return points[np.sort(idx)]
