# 2025-09-23 | FLIR Breakout V2.0 레퍼런스 문서(데이터 시트) 확보 및 확인

---
(1_project_preparation\2_single_module_experiment\3_Jetson_FLIR_Lepton\document\2_Breakout V2.0\pdf\DS-16912-FLiR_Lepton_-_Breakout_Board_V2.pdf)


## 1. FLIR Lepton 3.5 PIN map
### 1.Mechanical(카메라 소켓 방향 기준)
|  1 |  3 |  5 |  7 |  9 | 11 | 13 | 15 | 17 | 19 |
|----|----|----|----|----|----|----|----|----|----|
|  2 |  4 |  6 |  8 | 10 | 12 | 14 | 16 | 18 | 20 |

### 2. ELECTRICAL SPECIFICATIONS
회로도: 250-0577-24, R200
조립도: 250-0577-25, R200
전원 입력: J2의 2번 핀(3<del>5.5V) 또는 J3의 2번 핀(3</del>5V)
출고 시 J5~J9 점퍼가 장착되어 있음
→ 모든 점퍼가 장착된 상태에서는 J2에서 전원 공급 가능
→ 점퍼를 제거하면 외부에서 전압, 마스터 클럭, 전원 시퀀스 제어 가능
주의: R120 버전 보드의 D1 다이오드 방향 오류로 J2 2번 핀에서 전원 공급이 안 될 수 있음
→ 이 경우 J3 2번 핀을 사용해야 함

### 3. PIN-OUT
| Pin | Function      | Pin | Function         |
|-----|--------------|-----|-----------------|
|  1  | GND          |  2  | Power in 3~5.5V |
|  3  | VPROG        |  4  | VCC28           |
|  5  | SDA          |  6  | VCC28_IO        |
|  7  | SPI_CLK      |  8  | SCL             |
|  9  | SPI_MOSI     | 10  | SPI_CS          |
| 11  | GPIO0        | 12  | SPI_MISO        |
| 13  | GPIO2        | 14  | GPIO1           |
| 15  | GPIO3/VSYNC  | 16  | VCC12           |
| 17  | RESET_L      | 18  | MASTER_CLK      |
| 19  | GND          | 20  | PW_DWN_L        |
#### 3.1 각 Function의 의미

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

**[필수] VCC28_IO**  
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