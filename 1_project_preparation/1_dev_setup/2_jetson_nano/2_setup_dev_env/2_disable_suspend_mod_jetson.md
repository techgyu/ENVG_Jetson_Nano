# 2025-09-18 | Jetson Nano 절전 모드 해제 설정

---

## 1. 전원 관련 절전 설정 확인
```bash
gsettings get org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type
gsettings get org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type
```
→ 두 값이 'nothing' 이면 절전모드 안 들어갑니다.

## 2. 화면 자동 꺼짐(Blank Screen) 확인
```bash
gsettings get org.gnome.desktop.session idle-delay
```
- 값이 uint32 0 → 화면이 자동으로 꺼지지 않음
- 값이 uint32 300 → 300초(5분) 후 화면 꺼짐

## 3. 시스템 전체 suspend 설정 확인
```bash
systemctl status sleep.target suspend.target hibernate.target hybrid-sleep.target
```
- "disabled" 상태면 해당 모드로 진입하지 않음