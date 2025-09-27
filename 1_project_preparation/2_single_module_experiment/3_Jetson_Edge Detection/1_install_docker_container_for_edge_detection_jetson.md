# 2025-09-22 | Jetson Nano Edge Detection용 Docker 컨테이너 생성

---

## 1. 기존에 동작 중인 컨테이너 중단
```bash
sudo docker stop jetson_yolo11
sudo docker stop jetson_yolo11_v1
```

## 2. 동작 중인 컨테이너 확인
```bash
sudo docker ps -a
```

## 3. 저장된 이미지 확인
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
## 4. Edge Detection 실험용 컨테이너 생성
```bash
sudo docker run -it -d --name jetson_yolo11_v1_EdgeDetection -v ${PWD}:/workspace --ipc=host --runtime=nvidia my_yolo11n_image:v1
```

## 5. Edge Detection용 컨테이너 접속
```bash
sudo docker start jetson_yolo11_v1_EdgeDetection
sudo docker exec -it jetson_yolo11_v1_EdgeDetection bash
```