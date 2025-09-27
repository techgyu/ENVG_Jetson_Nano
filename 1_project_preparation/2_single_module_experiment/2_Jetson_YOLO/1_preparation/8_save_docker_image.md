# 2025-09-22 | Jetson Nano 실험이 성공한 Docker 이미지 저장

---

## 1. 컨테이너 조회
```bash
docker ps
```
**출력 결과**
```bash
user@ubuntu:~/Desktop/ENVG_Jetson_Nano$ docker ps
CONTAINER ID   IMAGE                                            COMMAND       CREATED      STATUS      PORTS     NAMES
4d964ff22ba6   ultralytics/ultralytics:latest-jetson-jetpack4   "/bin/bash"   2 days ago   Up 2 days    
         jetson_yolo11
```

## 2. 이미지 저장
```bash
docker commit 4d964ff22ba6 my_yolo11n_image:v1
```

## 3. 저장된 이미지 확인
```bash
docker images
```
**출력 결과**
```bash
user@ubuntu:~/Desktop/ENVG_Jetson_Nano$ docker images
REPOSITORY                TAG                      IMAGE ID       CREATED              SIZE
my_yolo11n_image          v1                       9a7eba310c71   About a minute ago   5.62GB
ultralytics/ultralytics   latest-jetson-jetpack4   bab69653dae5   2 days ago           5.54GB
```
## 4. Docker 컨테이너 실행
```bash
sudo docker run -it -d --name jetson_yolo11_v1 -v ${PWD}:/workspace --ipc=host --runtime=nvidia my_yolo11n_image:v1
```

## 5. 컨테이너 목록 확인
```bash
sudo docker ps -a
```

## 6. 컨테이너 시작
```bash
sudo docker start jetson_yolo11_v1
sudo docker exec -it jetson_yolo11_v1 bash
```

## 7. 기존에 빌드된 yolo11n 모델 삭제
```bash
rm 'yolo11n.engine' 'yolo11n.onnx' 'yolo11n.pt'
```

## 8. 폴더 삭제
```bash
rm -r runs
``` 

## 9. YOLO11n 빌드 코드 실행
```bash
python3 test2_yolo11n_tensorRT.py
```

