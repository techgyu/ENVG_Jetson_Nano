
# 2025-09-15 (월) | RTX 4090 Ubuntu 한글 입력/언어 설정 가이드

---

## Ubuntu 한글 입력기/언어팩 설정 절차

1. 패키지 업데이트
	```bash
	sudo apt update
	```
	- 시스템 패키지 목록을 최신으로 갱신합니다.

2. 한글 언어팩 설치
	```bash
	sudo apt install language-pack-ko
	```
	- 한글 메뉴/환경을 위한 언어팩을 설치합니다.

3. 한글 입력기(ibus-hangul) 설치
	```bash
	sudo apt install ibus-hangul
	```
	- 한글 입력을 위한 ibus-hangul 입력기를 설치합니다.

4. 시스템 재부팅
	```bash
	sudo reboot
	```
	- 입력기 및 언어팩 적용을 위해 재부팅합니다.

5. 입력 소스 추가 및 설정
	1) **설정(Settings)** → **Region & Language(지역 및 언어)** → **Input Sources(입력 소스)** 이동
	2) **+** 버튼 클릭 → **Korean(한국어)** → **Korean(Hangul)** 선택 후 추가
	3) 추가된 입력기를 기본값으로 설정하거나, 단축키(기본: `Super+Space` 또는 `Ctrl+Space`)로 한/영 전환 가능

---

## 참고/팁
- 한글 입력이 안 될 경우, ibus 재시작: `ibus restart`
- 입력기 전환 단축키는 **Settings → Keyboard Shortcuts**에서 변경 가능
- 한글/영문 전환이 안 될 때는 로그아웃 후 재로그인 또는 재부팅 권장