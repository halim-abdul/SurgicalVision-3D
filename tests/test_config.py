from pathlib import Path

from surgicalvision3d.common.config import load_yaml


def test_base_config_is_mapping() -> None:
    path=Path(__file__).parents[1]/"configs"/"base.yaml"
    cfg=load_yaml(path)
    assert isinstance(cfg,dict)
    assert "seed" in cfg
