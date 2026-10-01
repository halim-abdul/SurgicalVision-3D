# Instrument and Anatomy Segmentation

The segmentation module provides a transparent U-Net baseline, Dice+cross-entropy objective, per-class metrics and mask plausibility checks.

## Scenarios to test
- thin instruments and small landmarks;
- specular highlights and smoke;
- partial instrument entry at the image boundary;
- motion blur;
- class imbalance;
- unseen instrument appearance;
- anatomy visually similar to foreground tools.

## Error propagation
Segmentation is not isolated from geometry: false foreground pixels can create spurious 3D points, while missing boundaries can bias surface measurements. Geometry experiments should therefore compare reconstruction metrics under ground-truth-like masks, predicted masks and deliberately corrupted masks.
