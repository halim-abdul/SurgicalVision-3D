from __future__ import annotations

import numpy as np


def depth_to_points(depth: np.ndarray, fx: float, fy: float, cx: float, cy: float, mask: np.ndarray | None = None) -> np.ndarray:
    """Back-project a metric depth map into a Nx3 point cloud."""
    h, w = depth.shape
    yy, xx = np.mgrid[:h, :w]
    valid = np.isfinite(depth) & (depth > 0)
    if mask is not None:
        valid &= mask.astype(bool)
    z = depth[valid]
    x = (xx[valid] - cx) * z / fx
    y = (yy[valid] - cy) * z / fy
    return np.column_stack([x, y, z]).astype(np.float32)


def transform_points(points: np.ndarray, T: np.ndarray) -> np.ndarray:
    ones = np.ones((len(points), 1), dtype=points.dtype)
    hom = np.concatenate([points, ones], axis=1)
    return (T @ hom.T).T[:, :3]
