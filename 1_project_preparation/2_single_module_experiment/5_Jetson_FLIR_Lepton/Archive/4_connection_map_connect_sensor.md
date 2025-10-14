# 2025-09-23 | 핀맵 설계도 작성 및 저항 추가 부분 확인, 센서 연결

---

## 1. NVIDIA Jetson Nano

### 1.1 Jetson Nano J41 Header Pin Map
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

#### 1.1.1 각 Function의 의미

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

---

## 2. Breakout Board V2.0 

### 2.1 PIN-OUT
| Pin | Function     | Pin | Function            |
|-----|--------------|-----|---------------------|
|  1  | **GND**      |  2  | **Power in 3~5.5V** |
|  3  | VPROG        |  4  | VCC28               |
|  5  | **SDA**      |  6  | VCC28_IO            |
|  7  | **SPI_CLK**  |  8  | **SCL**             |
|  9  | **SPI_MOSI** | 10  | **SPI_CS**          |
| 11  | GPIO0        | 12  | **SPI_MISO**        |
| 13  | GPIO2        | 14  | GPIO1               |
| 15  | GPIO3/VSYNC  | 16  | VCC12               |
| 17  | RESET_L      | 18  | MASTER_CLK          |
| 19  | GND          | 20  | PW_DWN_L            |

#### 2.1.1 각 Function의 의미

**[필수] GND**: Ground(접지)  
- 전기 회로에서 기준 전압으로 사용되는 접지 신호입니다.
- 접지: 이상 전압 발생 시, 접지를 통해 방전

**[필수] Power in 3~5.5V**  
- Breakout 보드 및 Lepton 모듈에 전원을 공급하는 입력 핀입니다. 3~5.5V 범위의 전압을 인가해야 합니다.

**VPROG**: Programming Voltage(프로그래밍 전압)  
- Lepton 모듈의 펌웨어 업데이트, 플래시 메모리 접근, 초기화 및 구성에 사용되는 전압 입력 핀입니다. 일반적인 사용에서는 연결하지 않습니다.

**VCC28**  
- Breakout 보드 내부의 2.8V 전원 레일입니다. 외부에서 전원을 공급하지 않고, 내부 회로에서 사용됩니다.

**[필수] SDA**: Serial Data Line(직렬 데이터 라인)  
- I2C 통신에서 데이터 송수신에 사용되는 신호선입니다. 마스터와 슬레이브 간 데이터 전송을 담당합니다.

**VCC28_IO**  
- 2.8V IO 전원 레일입니다. I/O 신호의 기준 전압으로 사용되며, 레벨시프터 등 외부 회로의 저전압 측 전원으로 활용할 수 있습니다.

**[필수] SPI_CLK**: Serial Peripheral Interface Clock(직렬 주변 장치 인터페이스 클록)  
- SPI 통신에서 클럭 신호를 제공하는 라인입니다. 데이터 전송의 동기화를 담당합니다.

**[필수] SCL**: Serial Clock Line(직렬 클럭 라인)  
- I2C 통신에서 클럭 신호를 제공하는 라인입니다. SDA와 함께 데이터 송수신을 동기화합니다.

**[필수] SPI_MOSI**: Master Out Slave In  
- SPI 통신에서 마스터(예: Jetson)에서 슬레이브(Lepton)로 데이터를 전송하는 신호선입니다.

**[필수] SPI_CS**: Chip Select  
- SPI 통신에서 슬레이브 장치를 선택하는 신호선입니다. 활성화 시 해당 슬레이브와 통신이 시작됩니다.

**GPIO0 ~ GPIO3/VSYNC**  
- 범용 입출력(GPIO) 핀입니다.  
- GPIO3/VSYNC는 동기화 신호(VSYNC)로도 사용될 수 있습니다.  
- 특정 제어, 상태 신호, 또는 사용자 정의 용도로 활용됩니다.

**[필수] SPI_MISO**: Master In Slave Out  
- SPI 통신에서 슬레이브(Lepton)에서 마스터(Jetson)로 데이터를 전송하는 신호선입니다.

**VCC12**  
- 1.2V 전원 레일입니다. 내부 회로나 특정 IO의 기준 전압으로 사용됩니다.

**RESET_L**: Reset (Active Low)  
- Lepton 모듈을 리셋(초기화)하는 신호입니다. Low(0V)로 입력 시 모듈이 리셋됩니다.

**MASTER_CLK**  
- Lepton 모듈에 마스터 클럭(25MHz 등)을 공급하는 입력 핀입니다.  
- 보통 Breakout 보드에서 온보드 클럭이 제공되며, 외부에서 공급할 수도 있습니다.

**PW_DWN_L**: Power Down (Active Low)  
- Lepton 모듈을 저전력(파워다운) 모드로 전환하는 신호입니다. Low(0V)로 입력 시 파워다운 상태가 됩니다.

---

## 3. Jetson Nano & FLIR Breakout V2.0 Connection Map

| Jetson Nano J41 Pin           | Signal Name      | Breakout Board V2.0 Pin | Signal Name      | 비고                       |
|-------------------------------|------------------|-------------------------|------------------|---------------------------|
|  6, 9, 14, 20, 25, 30, 34, 39 | GND              | 1, 19                   | GND              | 접지(공통 연결)             |
|  2 or 4                       | 5V Power         | 2                       | Power in 3~5.5V  | 전원 공급                  |
|  3                            | I2C_2_SDA (I2C1) | 5                       | SDA              | I2C 데이터                  |
|  5                            | I2C_2_SCL (I2C1) | 8                       | SCL              | I2C 클럭                  |
| 13                            | SPI_2_SCK        | 7                       | SPI_CLK          | SPI 클럭                  |
| 37                            | SPI_2_MOSI       | 9                       | SPI_MOSI         | SPI 데이터(마스터→슬레이브)|
| 22                            | SPI_2_MISO       | 12                      | SPI_MISO         | SPI 데이터(슬레이브→마스터)|
| 18                            | SPI_2_CS0        | 10                      | SPI_CS           | SPI 칩 선택               |

> **참고:**  
> - GND는 여러 핀 중 하나만 연결해도 되지만, 신호 안정성을 위해 2개 이상 연결 권장  
> - VCC28_IO, VCC28, VCC12, VPROG, GPIOx, RESET_L, MASTER_CLK, PW_DWN_L 등은 기본 연결 불필요(특수 목적 시만 사용)
> - Jetson Nano의 SPI_2, I2C_2를 사용한 예시입니다.  
> - 실제 연결 시 핀 번호와 방향을 반드시 확인하세요.
>

## 4. Resistance Connection Map
| Jetson Nano J41 Pin           | Signal Name      | Breakout Board V2.0 Pin | Signal Name      | 비고                       |
|-------------------------------|------------------|-------------------------|------------------|---------------------------|
|  3                            | I2C_2_SDA (I2C1) | 5                       | SDA              | I2C 데이터                  |
|  5                            | I2C_2_SCL (I2C1) | 8                       | SCL              | I2C 클럭                  |

- 4.7kΩ 풀업 저항 또는 10kΩ 풀업 저항을 SDA와 SCL 라인에 연결
- 해당 라인에 저항이 있는지 확인 필요

# 2025-09-29 | 핀맵 설계도 pptx 파일 추가 완료, 핀 연결 완료

# 2025-09-30 | Jetson Nano Expansion Header 설정
