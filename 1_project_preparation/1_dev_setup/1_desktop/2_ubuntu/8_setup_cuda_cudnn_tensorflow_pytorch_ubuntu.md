# 2025-09-17 | Desktop Ubuntu Tensorflow GPU 개발 환경 구축(CUDA, cuDNN, Tensorflow)

---

## 0. 현재 Desktop Ubuntu 환경 정보
- Ubuntu 22.04.3 LTS
- Anaconda 25.5.1
- GPU: NVIDIA RTX 4090 24GB

---

## 1. 공식 문서 및 버전 호환성 참고
- [Tensorflow GPU 지원 표](https://www.tensorflow.org/install/source#gpu)
- [PyTorch Get Started](https://pytorch.org/get-started/locally/)
- 주요 버전 조합 (2025년 9월 기준)
  - TensorFlow: 2.20.0
  - CUDA: 12.5
  - cuDNN: 9.3
  - Python: 3.9~3.13
  - GCC: 9.3 이상

---

## 2. 아나콘다 가상환경 생성
```bash
conda create -n tf_gpu python=3.13
conda activate tf_gpu
```
- 최신 Tensorflow, PyTorch 설치를 위한 별도 환경 생성

---

## 3. NVIDIA 드라이버 및 CUDA 12.5 설치 (공식 가이드 최신 기준)
 1. CUDA 저장소 pin 파일 등록
```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
```
2. CUDA 12.5 .deb 설치 파일 다운로드
```bash
wget https://developer.download.nvidia.com/compute/cuda/12.5.0/local_installers/cuda-repo-ubuntu2204-12-5-local_12.5.0-555.42.02-1_amd64.deb
```
3. CUDA 12.5 설치
```bash 
# .deb 파일 설치
sudo dpkg -i cuda-repo-ubuntu2204-12-5-local_12.5.0-555.42.02-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2204-12-5-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update

# CUDA 툴킷 설치
sudo apt-get -y install cuda-toolkit-12-5
```

4. 드라이버 설치 (선택, 이미 최신 드라이버가 있다면 생략 가능)
```bash
# 레거시 커널 모듈 드라이버
sudo apt-get install -y cuda-drivers

# 또는 오픈 커널 모듈 드라이버
sudo apt-get install -y nvidia-driver-555-open
sudo apt-get install -y cuda-drivers-555
```

5. 환경변수 등록
```bash
echo 'export PATH=/usr/local/cuda-12.5/bin${PATH:+:${PATH}}' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-12.5/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}' >> ~/.bashrc
source ~/.bashrc
```

6. 시스템 재부팅

7. 설치 확인
```bash
nvidia-smi
nvcc --version
```

---

## 4. cuDNN 9.3 설치 (CUDA 12.5용, 공식 가이드 기준)

> 아래 명령어는 반드시 Ubuntu 터미널에서 직접 입력해야 합니다.

1. cuDNN 9.3.0 설치 파일 다운로드  
   (공식 다운로드 페이지 또는 PC에서 받아 WinSCP 등으로 Ubuntu로 복사)
   ```bash
   wget https://developer.download.nvidia.com/compute/cudnn/9.3.0/local_installers/cudnn-local-repo-ubuntu2204-9.3.0_1.0-1_amd64.deb
   ```

2. 로컬 저장소 등록 및 키링 복사
   ```bash
   sudo dpkg -i cudnn-local-repo-ubuntu2204-9.3.0_1.0-1_amd64.deb
   sudo cp /var/cudnn-local-repo-ubuntu2204-9.3.0/cudnn-*-keyring.gpg /usr/share/keyrings/
   sudo apt-get update
   ```

   ```bash
   user@user:~$ sudo dpkg -i cudnn-local-repo-ubuntu2204-9.3.0_1.0-1_amd64.deb
    \Selecting previously unselected package cudnn-local-repo-ubuntu2204-9.3.0.
    (Reading database ... 218077 files and directories currently installed.)
    Preparing to unpack cudnn-local-repo-ubuntu2204-9.3.0_1.0-1_amd64.deb ...
    Unpacking cudnn-local-repo-ubuntu2204-9.3.0 (1.0-1) ...
    Setting up cudnn-local-repo-ubuntu2204-9.3.0 (1.0-1) ...

    The public cudnn-local-repo-ubuntu2204-9.3.0 GPG key does not appear to be installed.
    To install the key, run this command:
    sudo cp /var/cudnn-local-repo-ubuntu2204-9.3.0/cudnn-local-D9334AA3-keyring.gpg /usr/share/keyrings/

   user@user:~$ sudo apt-get update
    Get:1 file:/var/cuda-repo-ubuntu2204-12-5-local  InRelease [1,572 B]
    Get:2 file:/var/cudnn-local-repo-ubuntu2204-9.3.0  InRelease [1,572 B]
    Get:1 file:/var/cuda-repo-ubuntu2204-12-5-local  InRelease [1,572 B]
    Get:2 file:/var/cudnn-local-repo-ubuntu2204-9.3.0  InRelease [1,572 B]
    Get:3 file:/var/cudnn-local-repo-ubuntu2204-9.3.0  Packages [3,106 B]
    Hit:4 http://kr.archive.ubuntu.com/ubuntu jammy InRelease
    Hit:5 http://kr.archive.ubuntu.com/ubuntu jammy-updates InRelease                                                                       
    Hit:6 http://kr.archive.ubuntu.com/ubuntu jammy-backports InRelease
    Ign:7 http://dl.google.com/linux/chrome-remote-desktop/deb stable InRelease
    Hit:8 https://dl.google.com/linux/chrome/deb stable InRelease
    Hit:9 http://dl.google.com/linux/chrome-remote-desktop/deb stable Release    
    Hit:11 http://security.ubuntu.com/ubuntu jammy-security InRelease
    Reading package lists... Done
    ```

3. cuDNN 패키지 설치
   ```bash
   sudo apt-get -y install cudnn
   ```
   ```bash
    user@user:~$ sudo apt-get -y install cudnn
    Reading package lists... Done
    Building dependency tree... Done
    Reading state information... Done
    The following package was automatically installed and is no longer required:
    libffi7
    Use 'sudo apt autoremove' to remove it.
    The following additional packages will be installed:
    cudnn9 cudnn9-cuda-12 cudnn9-cuda-12-6 libcudnn9-cuda-12 libcudnn9-dev-cuda-12 libcudnn9-samples libcudnn9-static-cuda-12
    The following NEW packages will be installed:
    cudnn cudnn9 cudnn9-cuda-12 cudnn9-cuda-12-6 libcudnn9-cuda-12 libcudnn9-dev-cuda-12 libcudnn9-samples libcudnn9-static-cuda-12
    0 upgraded, 8 newly installed, 0 to remove and 0 not upgraded.
    Need to get 0 B/769 MB of archives.
    After this operation, 1,898 MB of additional disk space will be used.
    Get:1 file:/var/cudnn-local-repo-ubuntu2204-9.3.0  libcudnn9-cuda-12 9.3.0.75-1 [381 MB]
    Get:2 file:/var/cudnn-local-repo-ubuntu2204-9.3.0  libcudnn9-dev-cuda-12 9.3.0.75-1 [34.1 kB]
    Get:3 file:/var/cudnn-local-repo-ubuntu2204-9.3.0  libcudnn9-static-cuda-12 9.3.0.75-1 [387 MB]
    Get:4 file:/var/cudnn-local-repo-ubuntu2204-9.3.0  cudnn9-cuda-12-6 9.3.0.75-1 [12.3 kB]
    Get:5 file:/var/cudnn-local-repo-ubuntu2204-9.3.0  cudnn9-cuda-12 9.3.0.75-1 [12.3 kB]
    Get:6 file:/var/cudnn-local-repo-ubuntu2204-9.3.0  libcudnn9-samples 9.3.0.75-1 [1,672 kB]
    Get:7 file:/var/cudnn-local-repo-ubuntu2204-9.3.0  cudnn9 9.3.0-1 [2,438 B]
    Get:8 file:/var/cudnn-local-repo-ubuntu2204-9.3.0  cudnn 9.3.0-1 [2,414 B]
    Selecting previously unselected package libcudnn9-cuda-12.
    (Reading database ... 218103 files and directories currently installed.)
    Preparing to unpack .../0-libcudnn9-cuda-12_9.3.0.75-1_amd64.deb ...
    Unpacking libcudnn9-cuda-12 (9.3.0.75-1) ...
    Selecting previously unselected package libcudnn9-dev-cuda-12.
    Preparing to unpack .../1-libcudnn9-dev-cuda-12_9.3.0.75-1_amd64.deb ...
    Unpacking libcudnn9-dev-cuda-12 (9.3.0.75-1) ...
    Selecting previously unselected package libcudnn9-static-cuda-12.
    Preparing to unpack .../2-libcudnn9-static-cuda-12_9.3.0.75-1_amd64.deb ...
    Unpacking libcudnn9-static-cuda-12 (9.3.0.75-1) ...
    Selecting previously unselected package cudnn9-cuda-12-6.
    Preparing to unpack .../3-cudnn9-cuda-12-6_9.3.0.75-1_amd64.deb ...
    Unpacking cudnn9-cuda-12-6 (9.3.0.75-1) ...
    Selecting previously unselected package cudnn9-cuda-12.
    Preparing to unpack .../4-cudnn9-cuda-12_9.3.0.75-1_amd64.deb ...
    Unpacking cudnn9-cuda-12 (9.3.0.75-1) ...
    Selecting previously unselected package libcudnn9-samples.
    Preparing to unpack .../5-libcudnn9-samples_9.3.0.75-1_all.deb ...
    Unpacking libcudnn9-samples (9.3.0.75-1) ...
    Selecting previously unselected package cudnn9.
    Preparing to unpack .../6-cudnn9_9.3.0-1_amd64.deb ...
    Unpacking cudnn9 (9.3.0-1) ...
    Selecting previously unselected package cudnn.
    Preparing to unpack .../7-cudnn_9.3.0-1_amd64.deb ...
    Unpacking cudnn (9.3.0-1) ...
    Setting up libcudnn9-samples (9.3.0.75-1) ...
    Setting up libcudnn9-cuda-12 (9.3.0.75-1) ...
    Setting up libcudnn9-dev-cuda-12 (9.3.0.75-1) ...
    update-alternatives: using /usr/include/x86_64-linux-gnu/cudnn_v9.h to provide /usr/include/cudnn.h (libcudnn) in auto mode
    Setting up libcudnn9-static-cuda-12 (9.3.0.75-1) ...
    Setting up cudnn9-cuda-12-6 (9.3.0.75-1) ...
    Setting up cudnn9-cuda-12 (9.3.0.75-1) ...
    Setting up cudnn9 (9.3.0-1) ...
    Setting up cudnn (9.3.0-1) ...
    Processing triggers for libc-bin (2.35-0ubuntu3.10) ...
    user@user:~$ 
   ```

4. CUDA 12.x 전용 cuDNN 패키지 설치
   ```bash
   sudo apt-get -y install cudnn-cuda-12
   ```
   ```bash
   user@user:~$ sudo apt-get -y install cudnn-cuda-12
    Reading package lists... Done
    Building dependency tree... Done
    Reading state information... Done
    Note, selecting 'cudnn9-cuda-12' instead of 'cudnn-cuda-12'
    cudnn9-cuda-12 is already the newest version (9.3.0.75-1).
    cudnn9-cuda-12 set to manually installed.
    The following package was automatically installed and is no longer required:
    libffi7
    Use 'sudo apt autoremove' to remove it.
    0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
    ```

5. 설치 확인
   ```bash
   dpkg -l | grep cudnn
   ```
   ```
   user@user:~$ dpkg -l | grep cudnn
    ii  cudnn                                      9.3.0-1                                 amd64        NVIDIA CUDA Deep Neural Network library (cuDNN)
    ii  cudnn-local-repo-ubuntu2204-9.3.0          1.0-1                                   amd64        cudnn-local repository configuration files
    ii  cudnn9                                     9.3.0-1                                 amd64        NVIDIA CUDA Deep Neural Network library (cuDNN)
    ii  cudnn9-cuda-12                             9.3.0.75-1                              amd64        NVIDIA cuDNN for CUDA 12
    ii  cudnn9-cuda-12-6                           9.3.0.75-1                              amd64        NVIDIA cuDNN for CUDA 12.6
    ii  libcudnn9-cuda-12                          9.3.0.75-1                              amd64        cuDNN runtime libraries for CUDA 12.6
    ii  libcudnn9-dev-cuda-12                      9.3.0.75-1                              amd64        cuDNN development headers and symlinks for CUDA 12.6
    ii  libcudnn9-samples                          9.3.0.75-1                              all          cuDNN samples
    ii  libcudnn9-static-cuda-12                   9.3.0.75-1                              amd64        cuDNN static libraries for CUDA 12.6user@user:~$
    ```
> 참고: CUDA 11.x 환경에서는 `sudo apt-get -y install cudnn-cuda-11` 명령어를 사용합니다.

---

## 5. Tensorflow 2.20.0 (CUDA 12.x 지원) 설치

1. 아나콘다 가상환경(tf_gpu)에서 아래 명령어 실행(conda로는 아직 공식 conda 패키지로 등록되지 않아 설치 불가)
   ```bash
   conda activate tf_gpu
   pip install tensorflow==2.20.0
   ```
2. 설치 확인
   ```bash
   python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
   ```
   - GPU 정보가 출력되면 정상 설치

---