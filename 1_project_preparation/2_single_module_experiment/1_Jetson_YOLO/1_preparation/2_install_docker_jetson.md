# 2025-09-19 | Jetson Nano Docker 설치

---

## 1. Docker 설치
```bash
sudo apt update
sudo apt install -y docker.io
```

## 2. Docker 서비스 활성화
```bash
sudo systemctl enable docker
sudo systemctl start docker
```

## 3. Docker 그룹에 사용자 추가
```bash
sudo usermod -aG docker $USER
```

## 4. 현재 Docker 서비스 상태 확인
```bash
systemctl status docker
```

```bash
user@ubuntu:~$ systemctl status docker
● docker.service - Docker Application Container Engine
   Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)  
   Active: active (running) since Thu 2025-09-18 21:37:05 KST; 17h ago
     Docs: https://docs.docker.com
 Main PID: 4097 (dockerd)
    Tasks: 10
   CGroup: /system.slice/docker.service
           └─4097 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock 

 9월 18 21:37:04 ubuntu dockerd[4097]: time="2025-09-18T21:37:04.139983821+09:00" level=w 9월 18 21:37:04 ubuntu dockerd[4097]: time="2025-09-18T21:37:04.140041425+09:00" level=w 9월 18 21:37:04 ubuntu dockerd[4097]: time="2025-09-18T21:37:04.140064550+09:00" level=w 9월 18 21:37:04 ubuntu dockerd[4097]: time="2025-09-18T21:37:04.140653664+09:00" level=i 9월 18 21:37:04 ubuntu dockerd[4097]: time="2025-09-18T21:37:04.795471216+09:00" level=i 9월 18 21:37:04 ubuntu dockerd[4097]: time="2025-09-18T21:37:04.969469862+09:00" level=i 9월 18 21:37:05 ubuntu dockerd[4097]: time="2025-09-18T21:37:05.181886060+09:00" level=i 9월 18 21:37:05 ubuntu dockerd[4097]: time="2025-09-18T21:37:05.183061477+09:00" level=i
```

## 5. Docker 데몬 정보 확인
```bash
docker info
```

```bash
user@ubuntu:~$ docker info
Client:
 Context:    default
 Debug Mode: false

Server:
 Containers: 0 # 컨테이너 개수
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 0 # 저장된 이미지 개수
 Server Version: 20.10.21
 Storage Driver: overlay2
  Backing Filesystem: extfs
  Supports d_type: true
  Native Overlay Diff: true
  userxattr: false
 Logging Driver: json-file
 Cgroup Driver: cgroupfs
 Cgroup Version: 1
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local logentries splunk syslog    
 Swarm: inactive
 Runtimes: io.containerd.runtime.v1.linux nvidia runc io.containerd.runc.v2
 Default Runtime: runc
 Init Binary: docker-init
 containerd version:
 runc version:
 init version:
 Security Options:
  seccomp
   Profile: default
 Kernel Version: 4.9.337-tegra
 Operating System: Ubuntu 18.04.6 LTS
 OSType: linux
 Architecture: aarch64
 CPUs: 4
 Total Memory: 3.871GiB
 Name: ubuntu
 ID: BDFL:MTX4:ECWF:KNJD:D6YG:C47O:Z2MJ:6L76:H62W:7RN5:CMV4:LNTI
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Registry: https://index.docker.io/v1/
 Labels:
 Experimental: false
 Insecure Registries:
  127.0.0.0/8
 Live Restore Enabled: false
 ```

## 6. Docker 볼륨 목록 확인
```bash
docker volume ls
```

```bash
user@ubuntu:~$ docker volume ls
DRIVER    VOLUME NAME
```

## 7. Docker 이미지 목록 확인
```bash
docker images
```

```bash
user@ubuntu:~$ docker images
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
```

## 8. Docker 컨테이너 목록 확인
```bash
docker ps -a
```

```bash
user@ubuntu:~$ docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

## 9. Docker에서 볼륨/이미지/컨테이너 차이
- 볼륨(Volume): Docker 컨테이너가 사용하는 **데이터를 저장하는 공간**입니다. 컨테이너가 삭제되어도 볼륨은 유지되어 데이터가 보존됩니다.
- 비유: 외장 하드, USB, 또는 가상머신의 "공유 폴더"

- 이미지(Image): Docker 컨테이너를 생성하는 데 **사용되는 템플릿**입니다. 애플리케이션과 그 종속성을 포함하며, 읽기 전용입니다.
- 비유: CD/DVD 이미지 파일과 비슷합니다.
 
- 컨테이너(Container): 이미지를 실행한 상태로, **애플리케이션이 실제로 동작하는 환경**입니다. 컨테이너는 격리된 환경에서 실행되며, 필요에 따라 생성 및 삭제할 수 있습니다.
- 비유: 이미지로부터 만들어진 "실행 중인 프로그램" 또는 "실행 중인 가상 머신"