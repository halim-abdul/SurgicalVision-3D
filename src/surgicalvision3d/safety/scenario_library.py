from __future__ import annotations

from .decision_tree import SceneQuality


def canonical_scenarios() -> dict[str, SceneQuality]:
    return {
        "healthy": SceneQuality(),
        "missing_calibration": SceneQuality(calibration_present=False),
        "calibration_drift": SceneQuality(epipolar_error_px=2.4),
        "blurred_frame": SceneQuality(blur_score=0.91),
        "spectral_corruption": SceneQuality(spectral_finite_fraction=0.8),
        "depth_holes": SceneQuality(valid_depth_fraction=0.18),
        "stereo_mismatch": SceneQuality(lr_consistency=0.35),
        "low_confidence_models": SceneQuality(segmentation_confidence=0.43, phase_confidence=0.48),
    }
