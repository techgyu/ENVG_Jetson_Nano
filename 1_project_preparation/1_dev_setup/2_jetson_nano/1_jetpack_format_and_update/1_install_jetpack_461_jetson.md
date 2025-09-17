# 2025-09-14 |Jetson Nano SD 카드 포맷 매뉴얼

---

## 준비물
- Jetson Nano 개발자 키트
- microSD 카드 (최소 16GB, 권장 32GB 이상, UHS-1 지원)
- microSD 카드 리더기
- Windows PC (Rufus 사용)
- 네트워크 연결

## 1. Jetson Nano 이미지 다운로드
- [JetPack 4.6.1 다운로드](https://developer.nvidia.com/jetpack-sdk-466)
  - JetPack 4.6.1 선택
  - SD Card Image Method → JETSON NANO DEVELOPER KITS 클릭
  - 이미지 파일 다운로드 (확장자: .img 혹은 .iso)

## 2. Rufus 다운로드 및 설치
- [Rufus 공식 사이트](https://rufus.ie/ko/)
  - Rufus 다운로드
  - `rufus-4.9.exe` 실행 (설치 불필요, 바로 실행 가능)

## 3. SD 카드 포맷 및 이미지 굽기
1. microSD 카드를 카드 리더기에 삽입 후 PC에 연결
2. Rufus 실행
3. **장치(Device)**: microSD 카드 선택
4. **부트 선택(Boot selection)**: 다운로드한 Jetson Nano 이미지 파일 선택
5. **파티션 방식(Partition scheme)**: MBR (기본값)
6. **파일 시스템(File system)**: FAT32 (기본값)
7. **시작(Start)** 클릭
8. 경고 팝업에서 **확인(OK)** 클릭
9. ISO / DD 이미지 모드 선택 팝업에서 **ISO 이미지 모드** 선택
10. 포맷 및 이미지 굽기 완료 후 SD 카드 리더기에서 SD 카드 제거

## 4. Jetson Nano에 microSD 카드 삽입 및 부팅
- microSD 카드를 Jetson Nano에 삽입
- 전원 연결 및 HDMI/USB 등 주변기기 연결
- Jetson Nano 부팅 (최초 부팅 시 초기 설정 진행)

## 참고 사항
- 이미지 파일 다운로드 및 굽기 시 네트워크 연결 필요
- microSD 카드 포맷 시 기존 데이터가 모두 삭제되므로 백업 필요
- Jetson Nano 최초 부팅 후 OS 초기 설정(언어, 네트워크 등) 진행
- JetPack 버전 및 이미지 파일은 프로젝트 요구에 따라 최신 버전 사용 가능

---