# Exception Handling Decision Tree

The decision layer is **research quality-control**, not a clinical decision system.

```mermaid
flowchart TD
A[Input frame/cube/stereo pair] --> B{Calibration present?}
B -- No --> R1[RECALIBRATE]
B -- Yes --> C{Epipolar error <= 1 px?}
C -- No --> R1
C -- Yes --> D{Spectral values finite?}
D -- No --> R2[REJECT]
D -- Yes --> E{Severe saturation/blur?}
E -- Yes --> R3[RECAPTURE]
E -- No --> F{Valid depth >= 40%?}
F -- No --> R2
F -- Yes --> G{Stereo consistency >= 60%?}
G -- No --> R4[REVIEW]
G -- Yes --> H{Model confidence >= 0.55?}
H -- No --> R4
H -- Yes --> R5[ACCEPT research output]
```

## Why explicit routing?
A numerical model can return a prediction even when the acquisition is invalid. The tree makes such assumptions visible and testable. Thresholds are engineering defaults for experiments, not clinically validated values.
