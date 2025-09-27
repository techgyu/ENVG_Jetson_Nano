# 2025-09-22 | Jetson Nano Edge Detection 관련 라이브러리 버전 확인

---

## 1. Edge Detection용 컨테이너 접속
```bash
sudo docker start jetson_yolo11_v1_EdgeDetection
sudo docker exec -it jetson_yolo11_v1_EdgeDetection bash
```

## 2. Edge Detection 관련 라이브러리 버전 확인
```bash
python3 -c "import cv2; print('OpenCV version:', cv2.__version__)"
python3 -c "import numpy as np; print('NumPy version:', np.__version__)"
python3 -c "import torch; print('PyTorch version:', torch.__version__)"
python3 -c "import torchvision; print('TorchVision version:', torchvision.__version__)"
python3 -c "import PIL; print('Pillow version:', PIL.__version__)"
```

**출력 결과**
```bash
root@55467b5939f6:/workspace# python3 -c "import cv2; print('OpenCV version:', cv2.__version__)"
OpenCV version: 4.12.0
root@55467b5939f6:/workspace# python3 -c "import numpy as np; print('NumPy version:', np.__version__)"
NumPy version: 1.23.5
root@55467b5939f6:/workspace# python3 -c "import torch; print('PyTorch version:', torch.__version__)"
PyTorch version: 1.11.0a0+gitbc2c6ed
root@55467b5939f6:/workspace# python3 -c "import torchvision; print('TorchVision version:', torchvision.__version__)"
TorchVision version: 0.12.0a0+9b5a3fe
root@55467b5939f6:/workspace# python3 -c "import PIL; print('Pillow version:', PIL.__version__)"
Pillow version: 10.4.0
```

- OpenCV version: 4.12.0
- NumPy version: 1.23.5
- PyTorch version: 1.11.0a0+gitbc2c6ed
- TorchVision version: 0.12.0a0+9b5a3fe
- Pillow version: 10.4.0