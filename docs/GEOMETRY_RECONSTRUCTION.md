# 3D Laparoscopic Scene Reconstruction

## Pipeline
Calibrated stereo → disparity → depth → segmentation-aware back-projection → point filtering → normals → temporal registration → optional surface reconstruction.

## Research questions
- How much segmentation error transfers to geometric surface error?
- How stable is reconstruction under low-texture stereo regions?
- Can temporal registration reduce frame-wise depth noise without erasing real deformation?
- Which metrics reveal local failures hidden by global averages?

## Non-rigid caveat
Surgical tissue can deform. The included SVD registration is a rigid baseline; deformation-aware models should be evaluated separately rather than assuming a rigid scene.
