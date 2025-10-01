# 2025-09-30 | opencv demo 코드 실행

---

## 1. 오류 로그
```bash
user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ ./opencv_demo 
OpenCV demo for Lepton3 on Nvidia Jetson
Code 1
Code 2
Code 3
Code 4
Code 5
 * Radiometry disabled
 * AGC enabled 
 * RGB enabled 
Code 6
Code 7
Code 8
Code 9
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39

*** Forcing RESYNC *** [1 - 1]
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
Code 10
Code 11
Code 12
Code 13
Code 39
```

**분석 결과**
```C++
lepton3 = new Lepton3( "/dev/spidev1.0", "/dev/i2c-0", deb_lvl ); // Lepton3 객체 생성 (SPI, I2C 포트 지정)

lepton3->start(); // 카메라 시작

const uint16_t* data16 = lepton3->getLastFrame16( w, h, &min, &max ); // 16비트 프레임 데이터 가져오기

const uint8_t* dataRGB = lepton3->getLastFrameRGB( w, h ); // RGB 프레임 데이터 가져오기
```

data16과 dataRGB가 nullptr임

## 2. 추가 출력문 삽입 후 재실행
```bash
user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ ./opencv_demo
OpenCV demo for Lepton3 on Nvidia Jetson
Code 1
Code 2
Code 3
Code 4
Code 5
 * Radiometry disabled
 * AGC enabled
 * RGB enabled 
Code 6
Code 7
Code 8
Code 9
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39

*** Forcing RESYNC *** [1 - 1]
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
^C
Ctrl+C pressed...
```

## 3. 추가 분석
```bash
user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ ls -l /dev/spidev*
crw-rw---- 1 root gpio 153, 0  9월 30 13:25 /dev/spidev0.0
crw-rw---- 1 root gpio 153, 1  9월 30 13:25 /dev/spidev0.1
crw-rw---- 1 root gpio 153, 2  9월 30 13:25 /dev/spidev1.0
crw-rw---- 1 root gpio 153, 3  9월 30 13:25 /dev/spidev1.1
user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ ls -l /dev/i2c*
crw-rw---- 1 root i2c 89,   0  9월 30 13:25 /dev/i2c-0
crw-rw---- 1 root i2c 89,   1  9월 30 13:25 /dev/i2c-1
crw-rw---- 1 root i2c 89, 101  9월 30 13:25 /dev/i2c-101
crw-rw---- 1 root i2c 89,   2  9월 30 13:25 /dev/i2c-2
crw-rw---- 1 root i2c 89,   3  9월 30 13:25 /dev/i2c-3
crw-rw---- 1 root i2c 89,   4  9월 30 13:25 /dev/i2c-4
crw-rw---- 1 root i2c 89,   5  9월 30 13:25 /dev/i2c-5
crw-rw---- 1 root i2c 89,   6  9월 30 13:25 /dev/i2c-6
crw-rw---- 1 root i2c 89,   7  9월 30 13:25 /dev/i2c-7
crw-rw---- 1 root i2c 89,   8  9월 30 13:25 /dev/i2c-8
user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ 
```

## 4. sudo 권한으로 실행
```bash
user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ sudo ./opencv_demo
[sudo] password for user: 
OpenCV demo for Lepton3 on Nvidia Jetson
Code 1
Code 2
Code 3
Code 4
Code 5
 * Radiometry disabled
 * AGC enabled
 * RGB enabled 
Code 6
Code 7
Code 8
Code 9
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39

*** Forcing RESYNC *** [1 - 1]
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
Code 10
^CCode 10

Ctrl+C pressed...
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
data16 is NULL
Code 11
w: 0, h: 0, min: 0, max: 0
frameIdx: 0
rgb_mode: 1
dataRGB is NULL
Code 12
Code 13
Code 39
```

## 5. I2C 설정 확인
```bash
user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ sudo i2cdetect -y -r 0                                                                                                                        
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- 2a -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --
```

