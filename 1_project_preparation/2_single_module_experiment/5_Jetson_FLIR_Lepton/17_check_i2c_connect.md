# 2025-09-30 | Check I2C Connection

---

## 1. SPI Buffer Size 설정 및 I2C 통신 확인
영구적으로 SPI 버퍼 값을 설정하려면 modeprobe용 구성 파일을 만들어야 합니다.

```bash
$ sudo nano /etc/modprobe.d/spidev.conf
```

아래 줄을 입력합니다.

```bash
options spidev bufsiz=20480
```

저장하고 Jetson Nano를 재부팅합니다.

---

### SPI Buffer size check (SPI 버퍼 크기 확인)
SPI 버퍼 크기가 올바른 값을 가지고 있는지 확인하려면 다음 명령을 사용하여 /sys/module/spidev/parameters/bufsiz 파일의 내용을 확인할 수 있습니다.

```bash
$ cat /sys/module/spidev/parameters/bufsiz
```
구성 절차를 올바르게 따르면 출력은 20480이어야 합니다.

## 2. i2c-tools 최신 버전 업데이트
```bash
sudo apt update
sudo apt install -y i2c-tools
```

## 3. I2C 통신 확인
I2C 케이블이 정확히 연결되었는지 확인하려면 다음 명령을 사용할 수 있습니다.

```bash
$ i2cdetect -y -r 0
$ i2cdetect -y -r 1
```

**출력 결과: 안 나옴**

## 4. I2C Pin을 (2) -> (1)로 변경 후
i2cdetect -y -r 1 명령어 실행 시 하기와 같은 정상 표출 확인
```bash
user@ubuntu:~$ i2cdetect -y -r 0
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