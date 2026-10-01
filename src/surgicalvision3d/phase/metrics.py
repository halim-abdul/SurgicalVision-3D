from __future__ import annotations

import numpy as np
from sklearn.metrics import accuracy_score, f1_score, balanced_accuracy_score


def phase_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> dict[str, float]:
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "balanced_accuracy": float(balanced_accuracy_score(y_true, y_pred)),
        "macro_f1": float(f1_score(y_true, y_pred, average="macro", zero_division=0)),
    }


def transition_rate(labels: np.ndarray) -> float:
    if labels.size < 2:
        return 0.0
    return float(np.mean(labels[1:] != labels[:-1]))
