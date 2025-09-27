# 2025-09-22 | FLIR Lepton 3.5, Breakout Board V2.0 연결용 Docker 컨테이너 생성

---

## 1. 동작 중인 컨테이너 확인
```bash
sudo docker ps -a
```

## 2. 기존에 동작 중인 컨테이너 중단
```bash
sudo docker stop jetson_yolo11
sudo docker stop jetson_yolo11_v1
```

## 3. 동작 중인 컨테이너 확인
```bash
sudo docker ps -a
```

## 4. 저장된 이미지 확인
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
## 4. FLIR 연결용 컨테이너 생성
```bash
sudo docker run -it -d --name jetson_yolo11_v1_FLIR -v ${PWD}:/workspace --ipc=host --runtime=nvidia my_yolo11n_image:v1
```

## 5. FLIR 연결용 컨테이너 접속
```bash
sudo docker start jetson_yolo11_v1_FLIR
sudo docker exec -it jetson_yolo11_v1_FLIR bash
```