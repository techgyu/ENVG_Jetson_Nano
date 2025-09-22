# 2025-09-20 | 컨테이너, 이미지 삭제 후 재설치

---
## 0. 컨테이너 목록 확인
```bash
sudo docker ps -a
```

## 1. 컨테이너 작동 중단
```bash
sudo docker stop jetson_yolo11
```

## 2. 컨테이너 삭제
```bash
sudo docker rm jetson_yolo11
```

## 3. 컨테이너 목록 확인
```bash
sudo docker ps -a
```

## 4. 이미지 삭제
```bash
sudo docker rmi ultralytics/ultralytics:latest-jetson-jetpack4
```

## 5. 이미지 목록 확인
```bash 
sudo docker images
```

## 6. 이미지 재설치
### 6.1 터미널 환경 변수 설정
```bash
t=ultralytics/ultralytics:latest-jetson-jetpack4
```

### 6.2 Docker 이미지 다운로드
```bash
sudo docker pull $t
```

### 6.3 Docker 이미지 확인
```bash
sudo docker image ls
```

**출력 결과 예시:**
```bash
REPOSITORY                TAG                      IMAGE ID       CREATED        SIZE  
ultralytics/ultralytics   latest-jetson-jetpack4   704b5fa7ea6f   17 hours ago   5.54GB
```

## 7. Docker 컨테이너 실행
```bash
sudo docker run -it --ipc=host --runtime=nvidia $t
```

- **설명:**  
  - 터미널에서 바로 컨테이너에 진입하여 상호작용할 수 있습니다.
  - 컨테이너 이름은 자동으로 부여됩니다.
  - 호스트와 컨테이너 간 파일 공유(볼륨 마운트)는 없습니다.
  - 컨테이너가 종료되면 터미널도 함께 종료됩니다.

또는

```bash
sudo docker run -it -d --name jetson_yolo11 -v ${PWD}:/workspace --ipc=host --runtime=nvidia ultralytics/ultralytics:latest-jetson-jetpack4
```

- **설명:**  
  - `-d` 옵션으로 컨테이너를 백그라운드(detached)로 실행합니다.
  - `--name jetson_yolo11`로 컨테이너 이름을 직접 지정할 수 있습니다.
  - `-v ${PWD}:/workspace` 옵션으로 현재 디렉토리를 컨테이너의 `/workspace`에 마운트하여, 호스트와 컨테이너 간 파일을 공유할 수 있습니다.
  - 컨테이너 실행 후, 필요할 때 아래 명령어로 접속할 수 있습니다:
    ```bash
    sudo docker exec -it jetson_yolo11 bash
    ```

## 10. Docker 컨테이너 켜기
```bash
sudo docker start jetson_yolo11 # 중지된 컨테이너를 다시 시작
sudo docker exec -it jetson_yolo11 bash # 실행 중인 컨테이너에 bash 셀로 접속(컨테이너 내부에서 직접 명령 입력)

```

## 11. 현재 컨테이너에 설치된 패키지 목록 확인
```bash
pip list
```
**출력 결과**
```bash
oot@4d964ff22ba6:/workspace/Desktop# pip list
Package                      Version             Editable project location
---------------------------- ------------------- -------------------------
absl-py                      2.3.1
astunparse                   1.6.3
attrs                        25.3.0
cachetools                   5.5.2
cattrs                       24.1.3
certifi                      2025.8.3
charset-normalizer           3.4.3
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
mpmath                       1.3.0
numpy                        1.24.4
oauthlib                     3.3.1
onnx                         1.12.0
onnxruntime-gpu              1.8.0
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

## 12. numpy, torch tensorrt ultralytics 버전 확인
```bash
python3 -c "import numpy; print(numpy.__version__)"
python3 -c "import torch; print(torch.__version__)"
python3 -c "import tensorrt; print(tensorrt.__version__)"
python3 -c "import ultralytics; print(ultralytics.__version__)"
```

**정상 출력**
```bash
root@4d964ff22ba6:/workspace/Desktop# python3 -c "import numpy; print(numpy.__version__)"
1.24.4
root@4d964ff22ba6:/workspace/Desktop# python3 -c "import torch; print(torch.__version__)"
1.11.0a0+gitbc2c6ed
root@4d964ff22ba6:/workspace/Desktop# python3 -c "import tensorrt; print(tensorrt.__version__)"
8.2.0.6
root@4d964ff22ba6:/workspace/Desktop# python3 -c "import ultralytics; print(ultralytics.__version__)"
Creating new Ultralytics Settings v0.0.6 file ✅ 
View Ultralytics Settings with 'yolo settings' or at '/root/.config/Ultralytics/settings.json'
Update Settings with 'yolo settings key=value', i.e. 'yolo settings runs_dir=path/to/dir'. For help see https://docs.ultralytics.com/quickstart/#ultralytics-settings.
8.3.202
root@4d964ff22ba6:/workspace/Desktop#
```

## 13. 작업 디렉토리에 존재하는 기존 yolo11n.pt 및 관련 파일 삭제
```bash
rm yolo11n.pt yolo11n.engine yolo11n.onnx
```

## 14. Docker 이미지가 생성해낸 yolo11n.pt 파일을 현재 작업 디렉토리로 복사
```bash
cp /ultralytics/yolo11n.pt ./
```

## 15. 실행 전 terminal clear
```bash
clear
```

## 16. 실행
```bash
python3 test_yolo11n_tensorRT.py
```

**출력 결과 로그**
```bash
# 파일 실행
root@4d964ff22ba6:/workspace/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation# python3 test_yolo11n_tensorRT.py

