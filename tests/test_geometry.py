import numpy as np

from surgicalvision3d.geometry.pointcloud import depth_to_points
from surgicalvision3d.geometry.registration import rigid_transform_svd


def test_backprojection_count() -> None:
    z=np.ones((4,5),dtype=float)
    pts=depth_to_points(z,100,100,2,2)
    assert pts.shape == (20,3)


def test_rigid_identity() -> None:
    p=np.array([[0.,0,0],[1,0,0],[0,1,0],[0,0,1]])
    T=rigid_transform_svd(p,p)
    assert np.allclose(T,np.eye(4),atol=1e-6)
