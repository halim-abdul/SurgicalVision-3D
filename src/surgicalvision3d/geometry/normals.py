from __future__ import annotations

import numpy as np


def depth_normals(depth: np.ndarray, fx: float, fy: float) -> np.ndarray:
    """Approximate camera-space normals from depth gradients."""
    dzdy, dzdx = np.gradient(depth.astype(np.float32))
    nx = -dzdx * fx
    ny = -dzdy * fy
    nz = np.ones_like(depth)
    n = np.stack([nx, ny, nz], axis=-1)
    norm = np.linalg.norm(n, axis=-1, keepdims=True)
    return n / np.maximum(norm, 1e-8)
