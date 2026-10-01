# Geometry Failure Catalogue

| Situation | Signal | Action |
|---|---|---|
| depth holes | low valid fraction | reject/recapture |
| calibration drift | epipolar residual rises | recalibrate |
| specular region | unstable disparity | mask or review |
| segmentation leak | points outside plausible ROI | reject mask/geometry |
| excessive depth | implausible Z range | unit/calibration check |
| rigid alignment fails | high residual | try robust/non-rigid method |
| sparse cloud | low point count | defer surface reconstruction |
