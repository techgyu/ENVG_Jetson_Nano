# 2025-09-18 | Jetson Nano 무선 설정

---

## 1. 메뉴 / settings / Network 접속

## 2. Wireless 네트워크 / options 선택

## 3. IPv4 탭 선택 / Method: Manual 선택

## 4. Add 버튼 클릭 / IP 주소, 넷마스크, 게이트웨이 입력
- IP 주소: DHCP 자동 할당하는 범위 외에서 설정
- 넷마스크: ip a 명령 날렸을 때 /24로 되어 있으면 255.255.255.0
- 게이트웨이: 공유기 IP 주소
- DNS: 8.8.8.8

---

# 2025-09-19 | 5G WIFI 연결 불가 증상 발생

---

## 1. 증상
- 5G WIFI Online 상태이나, Jetson Nano에서 WIFI 신호 수신 불가

## 2. 펌웨어 업데이트
- 터미널에서 아래 명령어 실행
```bash
sudo apt update
sudo apt install --reinstall linux-firmware
```

## 3. 결론
- 5G WIFI와 관련하여 연결 불안정 증상이 있는 것으로 추정됨.
- 따라서, 원격 개발 환경을 위해서는 유선 LAN을 활용하여 안정적인 네트워크 연결이 필요한 것으로 판단하여, 무선 설정 OFF 후 유선 LAN으로 전환.