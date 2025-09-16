# 2025-09-14 (일요일) | Desktop Ubuntu 포멧 로그

---

## 0. 준비물
- 사용하려는 우분투 버전에서 메인보드의 유선 랜 카드를 지원하는지 확인
- ASUS TUF B350M-PLUS GAMING 메인보드: Realtek RTL8111H 지원
- ASUS B650E-E GAMING WIFI 메인보드: Intel I225-V "미"지원
- 미지원 렌 카드 보드에 우분투 설치 시, 해결 매우 곤란

## 1. Ubuntu 18.04 이미지 다운로드
- [Ubuntu 18.04 다운로드](https://releases.ubuntu.com/18.04/)
  - Desktop Image / Ubuntu 18.04 LTS 선택
  - 이미지 파일 다운로드 (확장자: .img 혹은 .iso)

## 2. Rufus 다운로드 및 실행
- [Rufus 공식 사이트](https://rufus.ie/ko/)
  - Rufus 다운로드
  - `rufus-4.9.exe` 실행

## 3. USB에 이미지 굽기
1. USB 메모리를 USB 포트에 삽입
2. Rufus 실행
3. **장치**: USB 메모리 선택
4. **부트 선택**: 다운로드한 Ubuntu 18.04 ISO 이미지 선택
5. **옵션**: 
    Large FAT32 파일 시스템 선택 (기본값)
    GPT 파티션 선택 (기본값)
    32KB 클러스터 크기 선택 (기본값)
6. **시작** 클릭
7. 경고 팝업에서 **확인** 클릭
8. ISO / DD 이미지 모드 선택 팝업에서 **ISO 이미지 모드** 선택
9. 포맷 완료 후 USB 메모리 제거

## 4. Desktop에 Ubuntu 설치
1. USB 메모리를 Desktop에 삽입 후 부팅
2. BIOS 진입 (보통 F2, F12, DEL 키)
3. 부팅 순서 변경: USB 메모리를 최우선으로 설정
4. ASUS BIOS / Boot / Secure Boot Control → other os 선택
5. 변경 사항 저장 후 재부팅
6. Ubuntu 설치 화면에서 "Ubuntu 설치" 선택
7. 언어 선택 후 "계속" 클릭
8. 키보드 레이아웃 선택 후 "계속" 클릭
9. ✅ 설정 방법 (SSD 전체를 우분투 전용으로)
   - Installation type에서 👉 Something else 선택
   - (자동 설치 옵션 쓰면 윈도우 SSD까지 건드릴 위험 있어서 수동이 안전해요)
   - 디스크 (nvme0n1) 선택 후 → 기존 파티션 싹 지움 (Delete)
   - + 버튼 눌러서 새 파티션 생성
     - Type: Primary
     - Location: Beginning of this space
     - Use as: Ext4 journaling file system
     - Mount point: /
   - Device for boot loader installation → 반드시 nvme0n1 (우분투 SSD) 선택
   - 🚀 결과
     - SSD 하나 전체가 Ext4 루트 파티션(/) 으로 잡힘
     - 우분투 운영체제, 프로그램, 데이터 전부 이 한 파티션에 들어감
     - EFI는 건드리지 않고 → GRUB이 윈도우 SSD EFI에 항목만 추가 → 설치 끝나고 재부팅하면 듀얼부팅 자동 완성
10. 위치 선택 후 "계속" 클릭
11. 사용자 정보 입력 후 "계속" 클릭
12. 설치 완료 후 재부팅
13. USB 메모리 제거
14. Ubuntu 로그인 화면에서 사용자 정보 입력 후 로그인

---
