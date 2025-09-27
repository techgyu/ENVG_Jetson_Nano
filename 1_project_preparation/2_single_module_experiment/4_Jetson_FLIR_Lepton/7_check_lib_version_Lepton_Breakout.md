# 2025-09-23 | FLIR Lepton 3.5와 Breakout V2.0 관련 라이브러리 버전 확인

---

## 0. 현재 Jetson Nano의 OS, Python, 주요 패키지 버전 확인
```bash
# OS 버전 확인
cat /etc/os-release

# Python 버전 확인
python3 --version

# pip 버전 확인
pip3 --version

# 설치된 모든 패키지 버전 확인
pip list
```

**출력 결과**
```bash
root@12caaef4bcf9:/workspace/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/3_Jetson_FLIR_Lepton# cat /etc/os-release
NAME="Ubuntu"
VERSION="18.04.6 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.6 LTS"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic
root@12caaef4bcf9:/workspace/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/3_Jetson_FLIR_Lepton# python3 --version
Python 3.8.0
root@12caaef4bcf9:/workspace/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/3_Jetson_FLIR_Lepton# pip3 --version
pip 25.0.1 from /usr/local/lib/python3.8/dist-packages/pip (python 3.8)
---
root@12caaef4bcf9:/workspace/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/3_Jetson_FLIR_Lepton# pip list
Package                      Version             Editable project location
---------------------------- ------------------- -------------------------
absl-py                      2.3.1
astunparse                   1.6.3
attrs                        25.3.0
cachetools                   5.5.2
cattrs                       24.1.3
certifi                      2025.8.3
charset-normalizer           3.4.3
colorama                     0.4.6
contourpy                    1.1.1
coremltools                  8.3.0
cycler                       0.12.1
exceptiongroup               1.3.0
flatbuffers                  25.2.10
fonttools                    4.57.0
gast                         0.4.0
google-auth                  2.40.3
google-auth-oauthlib         0.4.6
google-pasta                 0.2.0
grpcio                       1.70.0
h5py                         3.10.0
idna                         3.10
importlib_metadata           8.5.0
importlib_resources          6.4.5
joblib                       1.4.2
keras                        2.11.0
kiwisolver                   1.4.7
libclang                     18.1.1
Markdown                     3.7
MarkupSafe                   2.1.5
matplotlib                   3.7.5
ml-dtypes                    0.2.0
mpmath                       1.3.0
numpy                        1.23.5
oauthlib                     3.3.1
onnx                         1.12.0
onnxruntime-gpu              1.8.0
onnxslim                     0.1.68
opencv-python-headless       4.12.0.88
openvino                     2024.0.0
openvino-telemetry           2025.2.0
opt_einsum                   3.4.0
packaging                    20.9
pillow                       10.4.0
pip                          25.0.1
polars                       1.8.2
protobuf                     3.19.6
psutil                       7.1.0
pyaml                        25.7.0
pyasn1                       0.6.1
pyasn1_modules               0.4.2
pyparsing                    3.1.4
python-dateutil              2.9.0.post0
PyYAML                       6.0.2
requests                     2.32.4
requests-oauthlib            2.0.0
rsa                          4.9.1
scikit-learn                 1.3.2
scipy                        1.10.1
setuptools                   75.3.2
six                          1.17.0
sympy                        1.13.3
tensorboard                  2.11.2
tensorboard-data-server      0.6.1
tensorboard-plugin-wit       1.8.1
tensorflow                   2.11.0
tensorflow-cpu-aws           2.11.0
tensorflow-estimator         2.11.0
tensorflow-hub               0.12.0
tensorflow-io-gcs-filesystem 0.35.0
tensorflowjs                 3.18.0
tensorrt                     8.2.0.6
termcolor                    2.4.0
threadpoolctl                3.5.0
torch                        1.11.0a0+gitbc2c6ed
torchvision                  0.12.0a0+9b5a3fe
tqdm                         4.67.1
typing_extensions            4.13.2
ultralytics                  8.3.202             /ultralytics
ultralytics-thop             2.0.17
urllib3                      2.2.3
uv                           0.8.18
Werkzeug                     3.0.6
wheel                        0.45.1
wrapt                        1.17.3
zipp                         3.20.2
```

## 1. FLIR Lepton 3.5와 Breakout Board V2.0을 사용할 수 있는 파이썬 라이브러리

FLIR Lepton 3.5와 Breakout Board V2.0을 Jetson Nano 등에서 제어/영상 수신에 사용할 수 있는 주요 파이썬 라이브러리들은 다음과 같습니다.

### 1.1 flirpy  
- [GitHub: flirpy](https://github.com/groupgets/flirpy)  
- FLIR Lepton(특히 2.x, 3.x 시리즈) 지원  
- I2C 제어 및 SPI 영상 데이터 스트림 수신 지원  
- Jetson Nano, Raspberry Pi 등에서 사용 가능  
- 설치: `pip install flirpy`

### 1.2 pylepton  
- [GitHub: pylepton](https://github.com/groupgets/pylepton)  
- Lepton 2.x/3.x 지원, C 확장 기반  
- SPI를 통한 영상 데이터 캡처  
- Jetson Nano에서 사용하려면 spidev, smbus 등 의존성 필요

### 1.3 purethermal1-uvc-capture  
- [GitHub: groupgets/purethermal1-uvc-capture](https://github.com/groupgets/purethermal1-uvc-capture)  
- PureThermal 보드(USB UVC) 기반이지만, 일부 코드 참고 가능  
- Lepton 모듈 직접 연결에는 flirpy/pylepton이 더 적합

### 1.4 기타 관련 라이브러리 및 참고  
- **spidev**: Python에서 SPI 통신을 위한 표준 라이브러리  
  - 설치: `pip install spidev`
- **smbus2**: Python에서 I2C 통신을 위한 표준 라이브러리  
  - 설치: `pip install smbus2`
- **lepton3**: [GitHub: lepton3](https://github.com/roger-/lepton3)  
  - C 기반, Python 바인딩은 직접 구현 필요

---