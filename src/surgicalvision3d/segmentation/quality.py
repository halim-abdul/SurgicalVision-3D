from __future__ import annotations

import numpy as np


def mask_quality_flags(mask: np.ndarray, min_fraction: float = 1e-4, max_fraction: float = 0.95) -> dict[str, bool]:
    fraction = float(np.mean(mask > 0))
    return {
        "empty_or_tiny": fraction < min_fraction,
        "implausibly_large": fraction > max_fraction,
        "touches_border": bool(np.any(mask[0]) or np.any(mask[-1]) or np.any(mask[:, 0]) or np.any(mask[:, -1])),
    }
