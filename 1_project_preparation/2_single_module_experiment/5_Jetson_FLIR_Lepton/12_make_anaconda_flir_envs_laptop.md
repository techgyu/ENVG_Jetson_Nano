# 2025-09-30 | Laptop에 Anaconda로 FLIR Lepton용 개발 환경 만들기

---

## 1. Anaconda 환경 생성
```bash
conda create -n flir_env python=3.8 -y
```

## 2. 환경 활성화
```bash
conda activate flir_env
```

## 3. flirpy 0.3.0 버전 설치
```bash
pip install flirpy==0.3.0
```

