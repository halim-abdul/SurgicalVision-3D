from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Decision(str, Enum):
    ACCEPT = "accept"
    REVIEW = "review"
    RECAPTURE = "recapture"
    RECALIBRATE = "recalibrate"
    REJECT = "reject"


@dataclass(frozen=True)
class SceneQuality:
    calibration_present: bool = True
    epipolar_error_px: float = 0.0
    blur_score: float = 0.0
    saturation_fraction: float = 0.0
    valid_depth_fraction: float = 1.0
    lr_consistency: float = 1.0
    segmentation_confidence: float = 1.0
    phase_confidence: float = 1.0
    spectral_finite_fraction: float = 1.0


def decide_scene(q: SceneQuality) -> tuple[Decision, str]:
    """Conservative research-only routing tree for invalid/uncertain inputs."""
    if not q.calibration_present:
        return Decision.RECALIBRATE, "missing calibration metadata"
    if q.epipolar_error_px > 1.0:
        return Decision.RECALIBRATE, "epipolar error exceeds research threshold"
    if q.spectral_finite_fraction < 0.99:
        return Decision.REJECT, "invalid hyperspectral values"
    if q.saturation_fraction > 0.15:
        return Decision.RECAPTURE, "severe saturation"
    if q.blur_score > 0.70:
        return Decision.RECAPTURE, "severe blur"
    if q.valid_depth_fraction < 0.40:
        return Decision.REJECT, "insufficient depth support"
    if q.lr_consistency < 0.60:
        return Decision.REVIEW, "stereo inconsistency"
    if min(q.segmentation_confidence, q.phase_confidence) < 0.55:
        return Decision.REVIEW, "low model confidence"
    return Decision.ACCEPT, "quality gates passed"
