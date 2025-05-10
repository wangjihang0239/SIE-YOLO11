In this paper, open source datasets HRSID and SSDD are used in the research process.In this thesis, HRSID (High Resolution SAR Images Dataset) is a dataset for the tasks of ship detection, semantic segmentation, and instance segmentation in high-resolution synthetic aperture radar (SAR) images. This project is mainly used for research and development of deep learning based ship detection and segmentation techniques.The main programming language of the HRSID project is Python, which is suitable for data processing and deep learning model development using Python.SSDD (SAR Ship Detection Dataset) is a dataset dedicated to the task of ship detection and segmentation in Synthetic Aperture Radar (SAR) images. dataset for ship target detection. It was produced by the Department of Electrical and Information Engineering at the Naval Aerospace University to provide a standardized platform so that researchers can compare the performance of different algorithms under identical conditions. They are available for download at the address below:

The HRSIFD dataset is available for download at:https:/gitcode.com/gh mirors/hr/HRSlD

The SSDD dataset is available for download at:https://gitcode.com/gh_mirrors/of/Official-SSDD/blob/main/README.md?utm_source=csdn_github_accelerator&isLogin=1

## <div align="center">Documentation</div>

See below for a quickstart install and usage examples, and see our [Docs](https://docs.ultralytics.com/) for full documentation on training, validation, prediction and deployment.

<details open>
<summary>Install</summary>

Pip install the Ultralytics package including all [requirements](https://github.com/ultralytics/ultralytics/blob/main/pyproject.toml) in a [**Python>=3.8**](https://www.python.org/) environment with [**PyTorch>=1.8**](https://pytorch.org/get-started/locally/).

[![PyPI - Version](https://img.shields.io/pypi/v/ultralytics?logo=pypi&logoColor=white)](https://pypi.org/project/ultralytics/) [![Ultralytics Downloads](https://static.pepy.tech/badge/ultralytics)](https://www.pepy.tech/projects/ultralytics) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ultralytics?logo=python&logoColor=gold)](https://pypi.org/project/ultralytics/)

```bash
pip install ultralytics
```

For alternative installation methods including [Conda](https://anaconda.org/conda-forge/ultralytics), [Docker](https://hub.docker.com/r/ultralytics/ultralytics), and Git, please refer to the [Quickstart Guide](https://docs.ultralytics.com/quickstart/).

[![Conda Version](https://img.shields.io/conda/vn/conda-forge/ultralytics?logo=condaforge)](https://anaconda.org/conda-forge/ultralytics) [![Docker Image Version](https://img.shields.io/docker/v/ultralytics/ultralytics?sort=semver&logo=docker)](https://hub.docker.com/r/ultralytics/ultralytics) [![Ultralytics Docker Pulls](https://img.shields.io/docker/pulls/ultralytics/ultralytics?logo=docker)](https://hub.docker.com/r/ultralytics/ultralytics)

</details>

<details open>
<summary>Usage</summary>

### CLI

YOLO may be used directly in the Command Line Interface (CLI) with a `yolo` command:

```bash
yolo predict model=yolo11n.pt source='https://ultralytics.com/images/bus.jpg'
```

`yolo` can be used for a variety of tasks and modes and accepts additional arguments, e.g. `imgsz=640`. See the YOLO [CLI Docs](https://docs.ultralytics.com/usage/cli/) for examples.

### Python

YOLO may also be used directly in a Python environment, and accepts the same [arguments](https://docs.ultralytics.com/usage/cfg/) as in the CLI example above:

```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")

# Train the model
train_results = model.train(
    data="coco8.yaml",  # path to dataset YAML
    epochs=100,  # number of training epochs
    imgsz=640,  # training image size
    device="cpu",  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
)

# Evaluate model performance on the validation set
metrics = model.val()

# Perform object detection on an image
results = model("path/to/image.jpg")
results[0].show()

# Export the model to ONNX format
path = model.export(format="onnx")  # return path to exported model
```

See YOLO [Python Docs](https://docs.ultralytics.com/usage/python/) for more examples.

</details>