## 6. SPI 설정 확인
```bash
sudo apt-get install spi-tools
sudo spidev_test -D /dev/spidev1.0
```

## 7. 현재 연결 상태
| Jetson Nano J41 Pin           | Signal Name      | Breakout Board V2.0 Pin | Signal Name      | 비고                       |
|-------------------------------|------------------|-------------------------|------------------|---------------------------|
|  34                           | GND              | 1                       | GND              | 접지(공통 연결)             |
|  2                            | 5V Power         | 2                       | Power in 3~5.5V  | 전원 공급                  |
|  27                           | I2C_1_SDA (I2C0) | 5                       | SDA              | I2C 데이터                  |
|  28                           | I2C_1_SCL (I2C0) | 8                       | SCL              | I2C 클럭                  |
| 13                            | SPI_2_SCK        | 7                       | SPI_CLK          | SPI 클럭                  |
| 37                            | SPI_2_MOSI       | 9                       | SPI_MOSI         | SPI 데이터(마스터→슬레이브)|
| 22                            | SPI_2_MISO       | 12                      | SPI_MISO         | SPI 데이터(슬레이브→마스터)|
| 18                            | SPI_2_CS0        | 10                      | SPI_CS           | SPI 칩 선택               |

## 8. SPI 테스트 코드 다운로드
```bash
wget https://raw.githubusercontent.com/torvalds/linux/master/tools/spi/spidev_test.c
gcc -o spidev_test spidev_test.c
```

**출력 결과**
```bash
user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ wget https://raw.githubusercontent.com/torvalds/linux/master/tools/spi/spidev_test.c
--2025-09-30 20:13:59--  https://raw.githubusercontent.com/torvalds/linux/master/tools/spi/spidev_test.c
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.111.133, 185.199.108.133, 185.199.109.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.111.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 11922 (12K) [text/plain]
Saving to: ‘spidev_test.c’

spidev_test.c                             100%[=====================================================================================>]  11.64K  --.-KB/s    in 0.004s   

2025-09-30 20:14:00 (2.95 MB/s) - ‘spidev_test.c’ saved [11922/11922]

user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ gcc -o spidev_test spidev_test.c
spidev_test.c: In function ‘transfer’:
spidev_test.c:128:4: error: ‘struct spi_ioc_transfer’ has no member named ‘word_delay_usecs’; did you mean ‘delay_usecs’?
   .word_delay_usecs = word_delay,
    ^~~~~~~~~~~~~~~~
    delay_usecs
spidev_test.c:133:13: error: ‘SPI_TX_OCTAL’ undeclared (first use in this function); did you mean ‘SPI_TX_DUAL’?
  if (mode & SPI_TX_OCTAL)
             ^~~~~~~~~~~~
             SPI_TX_DUAL
spidev_test.c:133:13: note: each undeclared identifier is reported only once for each function it appears in
spidev_test.c:139:13: error: ‘SPI_RX_OCTAL’ undeclared (first use in this function); did you mean ‘SPI_TX_OCTAL’?
  if (mode & SPI_RX_OCTAL)
             ^~~~~~~~~~~~
             SPI_TX_OCTAL
spidev_test.c: In function ‘parse_opts’:
spidev_test.c:291:12: error: ‘SPI_3WIRE_HIZ’ undeclared (first use in this function); did you mean ‘SPI_3WIRE’?
    mode |= SPI_3WIRE_HIZ;
            ^~~~~~~~~~~~~
            SPI_3WIRE
spidev_test.c:294:12: error: ‘SPI_RX_CPHA_FLIP’ undeclared (first use in this function); did you mean ‘SPI_RX_DUAL’?
    mode |= SPI_RX_CPHA_FLIP;
            ^~~~~~~~~~~~~~~~
            SPI_RX_DUAL
spidev_test.c:297:12: error: ‘SPI_MOSI_IDLE_LOW’ undeclared (first use in this function); did you mean ‘SPI_MODE_0’?
    mode |= SPI_MOSI_IDLE_LOW;
            ^~~~~~~~~~~~~~~~~
            SPI_MODE_0
spidev_test.c:318:12: error: ‘SPI_TX_OCTAL’ undeclared (first use in this function); did you mean ‘SPI_TX_DUAL’?
    mode |= SPI_TX_OCTAL;
            ^~~~~~~~~~~~
            SPI_TX_DUAL
spidev_test.c:336:12: error: ‘SPI_RX_OCTAL’ undeclared (first use in this function); did you mean ‘SPI_TX_OCTAL’?
    mode |= SPI_RX_OCTAL;
            ^~~~~~~~~~~~
            SPI_TX_OCTAL
user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ 
```

