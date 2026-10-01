import torch

from surgicalvision3d.segmentation.unet import UNet
from surgicalvision3d.segmentation.losses import DiceCrossEntropyLoss


def test_unet_shape_and_loss() -> None:
    x = torch.randn(2, 3, 64, 64)
    target = torch.randint(0, 3, (2, 64, 64))
    logits = UNet(3)(x)
    assert logits.shape == (2, 3, 64, 64)
    loss = DiceCrossEntropyLoss()(logits, target)
    assert torch.isfinite(loss)
