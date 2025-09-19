# 2025-09-19 |Jetson Nano 전원, 클럭 옵션 활성화

---

## 1. Jetson Nano 전원 모드 설정
```bash
sudo nvpmodel -m 0
```

## 2. 현재 전원 모드 확인
```bash
sudo nvpmodel -q
```

## 3. Jetson Nano 클럭 최대화
```bash
sudo jetson_clocks
```

**출력 결과**:
```bash
user@ubuntu:~/Desktop/ENVG_Jetson_Nano$ sudo nvpmodel -q
NVPM WARN: fan mode is not set!
NV Power Mode: MAXN # 전원모드가 최대 성능(MAXN)으로 설정됨
0
```

## 4. 현재 클럭 상태 확인
```bash
sudo jetson_clocks --show
```

**출력 결과**:
```bash
user@ubuntu:~/Desktop/ENVG_Jetson_Nano$ sudo jetson_clocks --show
SOC family:tegra210  Machine:NVIDIA Jetson Nano Developer Kit
Online CPUs: 0-3
# 하기 CPU/GPU 클럭이 모두 최대치로 설정됨
cpu0: Online=1 Governor=schedutil MinFreq=1479000 MaxFreq=1479000 CurrentFreq=1479000 IdleStates: WFI=0 c7=0 
cpu1: Online=1 Governor=schedutil MinFreq=1479000 MaxFreq=1479000 CurrentFreq=1479000 IdleStates: WFI=0 c7=0 
cpu2: Online=1 Governor=schedutil MinFreq=1479000 MaxFreq=1479000 CurrentFreq=1479000 IdleStates: WFI=0 c7=0 
cpu3: Online=1 Governor=schedutil MinFreq=1479000 MaxFreq=1479000 CurrentFreq=1479000 IdleStates: WFI=0 c7=0 
GPU MinFreq=921600000 MaxFreq=921600000 CurrentFreq=921600000
EMC MinFreq=204000000 MaxFreq=1600000000 CurrentFreq=1600000000 FreqOverride=1
Fan: PWM=34
NV Power Mode: MAXN # 전원모드가 최대 성능(MAXN)으로 설정됨
```

---