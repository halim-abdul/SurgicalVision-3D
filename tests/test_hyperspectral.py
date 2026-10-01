import numpy as np
import torch

from surgicalvision3d.hyperspectral.model import SpectralSpatialNet
from surgicalvision3d.hyperspectral.preprocess import reflectance_calibration


def test_spectral_model_shape() -> None:
    x = torch.randn(3, 1, 31, 16, 16)
    assert SpectralSpatialNet(4)(x).shape == (3, 4)


def test_reflectance_is_finite() -> None:
    raw=np.ones((4,4,5))*5; white=np.ones_like(raw)*10; dark=np.zeros_like(raw)
    out=reflectance_calibration(raw, white, dark)
    assert np.isfinite(out).all()
