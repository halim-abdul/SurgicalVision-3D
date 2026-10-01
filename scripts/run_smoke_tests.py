from __future__ import annotations

import torch


def main() -> None:
    from surgicalvision3d.phase.model import PhaseRecognitionModel
    from surgicalvision3d.segmentation.unet import UNet

    phase = PhaseRecognitionModel(7).eval()(torch.randn(1, 2, 3, 64, 64))
    seg = UNet(3).eval()(torch.randn(1, 3, 64, 64))
    assert phase.shape == (1, 2, 7)
    assert seg.shape == (1, 3, 64, 64)
    print("smoke tests passed")


if __name__ == "__main__":
    main()
