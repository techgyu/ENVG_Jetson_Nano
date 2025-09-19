# 2025-09-19 | Jetson Nano Anaconda(=Jetconda) 설치

---

## 1. Jetson Nano용 Anaconda(=Jetconda) 설치 파일 다운로드

Jetson Nano는 ARM(aarch64) 아키텍처이므로, 공식 Anaconda가 아닌 Jetconda(ARM용 포크)를 사용해야 합니다.

```bash
wget https://github.com/seibert/jetconda/releases/download/v1.0.0-tx2/Jetconda3-1.0.0-Linux-aarch64.sh
chmod +x Jetconda3-1.0.0-Linux-aarch64.sh
```

---

## 2. Anaconda(=Jetconda) 설치

```bash
./Jetconda3-1.0.0-Linux-aarch64.sh
```
- 설치 중 [yes/no] 질문에는 모두 yes, Enter를 입력
- 설치 경로를 바꾸고 싶으면 마지막 Enter 전에 경로를 수정

설치가 끝나면, bashrc에 자동으로 PATH가 등록됩니다.

---

## 3. conda 명령어 인식이 안 될 때

설치 후 아래 명령어로 conda 버전을 확인합니다.

```bash
conda --version
```

만약 `conda: command not found`가 뜬다면, 아래처럼 환경변수를 추가합니다.

```bash
vi ~/.bashrc
# 맨 아래에 추가 (username은 본인 계정명으로)
export PATH="/home/username/jetconda3/bin:$PATH"
# 저장 후 종료 (:wq)
source ~/.bashrc
conda --version
```

---

## 4. 가상환경 관리 예시

- 가상환경 생성  
  ```bash
  conda create -n jetson python=3.6
  ```
- 가상환경 삭제  
  ```bash
  conda remove -n jetson --all
  ```
- 가상환경 목록 확인  
  ```bash
  conda info --envs
  ```
- 가상환경 활성화  
  ```bash
  source activate jetson
  ```
- 가상환경 비활성화  
  ```bash
  source deactivate
  ```

---

## 결론
- Anaconda에서 공식적으로 ARM 아키텍처를 지원하지 않으므로, Jetson Nano에서는 custom 빌드된 Jetconda를 사용해야 함.
- 따라서, 패키지 호환성과 관련하여 문제가 발생할 소지가 증가하기 때문에 Jetson Nano에서는 로컬 가상환경(venv)를 사용할 것임.

---