# 자동 GPU 할당 경고
WARNING ⚠️ TensorRT requires GPU export, automatically assigning device=0
# Ultralytics 8.3.202 버전, 파이썬: 3.8.0 버전, 토치: 1.11.a0 버전, 쿠다 0번(GPU) 사용
Ultralytics 8.3.202 🚀 Python-3.8.0 torch-1.11.0a0+gitbc2c6ed CUDA:0 (NVIDIA Tegra X1, 3964MiB)
# 모델 yolo11n.pt 로드: 100개의 레이어, 2,616,248개의 파라미터, 0개의 그래디언트, 6.5 GFLOPs
YOLO11n summary (fused): 100 layers, 2,616,248 parameters, 0 gradients, 6.5 GFLOPs

# PyTorch: 시작 'yolo11n.pt'에서 입력 모양 (배치: 1, 채널: 3, 높이: 640, 너비: 640) BCHW 및 출력 모양 (1, 84, 8400) (모델 파일 크기: 5.4 MB)
PyTorch: starting from 'yolo11n.pt' with input shape (1, 3, 640, 640) BCHW and output shape(s) (1, 84, 8400) (5.4 MB)
# onnxslim 0.1.67 이상 필요, 현재 없어서 자동 업데이트 시도...
requirements: Ultralytics requirement ['onnxslim>=0.1.67'] not found, attempting AutoUpdate...
# pip 가상환경 사용 권장 안내
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
# onnxslim 0.1.67 이상 설치 시도
Collecting onnxslim>=0.1.67
    # 0.1.68 버전 메타 데이터 다운로드
  Downloading onnxslim-0.1.68-py3-none-any.whl.metadata (7.6 kB)
# onnxslim이 필요로 하는 onnx 패키지는 "/usr/local/lib/python3.8/dist-packages"에 이미 설치되어 있음(1.12.0 버전으로)
Requirement already satisfied: onnx in /usr/local/lib/python3.8/dist-packages (from onnxslim>=0.1.67) (1.12.0)
# onnxslim이 필요로 하는 sympy 패키지는 "/usr/local/lib/python3.8/dist-packages"에 이미 설치되어 있음(1.13.3 버전으로)
Requirement already satisfied: sympy>=1.13.3 in /usr/local/lib/python3.8/dist-packages (from onnxslim>=0.1.67) (1.13.3)
# onnxslim이 필요로 하는 packaging 패키지는 "/usr/local/lib/python3.8/dist-packages"에 이미 설치되어 있음(20.9 버전으로)
Requirement already satisfied: packaging in /usr/local/lib/python3.8/dist-packages (from onnxslim>=0.1.67) (20.9)      
# onnxslim이 필요로 하는 colorama 패키지는 현재 설치되어 있지 않음, 설치 진행 중...
Collecting colorama (from onnxslim>=0.1.67)
    # 0.4.6 버전 메타 데이터 다운로드
  Downloading colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
# onnxslim이 필요로 하는 ml_dtypes 패키지는 현재 설치되어 있지 않음, 설치 진행 중...
Collecting ml_dtypes (from onnxslim>=0.1.67)
    # 0.2.0 버전 메타 데이터 다운로드
  Downloading ml_dtypes-0.2.0-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl.metadata (20 kB)

#  sympy가 필요로 하는  mpmath 패키지(1.1.0 ~ 1.4)는 "/usr/local/lib/python3.8/dist-packages"에 이미 설치되어 있음(1.3.0 버전으로)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/lib/python3.8/dist-packages (from sympy>=1.13.3->onnxslim>=0.1.67) (1.3.0)

# ml_dtypes가 필요로 하는 numpy 패키지(1.20 ~)는 "/usr/local/lib/python3.8/dist-packages"에 이미 설치되어 있음(1.24.4 버전으로)
Requirement already satisfied: numpy>1.20 in /usr/local/lib/python3.8/dist-packages (from ml_dtypes->onnxslim>=0.1.67) (1.24.4)

