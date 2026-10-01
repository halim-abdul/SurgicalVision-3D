# Surgical Phase Recognition

## Objective
Estimate the operative workflow state from a temporal clip rather than a single frame. The baseline uses a CNN frame encoder and bidirectional GRU, while the interfaces permit ViT/Transformer replacements.

## Failure situations to stratify
- smoke, blood, blur or specular highlights;
- instrument absence or sudden camera motion;
- uncommon phase ordering;
- long idle periods;
- transitions near clip boundaries;
- domain shift across devices/sites.

## Research evaluation
Report frame accuracy, macro-F1, balanced accuracy, per-phase recall, confusion matrix, transition rate and temporal edit-style errors. Do not interpret phase predictions as clinical instructions.

## Ablations
1. frame-only vs temporal;
2. uni- vs bidirectional sequence model;
3. clip length;
4. class-balanced objective;
5. temporal smoothing after logits;
6. calibration under corruption severity.
