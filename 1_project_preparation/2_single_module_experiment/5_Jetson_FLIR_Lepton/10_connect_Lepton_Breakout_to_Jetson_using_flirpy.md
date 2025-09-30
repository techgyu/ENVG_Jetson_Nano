# 2025-09-30 | flirpy를 이용한 Jetson Nano & FLIR Lepton 3.5 연결 실험

---

## 0. 확인사항
- Jetson Nano Expansion Header Tool을 이용해 SPI_2 핀 설정 완료

## 1. 핀맵 연결 상태 확인

| Jetson Nano J41 Pin           | Signal Name      | Breakout Board V2.0 Pin | Signal Name      | 비고                       |
|-------------------------------|------------------|-------------------------|------------------|---------------------------|
|  34                           | GND              | 1                       | GND              | 접지(공통 연결)             |
|  25                           | GND              | 19                      | GND              | 접지(공통 연결)             |
|  2                            | 5V Power         | 2                       | Power in 3~5.5V  | 전원 공급                  |
|  3                            | I2C_2_SDA (I2C1) | 5                       | SDA              | I2C 데이터                  |
|  5                            | I2C_2_SCL (I2C1) | 8                       | SCL              | I2C 클럭                  |
| 13                            | SPI_2_SCK        | 7                       | SPI_CLK          | SPI 클럭                  |
| 37                            | SPI_2_MOSI       | 9                       | SPI_MOSI         | SPI 데이터(마스터→슬레이브)|
| 22                            | SPI_2_MISO       | 12                      | SPI_MISO         | SPI 데이터(슬레이브→마스터)|
| 18                            | SPI_2_CS0        | 10                      | SPI_CS           | SPI 칩 선택               |

## 2. 저항 연결 상태 확인(4.7kΩ)
| Jetson Nano J41 Pin           | Signal Name      | Breakout Board V2.0 Pin | Signal Name      | 비고                       |
|-------------------------------|------------------|-------------------------|------------------|---------------------------|
|  3                            | I2C_2_SDA (I2C1) | 5                       | SDA              | I2C 데이터                  |
|  5                            | I2C_2_SCL (I2C1) | 8                       | SCL              | I2C 클럭                  |

