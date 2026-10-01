from __future__ import annotations

import numpy as np
import cv2


def compute_sgbm(left_gray: np.ndarray, right_gray: np.ndarray, min_disparity: int = 0, num_disparities: int = 128, block_size: int = 5) -> np.ndarray:
    if num_disparities % 16:
        raise ValueError("num_disparities must be divisible by 16")
    matcher = cv2.StereoSGBM_create(
        minDisparity=min_disparity,
        numDisparities=num_disparities,
        blockSize=block_size,
        P1=8 * block_size ** 2,
        P2=32 * block_size ** 2,
        uniquenessRatio=10,
        speckleWindowSize=100,
        speckleRange=2,
        disp12MaxDiff=1,
    )
    return matcher.compute(left_gray, right_gray).astype(np.float32) / 16.0


def disparity_to_depth(disparity: np.ndarray, focal_px: float, baseline_m: float, min_disparity: float = 1e-3) -> np.ndarray:
    valid = disparity > min_disparity
    depth = np.full(disparity.shape, np.nan, dtype=np.float32)
    depth[valid] = focal_px * baseline_m / disparity[valid]
    return depth
