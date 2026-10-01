import torch

from surgicalvision3d.phase.model import PhaseRecognitionModel


def test_phase_model_shape() -> None:
    model = PhaseRecognitionModel(num_phases=7)
    x = torch.randn(2, 4, 3, 64, 64)
    y = model(x)
    assert y.shape == (2, 4, 7)
