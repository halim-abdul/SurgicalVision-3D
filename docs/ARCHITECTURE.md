# Architecture

SurgicalVision-3D separates **perception**, **geometry**, **decision logic**, and **evaluation**.

## Data plane
RGB/stereo video, calibration metadata and hyperspectral cubes are transformed into tensors plus provenance metadata. No module assumes that patient identifiers are available.

## Perception plane
- temporal phase recognition;
- semantic/multi-label segmentation;
- tissue classification from spectral-spatial context;
- stereo disparity/depth.

## Geometry plane
Calibrated depth + segmentation create masked point clouds and surfaces. Registration provides temporal alignment and change estimates.

## Decision plane
A conservative rule/decision-tree layer consumes confidence, calibration validity, blur/saturation indicators, disparity coverage and geometric consistency. Invalid states are routed to `REJECT`, `RECALIBRATE`, `RECAPTURE` or `REVIEW` rather than silently producing a confident output.

## Evaluation plane
Metrics are grouped by task, but all experiments should report data split, preprocessing, seed and uncertainty.