**출력 결과**
```bash
root@a356d03d6698:/workspace/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation# python3 test2_yolo11n_tensorRT.py
test2_yolo11n_tensorRT.py:2: DeprecationWarning: `np.bool` is a deprecated alias for the builtin `bool`. To silence this warning, use `bool` by itself. Doing this will not modify any behavior and is safe. If you 
specifically wanted the numpy scalar type, use `np.bool_` here.
Deprecated in NumPy 1.20; for more details and guidance: https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations
  if not hasattr(np, 'bool'):
Downloading https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt to 'yolo11n.pt': 100Downloading https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt to 'yolo11n.pt': 100% ━━━━━━━━━━━━ 5.4MB 67.8MB/s 0.1s
WARNING ⚠️ TensorRT requires GPU export, automatically assigning device=0
Ultralytics 8.3.202 🚀 Python-3.8.0 torch-1.11.0a0+gitbc2c6ed CUDA:0 (NVIDIA Tegra X1, 3964MiB)
YOLO11n summary (fused): 100 layers, 2,616,248 parameters, 0 gradients, 6.5 GFLOPs

PyTorch: starting from 'yolo11n.pt' with input shape (1, 3, 640, 640) BCHW and output shape(s) (1, 84, 8400) (5.4 MB)

ONNX: starting export with onnx 1.12.0 opset 14...
WARNING: The shape inference of prim::Constant type is missing, so it may result in wrong shape inference 
for the exported graph. Please consider adding it in symbolic function.
WARNING: The shape inference of prim::Constant type is missing, so it may result in wrong shape inference 
for the exported graph. Please consider adding it in symbolic function.
WARNING: The shape inference of prim::Constant type is missing, so it may result in wrong shape inference 
for the exported graph. Please consider adding it in symbolic function.
WARNING: The shape inference of prim::Constant type is missing, so it may result in wrong shape inference 
for the exported graph. Please consider adding it in symbolic function.
WARNING: The shape inference of prim::Constant type is missing, so it may result in wrong shape inference 
for the exported graph. Please consider adding it in symbolic function.
WARNING: The shape inference of prim::Constant type is missing, so it may result in wrong shape inference 
for the exported graph. Please consider adding it in symbolic function.
WARNING ⚠️ ONNX: simplifier failure: FLOAT8E4M3FN
ONNX: export success ✅ 14.4s, saved as 'yolo11n.onnx' (10.2 MB)

TensorRT: starting export with TensorRT 8.2.0.6...
[09/22/2025-07:24:23] [TRT] [I] [MemUsageChange] Init CUDA: CPU +210, GPU +0, now: CPU 1465, GPU 3842 (MiB)
[09/22/2025-07:24:24] [TRT] [I] [MemUsageSnapshot] Begin constructing builder kernel library: CPU 1465 MiB, GPU 3857 MiB
[09/22/2025-07:24:24] [TRT] [I] [MemUsageSnapshot] End constructing builder kernel library: CPU 1494 MiB, 
GPU 3845 MiB
[09/22/2025-07:24:24] [TRT] [I] ----------------------------------------------------------------
[09/22/2025-07:24:24] [TRT] [I] Input filename:   yolo11n.onnx
[09/22/2025-07:24:24] [TRT] [I] ONNX IR version:  0.0.7
[09/22/2025-07:24:24] [TRT] [I] Opset version:    14
[09/22/2025-07:24:24] [TRT] [I] Producer name:    pytorch
[09/22/2025-07:24:24] [TRT] [I] Producer version: 1.11.0
[09/22/2025-07:24:24] [TRT] [I] Domain:
[09/22/2025-07:24:24] [TRT] [I] Model version:    0
[09/22/2025-07:24:24] [TRT] [I] Doc string:
[09/22/2025-07:24:24] [TRT] [I] ----------------------------------------------------------------
[09/22/2025-07:24:24] [TRT] [W] onnx2trt_utils.cpp:366: Your ONNX model has been generated with INT64 weights, while TensorRT does not natively support INT64. Attempting to cast down to INT32.
TensorRT: input "images" with shape(1, 3, 640, 640) DataType.FLOAT
TensorRT: output "output0" with shape(1, 84, 8400) DataType.FLOAT
TensorRT: building FP32 engine as yolo11n.engine
[09/22/2025-07:24:25] [TRT] [I] ---------- Layers Running on DLA ----------
[09/22/2025-07:24:25] [TRT] [I] ---------- Layers Running on GPU ----------
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_0
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_1), Mul_2)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_3
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_4), Mul_5)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_6
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_7), Mul_8)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Split_10
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Split_10_0
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_11
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_12), Mul_13)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_14
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_15), Mul_16), Add_17)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] input.12 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_19
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_20), Mul_21)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_22
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_23), Mul_24)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_25
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_26), Mul_27)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_30
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_31), Mul_32)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_33
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_34), Mul_35), Add_36)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Concat_206 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] input.40 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_38
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_39), Mul_40)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_41
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_42), Mul_43)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_44
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_45), Mul_46)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_49 || Conv_66
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_50), Mul_51)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_67), Mul_68)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_52
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_53), Mul_54)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_55
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_56), Mul_57), Add_58)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_59
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_60), Mul_61)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_62
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_63), Mul_64), Add_65)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_70
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_71), Mul_72)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Concat_226 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] input.68 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_74
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_75), Mul_76)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_77
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_78), Mul_79)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_80
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_81), Mul_82)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_85 || Conv_102
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_86), Mul_87)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_103), Mul_104)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_88
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_89), Mul_90)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_91
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_92), Mul_93), Add_94)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_95
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_96), Mul_97)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_98
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_99), Mul_100), Add_101)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_106
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_107), Mul_108)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Concat_263 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] input.124 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_110
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_111), Mul_112)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_113
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_114), Mul_115)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] MaxPool_116
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] MaxPool_117
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] MaxPool_118
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::MaxPool_295 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::MaxPool_296 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::MaxPool_297 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Concat_298 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_120
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_121), Mul_122)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_123
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_124), Mul_125)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Split_127_4
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_128
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Reshape_129
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Split_131
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Split_131_5
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Split_131_6
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Reshape_140
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] MatMul_133
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Mul_333 + (Unnamed Layer* 136) [Shuffle] + Mul_135       
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Softmax_136
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] MatMul_138
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Reshape_139
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_141 + Add_142
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_143 + Add_144
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_145
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_146), Mul_147)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_148 + Add_149
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Concat_307 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Concat_366 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_151
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_152), Mul_153)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Resize_154
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Concat_375 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_156
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_157), Mul_158)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_161
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_162), Mul_163)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_164
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_165), Mul_166), Add_167)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Concat_381 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] input.224 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_169
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_170), Mul_171)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Resize_172
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Concat_398 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_174
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_175), Mul_176)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_179
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_180), Mul_181)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_182
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_183), Mul_184), Add_185)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Concat_404 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] input.252 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_187
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_188), Mul_189)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_190
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_247
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_254
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_191), Mul_192)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_248), Mul_249)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_255), Mul_256)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Resize_393 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_250
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_257
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_194
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_251), Mul_252)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_258), Mul_259)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_195), Mul_196)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_253
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_260
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_199
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_261), Mul_262)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_263
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_200), Mul_201)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_202
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_264), Mul_265)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_266
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_203), Mul_204), Add_205)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Concat_425 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] input.284 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_207
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_208), Mul_209)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Reshape_316
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_210
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_268
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_275
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_211), Mul_212)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_269), Mul_270)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_276), Mul_277)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Resize_370 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_271
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_278
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_214
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_272), Mul_273)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_279), Mul_280)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_215), Mul_216)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_274
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_281
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_219 || Conv_236
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_282), Mul_283)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_284
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_220), Mul_221)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_237), Mul_238)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_222
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_285), Mul_286)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_287
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_223), Mul_224)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_225
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Reshape_320
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_226), Mul_227), Add_228)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_229
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_230), Mul_231)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_232
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(PWN(Sigmoid_233), Mul_234), Add_235)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_240
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_241), Mul_242)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Concat_446 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] input.316 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_244
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_245), Mul_246)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_289
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_296
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_290), Mul_291)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_297), Mul_298)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_292
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_299
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_293), Mul_294)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_300), Mul_301)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_295
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_302
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_303), Mul_304)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_305
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(PWN(Sigmoid_306), Mul_307)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_308
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Reshape_324
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Concat_551 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Concat_561 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Concat_571 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Split_327
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Split_327_11
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Reshape_339 + Transpose_340
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Softmax_341
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Conv_342
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Reshape_348
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Slice_359
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Slice_362
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Sub_620
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Sub_364
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Add_622
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Add_366
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(onnx::Div_625 + (Unnamed Layer* 413) [Shuffle], PWN(Add_367, Div_369))
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Sub_370
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Concat_626 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Concat_627 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Mul_629 + (Unnamed Layer* 418) [Shuffle]
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] Mul_373
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] PWN(Sigmoid_374)
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Concat_630 copy
[09/22/2025-07:24:25] [TRT] [I] [GpuLayer] onnx::Concat_631 copy
[09/22/2025-07:24:25] [TRT] [I] [MemUsageChange] Init cuBLAS/cuBLASLt: CPU +0, GPU +0, now: CPU 1507, GPU 
3851 (MiB)
[09/22/2025-07:24:29] [TRT] [I] [MemUsageChange] Init cuDNN: CPU +241, GPU -27, now: CPU 1748, GPU 3824 (MiB)
[09/22/2025-07:24:29] [TRT] [I] Local timing cache in use. Profiling results in this builder pass will not be stored.
[09/22/2025-07:24:52] [TRT] [I] Some tactics do not have sufficient workspace memory to run. Increasing workspace size may increase performance, please check verbose output.
[09/22/2025-07:27:38] [TRT] [I] Detected 1 inputs and 3 output network tensors.
[09/22/2025-07:27:38] [TRT] [I] Total Host Persistent Memory: 196976
[09/22/2025-07:27:38] [TRT] [I] Total Device Persistent Memory: 14257664
[09/22/2025-07:27:38] [TRT] [I] Total Scratch Memory: 0
[09/22/2025-07:27:38] [TRT] [I] [MemUsageStats] Peak memory usage of TRT CPU/GPU memory allocators: CPU 2 
MiB, GPU 171 MiB
[09/22/2025-07:27:38] [TRT] [I] [BlockAssignment] Algorithm ShiftNTopDown took 186.396ms to assign 9 blocks to 193 nodes requiring 19456001 bytes.
[09/22/2025-07:27:38] [TRT] [I] Total Activation Memory: 19456001
[09/22/2025-07:27:39] [TRT] [I] [MemUsageChange] Init cuBLAS/cuBLASLt: CPU +0, GPU +8, now: CPU 2007, GPU 
3900 (MiB)
[09/22/2025-07:27:39] [TRT] [I] [MemUsageChange] Init cuDNN: CPU +1, GPU -5, now: CPU 2008, GPU 3895 (MiB)[09/22/2025-07:27:39] [TRT] [I] [MemUsageChange] TensorRT-managed allocation in building engine: CPU +0, GPU +16, now: CPU 0, GPU 16 (MiB)
TensorRT: export success ✅ 214.7s, saved as 'yolo11n.engine' (16.3 MB)

Export complete (227.3s)
Results saved to /workspace/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation  
Predict:         yolo predict task=detect model=yolo11n.engine imgsz=640
Validate:        yolo val task=detect model=yolo11n.engine imgsz=640 data=/usr/src/ultralytics/ultralytics/cfg/datasets/coco.yaml
Visualize:       https://netron.app
WARNING ⚠️ Unable to automatically guess model task, assuming 'task=detect'. Explicitly define task for yo
ur model, i.e. 'task=detect', 'segment', 'classify','pose' or 'obb'.
Loading yolo11n.engine for TensorRT inference...
[09/22/2025-07:27:39] [TRT] [I] The logger passed into createInferRuntime differs from one already provided for an existing builder, runtime, or refitter. Uses of the global logger, returned by nvinfer1::getLogger(), will return the existing value.

[09/22/2025-07:27:39] [TRT] [I] [MemUsageChange] Init CUDA: CPU +0, GPU +0, now: CPU 2008, GPU 3896 (MiB)
[09/22/2025-07:27:39] [TRT] [I] Loaded engine size: 16 MiB
[09/22/2025-07:27:40] [TRT] [I] [MemUsageChange] Init cuBLAS/cuBLASLt: CPU +0, GPU +0, now: CPU 2016, GPU 
3896 (MiB)
[09/22/2025-07:27:40] [TRT] [I] [MemUsageChange] Init cuDNN: CPU +0, GPU +0, now: CPU 2016, GPU 3896 (MiB)[09/22/2025-07:27:40] [TRT] [I] [MemUsageChange] TensorRT-managed allocation in engine deserialization: CPU +0, GPU +14, now: CPU 0, GPU 14 (MiB)
[09/22/2025-07:27:40] [TRT] [I] [MemUsageChange] Init cuBLAS/cuBLASLt: CPU +0, GPU +0, now: CPU 2032, GPU 
3897 (MiB)
[09/22/2025-07:27:40] [TRT] [I] [MemUsageChange] Init cuDNN: CPU +0, GPU +0, now: CPU 2032, GPU 3897 (MiB)[09/22/2025-07:27:40] [TRT] [I] [MemUsageChange] TensorRT-managed allocation in IExecutionContext creation: CPU +0, GPU +33, now: CPU 0, GPU 47 (MiB)

Downloading https://ultralytics.com/images/bus.jpg to 'bus.jpg': 100% ━━━━━━━━━━━━ 134.2KB 10.0MB/s 0.0s  
image 1/1 /workspace/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation/bus.jpg: 640x640 4 persons, 1 bus, 76.7ms
Speed: 270.5ms preprocess, 76.7ms inference, 272.9ms postprocess per image at shape (1, 3, 640, 640)      
root@a356d03d6698:/workspace/1_project_preparation/2_single_module_experiment/1_Jetson_YOLO/1_preparation#
```
- 정상 동작 확인 완료