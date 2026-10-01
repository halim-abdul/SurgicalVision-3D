# Contributing

## Workflow
1. Create a focused feature branch.
2. Add tests and a short method note for research-facing changes.
3. Keep patient-identifiable data out of the repository.
4. Report metrics with dataset split, seed, preprocessing and confidence intervals when applicable.
5. Prefer deterministic synthetic fixtures for tests.

## Code quality
- Python 3.10+
- type hints for public functions
- `ruff` and `pytest`
- functions should separate I/O, numerical kernels and visualization

## Medical-research boundary
This repository is for experimentation and reproducible research. Contributions must not claim clinical validation without evidence from an appropriate study and governance process.