## 3. Jetson Nano Pin Map
[Jetson Nano GPIO Header PINOUT](https://jetsonhacks.com/nvidia-jetson-nano-j41-header-pinout/)
| Pin | Name / 기능         | GPIO      | Pin | Name / 기능         | GPIO      |
|-----|---------------------|-----------|-----|---------------------|-----------|
|  1  | 3.3V Power          |           |  2  | 5V Power            |           |
|  3  | I2C_2_SDA (I2C1)    |           |  4  | 5V Power            |           |
|  5  | I2C_2_SCL (I2C1)    |           |  6  | GND                 |           |
|  7  | AUDIO_MCLK          | gpio216   |  8  | UART_2_TX (ttyTHS1) |           |
|  9  | GND                 |           | 10  | UART_2_RX (ttyTHS1) |           |
| 11  | UART_2_RTS          | gpio50    | 12  | I2S_4_SCLK          | gpio79    |
| 13  | SPI_2_SCK           | gpio14    | 14  | GND                 |           |
| 15  | LCD_TE              | gpio194   | 16  | SPI_2_CS1           | gpio232   |
| 17  | 3.3V Power          |           | 18  | SPI_2_CS0           | gpio15    |
| 19  | SPI_1_MOSI          | gpio16    | 20  | GND                 |           |
| 21  | SPI_1_MISO          | gpio17    | 22  | SPI_2_MISO          | gpio13    |
| 23  | SPI_1_SCK           | gpio18    | 24  | SPI_1_CS0           | gpio19    |
| 25  | GND                 |           | 26  | SPI_1_CS1           | gpio20    |
| 27  | I2C_1_SDA (I2C0)    |           | 28  | I2C_1_SCL (I2C0)    |           |
| 29  | CAM_AF_EN           | gpio149   | 30  | GND                 |           |
| 31  | GPIO_PZ0            | gpio200   | 32  | LCD_BL_PWM          | gpio168   |
| 33  | GPIO_PE6            | gpio38    | 34  | GND                 |           |
| 35  | I2S_4_LRCK          | gpio76    | 36  | UART_2_CTS          | gpio51    |
| 37  | SPI_2_MOSI          | gpio12    | 38  | I2S_4_SDIN          | gpio77    |
| 39  | GND                 |           | 40  | I2S_4_SDOUT         | gpio78    |

## 4. Breakout V2.0 Pin Map
| Pin | Function     | Pin | Function            |
|-----|--------------|-----|---------------------|
|  1  | **GND**      |  2  | **Power in 3~5.5V** |
|  3  | VPROG        |  4  | VCC28               |
|  5  | **SDA**      |  6  | VCC28_IO            |
|  7  | **SPI_CLK**  |  8  | **SCL**             |
|  9  | **SPI_MOSI** | 10  | **SPI_CS**          |
| 11  | GPIO0        | 12  | **SPI_MISO**        |
| 13  | GPIO2        | 14  | GPIO1               |
| 15  | GPIO3/VSYNC  | 16  | VCC12               |
| 17  | RESET_L      | 18  | MASTER_CLK          |
| 19  | **GND**      | 20  | PW_DWN_L            |

## 5. Flirpy 테스트용 Docker 접속
```bash
sudo docker start jetson_yolo11_v1_FLIR
sudo docker exec -it jetson_yolo11_v1_FLIR bash
```

### 2.1 결과 요약
- packing, tensorflowjs 충돌 상태에서, yolov11n 모델을 TensorRT로 변환하는데 성공함.

## 6 flirpy 실험 기록 확인
```bash
pip show flirpy
```
**출력 결과: flirpy 0.3.0 버전이 설치되어 있고, 설치 과정에서 packing, tensorflowjs 충돌 발생하였으나, yolo11n 모델 사용에 이상 없음.**
```bash
Name: flirpy
Version: 0.3.0
Summary: UNKNOWN
Home-page: UNKNOWN
Author: Josh Veitch-Michaelis
Author-email: j.veitchmichaelis@gmail.com
License: MIT
Location: /usr/local/lib/python3.8/dist-packages
Requires: libusb, natsort, numpy, opencv-python-headless, Pillow, psutil, pyftdi, pyserial, pyudev, pyusb, tqdm
Required-by:
```
## 7. SPI 디바이스 경로(/dev/spidev1.0)는 실제 연결에 따라 다를 수 있으니, 필요시 ls /dev/spidev*로 확인 필요
```bash
ls /dev/spidev*
```
**출력 결과: 안 나옴**

### 7.1 관련 NVIDIA 포럼 글 확인
[Cannot use SPI on jetson Nano (cannot see /dev/spidev)](https://forums.developer.nvidia.com/t/cannot-use-spi-on-jetson-nano-cannot-see-dev-spidev/198775/4)
- jetson-io.py로 spi 설정 후 재부팅
- sudo modprobe spidev로 spi 포트를 표출시킴 -> 표출되지 않음 -> 재부팅

### 7.2 관련 tistory 게시글 확인
[[SPI통신] 젯슨나노 SPI 포트 열기](https://merobot.tistory.com/36)
```bash
sudo modprobe spidev
```
**자동 spidev 로드 설정**
```bash
sudo nano /etc/modules
```
으로 연결 후, 마지막 줄에 `spidev` 추가하고 저장 후 종료

### 7.3 재부팅 후 SPI 디바이스 경로(/dev/spidev1.0) 확인
```bash
user@ubuntu:~$ ls /dev/spi*
/dev/spidev0.0  /dev/spidev0.1  /dev/spidev1.0  /dev/spidev1.1
```


## 8. 기존 도커 컨테이너 삭제 후 spidev 및 권장 옵션 부여하여 재설정
```bash
sudo docker rm jetson_yolo11_v1_FLIR
sudo docker run -it --name jetson_yolo11_v1_FLIR \
  --device=/dev/spidev1.0 --device=/dev/spidev0.0 \
  -v ${PWD}:/workspace \
  --ipc=host \
  --runtime=nvidia \
  my_yolo11n_image:v1 /bin/bash
```

**도커 재접속**
```bash
sudo docker start jetson_yolo11_v1_FLIR
sudo docker exec -it jetson_yolo11_v1_FLIR /bin/bash
```
-it 옵션: 컨테이너 안에서 bash 등 셀을 직접 조작할 수 있는 터미널 환경을 열어줌.
> 위 명령은 SPI, 볼륨 마운트, NVIDIA 런타임, IPC 옵션까지 모두 포함한 예시입니다.

## 9. 새로 생성된 도커 컨테이너에 flirpy 설치
**설치 로그**
```bash
root@8b936f9a1224:/# pip install flirpy
Collecting flirpy
  Downloading flirpy-0.3.0-py3-none-any.whl.metadata (11 kB)
Collecting pyserial (from flirpy)
  Downloading pyserial-3.5-py2.py3-none-any.whl.metadata (1.6 kB)
Requirement already satisfied: opencv-python-headless in /usr/local/lib/python3.8/dist-packages (from flirpy) (4.12.0.88)
Requirement already satisfied: tqdm in /usr/local/lib/python3.8/dist-packages (from flirpy) (4.67.1)
Requirement already satisfied: numpy in /usr/local/lib/python3.8/dist-packages (from flirpy) (1.23.5)
Collecting pyudev (from flirpy)
  Downloading pyudev-0.24.3-py3-none-any.whl.metadata (4.6 kB)
Requirement already satisfied: psutil in /usr/local/lib/python3.8/dist-packages (from flirpy) (7.1.0)
Collecting natsort (from flirpy)
  Downloading natsort-8.4.0-py3-none-any.whl.metadata (21 kB)
Collecting libusb (from flirpy)
  Downloading libusb-1.0.26b5-py3-none-any.whl.metadata (9.0 kB)
Collecting pyusb (from flirpy)
  Downloading pyusb-1.2.1-py3-none-any.whl.metadata (2.2 kB)
Collecting pyftdi (from flirpy)
  Downloading pyftdi-0.55.4-py3-none-any.whl.metadata (3.2 kB)
Requirement already satisfied: Pillow in /usr/local/lib/python3.8/dist-packages (from flirpy) (10.4.0)
Requirement already satisfied: setuptools>=63.2.0 in /usr/local/lib/python3.8/dist-packages (from libusb->flirpy) (75.3.2)
Collecting pkg-about>=1.0.7 (from libusb->flirpy)
  Downloading pkg_about-1.0.8-py3-none-any.whl.metadata (4.7 kB)
Collecting packaging>=21.3.0 (from pkg-about>=1.0.7->libusb->flirpy)
  Downloading packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Requirement already satisfied: importlib-resources>=5.7.1 in /usr/local/lib/python3.8/dist-packages (from pkg-about>=1.0.7->libusb->flirpy) (6.4.5)
Requirement already satisfied: importlib-metadata>=4.12.0 in /usr/local/lib/python3.8/dist-packages (from pkg-about>=1.0.7->libusb->flirpy) (8.5.0)
Collecting tomli>=2.0.1 (from pkg-about>=1.0.7->libusb->flirpy)
  Downloading tomli-2.2.1-py3-none-any.whl.metadata (10 kB)
Requirement already satisfied: zipp>=3.20 in /usr/local/lib/python3.8/dist-packages (from importlib-metadata>=4.12.0->pkg-about>=1.0.7->libusb->flirpy) (3.20.2)
Downloading flirpy-0.3.0-py3-none-any.whl (10.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.2/10.2 MB 11.8 MB/s eta 0:00:00
Downloading libusb-1.0.26b5-py3-none-any.whl (387 kB)
Downloading natsort-8.4.0-py3-none-any.whl (38 kB)
Downloading pyftdi-0.55.4-py3-none-any.whl (145 kB)
Downloading pyserial-3.5-py2.py3-none-any.whl (90 kB)
Downloading pyusb-1.2.1-py3-none-any.whl (58 kB)
Downloading pyudev-0.24.3-py3-none-any.whl (62 kB)
Downloading pkg_about-1.0.8-py3-none-any.whl (5.7 kB)
Downloading packaging-25.0-py3-none-any.whl (66 kB)
Downloading tomli-2.2.1-py3-none-any.whl (14 kB)
Installing collected packages: pyserial, tomli, pyusb, pyudev, packaging, natsort, pyftdi, pkg-about, libusb, flirpy
  Attempting uninstall: packaging
    Found existing installation: packaging 20.9
    Uninstalling packaging-20.9:
      Successfully uninstalled packaging-20.9
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
tensorflowjs 3.18.0 requires packaging~=20.9, but you have packaging 25.0 which is incompatible.
Successfully installed flirpy-0.3.0 libusb-1.0.26b5 natsort-8.4.0 packaging-25.0 pkg-about-1.0.8 pyftdi-0.55.4 pyserial-3.5 pyudev-0.24.3 pyusb-1.2.1 tomli-2.2.1
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
```
- 기존과 동일하게 packiaging과 tensorflowjs 충돌 발생, yolo11n 모델 사용에는 이상 없을 것으로 예상(이전에도 이상 없었으므로)


## 10. opencv-python-headless

### 10.1 있는지 확인
```bash
pip show opencv-python-headless
```
**출력 결과**
```bash
root@8b936f9a1224:/# pip show opencv-python-headless
Name: opencv-python-headless
Version: 4.12.0.88
Summary: Wrapper package for OpenCV python bindings.
Home-page: https://github.com/opencv/opencv-python
Author:
Author-email:
License: Apache 2.0
Location: /usr/local/lib/python3.8/dist-packages
Requires: numpy
Required-by: flirpy, ultralytics
```

## 7. flirpy 예제 코드 실행
```python

# flirpy를 이용한 FLIR Lepton 3.5 SPI 연결 예제 (Jetson Nano)
#
# 참고사항:
# - Jetson Nano Expansion Header Tool에서 SPI2 활성화 필요 (핀맵: SCK=13, MOSI=37, MISO=22, CS0=18)
# - Breakout Board와의 연결은 문서 상단 표 참고
# - I2C는 보통 제어용, SPI는 영상 데이터용
# - SPI 디바이스 경로는 ls /dev/spidev* 로 확인 가능
# - 실행 전 pip install flirpy opencv-python-headless 필요

from flirpy.camera.lepton import Lepton
import cv2
import numpy as np

# Lepton SPI 디바이스 경로 (Jetson Nano의 SPI2는 일반적으로 /dev/spidev1.0)
# 실제 연결에 따라 /dev/spidev0.0, /dev/spidev1.0 등으로 다를 수 있음
# 본 예제에서는 SPI_2_CS0 (J41 18번) 사용 시 /dev/spidev1.0이 일반적
SPI_DEVICE = "/dev/spidev1.0"

# Lepton 카메라 열기
with Lepton(SPI_DEVICE) as cam:
  print("FLIR Lepton 연결 성공!")
  for i in range(10):
    frame, _ = cam.capture()
    # 16비트 데이터를 8비트로 정규화
    img = np.uint8(255 * (frame - frame.min()) / (frame.ptp() + 1e-6))
    img_color = cv2.applyColorMap(img, cv2.COLORMAP_JET)
    out_path = f"lepton_capture_{i:02d}.png"
    cv2.imwrite(out_path, img_color)
    print(f"Saved: {out_path}")
  print("이미지 저장 완료. (lepton_capture_XX.png)")
```

## 8. git으로 Jetson Nano에 예제 코드 복사 후 실험 진행
```bash
python3 11_test_flirpy_Lepton.py
```

## 9. /dev/spidev1.0 오류 발생
```bash
root@8b936f9a1224:/workspace/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton# python3 11_test_flirpy_Lepton.py
Traceback (most recent call last):
  File "11_test_flirpy_Lepton.py", line 20, in <module>
    with Lepton(SPI_DEVICE) as cam:
  File "/usr/local/lib/python3.8/dist-packages/flirpy/camera/lepton.py", line 16, in __init__
    logging.basicConfig(level=loglevel)
  File "/usr/lib/python3.8/logging/__init__.py", line 1991, in basicConfig
    root.setLevel(level)
  File "/usr/lib/python3.8/logging/__init__.py", line 1409, in setLevel
    self.level = _checkLevel(level)
  File "/usr/lib/python3.8/logging/__init__.py", line 194, in _checkLevel
    raise ValueError("Unknown level: %r" % level)
ValueError: Unknown level: '/dev/spidev1.0
```