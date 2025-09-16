# 2025-09-15 (월요일) | RTX 4090 데스크탑 Ubuntu 설치/업그레이드 일지

---

## 0. 시스템 사양
- **CPU**: AMD Ryzen 7800X3D
- **메인보드**: ASUS B650E-E GAMING WIFI
- **LAN**: Intel I225-V (온보드)
- **RAM**: 32GB
- **GPU**: NVIDIA RTX 4090 24GB
- **SSD1**: SAMSUNG 980 PRO 2TB NVMe (Windows 10 22H2)
- **SSD2**: WD BLUE SN550 1TB NVMe (Ubuntu)

---

## 1. 포맷/업그레이드 배경
- Ubuntu 18.04 LTS 설치 상태에서 **Intel I225-V 랜카드 미지원**
- 유선/무선 네트워크 모두 연결 불가 → Ubuntu 20.04로 업그레이드 시도

---

## 2. Ubuntu 20.04 설치 과정
- [Ubuntu 20.04 다운로드](https://releases.ubuntu.com/20.04/)
  - Desktop Image / Ubuntu 20.04 LTS 선택, .iso 다운로드
- 설치 후 **유선 LAN은 정상 동작**, **무선 WIFI는 연결 불가**
  - 20.04 커널이 무선 칩셋을 지원하지 않음
- 무선 네트워크 필요로 인해 **Ubuntu 22.04 업그레이드 결정**

---

## 3. Ubuntu 22.04 업그레이드 및 문제 해결
- Ubuntu 20.04에서 **GUI 업그레이드 기능** 활용해 22.04로 업그레이드
- 업그레이드 후 **유선 LAN 정상 동작**
- **WIFI 연결 불가 현상** 지속 → 전원 OFF 후 완전 방전 & 재부팅 시 정상 연결됨
  - (메인보드/칩셋 초기화 효과)

---