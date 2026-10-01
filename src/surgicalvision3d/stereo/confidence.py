from __future__ import annotations

import numpy as np


def depth_quality(disparity: np.ndarray, depth: np.ndarray, max_depth_m: float = 2.0) -> dict[str, float]:
    valid_disp = np.isfinite(disparity) & (disparity > 0)
    valid_depth = np.isfinite(depth) & (depth > 0) & (depth < max_depth_m)
    if valid_depth.any():
        median_depth = float(np.nanmedian(depth[valid_depth]))
    else:
        median_depth = float("nan")
    return {
        "positive_disparity_fraction": float(valid_disp.mean()),
        "valid_depth_fraction": float(valid_depth.mean()),
        "median_valid_depth_m": median_depth,
    }


def left_right_consistency(left_disp: np.ndarray, right_disp: np.ndarray, tolerance: float = 1.5) -> float:
    h, w = left_disp.shape
    yy, xx = np.mgrid[:h, :w]
    xr = np.rint(xx - left_disp).astype(int)
    valid = (left_disp > 0) & (xr >= 0) & (xr < w)
    sampled = np.zeros_like(left_disp)
    sampled[valid] = right_disp[yy[valid], xr[valid]]
    consistent = valid & (np.abs(left_disp - sampled) <= tolerance)
    return float(consistent.sum() / max(valid.sum(), 1))
