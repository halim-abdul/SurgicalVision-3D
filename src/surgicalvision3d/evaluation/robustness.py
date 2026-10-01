from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RobustnessResult:
    corruption: str
    severity: float
    metric_name: str
    value: float


def relative_drop(clean: float, corrupted: float, eps: float = 1e-12) -> float:
    return float((clean - corrupted) / max(abs(clean), eps))
