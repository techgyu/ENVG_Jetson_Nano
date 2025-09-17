# 2025-09-16 | Dekstop Ubuntu 절전 모드 해제

---

## 1. 화면 보호기 설정 해제
settings / privacy / display / screen / blank screen delay : never 로 설정

## 2. 절전 모드 해제
```bash

# 어댑터 전원 연결 상태에서 절전 안 함
gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type 'nothing'

# 배터리 상태에서 절전 안 함
gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type 'nothing'

```

## 3. 절전 모드 해제 확인
```bash

gsettings get org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type
gsettings get org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type

```
- 둘 다 'nothing' 으로 나오면 설정 완료

## 4. 더블 체크
1. 전원 관련 절전 설정 확인
```bash
gsettings get org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type
gsettings get org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type
```
- 둘 다 'nothing' 으로 나오면 설정 완료

2. 화면 자동 꺼짐(Blank Screen) 확인
```bash
gsettings get org.gnome.desktop.session idle-delay
```
- 값이 uint32 0 → 화면이 자동으로 꺼지지 않음
- 값이 uint32 300 → 300초(5분) 후 화면 꺼짐

3. 시스템 전체 suspend 설정 확인
```bash
systemctl status sleep.target suspend.target hibernate.target hybrid-sleep.target
```
- "disabled" 상태면 해당 모드로 진입하지 않음