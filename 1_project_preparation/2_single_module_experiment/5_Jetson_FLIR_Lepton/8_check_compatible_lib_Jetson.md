# 2025-09-23 | Jetson Nano에서 호환이 가능한 라이브러리 실험

---

## 1. flirpy 설치 시도
```bash
pip install flirpy
```

**출력 로그**
```bash
root@12caaef4bcf9:/workspace/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/3_Jetson_FLIR_Lepton# pip install flirpy
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
Requirement already satisfied: importlib-resources>=5.7.1 in /usr/local/lib/python3.8/dist-packages (from pkg-about>=1.0.7->libusb->flirpy) 
(6.4.5)
Requirement already satisfied: importlib-metadata>=4.12.0 in /usr/local/lib/python3.8/dist-packages (from pkg-about>=1.0.7->libusb->flirpy) 
(8.5.0)
Collecting tomli>=2.0.1 (from pkg-about>=1.0.7->libusb->flirpy)
  Downloading tomli-2.2.1-py3-none-any.whl.metadata (10 kB)
Requirement already satisfied: zipp>=3.20 in /usr/local/lib/python3.8/dist-packages (from importlib-metadata>=4.12.0->pkg-about>=1.0.7->libusb->flirpy) (3.20.2)
Downloading flirpy-0.3.0-py3-none-any.whl (10.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.2/10.2 MB 21.0 MB/s eta 0:00:00
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
      Successfully uninstalled packaging-20.9 # packaging-20.9 제거 성공
# 에러 발생
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. 

# 아래와 같은 의존성 충돌이 발생함
This behaviour is the source of the following dependency conflicts.

# tensorflowjs 3.18.0은 packaging~=20.9 필요, 그러나 현재 packaging 25.0이 설치되어 있어 호환되지 않음
tensorflowjs 3.18.0 requires packaging~=20.9, but you have packaging 25.0 which is incompatible.

# 설치 성공한 패키지 목록
Successfully installed flirpy-0.3.0 libusb-1.0.26b5 natsort-8.4.0 packaging-25.0 pkg-about-1.0.8 pyftdi-0.55.4 pyserial-3.5 pyudev-0.24.3 pyusb-1.2.1 tomli-2.2.1 # packaging 25.0 설치되었음

# 경고 발생
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.

root@12caaef4bcf9:/workspace/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/3_Jetson_FLIR_Lepton#
```
### 1.1 결과 요약
- `flirpy` 설치는 성공했으나, `packaging` 패키지 버전(25.0 -> 20.0) 충돌로 인해 `tensorflowjs`가 영향을 받는 문제(20.9 미만 요구)가 발생함.

## 2. packaging, tensorflowjs 충돌 발생한 상황에서 yolo11n 빌드 시도

