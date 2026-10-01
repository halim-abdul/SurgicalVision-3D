# Hyperspectral Tissue Analysis

## Pipeline
1. raw cube + dark/white references;
2. reflectance calibration;
3. wavelength/band validation;
4. spectral-spatial patch extraction;
5. tissue classifier or spectral reconstruction model;
6. uncertainty + corruption stratification.

## Important situations
- saturated pixels;
- missing/dead spectral bands;
- wavelength misregistration;
- low signal-to-noise regions;
- illumination shift;
- specular reflection;
- spatial misalignment between RGB and HSI;
- device-specific spectral response.

A high class probability is insufficient if calibration metadata or spectral quality fails. The safety branch converts these checks into explicit decision states.
