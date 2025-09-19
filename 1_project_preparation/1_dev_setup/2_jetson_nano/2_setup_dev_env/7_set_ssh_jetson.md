# 2025-09-18 | Jetson Nano SSH 개방
- ENVG_Jetson_Nano\1_project_preparation\1_dev_setup\1_desktop\2_ubuntu\6_enable_ssh_ubuntu.md 의 내용을 참고

---

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

## 4. IP 주소 확인 및 WIFI 주소 DHCP 고정 설정
1. 공유기 관리자 페이지를 통해서 DHCP 할당 가능 범위 확인
- 예: 코넷 DHCP 할당 범위:
- 예: 프리미엄 DHCP 할당 범위:

2. WIFI에서 받아오는 IP 주소 DHCP 고정 설정
- Ubuntu의 WIFI 주소 설정에서 수동(manual) IP 주소 설정
- 단, IP 설정 시, 1번에서 설정한 코넷 DHCP 할당 범위와 프리미엄 DHCP 할당 범위 외에서 설정
- 만약 자동 할당되는 IP 주소와 겹칠 시, 네트워크 충돌 발생
- Netmask는 ip a 명령어를 통해 IPv4 주소 뒤에 /24로 표시되어 있으면 255.255.255.0으로 설정
- 게이트웨이는 공유기 IP 주소로 설정

3. WIFI 중단 후 재연결

## 5. 공유기 포트포워딩 설정
   - 공유기 IP 주소 접속 후 관리자 로그인
   - 포트포워딩 항목에서 2에서 고정 설정해둔 IP 주소를 입력
  
## 6. 외부망에서 SSH 서버 접속 테스트
1. 동일 PC에서 접속 테스트:
   ```bash
   ssh localhost
   ```
2. 다른 PC에서 접속:
   ```bash
   ssh -p 12351 user@221.163.171.7
   ```
3. 최초 접속 시 Ubuntu 사용자 계정 비밀번호 입력

---