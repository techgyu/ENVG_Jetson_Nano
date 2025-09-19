# 2025-09-14 | Desktop Ubuntu 18.04 NVIDIA SDK Manager 설치

---

## 1. Ubuntu 설치된 Desktop 부팅
- Ubuntu가 설치된 PC를 부팅합니다.
- 네트워크 연결(유선/무선) 및 관리자 권한 계정 준비.
- 시스템 업데이트 권장: `sudo apt update && sudo apt upgrade`

## 2. Ubuntu ARM64용 NVIDIA SDK 매니저 설치
- [NVIDIA SDK Manager 공식 사이트](https://developer.nvidia.com/nvidia-sdk-manager)에서 최신 버전 다운로드
- 설치 전, 의존성 패키지 설치: `sudo apt install -y curl wget gnupg2`
- 다운로드한 `.deb` 파일 설치: `sudo dpkg -i sdkmanager*.deb`
- 설치 후 실행: `sdkmanager`
- NVIDIA 계정 필요, 로그인 진행

---