# Contributing

Thanks for helping maintain this legacy 3D point-cloud segmentation reference. The goal is to improve reproducibility and documentation without losing the original competition workflow.

## Good First Contributions

- Improve setup and reproduction documentation.
- Add Docker or environment files for the legacy training stack.
- Add smoke tests for data conversion scripts using `sample_train_data/`.
- Translate existing Chinese reproduction notes into English.
- Report missing dependency versions, broken paths, or unclear assumptions.

## Opening Issues

Please include:

- What you were trying to run.
- Your operating system, Python version, CUDA version, and TensorFlow/tensorpack versions.
- The exact command and error message.
- Whether you used the sample data or your own dataset.

Do not attach private or competition-restricted datasets unless you have the right to share them.

## Pull Requests

Please keep changes small and focused. For code changes, include a short note describing:

- The affected script or workflow.
- The input data used for validation.
- The command used to verify the change.
- Any behavior differences from the original competition implementation.

Avoid broad refactors unless they are required for a reproducibility or maintenance task.

## Data and Weights

The original full competition dataset is not redistributed here, and the original released model-weight link is no longer valid. Contributions should assume that users may need to retrain models or adapt the scripts to their own permitted data.
