# Data Card

No patient data is distributed with SurgicalVision-3D.

## Bundled/Generated data
The repository can generate deterministic synthetic RGB frames, depth surfaces and stereo fixtures for tests, diagrams and notebooks. These are not intended to emulate the clinical distribution faithfully.

## External medical datasets
Users must separately obtain data under the relevant license, consent/governance rules and institutional approvals. Keep identifiers, raw patient data and credentials outside version control.

## Split discipline
For procedure/video data, prefer splitting at the patient/procedure level rather than randomly at the frame level to reduce leakage. Record the exact split manifest and preprocessing version.
