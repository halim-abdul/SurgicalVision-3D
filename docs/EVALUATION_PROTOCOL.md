# Evaluation Protocol

## Always report
- dataset/source and governance status;
- train/validation/test split strategy;
- subject/procedure leakage controls where applicable;
- preprocessing and calibration version;
- random seed and software environment;
- primary metric and confidence interval;
- failure/corruption strata;
- probability calibration when confidence is consumed downstream.

## Task metrics

### Phase recognition
Accuracy, balanced accuracy, macro-F1, per-class recall and temporal transition errors.

### Segmentation
Dice, IoU, per-class metrics, boundary/HD95 when appropriate.

### HSI classification/reconstruction
Macro-F1, AUROC when justified, spectral angle mapper, RMSE and band-wise error.

### Stereo/depth
MAE/RMSE, bad-pixel rate, valid-depth fraction, left-right consistency.

### Geometry
Chamfer distance, HD95, registration residual and point/surface coverage.

A model with strong average accuracy but poor calibration or severe subgroup failure should not be described as robust.
