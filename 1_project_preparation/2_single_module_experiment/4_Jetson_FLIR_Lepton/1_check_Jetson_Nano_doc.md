# 2025-09-22 | Jetson Nano 레퍼런스 문서(데이터 시트) 확보 및 확인

---

## 1. Jetson Nano Developer Kit User Guide
[Jetson Download Center](https://developer.nvidia.com/embedded/downloads#?search=Developer%20Kit%20User%20Guide)

## 2. Jetson Nano Developer Kit Datasheet
[Jetson Download Center](https://developer.nvidia.com/embedded/downloads#?search=Developer%20Kit%20Datasheet)

## 3. Jetson Nano J41 Header Pin Map
[Jetson Nano GPIO Header PINOUT](https://jetsonhacks.com/nvidia-jetson-nano-j41-header-pinout/)
| Pin | Name / 기능         | GPIO      | Pin | Name / 기능         | GPIO      |
|-----|---------------------|-----------|-----|---------------------|-----------|
|  1  | 3.3V Power          |           |  2  | 5V Power            |           |
|  3  | I2C_2_SDA (I2C1)    |           |  4  | 5V Power            |           |
|  5  | I2C_2_SCL (I2C1)    |           |  6  | GND                 |           |
|  7  | AUDIO_MCLK          | gpio216   |  8  | UART_2_TX (ttyTHS1) |           |
|  9  | GND                 |           | 10  | UART_2_RX (ttyTHS1) |           |
| 11  | UART_2_RTS          | gpio50    | 12  | I2S_4_SCLK          | gpio79    |
| 13  | SPI_2_SCK           | gpio14    | 14  | GND                 |           |
| 15  | LCD_TE              | gpio194   | 16  | SPI_2_CS1           | gpio232   |
| 17  | 3.3V Power          |           | 18  | SPI_2_CS0           | gpio15    |
| 19  | SPI_1_MOSI          | gpio16    | 20  | GND                 |           |
| 21  | SPI_1_MISO          | gpio17    | 22  | SPI_2_MISO          | gpio13    |
| 23  | SPI_1_SCK           | gpio18    | 24  | SPI_1_CS0           | gpio19    |
| 25  | GND                 |           | 26  | SPI_1_CS1           | gpio20    |
| 27  | I2C_1_SDA (I2C0)    |           | 28  | I2C_1_SCL (I2C0)    |           |
| 29  | CAM_AF_EN           | gpio149   | 30  | GND                 |           |
| 31  | GPIO_PZ0            | gpio200   | 32  | LCD_BL_PWM          | gpio168   |
| 33  | GPIO_PE6            | gpio38    | 34  | GND                 |           |
| 35  | I2S_4_LRCK          | gpio76    | 36  | UART_2_CTS          | gpio51    |
| 37  | SPI_2_MOSI          | gpio12    | 38  | I2S_4_SDIN          | gpio77    |
| 39  | GND                 |           | 40  | I2S_4_SDOUT         | gpio78    |

## 4. 각 Function의 의미

**3.3V Power / 5V Power**  
- Jetson Nano 보드에 전원을 공급하거나, 외부 회로에 전원을 공급할 때 사용하는 핀입니다.  
- 3.3V, 5V 각각의 전압을 제공합니다.

**GND**  
- 회로의 기준 전압(0V)인 접지(Ground) 신호입니다.

**I2C_2_SDA (I2C1), I2C_2_SCL (I2C1), I2C_1_SDA (I2C0), I2C_1_SCL (I2C0)**  
- I2C 통신용 데이터(SDA) 및 클럭(SCL) 신호선입니다.  
- 센서, 주변장치 등과 직렬 통신에 사용됩니다.

**AUDIO_MCLK**  
- 오디오용 마스터 클럭 신호입니다.

**UART_2_TX, UART_2_RX, UART_2_RTS, UART_2_CTS**  
- UART(직렬통신)용 송신(TX), 수신(RX), 요청(RTS), 클리어(CTS) 신호입니다.  
- 외부 장치와 시리얼 통신에 사용됩니다.

**I2S_4_SCLK, I2S_4_LRCK, I2S_4_SDIN, I2S_4_SDOUT**  
- I2S(오디오 직렬 버스)용 클럭, LRCK, 데이터 입력/출력 신호입니다.  
- 오디오 데이터 전송에 사용됩니다.

**SPI_1_MOSI, SPI_1_MISO, SPI_1_SCK, SPI_1_CS0, SPI_1_CS1**  
- SPI1 버스용 데이터 송신(MOSI), 수신(MISO), 클럭(SCK), 칩 선택(CS) 신호입니다.

**SPI_2_MOSI, SPI_2_MISO, SPI_2_SCK, SPI_2_CS0, SPI_2_CS1**  
- SPI2 버스용 데이터 송신(MOSI), 수신(MISO), 클럭(SCK), 칩 선택(CS) 신호입니다.

**LCD_TE, LCD_BL_PWM**  
- LCD 패널용 타이밍 신호(TE) 및 백라이트 PWM 제어 신호입니다.

**CAM_AF_EN**  
- 카메라 오토포커스 구동 신호입니다.

**GPIO_xxx**  
- 범용 입출력(GPIO) 핀입니다.  
- 사용자가 원하는 신호 입력/출력, 제어 등에 활용할 수 있습니다.

