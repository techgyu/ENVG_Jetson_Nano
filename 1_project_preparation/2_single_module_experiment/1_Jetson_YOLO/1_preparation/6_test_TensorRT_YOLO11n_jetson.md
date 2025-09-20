# 2025-09-19 | Jetson Nano TensorRT 사용 실험

---

## 1. Docker 컨테이너 시작
```bash
sudo docker start jetson_yolo11 # 중지된 컨테이너를 다시 시작
```

## 2. Docker 컨테이너에 접속
```bash
sudo docker exec -it jetson_yolo11 bash # 실행 중인 컨테이너에 bash 셀로 접속(컨테이너 내부
```

## 3. Jetson Nano stats 애플리케이션 실행 (선택 사항)
```bash
jtop
```

## 4. Jetson Nano에서 ultralytics의 위치
```bash

## 5. YOLO11n TensorRT 모델 테스트
```python
from ultralytics import YOLO

# Load a YOLO11n PyTorch model
model = YOLO("yolo11n.pt")

# Export the model to TensorRT
model.export(format="engine")  # creates 'yolo11n.engine'

# Load the exported TensorRT model
trt_model = YOLO("yolo11n.engine")

# Run inference
results = trt_model("https://ultralytics.com/images/bus.jpg")
```

# 2025-09-20 | Jetson Nano TensorRT 실행 오류

```
root@dbe86e6a1b08:/workspace/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation# python3 test_yolo11n_tensorRT.py
Illegal instruction (core dumped)
```

## 1. 원인 분석: 아키텍처 불일치, 라이브러리 호환성 문제, 빌드 오류

## 2. numpy 버전 확인
```bash
pip3 show numpy
``` 

**출력 결과**
```
_preparation# pip3 show numpy
Name: numpy
Version: 1.19.5
Summary: NumPy is the fundamental package for array computing with Python.
Home-page: https://www.numpy.org
Author: Travis E. Oliphant et al.
Author-email:
License: BSD
Location: /usr/local/lib/python3.8/dist-packages
Requires:
Required-by: contourpy, coremltools, h5py, matplotlib, ml-dtypes, onnx, onnxruntime-gpu, opencv-python-headless, openvino, scikit-learn, scipy, tensorboard, tensorflow-cpu-aws, tensorflow-hub, torchvision, ultralytics, ultralytics-thop
root@dbe86e6a1b08:/workspace/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation#
```

## 3. torchm tesorrt ultralytics 버전 확인
```bash
python3 -c "import torch; print(torch.__version__)"
python3 -c "import tensorrt; print(tensorrt.__version__)"
python3 -c "import ultralytics; print(ultralytics.__version__)"
```

**출력 결과**
```bash
root@dbe86e6a1b08:/workspace/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation# python3 -c "import torch; print(torch.__version__)"
Illegal instruction (core dumped)
root@dbe86e6a1b08:/workspace/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation# python3 -c "import tensorrt; print(tensorrt.__version__)"
8.2.0.6
root@dbe86e6a1b08:/workspace/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation# python3 -c "import ultralytics; print(ultralytics.__version__)" 
Illegal instruction (core dumped)
root@dbe86e6a1b08:/workspace/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation#
```

## 4. 컨테이너에서 Pytorch Ultralytics 삭제
```bash
pip3 uninstall torch torchvision torchaudio ultralytics
```

## 5. Jetson Nano 공식 PyTorch wheel 설치
```bash
pip3 install --upgrade pip
pip3 install numpy==1.19.5
pip3 install torch==1.10.0 torchvision==0.11.1 -f https://developer.download.nvidia.com/compute/redist/jp/v46
```

## 6. PyTorch wheel 설치 확인
```bash
python3 -c "import torch; print(torch.__version__)"
python3 -c "import torchvision; print(torchvision.__version__)"
```

## 7. 다시 삭제
```bash
pip3 uninstall torch torchvision torchaudio -y
```

## 8. 재 확인
```bash
pip3 list | grep torch
```

## 9. 캐시 삭제
```bash
pip3 cache purge
```
**출력 결과**
```bash
root@dbe86e6a1b08:/workspace/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation# pip3 cache purge
Files removed: 33 (100.3 MB)
```

## 10. PyTorch 및 torchvision 재설치
```bash
pip3 install torch==1.10.0 torchvision==0.11.1 -f https://developer.download.nvidia.com/compute/redist/jp/v46
```

**제거 및 설치 로그**
```bash
root@dbe86e6a1b08:/workspace/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation# pip3 uninstall torch torchvision torchaudio -y
Found existing installation: torch 1.10.0
Uninstalling torch-1.10.0:
  Successfully uninstalled torch-1.10.0
