# 2025-09-15 | Desktop 2번 디스크에 Ubuntu 설치
---

## 0. 시스템 사양
- CPU: AMD Ryzen 7800X3D
- MB: ASUS B650E-E GAMING WIFI (LAN: Intel I225-V)
- RAM: 32GB
- GPU: NVIDIA RTX 4090 24GB
- SSD1: SAMSUNG 980 PRO 2TB NVMe (Windows 10)
- SSD2: WD BLUE SN550 1TB NVMe (Ubuntu)

---

## 1. 이전 우분투 설치에서 발생했던 문제
- Ubuntu 18.04 LTS 설치 시 Intel I225-V 랜카드 미지원
- 유선/무선 네트워크 모두 연결 불가 → Ubuntu 20.04로 업그레이드 필요

---

## 2. Ubuntu 20.04 설치 파일 준비
- [Ubuntu 20.04 다운로드](https://releases.ubuntu.com/20.04/)
  - Desktop Image / Ubuntu 20.04 LTS 선택, .iso 다운로드

---

## 3. Rufus로 USB 부팅 디스크 제작
- [Rufus 공식 사이트](https://rufus.ie/ko/)
  - Rufus 다운로드 및 실행 (설치 불필요)
  - USB 메모리 연결 후, 다운로드한 Ubuntu 20.04 ISO 선택
  - 기본 옵션(Large FAT32, GPT, 32KB)으로 굽기

---

## 4. Ubuntu 20.04 설치
- USB로 부팅 후 설치 진행
- 언어/키보드/디스크 파티션 등 기본 설정
- SSD2(1TB)에 Ubuntu 설치, 설치 완료 후 재부팅

---

## 5. Ubuntu 20.04 부팅 후 식별된 문제점
- 유선 LAN은 정상 동작, 무선 WIFI는 연결 불가
  - 20.04 커널이 무선 칩셋 미지원
- 무선 네트워크 사용을 위해 Ubuntu 22.04 업그레이드 필요

---

## 6. Ubuntu 22.04 업그레이드
- Ubuntu 20.04에서 GUI 업그레이드 기능으로 22.04로 업그레이드
- 업그레이드 후 유선 LAN 정상 동작, WIFI 여전히 미작동

---

## 7. WIFI 연결 불가 증상 해결
- 전원 OFF → 전원 코드 분리 → 전원 버튼 연타(완전 방전)
- 재부팅 후 WIFI 정상 연결 (메인보드/칩셋 초기화 효과)

---