
# Jetson Nano Expansion Header Tool 사용법 (단계별 정리)

---

## 1. Expansion Header Tool 실행

터미널에서 아래 명령어 입력:
```bash
sudo /opt/nvidia/jetson-io/jetson-io.py
```

---

## 2. 40핀 헤더 설정 메뉴 진입

실행 후 메뉴에서:

- `Configure Jetson 40pin Header` 선택 (엔터)

---

## 3. 핀 기능 수동 설정

메뉴에서 `Configure header pins manually` 선택 (엔터)

아래와 같이 원하는 기능(예: spi2, i2c2 등)에 엔터로 체크:
```
=================== Jetson Expansion Header Tool ===================
|                 [ ] spi1          (19,21,23,24,26)               |
|                 [ ] spi2          (13,16,18,22,37)               |
|                 [ ] i2c2          (3,5)                          |
|                 [ ] uartb-cts/rts (11,36)                        |
|                 ...                                              |
```
체크하면 `[x]`로 바뀜 → 해당 핀 기능 활성화

---

## 4. 설정 저장 및 적용

모든 핀 선택 후, 메뉴에서 아래 항목을 선택:

- `Save and reboot to reconfigure pins` (설정 저장 + 재부팅)

> **Tip:**
> - `Save and exit without rebooting`은 저장만 하고 재부팅은 직접 해야 적용됨
> - `Discard all pin changes`는 변경사항 취소

---

## 5. 적용 확인

재부팅 후 다시 Expansion Header Tool 실행:
```bash
sudo /opt/nvidia/jetson-io/jetson-io.py
```
핀맵/기능이 원하는 대로 적용됐는지 확인

---

## 6. 참고

- 핀 기능 변경 후 반드시 재부팅 필요
- 실제 하드웨어 연결 전 핀맵/기능 재확인
- 여러 기능을 동시에 활성화 가능 (단, 핀 충돌 주의)

---