## 8.1 SPI 테스트 코드 수정
```bash
wget https://raw.githubusercontent.com/raspberrypi/linux/raspberrypi-kernel_1.20200212-1/tools/spi/spidev_test.c
gcc -o spidev_test spidev_test.c
```

```bash
master/build/opencv_demo$ sudo ./spidev_test -D /dev/spidev1.0 -v
spi mode: 0x0
bits per word: 8
max speed: 500000 Hz (500 KHz)
TX | FF FF FF FF FF FF 40 00 00 00 00 95 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF F0 0D  | ......@.......................
RX | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  | ................................
user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ 
```

**분석 결과:**
- SPI 통신이 정상적으로 이루어지지 않음을 확인.
- RX 데이터가 모두 0으로 수신됨.
- I2C 통신은 정상적으로 작동하는 것으로 보임.

## 9. SPI 통신 설정 기본 계획
### 1. (확인 완료)Jetson Nano의 SPI 인터페이스 활성화
   - Jetson Nano의 설정 메뉴에서 SPI 1 / 2 인터페이스를 활성화 후 재부팅
    ```bash
    sudo /opt/nvidia/jetson-io/jetson-io.py

    |                     Select one of the following:                    |
    |                                                                    |
    |                   Configure Jetson 40pin Header                    |
    |                Configure Jetson Nano CSI Connector                 |
    |                  Configure Jetson M.2 Key E Slot                   |
    |                                Exit                                |

     =================== Jetson Expansion Header Tool ===================
    |                                                                    |
    |                                                                    |
    |                      3.3V (  1) .. (  2) 5V                        |
    |                      i2c2 (  3) .. (  4) 5V                        |
    |                      i2c2 (  5) .. (  6) GND                       |
    |                    unused (  7) .. (  8) uartb                     |
    |                       GND (  9) .. ( 10) uartb                     |
    |                    unused ( 11) .. ( 12) unused                    |
    |                  spi2_sck ( 13) .. ( 14) GND                       |
    |                        NA ( 15) .. ( 16) spi2_cs1                  |
    |                      3.3V ( 17) .. ( 18) spi2_cs0                  |
    |                    unused ( 19) .. ( 20) GND                       |
    |                    unused ( 21) .. ( 22) spi2_din                  |
    |                    unused ( 23) .. ( 24) unused                    |
    |                       GND ( 25) .. ( 26) unused                    |
    |                      i2c1 ( 27) .. ( 28) i2c1                      |
    |                        NA ( 29) .. ( 30) GND                       |
    |                        NA ( 31) .. ( 32) unused                    |
    |                    unused ( 33) .. ( 34) GND                       |
    |                    unused ( 35) .. ( 36) unused                    |
    |                 spi2_dout ( 37) .. ( 38) unused                    |
    |                       GND ( 39) .. ( 40) unused                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                        Jetson 40pin Header:                        |
    |                                                                    |
    |                 Configure for compatible hardware                  |
    |                   Configure header pins manually                   |
    |                                Back                                |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    ====================================================================

    =================== Jetson Expansion Header Tool =================== 
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                Select desired functions (for pins):                |
    |                                                                    |
    |                 [ ] aud_mclk      (7)                              |
    |                 [ ] i2s4          (12,35,38,40)                    |
    |                 [ ] pwm0          (32)                             |
    |                 [ ] pwm2          (33)                             |
    |                 [*] spi1          (19,21,23,24,26)                 |
    |                 [ ] spi2          (13,16,18,22,37)                 |
    |                 [ ] uartb-cts/rts (11,36)                          |
    |                                                                    |
    |                                Back                                |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    ====================================================================

      =================== Jetson Expansion Header Tool ===================
    |                                                                    |
    |                                                                    |
    |                      3.3V (  1) .. (  2) 5V                        |
    |                      i2c2 (  3) .. (  4) 5V                        |
    |                      i2c2 (  5) .. (  6) GND                       |
    |                    unused (  7) .. (  8) uartb                     |
    |                       GND (  9) .. ( 10) uartb                     |
    |                    unused ( 11) .. ( 12) unused                    |
    |                    unused ( 13) .. ( 14) GND                       |
    |                        NA ( 15) .. ( 16) unused                    |
    |                      3.3V ( 17) .. ( 18) unused                    |
    |                 spi1_dout ( 19) .. ( 20) GND                       |
    |                  spi1_din ( 21) .. ( 22) unused                    |
    |                  spi1_sck ( 23) .. ( 24) spi1_cs0                  |
    |                       GND ( 25) .. ( 26) spi1_cs1                  |
    |                      i2c1 ( 27) .. ( 28) i2c1                      |
    |                        NA ( 29) .. ( 30) GND                       |
    |                        NA ( 31) .. ( 32) unused                    |
    |                    unused ( 33) .. ( 34) GND                       |
    |                    unused ( 35) .. ( 36) unused                    |
    |                    unused ( 37) .. ( 38) unused                    |
    |                       GND ( 39) .. ( 40) unused                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                        Jetson 40pin Header:                        |
    |                                                                    |
    |                   Export as Device-Tree Overlay                    |
    |                          Save pin changes                          |
    |                        Discard pin changes                         |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    ====================================================================

    =================== Jetson Expansion Header Tool ===================
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                    Select one of the following:                    |
    |                                                                    |
    |                  Re-configure Jetson 40pin Header                  |
    |                Configure Jetson Nano CSI Connector                 |
    |                  Configure Jetson M.2 Key E Slot                   |
    |                Save and reboot to reconfigure pins                 |
    |                  Save and exit without rebooting                   |
    |                      Discard all pin changes                       |
    |                                Exit                                |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    ====================================================================

      =================== Jetson Expansion Header Tool ===================
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                    Configuration saved to file                     |
    |  /boot/kernel_tegra210-p3448-0000-p3449-0000-b00-user-custom.dtb.  |
    |                                                                    |
    |     Press any key to reboot the system now or Ctrl-C to abort      |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    |                                                                    |
    ====================================================================
    ```
    ### 2. Jetson Nano dev/spidev 활성화 확인
    ```bash
    ls -l /dev/spidev*
    ```
    ```bash
    crw-rw---- 1 root gpio 153, 0 10월  1 11:16 /dev/spidev0.0            |
    crw-rw---- 1 root gpio 153, 1 10월  1 11:16 /dev/spidev0.1            |
    crw-rw---- 1 root gpio 153, 2 10월  1 11:16 /dev/spidev1.0            |
    crw-rw---- 1 root gpio 153, 3 10월  1 11:16 /dev/spidev1.1            |
    ```

