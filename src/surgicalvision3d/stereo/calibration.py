from __future__ import annotations

from dataclasses import dataclass
import numpy as np
import cv2


@dataclass
class StereoCalibration:
    K1: np.ndarray
    D1: np.ndarray
    K2: np.ndarray
    D2: np.ndarray
    R: np.ndarray
    T: np.ndarray
    image_size: tuple[int, int]

    def rectify_maps(self):
        R1, R2, P1, P2, Q, _, _ = cv2.stereoRectify(
            self.K1, self.D1, self.K2, self.D2, self.image_size, self.R, self.T,
            flags=cv2.CALIB_ZERO_DISPARITY, alpha=0,
        )
        m1x, m1y = cv2.initUndistortRectifyMap(self.K1, self.D1, R1, P1, self.image_size, cv2.CV_32FC1)
        m2x, m2y = cv2.initUndistortRectifyMap(self.K2, self.D2, R2, P2, self.image_size, cv2.CV_32FC1)
        return (m1x, m1y), (m2x, m2y), Q


def mean_epipolar_error(points_left: np.ndarray, points_right: np.ndarray, F: np.ndarray) -> float:
    ones = np.ones((len(points_left), 1))
    xl = np.c_[points_left, ones]
    xr = np.c_[points_right, ones]
    lines = (F @ xl.T).T
    num = np.abs(np.sum(lines * xr, axis=1))
    den = np.sqrt(lines[:, 0] ** 2 + lines[:, 1] ** 2) + 1e-12
    return float(np.mean(num / den))
