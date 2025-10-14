
# 2025-09-30 | Thermal Images on Jetson™ Nano with FLIR Lepton3

---

## 1. Reference
- [Thermal Images on Jetson™ Nano with FLIR Lepton3](https://www.myzhar.com/blog/jetson-nano-with-flir-lepton3/)
- [Lepton3_Jetson](https://github.com/Myzhar/Lepton3_Jetson/tree/master)

---

## 2. 전문 해석 및 정리 (영문/한글 병기)

### Introduction
In the far 2017, I participated (and won) in a challenge promoted by FLIR and the BeagleBoard.org Foundation. I used a FLIR Lepton3 module and a BeagleBone Blue to detect and track people using their temperature.
2017년, 저는 FLIR과 BeagleBoard.org 재단이 주최한 챌린지에 참가해 우승했습니다. 당시 FLIR Lepton3 모듈과 BeagleBone Blue를 사용해 사람을 온도로 감지하고 추적하는 프로젝트를 진행했습니다.

In this article, I will explain how to use the same Lepton3 module with an NVIDIA® Jetson™ Nano.
이 글에서는 동일한 Lepton3 모듈을 NVIDIA® Jetson™ Nano에서 사용하는 방법을 설명합니다.

---

### FLIR Lepton3
The FLIR Lepton® is a radiometric-capable LWIR camera solution that is smaller than a dime, fits inside a smartphone, and is one tenth the cost of traditional IR cameras. Using focal plane arrays of either 160×120 or 80×60 active pixels, Lepton easily integrates into native mobile-devices and other electronics as an IR sensor or thermal imager. The radiometric Lepton captures accurate, calibrated, and noncontact temperature data in every pixel of each image.
FLIR Lepton®은 방사선(온도 측정) 기능이 있는 LWIR(장파장 적외선) 카메라 솔루션으로, 10원짜리 동전보다 작고 스마트폰에도 들어갈 수 있으며, 기존 적외선 카메라 대비 1/10 가격입니다. 160×120 또는 80×60 활성 픽셀의 초점면 배열(FPA)을 사용하여, Lepton은 IR 센서나 열화상 카메라로 모바일 기기 및 각종 전자기기에 쉽게 통합할 수 있습니다. 방사선 기능이 있는 Lepton은 각 이미지의 모든 픽셀에서 정확하고 보정된 비접촉 온도 데이터를 캡처할 수 있습니다.

---

### Communication Channels
The FLIR Lepton3 communicates with the host using two different communication channels:
FLIR Lepton3는 호스트와 두 가지 다른 통신 채널을 사용하여 통신합니다:

- I2C to control the sensor settings
     - I2C를 통해 센서 설정 제어
- SPI to send thermal image data
     - SPI를 통해 열화상 데이터 전송

---

### The breakout board
The FLIR Lepton3 module requires a breakout board to connect it to our device. I use the GroupGets FLIR breakout board v1.4. All required Lepton system voltages, I2C pull-ups, and the clock is provided by this board so you can focus on your application software and not the Lepton setup hardware. Recently the new breakout board v2 has been released with a useful VSINC signal and other useful features, that allow realizing more stable communication drivers.
FLIR Lepton3 모듈은 장치에 연결하기 위해 브레이크아웃 보드가 필요합니다. 저는 GroupGets FLIR 브레이크아웃 보드 v1.4를 사용합니다. 이 보드는 필요한 모든 Lepton 시스템 전압, I2C 풀업, 클럭을 제공하므로 Lepton 설정 하드웨어가 아닌 애플리케이션 소프트웨어에 집중할 수 있습니다. 최근에는 유용한 VSINC 신호와 기타 기능이 추가된 새로운 브레이크아웃 보드 v2가 출시되어 보다 안정적인 통신 드라이버 구현이 가능합니다.

---

### Connection (연결 방법)
The schematic of the connections is reported below
아래에 연결 회로도가 나와 있습니다.

#### Lepton3와 Jetson Nano 연결표 (Connection Table)

| Lepton3 PIN | 신호명 | 색상   | Jetson Nano 신호명 | Jetson Nano 핀번호 |
|:-----------:|:------:|:------:|:------------------:|:------------------:|
| 1           | CS     | Green  | SPI1-CS0           | 24                 |
| 2           | MOSI   | –      | N.C.               | N.C.               |
| 3           | MISO   | Yellow | SPI1-MISO          | 21                 |
| 4           | CLK    | White  | SPI1-CLK           | 23                 |
| 5           | GND    | Black  | GND                | 6                  |
| 6           | VIN    | Red    | 3V3                | 1                  |
| 7           | SDA    | Orange | I2C1-SDA           | 27                 |
| 8           | SCL    | Brown  | I2C1-SCL           | 28                 |

I created a simple carrier board using a protoboard to keep the FLIR Lepton 3 vertical, but the cables can be directly connected to the pin headers of the breakout board v1.4.
저는 FLIR Lepton 3를 수직으로 고정하기 위해 프로토보드를 사용해 간단한 캐리어 보드를 만들었지만, 케이블을 브레이크아웃 보드 v1.4의 핀 헤더에 직접 연결할 수도 있습니다.

An optional resistor of 10KΩ is connected between MOSI and GND to keep the connection stable.
연결의 안정성을 위해 MOSI와 GND 사이에 10KΩ 저항을 추가로 연결할 수 있습니다.

If you are curious about the rear single pin… it’s a GND test point, useful to connect the GND of the probe of the oscilloscope to analyze the status of each signal.
만약, 뒷면의 단일 핀에 대해 궁금하다면… 이는 GND 테스트 포인트로, 오실로스코프 프로브의 GND를 연결하여 각 신호의 상태를 분석하는 데 유용합니다.

---

### Enable SPI (SPI 활성화)
The first operation to perform is enabling one SPI port on the Jetson™ Nano. The operation is quite simple, there is a very good guide to follow and I will not replicate every step here, just go to visit the JetsonHacks blog and follow the guidance of my friend kangalow about using the Jetson-IO tool to enable the SPI1 port available on the PINS 19,21,23,24,26 of the expansion header (J41) of the NVIDIA® Jetson™ Nano Developer Kit.
첫 번째로 수행할 작업은 Jetson™ Nano에서 하나의 SPI 포트를 활성화하는 것입니다. 이 작업은 매우 간단하며, 따라야 할 매우 좋은 가이드가 있습니다. 여기서 모든 단계를 복제하지 않고 JetsonHacks 블로그를 방문하여 제 친구 kangalow의 지침을 따라 NVIDIA® Jetson™ Nano 개발 키트의 확장 헤더(J41)의 핀 19, 21, 23, 24, 26에서 사용할 수 있는 SPI1 포트를 활성화하는 방법을 알아보세요.

---

### Change SPI buffer size (SPI 버퍼 크기 변경)
The default buffer size used for SPI communication is set to 4096 bytes by the spidev module. Lepton3 requires 20KB of buffer to retrieve a full segment of data that composes the thermal image.
SPI 통신에 사용되는 기본 버퍼 크기는 spidev 모듈에 의해 4096바이트로 설정되어 있습니다. Lepton3는 열화상 이미지를 구성하는 전체 데이터 세그먼트를 검색하기 위해 20KB의 버퍼가 필요합니다.

To change the size of the SPI buffer we have two methods. The first is temporary and the default buffer size will be restored after the next reboot, the second is permanent.
SPI 버퍼 크기를 변경하는 방법은 두 가지가 있습니다. 첫 번째는 임시 방법으로, 다음 재부팅 후 기본 버퍼 크기가 복원됩니다. 두 번째는 영구적인 방법입니다.

#### Temporary method (임시 방법)
First of all, remove the spidev module from the Kernel
가장 먼저, 커널에서 spidev 모듈을 제거합니다.

```bash
$ sudo rmmod spidev
```

then reload the module setting the required parameter
그 후, 필요한 매개변수를 설정하여 모듈을 다시 로드합니다.

```bash
$ sudo modprobe spidev bufsize=20480
```

#### Permanent method (영구 방법)
To permanently set the value of the SPI buffer you must create a configuration file for modeprobe
영구적으로 SPI 버퍼 값을 설정하려면 modeprobe용 구성 파일을 만들어야 합니다.

```bash
$ sudo nano /etc/modprobe.d/spidev.conf
```

Enter the following line
아래 줄을 입력합니다.

```bash
options spidev bufsiz=20480
```

Save and reboot the Jetson Nano
저장하고 Jetson Nano를 재부팅합니다.

---

### SPI Buffer size check (SPI 버퍼 크기 확인)
To be sure that the buffer size of the SPI has the correct value we can check the content of the file /sys/module/spidev/parameters/bufsiz using the command
SPI 버퍼 크기가 올바른 값을 가지고 있는지 확인하려면 다음 명령을 사용하여 /sys/module/spidev/parameters/bufsiz 파일의 내용을 확인할 수 있습니다.

```bash
$ cat /sys/module/spidev/parameters/bufsiz
```

if you correctly followed the configuration procedure, the output should be 20480 .
구성 절차를 올바르게 따르면 출력은 20480이어야 합니다.

---

### Check I2C communication (I2C 통신 확인)
To verify that the I2C cables are correctly connected you can use the command
I2C 케이블이 정확히 연결되었는지 확인하려면 다음 명령을 사용할 수 있습니다.

```bash
$ i2cdetect -y -r 0
```

the I2C interface of the FLIR Lepton3 module should reply at address 0x2a
FLIR Lepton3 모듈의 I2C 인터페이스는 주소 0x2a에서 응답해야 합니다.

```
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

---

### Software
A GitHub repository is available that contains a library driver to control the Lepton3 by I2C and to get the thermal images by SPI.
깃허브 저장소를 통해 I2C로 Lepton3를 제어하고 SPI로 열화상 이미지를 얻기 위한 라이브러리 드라이버를 제공합니다.

The repository contains a sample demo that illustrates how to control the sensor features, how to acquire thermal images and how to display them using OpenCV.
저장소에는 센서 기능을 제어하는 방법, 열화상 이미지를 획득하는 방법, OpenCV를 사용하여 이미지를 표시하는 방법을 설명하는 샘플 데모가 포함되어 있습니다.

The repository contains also a real world application that illustrates how to convert raw data values to real temperature values.
저장소에는 원시 데이터 값을 실제 온도 값으로 변환하는 방법을 설명하는 실제 애플리케이션도 포함되어 있습니다.