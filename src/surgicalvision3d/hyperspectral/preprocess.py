from __future__ import annotations

import numpy as np


def reflectance_calibration(raw: np.ndarray, white: np.ndarray, dark: np.ndarray, eps: float = 1e-6) -> np.ndarray:
    """Convert raw HSI values to approximate reflectance using white/dark references."""
    calibrated = (raw.astype(np.float32) - dark) / (white - dark + eps)
    return np.clip(calibrated, 0.0, 1.5)


def standardize_spectra(cube: np.ndarray, eps: float = 1e-6) -> np.ndarray:
    mean = cube.mean(axis=-1, keepdims=True)
    std = cube.std(axis=-1, keepdims=True)
    return (cube - mean) / (std + eps)


def drop_bands(cube: np.ndarray, indices: list[int]) -> np.ndarray:
    keep = np.ones(cube.shape[-1], dtype=bool)
    keep[indices] = False
    return cube[..., keep]
