from __future__ import annotations

import numpy as np


def synthetic_laparoscopic_frame(height: int = 256, width: int = 256, seed: int = 11711) -> np.ndarray:
    """Generate a non-clinical RGB fixture resembling soft illumination and tool-like edges."""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[:height, :width]
    radial = np.sqrt(((xx-width/2)/(width/2))**2 + ((yy-height/2)/(height/2))**2)
    base = np.clip(1-radial,0,1)
    image = np.stack([0.55+0.25*base,0.18+0.12*base,0.16+0.10*base],axis=-1)
    image += rng.normal(0,0.02,image.shape)
    image = np.clip(image,0,1)
    # tool-like neutral diagonal
    for offset in range(-3,4):
        y=np.arange(height); x=(0.25*width + 0.65*y + offset).astype(int)
        valid=(x>=0)&(x<width); image[y[valid],x[valid],:]=0.65
    return (image*255).astype(np.uint8)


def synthetic_depth_surface(height: int = 128, width: int = 160) -> np.ndarray:
    yy,xx=np.mgrid[:height,:width]
    return (0.35 + 0.025*np.sin(xx/13.0)*np.cos(yy/11.0)).astype(np.float32)


def corrupt_image(image: np.ndarray, mode: str, severity: float = 0.5) -> np.ndarray:
    out=image.astype(np.float32).copy()
    if mode == "brightness":
        out *= 1.0 + severity
    elif mode == "noise":
        rng=np.random.default_rng(7); out += rng.normal(0,35*severity,out.shape)
    elif mode == "saturation":
        out[out > np.quantile(out,1-severity*0.2)] = 255
    else:
        raise ValueError(f"unknown corruption: {mode}")
    return np.clip(out,0,255).astype(np.uint8)
