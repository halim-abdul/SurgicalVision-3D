# Reproducibility

## Minimum experiment record
- Git commit SHA;
- configuration file;
- random seed;
- Python/PyTorch/CUDA versions;
- dataset manifest/version and split policy;
- calibration metadata version;
- preprocessing choices;
- checkpoint hash;
- evaluation command and output metrics.

## Determinism
`seed_everything` seeds Python, NumPy and PyTorch and enables deterministic algorithms where possible. Some GPU kernels or third-party libraries may still vary; document any known nondeterminism.

## CI
GitHub Actions checks Python 3.10/3.11, linting and unit tests. Research notebooks should remain lightweight and avoid embedding private datasets or large binary outputs.