**출력 로그**
```bash
root@12caaef4bcf9:/workspace/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_root@12caaef4bcf9:/workspace/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation# python3 test2_yolo11n_tensorRT.py
test2_yolo11n_tensorRT.py:2: DeprecationWarning: `np.bool` is a deprecated alias for the builtin `bool`. To silence this warning, use `bool` by itself. Doing this will not modify any behavior and is safe. If you specifically wanted the numpy scalar type, use `np.bool_` here.     
Deprecated in NumPy 1.20; for more details and guidance: https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations
  if not hasattr(np, 'bool'):
Downloading https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt to 'yolo11n.pt': 59% ━━━━━━━───── 3.2/5.4MB 31.8MB/s 0Downloading https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt to 'yolo11n.pt': 100% ━━━━━━━━━━━━ 5.4MB 35.6MB/s 0.2sWARNING ⚠️ TensorRT requires GPU export, automatically assigning device=0
Ultralytics 8.3.202 🚀 Python-3.8.0 torch-1.11.0a0+gitbc2c6ed CUDA:0 (NVIDIA Tegra X1, 3964MiB)
YOLO11n summary (fused): 100 layers, 2,616,248 parameters, 0 gradients, 6.5 GFLOPs

PyTorch: starting from 'yolo11n.pt' with input shape (1, 3, 640, 640) BCHW and output shape(s) (1, 84, 8400) (5.4 MB)

ONNX: starting export with onnx 1.12.0 opset 14...
WARNING: The shape inference of prim::Constant type is missing, so it may result in wrong shape inference for the exported graph. Please consider adding it in symbolic function.
WARNING: The shape inference of prim::Constant type is missing, so it may result in wrong shape inference for the exported graph. Please consider adding it in symbolic function.
WARNING: The shape inference of prim::Constant type is missing, so it may result in wrong shape inference for the exported graph. Please consider adding it in symbolic function.
WARNING: The shape inference of prim::Constant type is missing, so it may result in wrong shape inference for the exported graph. Please consider adding it in symbolic function.
WARNING: The shape inference of prim::Constant type is missing, so it may result in wrong shape inference for the exported graph. Please consider adding it in symbolic function.
WARNING: The shape inference of prim::Constant type is missing, so it may result in wrong shape inference for the exported graph. Please consider adding it in symbolic function.
WARNING ⚠️ ONNX: simplifier failure: FLOAT8E4M3FN
ONNX: export success ✅ 14.3s, saved as 'yolo11n.onnx' (10.2 MB)

TensorRT: starting export with TensorRT 8.2.0.6...
[09/23/2025-01:35:15] [TRT] [I] [MemUsageChange] Init CUDA: CPU +210, GPU +0, now: CPU 1465, GPU 3544 (MiB)
[09/23/2025-01:35:16] [TRT] [I] [MemUsageSnapshot] Begin constructing builder kernel library: CPU 1465 MiB, GPU 3524 MiB
[09/23/2025-01:35:16] [TRT] [I] [MemUsageSnapshot] End constructing builder kernel library: CPU 1495 MiB, GPU 3554 MiB
[09/23/2025-01:35:16] [TRT] [I] ----------------------------------------------------------------
[09/23/2025-01:35:16] [TRT] [I] Input filename:   yolo11n.onnx
[09/23/2025-01:35:16] [TRT] [I] ONNX IR version:  0.0.7
[09/23/2025-01:35:16] [TRT] [I] Opset version:    14
[09/23/2025-01:35:16] [TRT] [I] Producer name:    pytorch
[09/23/2025-01:35:16] [TRT] [I] Producer version: 1.11.0
[09/23/2025-01:35:16] [TRT] [I] Domain:
[09/23/2025-01:35:16] [TRT] [I] Model version:    0
[09/23/2025-01:35:16] [TRT] [I] Doc string:
[09/23/2025-01:35:16] [TRT] [I] ----------------------------------------------------------------
[09/23/2025-01:35:16] [TRT] [W] onnx2trt_utils.cpp:366: Your ONNX model has been generated with INT64 weights, while TensorRT does not natively support INT64. Attempting to cast down to INT32.
TensorRT: input "images" with shape(1, 3, 640, 640) DataType.FLOAT
TensorRT: output "output0" with shape(1, 84, 8400) DataType.FLOAT
TensorRT: building FP32 engine as yolo11n.engine
[09/23/2025-01:35:17] [TRT] [I] ---------- Layers Running on DLA ----------
[09/23/2025-01:35:17] [TRT] [I] ---------- Layers Running on GPU ----------
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_0
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_1), Mul_2)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_3
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_4), Mul_5)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_6
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_7), Mul_8)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Split_10
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Split_10_0
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_11
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_12), Mul_13)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_14
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_15), Mul_16), Add_17)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] input.12 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_19
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_20), Mul_21)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_22
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_23), Mul_24)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_25
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_26), Mul_27)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_30
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_31), Mul_32)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_33
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_34), Mul_35), Add_36)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Concat_206 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] input.40 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_38
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_39), Mul_40)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_41
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_42), Mul_43)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_44
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_45), Mul_46)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_49 || Conv_66
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_50), Mul_51)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_67), Mul_68)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_52
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_53), Mul_54)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_55
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_56), Mul_57), Add_58)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_59
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_60), Mul_61)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_62
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_63), Mul_64), Add_65)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_70
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_71), Mul_72)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Concat_226 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] input.68 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_74
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_75), Mul_76)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_77
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_78), Mul_79)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_80
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_81), Mul_82)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_85 || Conv_102
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_86), Mul_87)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_103), Mul_104)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_88
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_89), Mul_90)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_91
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_92), Mul_93), Add_94)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_95
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_96), Mul_97)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_98
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_99), Mul_100), Add_101)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_106
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_107), Mul_108)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Concat_263 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] input.124 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_110
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_111), Mul_112)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_113
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_114), Mul_115)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] MaxPool_116
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] MaxPool_117
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] MaxPool_118
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::MaxPool_295 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::MaxPool_296 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::MaxPool_297 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Concat_298 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_120
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_121), Mul_122)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_123
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_124), Mul_125)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Split_127_4
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_128
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Reshape_129
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Split_131
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Split_131_5
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Split_131_6
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Reshape_140
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] MatMul_133
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Mul_333 + (Unnamed Layer* 136) [Shuffle] + Mul_135
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Softmax_136
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] MatMul_138
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Reshape_139
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_141 + Add_142
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_143 + Add_144
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_145
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_146), Mul_147)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_148 + Add_149
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Concat_307 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Concat_366 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_151
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_152), Mul_153)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Resize_154
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Concat_375 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_156
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_157), Mul_158)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_161
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_162), Mul_163)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_164
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_165), Mul_166), Add_167)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Concat_381 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] input.224 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_169
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_170), Mul_171)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Resize_172
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Concat_398 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_174
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_175), Mul_176)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_179
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_180), Mul_181)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_182
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_183), Mul_184), Add_185)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Concat_404 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] input.252 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_187
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_188), Mul_189)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_190
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_247
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_254
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_191), Mul_192)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_248), Mul_249)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_255), Mul_256)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Resize_393 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_250
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_257
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_194
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_251), Mul_252)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_258), Mul_259)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_195), Mul_196)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_253
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_260
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_199
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_261), Mul_262)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_263
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_200), Mul_201)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_202
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_264), Mul_265)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_266
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_203), Mul_204), Add_205)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Concat_425 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] input.284 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_207
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_208), Mul_209)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Reshape_316
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_210
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_268
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_275
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_211), Mul_212)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_269), Mul_270)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_276), Mul_277)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Resize_370 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_271
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_278
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_214
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_272), Mul_273)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_279), Mul_280)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_215), Mul_216)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_274
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_281
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_219 || Conv_236
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_282), Mul_283)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_284
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_220), Mul_221)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_237), Mul_238)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_222
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_285), Mul_286)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_287
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_223), Mul_224)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_225
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Reshape_320
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_226), Mul_227), Add_228)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_229
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_230), Mul_231)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_232
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_233), Mul_234), Add_235)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_240
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_241), Mul_242)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Concat_446 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] input.316 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_244
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_245), Mul_246)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_289
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_296
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_290), Mul_291)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_297), Mul_298)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_292
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_299
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_293), Mul_294)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_300), Mul_301)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_295
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_302
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_303), Mul_304)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_305
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_306), Mul_307)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_308
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Reshape_324
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Concat_551 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Concat_561 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Concat_571 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Split_327
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Split_327_11
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Reshape_339 + Transpose_340
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Softmax_341
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Conv_342
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Reshape_348
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Slice_359
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Slice_362
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Sub_620
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Sub_364
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Add_622
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Add_366
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(onnx::Div_625 + (Unnamed Layer* 413) [Shuffle], PWN(Add_367, Div_369))
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Sub_370
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Concat_626 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Concat_627 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Mul_629 + (Unnamed Layer* 418) [Shuffle]
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] Mul_373
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] PWN(Sigmoid_374)
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Concat_630 copy
[09/23/2025-01:35:17] [TRT] [I] [GpuLayer] onnx::Concat_631 copy
[09/23/2025-01:35:17] [TRT] [I] [MemUsageChange] Init cuBLAS/cuBLASLt: CPU +0, GPU +0, now: CPU 1507, GPU 3526 (MiB)
[09/23/2025-01:35:21] [TRT] [I] [MemUsageChange] Init cuDNN: CPU +241, GPU +21, now: CPU 1748, GPU 3547 (MiB)
[09/23/2025-01:35:21] [TRT] [I] Local timing cache in use. Profiling results in this builder pass will not be stored.
[09/23/2025-01:35:43] [TRT] [I] Some tactics do not have sufficient workspace memory to run. Increasing workspace size may increase performance, please check verbose output.
[09/23/2025-01:38:26] [TRT] [I] Detected 1 inputs and 3 output network tensors.
[09/23/2025-01:38:26] [TRT] [I] Total Host Persistent Memory: 198016
[09/23/2025-01:38:26] [TRT] [I] Total Device Persistent Memory: 13641216
[09/23/2025-01:38:26] [TRT] [I] Total Scratch Memory: 0
[09/23/2025-01:38:26] [TRT] [I] [MemUsageStats] Peak memory usage of TRT CPU/GPU memory allocators: CPU 2 MiB, GPU 171 MiB
[09/23/2025-01:38:27] [TRT] [I] [BlockAssignment] Algorithm ShiftNTopDown took 188.018ms to assign 10 blocks to 195 nodes requiring 19456002 bytes.
[09/23/2025-01:38:27] [TRT] [I] Total Activation Memory: 19456002
[09/23/2025-01:38:27] [TRT] [I] [MemUsageChange] Init cuBLAS/cuBLASLt: CPU +1, GPU +2, now: CPU 2007, GPU 3633 (MiB)
[09/23/2025-01:38:27] [TRT] [I] [MemUsageChange] Init cuDNN: CPU +0, GPU +6, now: CPU 2007, GPU 3639 (MiB)
[09/23/2025-01:38:27] [TRT] [I] [MemUsageChange] TensorRT-managed allocation in building engine: CPU +0, GPU +16, now: CPU 0, GPU 16 (MiB)
TensorRT: export success ✅ 210.7s, saved as 'yolo11n.engine' (15.7 MB)

Export complete (224.1s)
Results saved to /workspace/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation
Predict:         yolo predict task=detect model=yolo11n.engine imgsz=640
Validate:        yolo val task=detect model=yolo11n.engine imgsz=640 data=/usr/src/ultralytics/ultralytics/cfg/datasets/coco.yaml
Visualize:       https://netron.app
WARNING ⚠️ Unable to automatically guess model task, assuming 'task=detect'. Explicitly define task for your model, i.e. 'task=detect', 'seg
ment', 'classify','pose' or 'obb'.
Loading yolo11n.engine for TensorRT inference...
[09/23/2025-01:38:27] [TRT] [I] The logger passed into createInferRuntime differs from one already provided for an existing builder, runtime, or refitter. Uses of the global logger, returned by nvinfer1::getLogger(), will return the existing value.

[09/23/2025-01:38:27] [TRT] [I] [MemUsageChange] Init CUDA: CPU +0, GPU +0, now: CPU 2007, GPU 3687 (MiB)
[09/23/2025-01:38:27] [TRT] [I] Loaded engine size: 15 MiB
[09/23/2025-01:38:27] [TRT] [I] [MemUsageChange] Init cuBLAS/cuBLASLt: CPU +0, GPU +0, now: CPU 2015, GPU 3703 (MiB)
[09/23/2025-01:38:27] [TRT] [I] [MemUsageChange] Init cuDNN: CPU +0, GPU +0, now: CPU 2015, GPU 3703 (MiB)
[09/23/2025-01:38:27] [TRT] [I] [MemUsageChange] TensorRT-managed allocation in engine deserialization: CPU +0, GPU +14, now: CPU 0, GPU 14 
(MiB)
[09/23/2025-01:38:27] [TRT] [I] [MemUsageChange] Init cuBLAS/cuBLASLt: CPU +0, GPU +0, now: CPU 2031, GPU 3703 (MiB)
[09/23/2025-01:38:28] [TRT] [I] [MemUsageChange] Init cuDNN: CPU +0, GPU +0, now: CPU 2031, GPU 3703 (MiB)
[09/23/2025-01:38:28] [TRT] [I] [MemUsageChange] TensorRT-managed allocation in IExecutionContext creation: CPU +0, GPU +31, now: CPU 0, GPU 45 (MiB)

Downloading https://ultralytics.com/images/bus.jpg to 'bus.jpg': 100% ━━━━━━━━━━━━ 134.2KB 19.5MB/s 0.0s
image 1/1 /workspace/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation/bus.jpg: 640x640 
4 persons, 1 bus, 96.4ms
Speed: 178.6ms preprocess, 96.4ms inference, 281.6ms postprocess per image at shape (1, 3, 640, 640)
root@12caaef4bcf9:/workspace/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation# 
```

### 2.1 결과 요약
- packing, tensorflowjs 충돌 상태에서, yolov11n 모델을 TensorRT로 변환하는데 성공함.

## 3.1 flirpy 설치 테스트
```bash
pip show flirpy
```
**출력 결과**
```bash
root@12caaef4bcf9:/workspace/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation# pip show
 flirpy
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
root@12caaef4bcf9:/workspace/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation#
```

## 3.2 flirpy import 테스트
```bash
python3 -c "import flirpy; print('flirpy import 성공')"
```
**출력 결과**
```bash
root@12caaef4bcf9:/workspace/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation# python3 
-c "import flirpy; print('flirpy import 성공')"
flirpy import 성공
```