# onnx가 필요로 하는 protobuf 패키지(3.12.2 ~ 3.20.1)는 "/usr/local/lib/python3.8/dist-packages"에 이미 설치되어 있음(3.19.6 버전으로)
Requirement already satisfied: protobuf<=3.20.1,>=3.12.2 in /usr/local/lib/python3.8/dist-packages (from onnx->onnxslim>=0.1.67) (3.19.6)

# onnx가 필요로 하는 typing-extensions 패키지(3.6.2.1 ~)는 "/usr/local/lib/python3.8/dist-packages"에 이미 설치되어 있음(4.13.2 버전으로)
Requirement already satisfied: typing-extensions>=3.6.2.1 in /usr/local/lib/python3.8/dist-packages (from onnx->onnxslim>=0.1.67) (4.13.2)

# packaging이 필요로 하는 pyparsing 패키지(2.0.2 ~)는 "/usr/local/lib/python3.8/dist-packages"에 이미 설치되어 있음(3.1.4 버전으로)
Requirement already satisfied: pyparsing>=2.0.2 in /usr/local/lib/python3.8/dist-packages (from packaging->onnxslim>=0.1.67) (3.1.4)

# onnxslim 0.1.68 버전 다운로드
Downloading onnxslim-0.1.68-py3-none-any.whl (164 kB)

# colorama 0.4.6 버전 다운로드
Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)