### 2. SPI 통신 속도 조정
   - SPI 통신 속도를 낮춰서 시도 (예: 500 KHz)
   - `spidev_test` 명령어에서 `-s` 옵션을 사용하여 속도 설정
   - 예: `sudo ./spidev_test -D /dev/spidev1.0 -s 500000 -v`
    ```bash
    user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ sudo ./spidev_test -D /dev/spidev0.0 -s 500000 -v
    [sudo] password for user: 
    spi mode: 0x0
    bits per word: 8
    max speed: 500000 Hz (500 KHz)
    TX | FF FF FF FF FF FF 40 00 00 00 00 95 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF F0 0D  | ......@.......................
    RX | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  | ................................
    user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ sudo ./spidev_test -D /dev/spidev0.0 -s 250000 -v
    spi mode: 0x0
    bits per word: 8
    max speed: 250000 Hz (250 KHz)
    TX | FF FF FF FF FF FF 40 00 00 00 00 95 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF F0 0D  | ......@.......................
    RX | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  | ................................
    user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ sudo ./spidev_test -D /dev/spidev0.0 -s 1000000 -v                                                                                            
    spi mode: 0x0
    bits per word: 8
    max speed: 1000000 Hz (1000 KHz)
    TX | FF FF FF FF FF FF 40 00 00 00 00 95 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF F0 0D  | ......@.......................
    RX | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  | ................................
    user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ sudo ./spidev_test -D /dev/spidev0.0 -s 2000000 -v
    spi mode: 0x0
    bits per word: 8
    max speed: 2000000 Hz (2000 KHz)
    TX | FF FF FF FF FF FF 40 00 00 00 00 95 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF F0 0D  | ......@.......................
    RX | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  | ................................
    user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ sudo ./spidev_test -D /dev/spidev0.0 -s 5000000 -v
    spi mode: 0x0
    bits per word: 8
    max speed: 5000000 Hz (5000 KHz)
    TX | FF FF FF FF FF FF 40 00 00 00 00 95 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF F0 0D  | ......@.......................
    RX | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  | ................................
    user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ sudo ./spidev_test -D /dev/spidev0.0 -s 10000000 -v
    spi mode: 0x0
    bits per word: 8
    max speed: 10000000 Hz (10000 KHz)
    TX | FF FF FF FF FF FF 40 00 00 00 00 95 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF F0 0D  | ......@.......................
    RX | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  | ................................
    user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ sudo ./spidev_test -D /dev/spidev0.1 -s 250000 -v                                                                                             
    spi mode: 0x0
    bits per word: 8
    max speed: 250000 Hz (250 KHz)
    TX | FF FF FF FF FF FF 40 00 00 00 00 95 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF F0 0D  | ......@.......................
    RX | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  | ................................
    user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ sudo ./spidev_test -D /dev/spidev0.1 -s 250000 -v
    spi mode: 0x0
    bits per word: 8
    max speed: 250000 Hz (250 KHz)
    TX | FF FF FF FF FF FF 40 00 00 00 00 95 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF F0 0D  | ......@.......................
    RX | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  | ................................
    user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ sudo ./spidev_test -D /dev/spidev0.1 -s 1000000 -v
    spi mode: 0x0
    bits per word: 8
    max speed: 1000000 Hz (1000 KHz)
    TX | FF FF FF FF FF FF 40 00 00 00 00 95 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF F0 0D  | ......@.......................
    RX | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  | ................................
    user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ sudo ./spidev_test -D /dev/spidev0.1 -s 2000000 -v                                                                                            
    spi mode: 0x0
    bits per word: 8
    max speed: 2000000 Hz (2000 KHz)
    TX | FF FF FF FF FF FF 40 00 00 00 00 95 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF F0 0D  | ......@.......................
    RX | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  | ................................
    user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ sudo ./spidev_test -D /dev/spidev0.1 -s 5000000 -v                                                                                            
    spi mode: 0x0
    bits per word: 8
    max speed: 5000000 Hz (5000 KHz)
    TX | FF FF FF FF FF FF 40 00 00 00 00 95 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF F0 0D  | ......@.......................
    RX | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  | ................................
    user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ sudo ./spidev_test -D /dev/spidev0.1 -s 10000000 -v
    spi mode: 0x0
    bits per word: 8
    max speed: 10000000 Hz (10000 KHz)
    TX | FF FF FF FF FF FF 40 00 00 00 00 95 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF F0 0D  | ......@.......................
    RX | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  | ................................
    user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ 

    ```

    ```bash
    user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ sudo ./spidev_test -D /dev/spidev0.0 -H -v
    spi mode: 0x1
    bits per word: 8
    max speed: 500000 Hz (500 KHz)
    TX | FF FF FF FF FF FF 40 00 00 00 00 95 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF F0 0D  | ......@.......................
    RX | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  | ................................
    user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ sudo ./spidev_test -D /dev/spidev0.1 -H -v
    spi mode: 0x1
    bits per word: 8
    max speed: 500000 Hz (500 KHz)
    TX | FF FF FF FF FF FF 40 00 00 00 00 95 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF F0 0D  | ......@.......................
    RX | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  | ................................
    user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ sudo ./spidev_test -D /dev/spidev1.0 -H -v
    spi mode: 0x1
    bits per word: 8
    max speed: 500000 Hz (500 KHz)
    TX | FF FF FF FF FF FF 40 00 00 00 00 95 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF F0 0D  | ......@.......................
    RX | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  | ................................
    user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ sudo ./spidev_test -D /dev/spidev1.1 -H -v
    spi mode: 0x1
    bits per word: 8
    max speed: 500000 Hz (500 KHz)
    TX | FF FF FF FF FF FF 40 00 00 00 00 95 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF F0 0D  | ......@.......................
    RX | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  | ................................
    user@ubuntu:~/Desktop/ENVG_Jetson_Nano/1_project_preparation/2_single_module_experiment/5_Jetson_FLIR_Lepton/Myzhar_Lepton3_Jetson/Lepton3_Jetson-master/Lepton3_Jetson-master/build/opencv_demo$ 
    ```

