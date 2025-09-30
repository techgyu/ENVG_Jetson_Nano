# 2025-09-19 | Jetson Nano Ultralytics jetpack4 Docker 이미지 다운로드

---

## 1. Jetson Nano JetPack(L4T) 버전 확인
```bash
dpkg-query --show nvidia-l4t-core
```
**출력 결과:**
```bash
user@ubuntu:~$ dpkg-query --show nvidia-l4t-core
nvidia-l4t-core 32.7.6-20241104234540
```
- JetPack 4.6.6의 L4T 버전은 32.7.6

## 2. 터미널 환경 변수 설정
```bash
t=ultralytics/ultralytics:latest-jetson-jetpack4
```

## 3. Docker 이미지 다운로드
```bash
sudo docker pull $t
```

## 4. Docker 이미지 확인
```bash
sudo docker image ls
```

**출력 결과 예시:**
```bash
REPOSITORY                TAG                      IMAGE ID       CREATED        SIZE  
ultralytics/ultralytics   latest-jetson-jetpack4   704b5fa7ea6f   17 hours ago   5.54GB
```

## 5. Docker 컨테이너 실행
```bash
sudo docker run -it --ipc=host --runtime=nvidia $t
```

- **설명:**  
  - 터미널에서 바로 컨테이너에 진입하여 상호작용할 수 있습니다.
  - 컨테이너 이름은 자동으로 부여됩니다.
  - 호스트와 컨테이너 간 파일 공유(볼륨 마운트)는 없습니다.
  - 컨테이너가 종료되면 터미널도 함께 종료됩니다.

또는

```bash
sudo docker run -it -d --name jetson_yolo11 -v ${PWD}:/workspace --ipc=host --runtime=nvidia ultralytics/ultralytics:latest-jetson-jetpack4
```

- **설명:**  
  - `-d` 옵션으로 컨테이너를 백그라운드(detached)로 실행합니다.
  - `--name jetson_yolo11`로 컨테이너 이름을 직접 지정할 수 있습니다.
  - `-v ${PWD}:/workspace` 옵션으로 현재 디렉토리를 컨테이너의 `/workspace`에 마운트하여, 호스트와 컨테이너 간 파일을 공유할 수 있습니다.
  - 컨테이너 실행 후, 필요할 때 아래 명령어로 접속할 수 있습니다:
    ```bash
    sudo docker exec -it jetson_yolo11 bash
    ```


## 6. Docker 컨테이너 중지
```bash
sudo docker stop jetson_yolo11
```

## 7. Docker 컨테이너 삭제
```bash
sudo docker rm jetson_yolo11
```

## 8. Docker 컨테이너 켜기
```bash
sudo docker start jetson_yolo11 # 중지된 컨테이너를 다시 시작
sudo docker exec -it jetson_yolo11 bash # 실행 중인 컨테이너에 bash 셀로 접속(컨테이너 내부에서 직접 명령 입력)
```

**출력 결과**
```bash
user@ubuntu:~/Desktop/ENVG_Jetson_Nano$ sudo docker exec -it jetson_yolo11 bash
root@dbe86e6a1b08:/ultralytics# 
```

## 9. 실행 중인 컨테이너 내부 bash 셀에서 나가기
```bash
exit
```