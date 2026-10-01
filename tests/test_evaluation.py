import numpy as np

from surgicalvision3d.evaluation.calibration import expected_calibration_error
from surgicalvision3d.evaluation.bootstrap import bootstrap_mean_ci


def test_ece_bounds() -> None:
    ece=expected_calibration_error(np.array([0.2,0.8,0.9]),np.array([0,1,1],dtype=bool),bins=5)
    assert 0 <= ece <= 1


def test_bootstrap_ci_order() -> None:
    m,lo,hi=bootstrap_mean_ci(np.array([1,2,3,4,5.]),samples=200)
    assert lo <= m <= hi
