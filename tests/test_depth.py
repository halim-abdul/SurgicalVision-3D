import numpy as np

from surgicalvision3d.stereo.depth import disparity_to_depth


def test_disparity_depth_relation() -> None:
    d=np.array([[10.0,20.0,0.0]],dtype=np.float32)
    z=disparity_to_depth(d, focal_px=500, baseline_m=0.05)
    assert np.isclose(z[0,0],2.5)
    assert np.isclose(z[0,1],1.25)
    assert np.isnan(z[0,2])
