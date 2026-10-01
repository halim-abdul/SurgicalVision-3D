from __future__ import annotations

import torch
from torch import nn


def train_epoch(model: nn.Module, loader, optimizer: torch.optim.Optimizer, device: torch.device) -> float:
    model.train()
    total_loss = 0.0
    total_steps = 0
    criterion = nn.CrossEntropyLoss()
    for clips, labels in loader:
        clips, labels = clips.to(device), labels.to(device)
        optimizer.zero_grad(set_to_none=True)
        logits = model(clips)
        loss = criterion(logits.flatten(0, 1), labels.flatten())
        loss.backward()
        nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()
        total_loss += float(loss.detach())
        total_steps += 1
    return total_loss / max(total_steps, 1)
