# 2025-09-15 | Desktop Ubuntu 무선 설정

---

## 1. 무선 랜 카드 정보 확인
```bash
user@user:~$ lspci | grep Network
07:00.0 Network controller: MEDIATEK Corp. Device 0616
```

## 2. MEDIATEK Corp. Device 0616 무선 랜카드를 지원하는 Ubuntu 버전
- Ubuntu 22.04 이상 버전에서 지원
- Ubuntu 18.04, 20.04에서는 지원하지 않음(네트워크 연결 불가)