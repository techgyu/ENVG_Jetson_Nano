# 2025-09-14 | Desktop Ubuntu 18.04 NVIDIA SDK Manager로 Jetson Nano Jetpack 4.6.1 -> 4.6.6 업데이트

---

## 1. Ubuntu 18.04 설치된 Desktop에서 SDK Manager 실행
- Ubuntu 18.04가 설치된 PC를 부팅합니다.
- SDK Manager 실행: 터미널에서 `sdkmanager` 명령어 입력 

## 2.SDK 매니저에서 Jetson Nano용 JetPack 4.6.6 선택 후 설치 진행
- SDK 매니저에서 Target Hardware: Jetson Nano 선택
- Jetson Nano Developer Kit: p3448-0002(sd카드 사용 버전) 선택
- JetPack Version: 4.6.6 선택
- OS 및 추가 패키지(DeepStream, CUDA 등) 선택 가능
- "Continue" 클릭하여 설치 진행

## 3. 설치 중 flash 옵션 발생 시 username과 password 신규 세팅
- Flash 단계에서 Jetson Nano의 OS 이미지가 SD 카드에 설치됨
- 사용자 계정(username)과 비밀번호(password) 신규 입력
- 계정 정보는 Jetson Nano 최초 부팅 시 로그인에 사용

## 4. 설치 중 IP Network 옵션 발생 시 USB 선택하여 진행
- 네트워크 연결 방식 선택 시 "USB" 또는 "Ethernet" 중 USB 선택
- USB 연결로 Jetson Nano와 PC 간 통신 및 설치 진행
- 네트워크 연결이 원활하지 않을 경우, 유선 LAN 연결도 가능

## 5. 설치 완료
- 설치가 완료되면 Jetson Nano가 자동으로 재부팅됨
- Jetson Nano에 모니터, 키보드, 마우스 연결 후 최초 로그인 진행
- 설치된 JetPack 및 추가 패키지 정상 동작 확인
- 필요 시 `sudo apt update && sudo apt upgrade`로 추가 업데이트

---