# ml_dtypes 0.2.0 버전 다운로드
Downloading ml_dtypes-0.2.0-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (1.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.0/1.0 MB 80.6 MB/s eta 0:00:00

# onnxslim, colorama, ml_dtypes 3개 패키지 설치 시도
Installing collected packages: ml_dtypes, colorama, onnxslim

# onnxslim, colorama, ml_dtypes 3개 패키지 설치 완료
Successfully installed colorama-0.4.6 ml_dtypes-0.2.0 onnxslim-0.1.68

# 필요한 패키지가 4.6초 만에 자동 업데이트 완료
requirements: AutoUpdate success ✅ 4.6s

# 설치된 패키지가 바로 적용되지 않을 수 있으니, 런타임을 재시작하거나 명령을 다시 실행하라는 경고
WARNING ⚠️ requirements: Restart runtime or rerun command for updates to take effect

# onnx 1.12.0, opset 14로 모델을 ONNX 형식으로 변환 시작
ONNX: starting export with onnx 1.12.0 opset 14...
# prim::Constant 타입의 shape 추론이 누락되어, 내보낸 그래프의 shape 추론이 잘못될 수 있다는 경고. 심볼릭 함수에 추가하는 것을 고려하라는 경고가 여러 번 반복 출력됨.
WARNING: The shape inference of prim::Constant type is missing, so it may result in wrong shape inference for the exported graph. Please consider adding it in symbolic function.
WARNING: The shape inference of prim::Constant type is missing, so it may result in wrong shape inference for the exported graph. Please consider adding it in symbolic function.
WARNING: The shape inference of prim::Constant type is missing, so it may result in wrong shape inference for the exported graph. Please consider adding it in symbolic function.
WARNING: The shape inference of prim::Constant type is missing, so it may result in wrong shape inference for the exported graph. Please consider adding it in symbolic function.
WARNING: The shape inference of prim::Constant type is missing, so it may result in wrong shape inference for the exported graph. Please consider adding it in symbolic function.
WARNING: The shape inference of prim::Constant type is missing, so it may result in wrong shape inference for the exported graph. Please consider adding it in symbolic function.
# ONNX 단순화(simplifier) 과정에서 FLOAT8E4M3FN 타입 관련 오류가 발생했다는 경고입니다.!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
WARNING ⚠️ ONNX: simplifier failure: FLOAT8E4M3FN
# ONNX 변환이 19.3초 만에 성공적으로 완료되었고, 결과 파일이 'yolo11n.onnx'(10.2MB)로 저장되었습니다.
ONNX: export success ✅ 19.3s, saved as 'yolo11n.onnx' (10.2 MB)

# TensorRT 8.2.0.6 버전으로 모델 변환(엔진 생성)을 시작합니다.
TensorRT: starting export with TensorRT 8.2.0.6...
# CUDA 초기화 시 CPU 메모리 210MiB 증가, 현재 CPU 1465MiB, GPU 3749MiB 사용 중.
[09/20/2025-06:14:42] [TRT] [I] [MemUsageChange] Init CUDA: CPU +210, GPU +0, now: CPU 1465, GPU 3749 (MiB)
# TensorRT 엔진 빌더 커널 라이브러리 생성 시작 시점의 메모리 사용량(스냅샷).
[09/20/2025-06:14:42] [TRT] [I] [MemUsageSnapshot] Begin constructing builder kernel library: CPU 1465 MiB, GPU 3783 MiB
# 커널 라이브러리 생성이 끝난 후의 메모리 사용량(스냅샷).
[09/20/2025-06:14:42] [TRT] [I] [MemUsageSnapshot] End constructing builder kernel library: CPU 1495 MiB, GPU 3815 MiB
# 구분선(로그 구분용).
[09/20/2025-06:14:42] [TRT] [I] ----------------------------------------------------------------
[09/20/2025-06:14:42] [TRT] [I] Input filename:   yolo11n.onnx # 변환에 사용할 입력 ONNX 파일 이름
[09/20/2025-06:14:42] [TRT] [I] ONNX IR version:  0.0.7 # ONNX 중간 표현(Intermediate Representation) 버전: 0.0.7.
[09/20/2025-06:14:42] [TRT] [I] Opset version:    14 # ONNX 모델의 opset(연산자 집합) 버전: 14.
[09/20/2025-06:14:42] [TRT] [I] Producer name:    pytorch # 이 ONNX 모델을 만든 프레임워크: PyTorch.
[09/20/2025-06:14:42] [TRT] [I] Producer version: 1.11.0 # PyTorch 버전: 1.11.0.
[09/20/2025-06:14:42] [TRT] [I] Domain: # 도메인 정보(비어 있음).
[09/20/2025-06:14:42] [TRT] [I] Model version:    0 # 모델 버전: 0.
[09/20/2025-06:14:42] [TRT] [I] Doc string: # 모델 설명(비어 있음).
# 구분선(로그 구분용).
[09/20/2025-06:14:42] [TRT] [I] ----------------------------------------------------------------

# 경고: ONNX 모델이 INT64 타입의 가중치를 포함하고 있는데, TensorRT는 INT64를 기본적으로 지원하지 않으므로 INT32로 변환을 시도한다는 의미입니다.
[09/20/2025-06:14:42] [TRT] [W] onnx2trt_utils.cpp:366: Your ONNX model has been generated with INT64 weights, while TensorRT does not natively support INT64. Attempting to cast down to INT32.

# TensorRT 엔진의 입력 텐서 이름은 "images"이고,입력 크기는 (1, 3, 640, 640) (배치, 채널, 높이, 너비), 데이터 타입은 FLOAT(실수)입니다.
TensorRT: input "images" with shape(1, 3, 640, 640) DataType.FLOAT
# TensorRT 엔진의 출력 텐서 이름은 "output0"이고, 출력 크기는 (1, 84, 8400), 데이터 타입은 FLOAT(실수)입니다.
TensorRT: output "output0" with shape(1, 84, 8400) DataType.FLOAT
# FP32(32비트 부동소수점) 연산을 사용하는 TensorRT 엔진을 yolo11n.engine 파일로 생성(빌드)하고 있다는 뜻입니다.
TensorRT: building FP32 engine as yolo11n.engine
# DLA(Deep Learning Accelerator)에서 실행되는 레이어 목록(여기서는 없음).
[09/20/2025-06:14:43] [TRT] [I] ---------- Layers Running on DLA ----------

# DLA(Deep Learning Accelerator)에서 실행되는 레이어 목록(여기서는 없음).
[09/20/2025-06:14:43] [TRT] [I] ---------- Layers Running on GPU ----------
# Conv_0 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_0
# Sigmoid_1, Mul_2 연산이 포함된 PWN 연산이 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_1), Mul_2)
# Conv_3 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_3
# Sigmoid_4, Mul_5 연산이 포함된 PWN 연산이 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_4), Mul_5)
# Conv_6 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_6
# Sigmoid_7, Mul_8 연산이 포함된 PWN 연산이 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_7), Mul_8)
# 텐서 분할 연산이 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Split_10
# Split_10의 첫 번째 출력이 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Split_10_0
# Conv_11 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_11
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_12), Mul_13)
# Conv_14 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_14
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_15), Mul_16), Add_17)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] input.12 copy
# Conv_19 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_19
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_20), Mul_21)
# Conv_22 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_22
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_23), Mul_24)
# Conv_25 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_25
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_26), Mul_27)
# Conv_30 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_30
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_31), Mul_32)
# Conv_33 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_33
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_34), Mul_35), Add_36)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Concat_206 copy
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] input.40 copy
# Conv_38 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_38
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_39), Mul_40)
# Conv_41 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_41
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_42), Mul_43)
# Conv_44 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_44
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_45), Mul_46)
# Conv_49 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_49 || Conv_66
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_50), Mul_51)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_67), Mul_68)
# Conv_52 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_52
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_53), Mul_54)
# Conv_55 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_55
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_56), Mul_57), Add_58)
# Conv_59 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_59
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_60), Mul_61)
# Conv_62 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_62
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_63), Mul_64), Add_65)
# Conv_70 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_70
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_71), Mul_72)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Concat_226 copy
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] input.68 copy
# Conv_74 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_74
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_75), Mul_76)
# Conv_77 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_77
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_78), Mul_79)
# Conv_80 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_80
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_81), Mul_82)
# Conv_85 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_85 || Conv_102
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_86), Mul_87)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_103), Mul_104)
# Conv_88 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_88
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_89), Mul_90)
# Conv_91 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_91
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_92), Mul_93), Add_94)
# Conv_95 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_95
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_96), Mul_97)
# Conv_98 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_98
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_99), Mul_100), Add_101)
# Conv_106 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_106
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_107), Mul_108)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Concat_263 copy
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] input.124 copy
# Conv_110 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_110
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_111), Mul_112)
# Conv_113 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_113
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_114), Mul_115)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] MaxPool_116
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] MaxPool_117
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] MaxPool_118
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::MaxPool_295 copy
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::MaxPool_296 copy
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::MaxPool_297 copy
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Concat_298 copy
# Conv_120 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_120
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_121), Mul_122)
# Conv_123 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_123
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_124), Mul_125)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Split_127_4
# Conv_128 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_128
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Reshape_129
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Split_131
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Split_131_5
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Split_131_6
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Reshape_140
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] MatMul_133
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Mul_333 + (Unnamed Layer* 136) [Shuffle] + Mul_135
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Softmax_136
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] MatMul_138
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Reshape_139
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_141 + Add_142
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_143 + Add_144
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_145
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_146), Mul_147)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_148 + Add_149
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Concat_307 copy
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Concat_366 copy
# Conv_151 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_151
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_152), Mul_153)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Resize_154
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Concat_375 copy
# Conv_156 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_156
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_157), Mul_158)
# Conv_161 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_161
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_162), Mul_163)
# Conv_164 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_164
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_165), Mul_166), Add_167)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Concat_381 copy
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] input.224 copy
# Conv_169 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_169
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_170), Mul_171)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Resize_172
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Concat_398 copy
# Conv_174 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_174
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_175), Mul_176)
# Conv_179 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_179
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_180), Mul_181)
# Conv_182 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_182
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_183), Mul_184), Add_185)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Concat_404 copy
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] input.252 copy
# Conv_187 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_187
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_188), Mul_189)
# Conv_190 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_190
# Conv_247 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_247
# Conv_254 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_254
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_191), Mul_192)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_248), Mul_249)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_255), Mul_256)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Resize_393 copy
# Conv_250 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_250
# Conv_257 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_257
# Conv_194 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_194
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_251), Mul_252)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_258), Mul_259)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_195), Mul_196)
# Conv_253 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_253
# Conv_260 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_260
# Conv_199 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_199
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_261), Mul_262)
# Conv_263 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_263
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_200), Mul_201)
# Conv_202 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_202
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_264), Mul_265)
# Conv_266 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_266
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_203), Mul_204), Add_205)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Concat_425 copy
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] input.284 copy
# Conv_207 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_207
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_208), Mul_209)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Reshape_316
# Conv_210 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_210
# Conv_268 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_268
# Conv_275 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_275
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_211), Mul_212)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_269), Mul_270)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_276), Mul_277)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Resize_370 copy
# Conv_271 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_271
# Conv_278 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_278
# Conv_214 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_214
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_272), Mul_273)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_279), Mul_280)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_215), Mul_216)
# Conv_274 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_274
# Conv_281 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_281
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_219 || Conv_236
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_282), Mul_283)
# Conv_284 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_284
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_220), Mul_221)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_237), Mul_238)
# Conv_222 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_222
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_285), Mul_286)
# Conv_287 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_287
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_223), Mul_224)
# Conv_225 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_225
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Reshape_320
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_226), Mul_227), Add_228)
# Conv_229 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_229
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_230), Mul_231)
# Conv_232 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_232
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_233), Mul_234), Add_235)
# Conv_240 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_240
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_241), Mul_242)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Concat_446 copy
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] input.316 copy
# Conv_244 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_244
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_245), Mul_246)
# Conv_289 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_289
# Conv_296 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_296
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_290), Mul_291)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_297), Mul_298)
# Conv_292 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_292
# Conv_299 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_299
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_293), Mul_294)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_300), Mul_301)
# Conv_295 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_295
# Conv_302 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_302
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_303), Mul_304)
# Conv_305 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_305
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_306), Mul_307)
# Conv_308 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_308
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Reshape_324
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Concat_551 copy
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Concat_561 copy
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Concat_571 copy
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Split_327
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Split_327_11
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Reshape_339 + Transpose_340
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Softmax_341
# Conv_342 레이어가 GPU에서 실행됨.
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Conv_342
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Reshape_348
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Slice_359
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Slice_362
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Sub_620
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Sub_364
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Add_622
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Add_366
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(onnx::Div_625 + (Unnamed Layer* 413) [Shuffle], PWN(Add_367, Div_369))
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Sub_370
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Concat_626 copy
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Concat_627 copy
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Mul_629 + (Unnamed Layer* 418) [Shuffle]
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] Mul_373
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] PWN(Sigmoid_374)
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Concat_630 copy
[09/20/2025-06:14:43] [TRT] [I] [GpuLayer] onnx::Concat_631 copy
# cuBLAS/cuBLASLt 라이브러리 초기화, CPU와 GPU 메모리 사용량 변화 없음(현재 CPU 1507MiB, GPU 3835MiB 사용 중).
[09/20/2025-06:14:43] [TRT] [I] [MemUsageChange] Init cuBLAS/cuBLASLt: CPU +0, GPU +0, now: CPU 1507, GPU 3835 (MiB)
# cuDNN 라이브러리 초기화, CPU 메모리 241MiB, GPU 메모리 62MiB 증가(현재 CPU 1748MiB, GPU 3897MiB 사용 중).
[09/20/2025-06:14:47] [TRT] [I] [MemUsageChange] Init cuDNN: CPU +241, GPU +62, now: CPU 1748, GPU 3897 (MiB)
# 로컬 타이밍 캐시를 사용 중이며, 이번 빌드의 프로파일링 결과는 저장되지 않음.
[09/20/2025-06:14:47] [TRT] [I] Local timing cache in use. Profiling results in this builder pass will not be stored.
# 일부 연산(tactic)에 할당된 워크스페이스 메모리가 부족할 수 있으니, 워크스페이스 크기를 늘리면 성능이 향상될 수 있음(자세한 내용은 verbose 출력 참고).
[09/20/2025-06:15:06] [TRT] [I] Some tactics do not have sufficient workspace memory to run. Increasing workspace size may increasease performance, please check verbose output.
# 입력 텐서 1개, 출력 텐서 3개가 감지됨.
[09/20/2025-06:17:52] [TRT] [I] Detected 1 inputs and 3 output network tensors.
# 호스트(메인 메모리)에서 영구적으로 할당된 메모리: 196,464 바이트.
[09/20/2025-06:17:53] [TRT] [I] Total Host Persistent Memory: 196464
# 디바이스(GPU)에서 영구적으로 할당된 메모리: 14,257,664 바이트.
[09/20/2025-06:17:53] [TRT] [I] Total Device Persistent Memory: 14257664
# 임시(scratch) 메모리 사용량: 0 바이트.
[09/20/2025-06:17:53] [TRT] [I] Total Scratch Memory: 0
# TensorRT 메모리 할당기의 최대 메모리 사용량: CPU 2MiB, GPU 171MiB.
[09/20/2025-06:17:53] [TRT] [I] [MemUsageStats] Peak memory usage of TRT CPU/GPU memory allocators: CPU 2 MiB, GPU 171 MiB
# ShiftNTopDown 알고리즘이 195개 노드에 10개 블록(총 19,456,002 바이트)을 할당하는 데 188ms 소요됨.
[09/20/2025-06:17:53] [TRT] [I] [BlockAssignment] Algorithm ShiftNTopDown took 188.003ms to assign 10 blocks to 195 nodes requiring 19456002 bytes.
# 활성화(activation) 메모리 총량: 19,456,002 바이트.
[09/20/2025-06:17:53] [TRT] [I] Total Activation Memory: 19456002
# cuBLAS/cuBLASLt 초기화로 GPU 메모리 18MiB 증가(현재 CPU 2007MiB, GPU 3890MiB 사용 중).
[09/20/2025-06:17:53] [TRT] [I] [MemUsageChange] Init cuBLAS/cuBLASLt: CPU +0, GPU +18, now: CPU 2007, GPU 3890 (MiB)
# cuDNN 초기화로 GPU 메모리 33MiB 감소(현재 CPU 2007MiB, GPU 3857MiB 사용 중).
[09/20/2025-06:17:53] [TRT] [I] [MemUsageChange] Init cuDNN: CPU +0, GPU -33, now: CPU 2007, GPU 3857 (MiB)
# TensorRT 엔진 빌드 과정에서 GPU 메모리 16MiB 추가 할당(현재 CPU 0MiB, GPU 16MiB 사용 중).
[09/20/2025-06:17:53] [TRT] [I] [MemUsageChange] TensorRT-managed allocation in building engine: CPU +0, GPU +16, now: CPU 0, GPU 16 (MiB)

