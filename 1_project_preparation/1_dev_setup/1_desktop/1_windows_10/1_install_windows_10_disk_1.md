# 2025-09-15 | Desktop 1번 디스크에 Windows 10 설치

---

## 1. Windows 10 설치 USB 준비

1. [Microsoft 공식 Windows 10 다운로드 페이지](https://www.microsoft.com/ko-kr/software-download/windows10) 접속
2. '미디어 생성 도구' 다운로드 및 실행
3. USB 메모리(8GB 이상) PC에 연결
4. 미디어 생성 도구에서 '다른 PC용 설치 미디어 만들기' 선택
5. 언어/에디션/아키텍처(64비트) 선택 후 USB 드라이브 지정
6. 설치 미디어 생성 완료 시까지 대기
7. 완료 후 USB 안전하게 분리

---

## 2. BIOS Boot 설정

1. 설치 USB를 데스크탑에 연결
2. PC 전원 ON → BIOS 진입 (DEL, F2, F12 등 메인보드별 진입키)
3. Boot 메뉴에서 'USB'를 부팅 우선순위 1번으로 설정
4. (ASUS 기준) Secure Boot → 'Other OS'로 변경, CSM(Compatibility Support Module) 활성화 필요 시 Enable
5. 변경사항 저장 후 재부팅

---

## 3. Windows 10 설치
1. USB로 부팅되면 Windows 설치 화면 진입
2. 언어/키보드/시간 등 기본 설정 후 '다음' 클릭
3. '지금 설치' 클릭
4. 제품 키 입력(없으면 '제품 키 없음' 선택)
5. 에디션 선택(Windows 10 Pro/ Home 등)
6. '사용자 지정: Windows만 설치(고급)' 선택
7. 설치할 디스크(1번 SSD) 선택 → 기존 파티션 모두 삭제 후 '새로 만들기'로 전체 공간 할당
8. 포맷 후 '다음' 클릭 → 설치 진행
9. 설치 완료 후 자동 재부팅, USB 제거
10. 초기 설정(계정, 네트워크, 개인정보 등) 완료
11. 바탕화면 진입 후 드라이버/윈도우 업데이트 진행
