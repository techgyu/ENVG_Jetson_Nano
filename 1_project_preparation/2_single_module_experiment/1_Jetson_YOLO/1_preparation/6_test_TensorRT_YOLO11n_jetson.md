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

## 4. YOLO11n TensorRT 모델 테스트
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