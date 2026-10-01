# HSI Experiment Matrix

| Experiment | Variable | Expected observation |
|---|---|---|
| Band dropout | 0/2/5/10 bands | graceful degradation or identified failure |
| Illumination scaling | 0.6–1.4 | invariance after calibration |
| Gaussian sensor noise | multiple SNRs | confidence should decrease |
| Spatial blur | kernel width | local classification may degrade |
| Spectral shift | band index offset | strong sensitivity indicates calibration risk |
| RGB-to-HSI reconstruction | wavelength RMSE/SAM | report spectral angle and per-band error |