# TensorRT 엔진 변환이 216.4초 만에 성공적으로 완료되었고, 결과 파일이 'yolo11n.engine'(16.3MB)로 저장됨.
TensorRT: export success ✅ 216.4s, saved as 'yolo11n.engine' (16.3 MB)
# 전체 내보내기(Export) 작업이 229.8초 만에 완료됨.
Export complete (229.8s)
# 결과 파일이 해당 경로에 저장됨.
Results saved to /workspace/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation
# 예측(Predict) 명령어 예시: yolo predict task=detect model=yolo11n.engine imgsz=640
Predict:         yolo predict task=detect model=yolo11n.engine imgsz=640
# 증(Validate) 명령어 예시: yolo val task=detect model=yolo11n.engine imgsz=640 data=...
Validate:        yolo val task=detect model=yolo11n.engine imgsz=640 data=/usr/src/ultralytics/ultralytics/cfg/datasets/coco.yaml
# 모델 구조 시각화는 https://netron.app 에서 가능함.
Visualize:       https://netron.app
# 모델의 작업 종류(task)를 자동으로 추정할 수 없어 'detect'로 가정함. 명시적으로 task를 지정하라는 경고.
WARNING ⚠️ Unable to automatically guess model task, assuming 'task=detect'. Explicitly define task for your model, i.e. 'task=d
etect', 'segment', 'classify','pose' or 'obb'.
# TensorRT 추론을 위해 yolo11n.engine 파일을 로드 중.
Loading yolo11n.engine for TensorRT inference...
# Ultralytics가 요구하는 numpy 1.23.5 버전이 없어 자동 업데이트를 시도함.
requirements: Ultralytics requirement ['numpy==1.23.5'] not found, attempting AutoUpdate...
# 첫 번째 시도에서 메모리 부족(Errno 12)으로 실패.
WARNING ⚠️ Retry 1/2 failed: [Errno 12] Cannot allocate memory
# 두 번째 시도에서도 메모리 부족으로 실패.
WARNING ⚠️ Retry 2/2 failed: [Errno 12] Cannot allocate memory
# 최종적으로도 메모리 부족으로 인해 필요한 패키지 설치에 실패했다는 경고.
WARNING ⚠️ requirements: ❌ [Errno 12] Cannot allocate memory
# createInferRuntime에 전달된 로거(logger)가 기존에 사용된 것과 다르다는 경고.
# (하지만 글로벌 로거가 계속 사용되므로 실제 동작에는 영향 없음.)
[09/20/2025-06:17:56] [TRT] [I] The logger passed into createInferRuntime differs from one already provided for an existing builder, runtime, or refitter. Uses of the global logger, returned by nvinfer1::getLogger(), will return the existing value.        
# CUDA 초기화, CPU/GPU 메모리 사용량 변화 없음(현재 CPU 2007MiB, GPU 3873MiB 사용 중).
[09/20/2025-06:17:56] [TRT] [I] [MemUsageChange] Init CUDA: CPU +0, GPU +0, now: CPU 2007, GPU 3873 (MiB)
# 로드된 TensorRT 엔진 파일 크기는 16MiB임.
[09/20/2025-06:17:56] [TRT] [I] Loaded engine size: 16 MiB
# cuBLAS/cuBLASLt 초기화, CPU/GPU 메모리 사용량 변화 없음(현재 CPU 2016MiB, GPU 3869MiB 사용 중).
[09/20/2025-06:17:56] [TRT] [I] [MemUsageChange] Init cuBLAS/cuBLASLt: CPU +0, GPU +0, now: CPU 2016, GPU 3869 (MiB)
# cuDNN 초기화, CPU/GPU 메모리 사용량 변화 없음(현재 CPU 2016MiB, GPU 3869MiB 사용 중).
[09/20/2025-06:17:56] [TRT] [I] [MemUsageChange] Init cuDNN: CPU +0, GPU +0, now: CPU 2016, GPU 3869 (MiB)
# 엔진 역직렬화 과정에서 TensorRT가 GPU 메모리 14MiB를 추가로 할당함(현재 CPU 0MiB, GPU 14MiB 사용 중).
[09/20/2025-06:17:56] [TRT] [I] [MemUsageChange] TensorRT-managed allocation in engine deserialization: CPU +0, GPU +14, now: CPU 0, GPU 14 (MiB)
# cuBLAS/cuBLASLt 재초기화, CPU/GPU 메모리 사용량 변화 없음(현재 CPU 2032MiB, GPU 3869MiB 사용 중).
[09/20/2025-06:17:56] [TRT] [I] [MemUsageChange] Init cuBLAS/cuBLASLt: CPU +0, GPU +0, now: CPU 2032, GPU 3869 (MiB)
# cuDNN 재초기화, GPU 메모리 2MiB 증가(현재 CPU 2032MiB, GPU 3871MiB 사용 중).
[09/20/2025-06:17:56] [TRT] [I] [MemUsageChange] Init cuDNN: CPU +0, GPU +2, now: CPU 2032, GPU 3871 (MiB)
# IExecutionContext 생성 과정에서 TensorRT가 GPU 메모리 33MiB를 추가로 할당함(현재 CPU 0MiB, GPU 47MiB 사용 중).
[09/20/2025-06:17:56] [TRT] [I] [MemUsageChange] TensorRT-managed allocation in IExecutionContext creation: CPU +0, GPU +33, now: CPU 0, GPU 47 (MiB)
# tensorrt 패키지에서 np.bool 사용에 대해, 앞으로는 numpy의 bool이 numpy 스칼라로 정의될 것이라는 경고(FutureWarning).
/usr/local/lib/python3.8/dist-packages/tensorrt/__init__.py:165: FutureWarning: In the future `np.bool` will be defined as the corresponding NumPy scalar.
  bool: np.bool,
