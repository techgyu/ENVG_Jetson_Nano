# 2025-09-15 (월요일) | Desktop SSH 설정 로그 (Windows & Ubuntu)

---

# Ubuntu SSH 설정

## 1. OpenSSH Server 설치
1. 터미널 열기 (Ctrl + Alt + T)
2. 패키지 목록 업데이트:
   ```bash
   sudo apt update
   ```
3. OpenSSH Server 설치:
   ```bash
   sudo apt install openssh-server
   ```

## 2. SSH 서비스 활성화 및 관리
1. SSH 서비스 상태 확인:
   ```bash
   sudo systemctl status ssh
   ```
2. SSH 서비스 시작:
   ```bash
   sudo systemctl start ssh
   ```
3. 부팅 시 자동 시작 설정:
   ```bash
   sudo systemctl enable ssh
   ```

## 3. 방화벽 설정 (UFW 사용 시)
1. UFW 상태 확인:
   ```bash
   sudo ufw status
   ```
2. SSH 포트(22) 허용:
   ```bash
   sudo ufw allow ssh
   ```
   또는
   ```bash
   sudo ufw allow 22
   ```

## 4. IP 주소 확인 및 포트포워딩
1. Ubuntu IP 주소 확인:
   ```bash
   ip addr show
   ```
   또는
   ```bash
   hostname -I
   ```
2. 공유기 포트포워딩 설정 (Windows와 동일)
   - 내부 IP: Ubuntu IP 주소
   - 내부 포트: 22
   - 외부 포트: 원하는 포트 번호

## 5. SSH 서버 접속 테스트
1. 동일 PC에서 접속 테스트:
   ```bash
   ssh localhost
   ```
2. 다른 PC에서 접속:
   ```bash
   ssh 사용자명@Ubuntu_IP주소
   ```
3. 최초 접속 시 Ubuntu 사용자 계정 비밀번호 입력

## 6. SSH 설정 파일 수정 (선택사항)
1. SSH 설정 파일 편집:
   ```bash
   sudo nano /etc/ssh/sshd_config
   ```
2. 주요 설정 옵션:
   - `Port 22` → 포트 변경
   - `PasswordAuthentication yes` → 비밀번호 인증 허용/거부
   - `PermitRootLogin no` → root 계정 로그인 허용/거부
3. 설정 변경 후 SSH 서비스 재시작:
   ```bash
   sudo systemctl restart ssh
   ```

## 7. Ubuntu 기타 참고 사항
- SSH 로그 확인: `sudo journalctl -u ssh`
- SSH 연결 로그: `/var/log/auth.log`
- 기본적으로 SSH는 22번 포트 사용
- 보안을 위해 키 기반 인증 설정 권장

---