### 3. SPI 채널 확인
   - Jetson Nano에서 사용 가능한 SPI 채널 확인
   - `/dev/spidev1.0` 또는 `/dev/spidev1.1` 등 올바른 장치 파일 사용
   - SPI1로 변경하였으므로, `/dev/spidev1.0` 또는 `/dev/spidev1.1` 사용

### 4. (변경 완료)회로 점검
    - 연결된 배선 및 핀 번호가 정확한지 확인
    - 접촉 불량이나 단선 여부 점검
    - 이전에 I2C 연결 또한, 2번 I2C로 연결 시 통신이 안 되어서, 1번 I2C로 변경하여 통신 성공
    - SPI 연결 시에도 동일하게 1번 SPI로 연결(회로도 수정 필요)
    
#### 4.1 현재 연결 상태
    | Jetson Nano J41 Pin           | Signal Name      | Breakout Board V2.0 Pin | Signal Name      | 비고                       |
    |-------------------------------|------------------|-------------------------|------------------|---------------------------|
    | 34                            | GND              | 1                       | GND              | 접지(공통 연결)             |
    | 4                             | 5V Power         | 2                       | Power in 3~5.5V  | 전원 공급                  |
    | 27                            | I2C_1_SDA (I2C0) | 5                       | SDA              | I2C 데이터                  |
    | 28                            | I2C_1_SCL (I2C0) | 8                       | SCL              | I2C 클럭                  |
    | 23                            | SPI_1_SCK        | 7                       | SPI_CLK          | SPI 클럭                  |
    | 19                            | SPI_1_MOSI       | 9                       | SPI_MOSI         | SPI 데이터(마스터→슬레이브)|
    | 21                            | SPI_1_MISO       | 12                      | SPI_MISO         | SPI 데이터(슬레이브→마스터)|
    | 24                            | SPI_1_CS0        | 10                      | SPI_CS           | SPI 칩 선택               |
  
### 5. (5V 핀 변경 완료)전원 공급 확인
    - Lepton 모듈에 안정적인 전원 공급이 이루어지고 있는지 확인
    - 전압 강하나 노이즈가 없는지 점검 필요
    - 전원 입력 핀을 변경하거나, 전원 수신 핀을 변경하여 점검 가능