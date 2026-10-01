# Failure Scenarios and Expected Routing

| Scenario | Detection signal | Route | Research response |
|---|---|---|---|
| missing calibration | no calibration metadata | RECALIBRATE | stop metric depth |
| calibration drift | high epipolar residual | RECALIBRATE | reacquire calibration |
| severe motion blur | high blur risk | RECAPTURE | exclude frame/clip |
| glare/saturation | saturated pixel fraction | RECAPTURE | improve acquisition/robustness |
| invalid HSI values | low finite fraction | REJECT | inspect sensor/calibration |
| depth holes | low valid-depth fraction | REJECT | no surface reconstruction |
| stereo mismatch | low L/R consistency | REVIEW | inspect rectification/motion |
| low semantic confidence | calibrated confidence low | REVIEW | human/research inspection |
| all gates healthy | metrics in range | ACCEPT | permit downstream research analysis |

The repository deliberately avoids rules that diagnose patients or direct surgical actions.