Found existing installation: torchvision 0.11.1
Uninstalling torchvision-0.11.1:
  Successfully uninstalled torchvision-0.11.1
WARNING: Skipping torchaudio as it is not installed.
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
root@dbe86e6a1b08:/workspace/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation# pip3 list | grep torch
root@dbe86e6a1b08:/workspace/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation# pip3 cache purge
Files removed: 33 (100.3 MB)
root@dbe86e6a1b08:/workspace/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation# pip3 install torch==1.10.0 torchvision==0.11.1 -f https://developer.download.nvidia.com/compute/redist/jp/v46
Looking in links: https://developer.download.nvidia.com/compute/redist/jp/v46
Collecting torch==1.10.0
  Downloading torch-1.10.0-cp38-cp38-manylinux2014_aarch64.whl.metadata (24 kB)
Collecting torchvision==0.11.1
  Downloading torchvision-0.11.1-cp38-cp38-manylinux2014_aarch64.whl.metadata (8.8 kB)
Requirement already satisfied: typing-extensions in /usr/local/lib/python3.8/dist-packages (from torch==1.10.0) (4.13.2)
Requirement already satisfied: numpy in /usr/local/lib/python3.8/dist-packages (from torchvision==0.11.1) (1.19.5)
Requirement already satisfied: pillow!=8.3.0,>=5.3.0 in /usr/local/lib/python3.8/dist-packages (from torchvision==0.11.1) (10.4.0)
Downloading torch-1.10.0-cp38-cp38-manylinux2014_aarch64.whl (50.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 50.8/50.8 MB 23.2 MB/s eta 0:00:00
Downloading torchvision-0.11.1-cp38-cp38-manylinux2014_aarch64.whl (14.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 14.7/14.7 MB 27.0 MB/s eta 0:00:00
Installing collected packages: torch, torchvision
Successfully installed torch-1.10.0 torchvision-0.11.1
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
root@dbe86e6a1b08:/workspace/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation#
```

## 11. 버전 재확인
```bash
python3 -c "import torch; print(torch.__version__)"
python3 -c "import torchvision; print(torchvision.__version__)"
```

**동일 증상 지속**
```bash
root@dbe86e6a1b08:/workspace/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation# python3 -c "import torch; print(torch.__version__)"
Illegal instruction (core dumped)
root@dbe86e6a1b08:/workspace/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation# python3 -c "import torchvision; print(torchvision.__version__)"
Illegal instruction (core dumped)
root@dbe86e6a1b08:/workspace/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation#
```
## 13. 다른 방법으로 버전 확인
```bash
python3
```
```python
import torch
print(torch.__version__)
```

## 14. 직접 확인
```bash
pip3 show torch
pip3 show torchvision
```
**출력 결과**
```bash
root@dbe86e6a1b08:/workspace/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation# pip3 show torch
Name: torch
Version: 1.10.0
Summary: Tensors and Dynamic neural networks in Python with strong GPU acceleration
Home-page: https://pytorch.org/
Author: PyTorch Team
Author-email: packages@pytorch.org
License: BSD-3
Location: /usr/local/lib/python3.8/dist-packages
Requires: typing-extensions
Required-by: torchvision, ultralytics-thop
root@dbe86e6a1b08:/workspace/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation# pip3 show torchvision
Name: torchvision
Version: 0.11.1
Summary: image and video datasets and models for torch deep learning
Home-page: https://github.com/pytorch/vision
Author: PyTorch Core Team
Author-email: soumith@pytorch.org
License: BSD
Location: /usr/local/lib/python3.8/dist-packages
Requires: numpy, pillow, torch
Required-by:
root@dbe86e6a1b08:/workspace/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation# python3 --version
Python 3.8.0
root@dbe86e6a1b08:/workspace/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation#
```

## 16. 컨테이너 삭제 후 재생성으로 결론 