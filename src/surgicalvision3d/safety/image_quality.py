from __future__ import annotations

import cv2
import numpy as np


def variance_of_laplacian(image: np.ndarray) -> float:
    gray = image if image.ndim == 2 else cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return float(cv2.Laplacian(gray, cv2.CV_64F).var())


def saturation_fraction(image: np.ndarray, low: int = 3, high: int = 252) -> float:
    arr = np.asarray(image)
    return float(np.mean((arr <= low) | (arr >= high)))


def normalized_blur_risk(image: np.ndarray, reference: float = 150.0) -> float:
    sharpness = variance_of_laplacian(image)
    return float(np.clip(1.0 - sharpness / reference, 0.0, 1.0))
