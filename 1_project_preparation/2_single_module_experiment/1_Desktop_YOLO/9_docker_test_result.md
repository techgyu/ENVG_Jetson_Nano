# 2025-09-27 | Laptop Docker 환경 기존 코드 실험 결과

---

## 1. 기존 아나콘다 환경에서 돌렸던 코드 정상 작동 확인
6_test_yolo11n_segmentation.py -> 경로 수정 후 정상 작동
7_test_yolo11n_segmentation_in_video.py -> 경로 수정 후 정상 작동
8_intergrate_frame_to_video.py -> Killed 발생


## 2. 8_intergrate_frame_to_video.py Killed 문제
### 2.1. docker 컨테이너 CPU, 메모리 할당 확인
``` bash
root@cd2f5ff9829d:/workspace# grep MemTotal /proc/meminfo
MemTotal:       16320688 kB
root@cd2f5ff9829d:/workspace# nproc
16
root@cd2f5ff9829d:/workspace# lscpu | grep '^CPU(s):'
CPU(s):                               16
```

**확인 결과: 메모리 16GB, CPU 16Core 할당 확인**

### 2.2. .wslconfig 설정하여, 메모리 제한량 16GB -> 32GB로 변경, swap 메모리 32GB 설정
``` ini
[wsl2]
memory=32GB
processors=16
swap=32GB
```

### 2.3. 재부팅 후 메모리 할당 재 확인 결과
``` bash
root@cd2f5ff9829d:/workspace# grep MemTotal /proc/meminfo
MemTotal:       32757928 kB
root@cd2f5ff9829d:/workspace# nproc
16
root@cd2f5ff9829d:/workspace# lscpu | grep '^CPU(s):'
CPU(s):                               16
```

### 2.4 SWAP 메모리 확인
``` bash
root@cd2f5ff9829d:/workspace# cat /proc/meminfo | grep -i swap
SwapCached:            0 kB
SwapTotal:      33554432 kB
SwapFree:       33554432 kB`
```
**확인 결과: SWAP 메모리 32GB 설정 확인**

### 2.5 영상 결합 코드 정상 작동 확인 - 테스트 종료