from surgicalvision3d.safety.decision_tree import SceneQuality, Decision, decide_scene


def test_healthy_scene_accepts() -> None:
    assert decide_scene(SceneQuality())[0] == Decision.ACCEPT


def test_missing_calibration_routes_recalibrate() -> None:
    assert decide_scene(SceneQuality(calibration_present=False))[0] == Decision.RECALIBRATE


def test_depth_failure_rejects() -> None:
    assert decide_scene(SceneQuality(valid_depth_fraction=0.1))[0] == Decision.REJECT
