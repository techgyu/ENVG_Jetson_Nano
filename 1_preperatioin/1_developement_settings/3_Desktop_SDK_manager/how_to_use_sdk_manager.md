# Jetson Nano SDK Manager 사용 메뉴얼

---

## 준비물
- Ubuntu 18.04 설치된 PC (권장: 최신 LTS 버전)
- Jetson Nano Developer Kit
- 5 pin to USB 케이블 (데이터 전송 지원)
- microSD 카드 (Jetson Nano용)
- 네트워크 연결
- NVIDIA 계정

## 1. Ubuntu 데스크탑 준비
- Ubuntu PC를 부팅 후 네트워크 연결 확인
- 관리자 권한 계정으로 로그인
- 시스템 업데이트 권장: `sudo apt update && sudo apt upgrade`

## 2. NVIDIA SDK Manager 설치
- [NVIDIA SDK Manager 공식 사이트](https://developer.nvidia.com/nvidia-sdk-manager)에서 최신 버전 다운로드
- 다운로드한 `.deb` 파일 설치: `sudo dpkg -i sdkmanager*.deb`
- 설치 후 터미널에서 `sdkmanager` 실행
- NVIDIA 계정으로 로그인

## 3. Jetson Nano Recovery 모드 진입
- Jetson Nano의 전원을 끈 상태에서 FEC RC와 GND를 점퍼로 연결
- 전원 케이블 연결 후 화면이 출력되지 않으면 Recovery 모드 진입 성공
- USB 케이블로 Jetson Nano와 Ubuntu PC 연결

## 4. SDK Manager에서 Jetson Nano 연결
- SDK Manager 실행 후 Recovery 모드 Jetson Nano를 USB로 연결
- 장치가 인식되지 않으면 USB 케이블 재연결 또는 Jetson Nano 재부팅

## 5. JetPack 및 타겟 하드웨어 선택
- Target Hardware: Jetson Nano 선택
- Jetson Nano Developer Kit: p3448-0002 (SD카드 사용 버전) 선택
- JetPack Version: 4.6.6 선택
- 필요시 DeepStream, CUDA 등 추가 패키지 선택
- "Continue" 클릭하여 설치 진행

## 6. Flash 옵션 및 계정 설정
- Flash 단계에서 Jetson Nano OS 이미지가 SD 카드에 설치됨
- 사용자 계정(username)과 비밀번호(password) 신규 입력
- 계정 정보는 Jetson Nano 최초 부팅 시 로그인에 사용

## 7. 네트워크 옵션 설정
- 설치 중 IP Network 옵션 발생 시 "USB" 또는 "Ethernet" 중 USB 선택
- USB 연결로 Jetson Nano와 PC 간 통신 및 설치 진행
- 네트워크 연결이 원활하지 않을 경우, 유선 LAN 연결도 가능

## 8. 설치 완료 및 확인
- 설치 완료 후 Jetson Nano가 자동으로 재부팅됨
- Jetson Nano에 모니터, 키보드, 마우스 연결 후 최초 로그인 진행
- 설치된 JetPack 및 추가 패키지 정상 동작 확인
- 필요시 `sudo apt update && sudo apt upgrade`로 추가 업데이트

---