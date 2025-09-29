# 2025-09-27 | Laptop에 Anaconda 설치 및 YOLO 환경 설정

---

## 1. 설치 사유
: Docker는 GUI 테스트가 불가능

## 2. Anaconda 설치 파일 다운로드 후 설치

## 3. 세팅해야 하는 환경 목록
```bash
Python 3.11.10
certifi                2025.8.3
charset-normalizer     3.4.3
contourpy              1.3.3
cycler                 0.12.1
filelock               3.19.1
fonttools              4.60.0
fsspec                 2025.9.0
idna                   3.10
Jinja2                 3.1.6
kiwisolver             1.4.9
MarkupSafe             3.0.2
matplotlib             3.10.6
mpmath                 1.3.0
networkx               3.5
numpy                  2.3.3
opencv-python-headless 4.11.0.86
packaging              25.0
pillow                 11.3.0
pip                    24.0
polars                 1.33.1
psutil                 7.1.0
pyparsing              3.2.5
python-dateutil        2.9.0.post0
PyYAML                 6.0.3
requests               2.32.5
scipy                  1.16.2
setuptools             65.5.1
six                    1.17.0
sympy                  1.14.0
torch                  2.8.0+cpu
torchvision            0.23.0+cpu
typing_extensions      4.15.0
ultralytics            8.3.203     /ultralytics
ultralytics-thop       2.0.17
urllib3                2.5.0
uv                     0.8.22
wheel                  0.45.1
```

## 3. 새로운 가상 환경 생성
```bash
conda create -n yolo11nseg_v1 python=3.11.10 -y
```

## 4. conda 초기화
```bash
conda init
```

## 5. 가상 환경 활성화
```bash
conda activate yolo11nseg_v1
```

## 6. pip 최신 버전으로 업그레이드
```bash
pip install --upgrade pip
```

## 7. 필요한 라이브러리 설치
```bash
pip install certifi==2025.8.3 charset-normalizer==3.4.3 contourpy==1.3.3 cycler==0.12.1 filelock==3.19.1 fonttools==4.60.0 fsspec==2025.9.0 idna==3.10 Jinja2==3.1.6 kiwisolver==1.4.9 MarkupSafe==3.0.2 matplotlib==3.10.6 mpmath==1.3.0 networkx==3.5 numpy==2.3.3 opencv-python-headless==4.11.0.86 packaging==25.0 pillow==11.3.0 polars==1.33.1 psutil==7.1.0 pyparsing==3.2.5 python-dateutil==2.9.0.post0 PyYAML==6.0.3 requests==2.32.5 scipy==1.16.2 setuptools==65.5.1 six==1.17.0 sympy==1.14.0 typing_extensions==4.15.0 ultralytics==8.3.203 ultralytics-thop==2.0.17 urllib3==2.5.0 uv==0.8.22 wheel==0.45.1
```

## 8. pytorhch 및 torchvision CPU 버전 설치
```bash
pip install torch==2.8.0 torchvision==0.23.0 --index-url https://download.pytorch.org/whl/cpu
```

## 9. 설치 후 결과 확인
```bash
certifi                2025.8.3
charset-normalizer     3.4.3
contourpy              1.3.3
cycler                 0.12.1
filelock               3.19.1
fonttools              4.60.0
fsspec                 2025.9.0
idna                   3.10
Jinja2                 3.1.6
kiwisolver             1.4.9
MarkupSafe             3.0.2
matplotlib             3.10.6
mpmath                 1.3.0
networkx               3.5
numpy                  2.3.3
opencv-python          4.11.0.86
opencv-python-headless 4.11.0.86
packaging              25.0
pillow                 11.3.0
pip                    25.2
polars                 1.33.1
psutil                 7.1.0
pyparsing              3.2.5
python-dateutil        2.9.0.post0
PyYAML                 6.0.3
requests               2.32.5
scipy                  1.16.2
setuptools             65.5.1
six                    1.17.0
sympy                  1.14.0
torch                  2.8.0+cpu
torchvision            0.23.0+cpu
typing_extensions      4.15.0
ultralytics            8.3.203
ultralytics-thop       2.0.17
urllib3                2.5.0
uv                     0.8.22
wheel                  0.45.1
```