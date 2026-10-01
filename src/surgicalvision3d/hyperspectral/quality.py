from __future__ import annotations

import numpy as np


def spectral_quality(cube: np.ndarray, saturation: float = 0.98) -> dict[str, float]:
    if cube.ndim < 2:
        raise ValueError("Expected spatial/spectral array")
    finite = np.isfinite(cube)
    return {
        "finite_fraction": float(finite.mean()),
        "saturation_fraction": float(np.mean(cube >= saturation)),
        "zero_fraction": float(np.mean(cube <= 0.0)),
        "mean_signal": float(np.nanmean(cube)),
        "spectral_std": float(np.nanstd(cube)),
    }
