# 2025-09-19 | Jetson Nano Tensorflow GPU 개발 환경 확인(CUDA, cuDNN)

---
## 1. 현재 설치되어 있는 CUDA 버전 확인
```bash
nvcc --version
```
**출력 결과:**
```bash
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2021 NVIDIA Corporation
Built on Sun_Feb_28_22:34:44_PST_2021
Cuda compilation tools, release 10.2, V10.2.300
Build cuda_10.2_r440.TC440_70.29663091_0
```
현재 설치된 CUDA 버전은 10.2.300

## 2. 현재 설치되어 있는 cuDNN 버전 확인
```bash
cat /usr/include/cudnn_version.h | grep CUDNN_MAJOR -A 2
```
**출력 결과:**
```bash
(jetson) user@ubuntu:~$ cat /usr/include/cudnn_version.h | grep CUDNN_MAJOR -A 2
#define CUDNN_MAJOR 8
#define CUDNN_MINOR 2
#define CUDNN_PATCHLEVEL 1
--
#define CUDNN_VERSION (CUDNN_MAJOR * 1000 + CUDNN_MINOR * 100 + CUDNN_PATCHLEVEL)

#endif /* CUDNN_VERSION_H */
```

- 현재 설치된 cuDNN 버전은 8.2.1


## 3. 현재 설치되어 있는 Tensorflow 버전 확인
```bash
python -c "import tensorflow as tf; print(tf.__version__)"
```
**출력 결과:**
```bash

```
