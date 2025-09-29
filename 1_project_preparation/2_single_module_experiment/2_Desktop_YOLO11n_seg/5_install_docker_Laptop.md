# 2025-09-27 | Laptop에 Docker 설치

---

## 1. Docker 설치
[Docker 사이트](https://www.docker.com/) 접속하여 Docker Windows(AMD 64용) 다운로드 및 설치


## 2. 설치 확인
```bash
docker --version
```
**출력 결과**
```bash
Docker version 28.4.0, build d8eb465
```

---

## 3. GitHub Ultralytics Docker CPU 이미지 다운로드
[Ultralytics](https://github.com/ultralytics/ultralytics/blob/main/docker/Dockerfile-cpu)

## 4. Docker 이미지 빌드(비어있는 디렉토리에서 실행)
```bash
docker build -f Dockerfile-cpu -t ultralytics-cpu .
```
### 4.1 각 명령어 설명
- `docker build`: Docker 이미지를 빌드하는 명령어입니다.
- 
- `-f Dockerfile-cpu`: 빌드에 사용할 Dockerfile을 지정합니다. 여기서는 `Dockerfile-cpu` 파일을 사용합니다.
- 
- `-t ultralytics-cpu`: 빌드된 이미지에 `ultralytics-cpu`라는 태그를 지정합니다. 이 태그는 이미지를 식별하는 데 사용됩니다.
- 
- `.`: 현재 디렉토리를 빌드 컨텍스트(현재 디렉토리에 있는 내용이 이미지에 저장)로 지정합니다.

## 5. Docker 이미지 확인
```bash
docker images
```
**출력 결과:**
```bash
REPOSITORY        TAG       IMAGE ID       CREATED       SIZE
ultralytics-cpu   latest    f02beab24750   9 hours ago   2.59GB
```

## 6. Docker 컨테이너 실행 (Windows)
```powershell
docker run -it -d --name ultralytics_cpu_seg_detection_v1 -v "${PWD}:/workspace" ultralytics-cpu
```

- `-it`: 터미널 입력을 활성화하고(interactive), 가상 터미널을 할당합니다.
- `-d`: 백그라운드(detached)로 실행합니다.
- `--name ultralytics_cpu_seg_detection_v1`: 컨테이너 이름을 지정합니다.
- `-v %cd%:/workspace`: 현재 윈도우 폴더를 컨테이너의 `/workspace`에 마운트합니다.
- `ultralytics-cpu`: 사용할 이미지 이름입니다.

## 7. 컨테이너 목록 확인
```bash
docker ps -a
```

## 8. 컨테이너 실행
```bash
docker exec -it ultralytics_cpu_seg_detection_v1 powershell
```

## 9. 컨테이너 접속
```bash
docker exec -it ultralytics_cpu_seg_detection_v1 /bin/bash
```

## 10. 컨테이너 중지
```bash
docker stop ultralytics_cpu_seg_detection_v1
```

## 11. 컨테이너 환경 나오기
```bash
exit
```

## 12. 파이썬 버전
```bash
python --version
```
**출력 결과**
```bash
Python 3.11.10
```

## 13. 설치되어 있는 라이브러리 버전 확인
```bash
pip list
```
**출력 결과**
```bash
Package                Version     Editable project location
---------------------- ----------- -------------------------
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

---