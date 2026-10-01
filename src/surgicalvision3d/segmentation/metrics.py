from __future__ import annotations

import torch


def confusion_matrix(pred: torch.Tensor, target: torch.Tensor, num_classes: int) -> torch.Tensor:
    mask = (target >= 0) & (target < num_classes)
    ids = num_classes * target[mask].to(torch.int64) + pred[mask].to(torch.int64)
    return torch.bincount(ids, minlength=num_classes ** 2).reshape(num_classes, num_classes)


def iou_from_confusion(cm: torch.Tensor, eps: float = 1e-8) -> torch.Tensor:
    tp = cm.diag().float()
    fp = cm.sum(0).float() - tp
    fn = cm.sum(1).float() - tp
    return tp / (tp + fp + fn + eps)


def dice_from_confusion(cm: torch.Tensor, eps: float = 1e-8) -> torch.Tensor:
    tp = cm.diag().float()
    fp = cm.sum(0).float() - tp
    fn = cm.sum(1).float() - tp
    return 2 * tp / (2 * tp + fp + fn + eps)
