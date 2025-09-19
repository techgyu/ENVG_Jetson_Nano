# 2025-09-19 | Jetson Nano 가상환경(venv) 설정

---

## 0. Jetson Nano 가상환경(venv) 란?
- Python 가상환경(venv)은 프로젝트별로 독립된 Python 환경을 제공
- 시스템 전체에 영향을 주지 않고 패키지 설치 및 관리를 할 수 있음
- Jetson Nano에서 Python 개발 시 권장

## 0.1 가상환경 venv에 설치되는 것들
- Python 인터프리터
- 표준 라이브러리
- pip 등 패키지 관리 도구
- 프로젝트별로 설치한 서드파티 패키지

## 1. venv 패키지 설치
```bash
sudo apt update
sudo apt install python3-venv
```

## 1. 가상환경(venv) 생성
```bash
python3 -m venv ~/envs/jetson
```
- `~/envs/jetson` 경로에 가상환경이 생성됨

## 2. 가상환경 활성화
```bash
source ~/envs/jetson/bin/activate
```

## 3. 가상환경 비활성화
```bash
deactivate
```

## 4. 가상환경 삭제
```bash
rm -rf ~/envs/jetson
```
- `~/envs/jetson` 경로의 가상환경이 삭제됨

## 관련 명령어

### 1. 현재 가상환경에 묶여있는 Python 버전 확인
```bash
python -V
```
**출력 결과:**
```bash
(jetson) user@ubuntu:~$ python -V
Python 3.6.9
```

### 2. 현재 가상환경에 설치된 모든 파이썬 패키지 목록 확인(명령어 1)
```bash
pip list
```
**출력 결과:**
```bash
pip (9.0.1)
pkg-resources (0.0.0)
setuptools (39.0.1)
```

#### 2.1 경고 발생
DEPRECATION: The default format will switch to columns in the future. You can use --format=(legacy|columns) (or define a format=(legacy|columns) in your pip.conf under the [list] section) to disable this warning.
**해석**
현재는 pip list가 "legacy" 형식(옛날 스타일)으로 출력되지만,
앞으로는 "columns" 형식(표 형태)으로 출력될 거라는 예고입니다.
기능에는 영향이 없고, 단순 안내 메시지입니다.

#### 2.2 패키지 설명
- pip (9.0.1)
Python 패키지 관리 도구입니다.
pip install, pip list 등으로 패키지 설치/관리를 할 수 있습니다.

- pkg-resources (0.0.0)
setuptools에서 제공하는 내부 유틸리티 패키지입니다.
실제로는 별도 설치된 패키지가 아니며, 패키지 의존성 관리에 사용됩니다. 버전은 항상 0.0.0으로 표시됩니다.

- setuptools (39.0.1)
Python 패키지의 빌드, 설치, 배포를 지원하는 핵심 도구입니다.
많은 패키지가 setuptools를 이용해 설치/배포됩니다.

### 2. 현재 가상환경에 설치된 모든 파이썬 패키지 목록 확인(명령어 2)

---