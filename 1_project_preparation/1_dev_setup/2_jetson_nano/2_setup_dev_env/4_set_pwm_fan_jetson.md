# 2025-09-18 | Jetson Nano PWM 팬 설정

---
## 1. 참고 자료
[Jetson Fan Control](https://github.com/jugfk/jetson-fan-ctl)

## 2. Python3 및 필수 패키지 설치
Jetson Nano 표준 이미지에는 Python3가 기본 설치되어 있습니다.  
버전을 확인하려면:
```bash
python3 --version
```
필요시 개발 패키지 설치:
```bash
sudo apt update
sudo apt install python3-dev
```

---

## 3. jetson-fan-ctl 설치

1. 터미널을 열고 아래 명령어를 순서대로 실행합니다.
    ```bash
    git clone https://github.com/jetsonworld/jetson-fan-ctl.git
    cd jetson-fan-ctl
    sudo sh install.sh
    ```
2. 설치가 완료되면, 팬 제어 스크립트가 부팅 시 자동으로 실행됩니다.

---

## 4. 팬 동작 온도 및 설정 커스터마이징

1. 설정 파일을 편집기로 엽니다.
    ```bash
    sudo nano /etc/automagic-fan/config.json
    ```
2. 주요 설정 예시:
    ```json
    {
      "FAN_OFF_TEMP": 20,
      "FAN_MAX_TEMP": 50,
      "UPDATE_INTERVAL": 2,
      "MAX_PERF": 1
    }
    ```
    - **FAN_OFF_TEMP**: 팬이 꺼지는 온도(°C)
    - **FAN_MAX_TEMP**: 팬이 100%로 동작하는 온도(°C)
    - **UPDATE_INTERVAL**: 팬 속도 갱신 주기(초)
    - **MAX_PERF**: 0보다 크면 CPU/GPU 클럭을 최대 성능으로 설정

3. 설정을 변경한 후에는 재부팅하거나, 아래 명령어로 즉시 적용할 수 있습니다.
    ```bash
    sudo service automagic-fan restart
    ```

---

## 5. 팬 서비스 수동 제어 및 상태 확인

- 서비스 시작:  
  ```bash
  sudo service automagic-fan start
  ```
- 서비스 중지:  
  ```bash
  sudo service automagic-fan stop
  ```
- 서비스 상태 확인:  
  ```bash
  sudo service automagic-fan status
  ```

---