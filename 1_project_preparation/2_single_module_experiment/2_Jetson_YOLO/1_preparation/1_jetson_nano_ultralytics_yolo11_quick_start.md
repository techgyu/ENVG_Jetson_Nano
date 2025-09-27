# 2025-09-19 | Jetson Nano Quick Start Guide: NVIDIA Jetson with Ultralytics YOLO11 문서 확인

[빠른 시작 가이드: Ultralytics YOLO11과 함께하는 NVIDIA Jetson](https://docs.ultralytics.com/ko/guides/nvidia-jetson/#nvidia-jetson-agx-orin-developer-kit-64gb_1)

---

## 1. NVIDIA Jetson이란 무엇입니까?
NVIDIA Jetson은 가속화된 AI(인공 지능) 컴퓨팅을 엣지 장치에 제공하도록 설계된 임베디드 컴퓨팅 보드 시리즈입니다. 이러한 작고 강력한 장치는 NVIDIA의 GPU 아키텍처를 기반으로 구축되었으며 클라우드 컴퓨팅 리소스에 의존할 필요 없이 복잡한 AI 알고리즘과 딥 러닝 모델을 장치에서 직접 실행할 수 있습니다. Jetson 보드는 로봇 공학, 자율 주행 차량, 산업 자동화 및 낮은 지연 시간과 높은 효율성으로 AI 추론을 로컬에서 수행해야 하는 기타 애플리케이션에 자주 사용됩니다. 또한 이러한 보드는 ARM64 아키텍처를 기반으로 하며 기존 GPU 컴퓨팅 장치에 비해 더 낮은 전력으로 실행됩니다.

## 2. NVIDIA Jetson 시리즈 비교
Jetson Orin은 이전 세대에 비해 AI 성능이 크게 향상된 NVIDIA Ampere 아키텍처를 기반으로 하는 NVIDIA Jetson 제품군의 최신 버전입니다. 아래 표는 에코시스템에 있는 몇 가지 Jetson 장치를 비교한 것입니다.

| 모델                        | Jetson AGX Orin 64GB | Jetson Orin NX 16GB | Jetson Orin Nano Super | Jetson AGX Xavier | Jetson Xavier NX | Jetson Nano      |
|-----------------------------|----------------------|---------------------|------------------------|-------------------|------------------|------------------|
| **AI 성능**                 | 275 TOPS             | 100 TOPS            | 67 TOPS                | 32 TOPS           | 21 TOPS          | 472 GFLOPS       |
| **GPU**                     | 2048코어 NVIDIA Ampere 아키텍처 GPU<br>64 Tensor 코어 | 1024코어 NVIDIA Ampere 아키텍처 GPU<br>32 Tensor 코어 | 1024코어 NVIDIA Ampere 아키텍처 GPU<br>32 Tensor 코어 | 512코어 NVIDIA Volta 아키텍처 GPU<br>64 Tensor 코어 | 384코어 NVIDIA Volta 아키텍처 GPU<br>48 Tensor 코어 | 128코어 NVIDIA Maxwell 아키텍처 GPU |
| **GPU 최대 주파수**         | 1.3 GHz              | 918 MHz             | 1020 MHz               | 1377 MHz          | 1100 MHz         | 921 MHz          |
| **CPU**                     | 12코어 NVIDIA Arm Cortex A78AE v8.2 64비트<br>3MB L2 + 6MB L3 | 8코어 NVIDIA Arm Cortex A78AE v8.2 64비트<br>2MB L2 + 4MB L3 | 6코어 Arm Cortex-A78AE v8.2 64비트<br>1.5MB L2 + 4MB L3 | 8코어 NVIDIA Carmel Arm v8.2 64비트<br>8MB L2 + 4MB L3 | 6코어 NVIDIA Carmel Arm v8.2 64비트<br>6MB L2 + 4MB L3 | 쿼드 코어 Arm Cortex-A57 MPCore 프로세서 |
| **CPU 최대 주파수**         | 2.2 GHz              | 2.0 GHz             | 1.7 GHz                | 2.2 GHz           | 1.9 GHz          | 1.43 GHz         |
| **메모리**                  | 64GB 256비트 LPDDR5<br>204.8GB/s | 16GB 128비트 LPDDR5<br>102.4GB/s | 8GB 128비트 LPDDR5<br>102GB/s | 32GB 256비트 LPDDR4x<br>136.5GB/s | 8GB 128비트 LPDDR4x<br>59.7GB/s | 4GB 64비트 LPDDR4<br>25.6GB/s |

## 3. NVIDIA JetPack이란 무엇입니까?
Jetson 모듈에 전원을 공급하는 NVIDIA JetPack SDK는 엔드 투 엔드 가속화된 AI 애플리케이션 구축을 위한 가장 포괄적인 솔루션이며 시장 출시 시간을 단축합니다. JetPack에는 부트 로더, Linux 커널, Ubuntu 데스크톱 환경 및 GPU 컴퓨팅, 멀티미디어, 그래픽 및 컴퓨터 비전 가속화를 위한 완벽한 라이브러리 세트가 포함된 Jetson Linux가 포함되어 있습니다. 또한 호스트 컴퓨터 및 개발자 키트 모두를 위한 샘플, 문서 및 개발자 도구가 포함되어 있으며 스트리밍 비디오 분석을 위한 DeepStream, 로보틱스를 위한 Isaac, 대화형 AI를 위한 Riva와 같은 더 높은 수준의 SDK를 지원합니다.

## 4. NVIDIA Jetson에 JetPack 플래싱
NVIDIA Jetson 장치를 처음 접한 후 가장 먼저 해야 할 일은 NVIDIA JetPack을 장치에 플래싱하는 것입니다. NVIDIA Jetson 장치를 플래싱하는 방법에는 여러 가지가 있습니다.

Jetson Orin Nano 개발자 키트와 같은 공식 NVIDIA 개발 키트를 소유하고 있다면, 이미지를 다운로드하고 JetPack으로 SD 카드를 준비하여 장치를 부팅할 수 있습니다.
다른 NVIDIA 개발 키트를 소유하고 있다면, SDK Manager를 사용하여 JetPack을 장치에 플래시할 수 있습니다.
Seeed Studio reComputer J4012 장치를 소유하고 있다면, JetPack을 포함된 SSD에 플래시할 수 있습니다. Seeed Studio reComputer J1020 v2 장치를 소유하고 있다면, JetPack을 eMMC/SSD에 플래시할 수 있습니다.
NVIDIA Jetson 모듈로 구동되는 다른 타사 장치를 소유하고 있다면, 명령줄 플래싱을 따르는 것이 좋습니다.


## 5. Jetson 장치 기반 JetPack 지원
아래 표는 다양한 NVIDIA Jetson 장치에서 지원하는 NVIDIA JetPack 버전을 강조 표시합니다.

| 장치                | JetPack 4 | JetPack 5 | JetPack 6 |
|---------------------|:---------:|:---------:|:---------:|
| Jetson Nano         |    ✅     |    ❌     |    ❌     |
| Jetson TX2          |    ✅     |    ❌     |    ❌     |
| Jetson Xavier NX    |    ✅     |    ✅     |    ❌     |
| Jetson AGX Xavier   |    ✅     |    ✅     |    ❌     |
| Jetson AGX Orin     |    ❌     |    ✅     |    ✅     |
| Jetson Orin NX      |    ❌     |    ✅     |    ✅     |
| Jetson Orin Nano    |    ❌     |    ✅     |    ✅     |

## 6. Docker로 빠른 시작
NVIDIA Jetson에서 Ultralytics YOLO11을 시작하는 가장 빠른 방법은 Jetson용으로 미리 빌드된 Docker 이미지를 사용하여 실행하는 것입니다. 위의 표를 참조하여 소유한 Jetson 장치에 따라 JetPack 버전을 선택하십시오.


JetPack 4
```bash
t=ultralytics/ultralytics:latest-jetson-jetpack4
sudo docker pull $t && sudo docker run -it --ipc=host --runtime=nvidia $t
```
이 작업이 완료되면 NVIDIA Jetson에서 TensorRT 사용 섹션으로 건너뜁니다.

## 7. NVIDIA Jetson에서 TensorRT 사용
Ultralytics에서 지원하는 모든 모델 내보내기 형식 중에서 TensorRT는 NVIDIA Jetson 장치에서 가장 높은 추론 성능을 제공하므로 Jetson 배포에 가장 적합한 권장 사항입니다. 설정 지침 및 고급 사용법은 전용 TensorRT 통합 가이드를 참조하십시오.

모델을 TensorRT로 변환하고 추론 실행
PyTorch 형식의 YOLO11n 모델이 TensorRT로 변환되어 내보낸 모델로 추론을 실행합니다.

예시

Python
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

## 8. NVIDIA Jetson 사용 시 모범 사례
NVIDIA Jetson을 사용할 때 YOLO11을 실행하는 NVIDIA Jetson에서 최대 성능을 활성화하기 위해 따라야 할 몇 가지 모범 사례가 있습니다.

### 1. 최대 전원 모드 활성화
Jetson에서 최대 전원 모드를 활성화하면 모든 CPU, GPU 코어가 켜집니다.

```bash
sudo nvpmodel -m 0
```
### 2. Jetson 클럭 활성화
Jetson 클럭을 활성화하면 모든 CPU, GPU 코어가 최대 주파수로 클럭됩니다.

```bash
sudo jetson_clocks
```
### 3. Jetson Stats 애플리케이션 설치
jetson stats 애플리케이션을 사용하여 시스템 구성 요소의 온도를 모니터링하고 CPU, GPU, RAM 사용률 보기, 전원 모드 변경, 최대 클럭 설정, JetPack 정보 확인과 같은 기타 시스템 세부 정보를 확인할 수 있습니다.

```bash
sudo apt update
sudo pip install jetson-stats
sudo reboot
jtop
```
---