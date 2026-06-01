# Roadmap

This project is being revived from a legacy competition codebase into a more reproducible and maintainable open-source reference for LiDAR BEV perception.

## Near-Term Maintenance

- Document the original data-processing pipeline from raw point-cloud CSV files to BEV-style training images.
- Add a Docker environment that captures the legacy Python, TensorFlow, tensorpack, and CUDA assumptions.
- Add CI smoke tests for data conversion scripts using the included sample data.
- Clarify dataset availability, missing model weights, and expected retraining steps.
- Translate key reproduction notes into English while preserving the original Chinese instructions.

## Reproducibility

- Provide a minimal end-to-end sample workflow using `sample_train_data/`.
- Add checks for VOC and COCO annotation conversion outputs.
- Record known dependency versions and any required patches for modern systems.
- Document expected input/output directories for training and inference scripts.

## Modernization

- Evaluate whether to keep the original TensorFlow/tensorpack implementation as the canonical legacy baseline.
- Add a separate modern baseline only if it can be validated against the original preprocessing workflow.
- Improve issue triage, pull-request review, release notes, and maintenance automation with Codex/API-assisted workflows.

## Non-Goals

- This repository will not redistribute the full competition dataset.
- This repository will not claim that the missing original model weights are recoverable.
- Modern rewrites should not replace the documented legacy workflow until their behavior is verified.
