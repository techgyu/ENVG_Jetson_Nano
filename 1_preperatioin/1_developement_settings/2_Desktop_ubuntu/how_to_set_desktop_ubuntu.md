# Desktop Ubuntu 포맷 메뉴얼

---

## 준비물
- 설치할 Ubuntu 버전에서 메인보드의 유선 랜 카드 지원 여부 확인
  - 예시: ASUS TUF B350M-PLUS GAMING (Realtek RTL8111H 지원)
  - 예시: ASUS B650E-E GAMING WIFI (Intel I225-V 미지원)
  - 미지원 랜카드 보드에 설치 시 네트워크 연결 곤란, 사전 확인 필수
- USB 메모리 (최소 8GB, 권장 16GB 이상)
- USB 메모리 리더기 또는 포트
- Windows PC (Rufus 사용)
- 네트워크 연결

## 1. Ubuntu 이미지 다운로드
- [Ubuntu 18.04 다운로드](https://releases.ubuntu.com/18.04/)
  - Desktop Image / Ubuntu 18.04 LTS 선택
  - 이미지 파일 다운로드 (.iso 권장)
  - 최신 버전 필요 시 [Ubuntu 공식 사이트](https://ubuntu.com/download/desktop) 참고

## 2. Rufus 다운로드 및 실행
- [Rufus 공식 사이트](https://rufus.ie/ko/)
  - Rufus 다운로드
  - `rufus-4.9.exe` 실행 (설치 불필요, 바로 실행 가능)

## 3. USB에 Ubuntu 이미지 굽기
1. USB 메모리를 PC에 연결
2. Rufus 실행
3. **장치(Device)**: USB 메모리 선택
4. **부트 선택(Boot selection)**: 다운로드한 Ubuntu ISO 이미지 선택
5. **파티션 방식(Partition scheme)**: GPT (대부분 최신 PC는 GPT, 구형은 MBR)
6. **파일 시스템(File system)**: Large FAT32 (기본값)
7. **클러스터 크기(Cluster size)**: 32KB (기본값)
8. **시작(Start)** 클릭
9. 경고 팝업에서 **확인(OK)** 클릭
10. ISO / DD 이미지 모드 선택 팝업에서 **ISO 이미지 모드** 선택
11. 포맷 및 이미지 굽기 완료 후 USB 메모리 제거

## 4. Desktop에 Ubuntu 설치
1. USB 메모리를 데스크탑에 삽입 후 부팅
2. BIOS 진입 (F2, F12, DEL 등)
3. 부팅 순서 변경: USB 메모리를 최우선으로 설정
4. (ASUS 기준) Boot → Secure Boot Control → Other OS 선택
5. 변경 사항 저장 후 재부팅
6. Ubuntu 설치 화면에서 "Ubuntu 설치" 선택
7. 언어 선택 후 "계속" 클릭
8. 키보드 레이아웃 선택 후 "계속" 클릭
9. "Ubuntu 설치 유형"에서 "디스크 지우고 Ubuntu 설치" 선택 후 "지금 설치" 클릭
10. 위치 선택 후 "계속" 클릭
11. 사용자 정보 입력 후 "계속" 클릭
12. 설치 완료 후 재부팅
13. USB 메모리 제거
14. Ubuntu 로그인 화면에서 사용자 정보 입력 후 로그인

## 참고 사항
- 설치 전 메인보드 랜카드 지원 여부 반드시 확인
- USB 메모리 포맷 시 기존 데이터가 모두 삭제되므로 백업 필요
- 설치 후 네트워크, 드라이버 등 추가 설정 필요할 수 있음
- 최신 Ubuntu 버전 설치 시 일부 옵션/화면이 다를 수 있음

---
