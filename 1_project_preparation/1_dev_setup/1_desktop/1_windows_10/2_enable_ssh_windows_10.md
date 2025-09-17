# 2025-09-15 (월요일) | Desktop Windows 10 SSH 설정 로그

---
## 1. OpenSSH 설치 및 활성화
1. **설정 → 앱 → 선택적 기능**로 이동
2. "OpenSSH Client"와 "OpenSSH Server"가 목록에 없으면 [기능 추가] 클릭 후 설치

---

## 2. Desktop 포트포워딩
1. WIFI 연결(WIFI가 공유기에 연결, 유선 랜은 아파트 백본에 붙어서 포트 포워딩 불가)
2. cmd / ipconfig 명령어에서 WIFI IP 주소, 게이트웨이 확인
3. 크롬 창에서 게이트웨이 주소 입력 후 공유기 설정 페이지 접속
4. 장치설정 / 트래픽 관리 / 포트 포워딩 설정 메뉴로 이동
5. 외부 포트(마음대로), 내부 IP 주소(WIFI IP 주소), 내부 포트(22), 설명 입력 후 설정 저장

---

## 3. PowerShell에서 SSH 서비스 활성화
1. Windows PowerShell을 관리자 권한으로 실행
2. 아래 명령어 입력 후 실행:
   - `Get-Service -Name sshd` (상태 확인)
   - `Start-Service -Name sshd` (서비스 시작)
   - `Set-Service -Name sshd -StartupType Automatic` (자동 시작 설정)
3. 서비스가 정상적으로 실행 중인지 확인

---

## 4. SSH 서버 접속 테스트
1. 동일 PC에서 `ssh localhost`로 접속 테스트
2. 다른 PC에서 `ssh 사용자명@Windows_IP주소`로 접속
3. 최초 접속 시 Windows 계정 비밀번호 입력

---

## 5. Windows 기타 참고 사항
- Windows 계정 비밀번호가 반드시 설정되어 있어야 SSH 접속 가능
- 네트워크 환경에 따라 방화벽/공유기 포트포워딩 필요
- SSH 서버 설정 파일: `C:\ProgramData\ssh\sshd_config` (포트 변경, 인증 방식 등)

---