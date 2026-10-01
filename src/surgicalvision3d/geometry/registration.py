from __future__ import annotations

import numpy as np


def rigid_transform_svd(source: np.ndarray, target: np.ndarray) -> np.ndarray:
    """Closed-form rigid alignment for paired 3D points."""
    if source.shape != target.shape or source.shape[1] != 3:
        raise ValueError("source and target must have shape [N,3]")
    cs, ct = source.mean(0), target.mean(0)
    H = (source - cs).T @ (target - ct)
    U, _, Vt = np.linalg.svd(H)
    R = Vt.T @ U.T
    if np.linalg.det(R) < 0:
        Vt[-1] *= -1
        R = Vt.T @ U.T
    t = ct - R @ cs
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = t
    return T
