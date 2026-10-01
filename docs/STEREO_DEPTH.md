# Stereo Calibration and Depth

## Core relation
For rectified stereo, approximate metric depth is `Z = f B / d`, with focal length `f` in pixels, baseline `B` in meters and disparity `d` in pixels.

## Quality gates
Before geometric reconstruction, test:
- calibration metadata present;
- epipolar residual below threshold;
- sufficient positive disparity coverage;
- left-right consistency;
- plausible depth range;
- no severe blur/saturation or frame desynchronization.

## Exception situations
A low-disparity textureless surface, reflective tissue, smoke, rapid motion or incorrect rectification can invalidate depth even if a matcher returns numeric values. These conditions are routed through the decision engine instead of being silently converted into 3D geometry.