# 에러(예외) 발생 위치 추적 시작.
Traceback (most recent call last):
# test_yolo11n_tensorRT.py 파일의 13번째 줄에서 trt_model() 함수 실행 중 에러 발생.
  File "test_yolo11n_tensorRT.py", line 13, in <module>
    results = trt_model("https://ultralytics.com/images/bus.jpg")
# model.py의 187번째 줄에서 self.predict() 호출.
  File "/ultralytics/ultralytics/engine/model.py", line 187, in __call__
    return self.predict(source, stream, **kwargs)
# model.py의 550번째 줄에서 self.predictor.setup_model() 호출.
  File "/ultralytics/ultralytics/engine/model.py", line 550, in predict
    self.predictor.setup_model(model=self.model, verbose=is_cli)
# predictor.py의 397번째 줄에서 AutoBackend 객체 생성.
  File "/ultralytics/ultralytics/engine/predictor.py", line 397, in setup_model
    self.model = AutoBackend(
# grad_mode.py의 27번째 줄에서 함수 실행.
  File "/usr/local/lib/python3.8/dist-packages/torch/autograd/grad_mode.py", line 27, in decorate_context
    return func(*args, **kwargs)
# autobackend.py의 387번째 줄에서 trt.nptype() 호출.
  File "/ultralytics/ultralytics/nn/autobackend.py", line 387, in __init__
    dtype = trt.nptype(model.get_binding_dtype(i))
# tensorrt의 165번째 줄에서 np.bool 사용.
  File "/usr/local/lib/python3.8/dist-packages/tensorrt/__init__.py", line 165, in nptype
    bool: np.bool,
# numpy의 305번째 줄에서 np.bool 속성이 없어서 AttributeError 발생.
  File "/usr/local/lib/python3.8/dist-packages/numpy/__init__.py", line 305, in __getattr__
    raise AttributeError(__former_attrs__[attr])
# numpy 모듈에 'bool' 속성이 없다는 에러.
AttributeError: module 'numpy' has no attribute 'bool'.
# np.bool은 파이썬 내장 bool의 deprecated(더 이상 사용되지 않음) 별칭이었음. 기존 코드는 그냥 bool로 바꾸면 되고, numpy 타입이 필요하면 np.bool_을 사용하라는 안내.
`np.bool` was a deprecated alias for the builtin `bool`. To avoid this error in existing code, use `bool` by itself. Doing this 
will not modify any behavior and is safe. If you specifically wanted the numpy scalar type, use `np.bool_` here.
# 이 별칭은 numpy 1.20부터 deprecated 되었으며, 자세한 내용은 공식 문서를 참고하라는 안내.
The aliases was originally deprecated in NumPy 1.20; for more details and guidance see the original release note at:
    https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations
# (프롬프트) 명령어 입력 대기 상태.
root@4d964ff22ba6:/workspace/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation#

```

**출력 결과 재 확인: 코드 실행 전 후 주요 라이브러리 셋에 변경 사항이 있는지 체크하기 위함**
```bash
root@4d964ff22ba6:/ultralytics# python3 -c "import numpy; print(numpy.__version__)"
1.24.4
root@4d964ff22ba6:/ultralytics# python3 -c "import torch; print(torch.__version__)"
1.11.0a0+gitbc2c6ed
root@4d964ff22ba6:/ultralytics# python3 -c "import tensorrt; print(tensorrt.__version__)"
8.2.0.6
root@4d964ff22ba6:/ultralytics# python3 -c "import ultralytics; print(ultralytics.__version__)"
8.3.202
```