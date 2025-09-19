# 2025-09-18 | Jetson Nano 한국어 입력 설정

---

## 1. 한글 언어팩 설치
```bash
sudo apt update
sudo apt install -y language-pack-ko fonts-nanum fonts-noto-cjk
```

## 2. 기본 언어 설정
```bash
sudo update-locale LANG=ko_KR.UTF-8
```
- 이 명령어로 시스템 기본 언어를 한국어로 변경합니다.
- 변경 후 재부팅이 필요합니다.

## 3. 입력기 설정
```bash
sudo apt install -y ibus ibus-hangul

ibus-daemon -drx

ibus-setup
```
- Input Method 탭 → Add → Korean - Hangul 선택

## 4. 적용 및 재부팅
```bash
sudo reboot
```

---