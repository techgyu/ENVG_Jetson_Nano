# 2025-10-13 | Jetson Nano 초기화(Reset)

---

## 1. 초기화하는 이유
Jetson Nano SPI 통신 테스트가 불가능한 상황인데, 하드웨어 또는 소프트웨어 설정이 꼬였을 가능성이 있음.
따라서, 최초 세팅에서 SPI 통신 테스트를 진행하여, Jetpack의 문제인지, 하드웨어 문제인지 확인하기 위해 초기화 진행.

## 2. 초기화 방법
이전의 Jetson Nano JetPack 4.6.1 설치 방법과 동일하게 진행.
[1_install_jetpack_461_jetson.md](../1_jetpack_format_and_update/1_install_jetpack_461_jetson.md) 참고.

## 3. 초기화 후 최초 부팅
**[유선_네트워크_설정]**: 5GHz WiFi 연결
**[사용자_이름]**: user
**[비밀번호]**: 1234567890a
- 비밀번호는 입력 시 화면에 표시되지 않음.