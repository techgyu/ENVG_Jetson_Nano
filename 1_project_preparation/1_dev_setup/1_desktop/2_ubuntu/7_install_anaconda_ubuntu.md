# 2025-09-17 | Desktop Ubuntu Anaconda 설치

---

## 1. Anaconda 설치 파일 다운로드

1. 최신 Anaconda 설치 파일 다운로드 (64-bit, Python 3.x 기준)
   ```bash
   wget https://repo.anaconda.com/archive/Anaconda3-2023.07-1-Linux-x86_64.sh
   ```
   > ※ 최신 버전은 [공식 다운로드 페이지](https://www.anaconda.com/products/distribution#download-section)에서 확인 가능

**다운로드 도중 속도 저하 문제 발생**
- 노트북에서 다운로드 후에 WinSCP로 Desktop Ubuntu로 전송해도 64KB/s로 느림

**현재 연결된 WIFI 정보 확인**
```bash
sudo nmcli device wifi
```
- 확인 결과 2.4GHz 대역으로 연결되어 있어 WIFI 교체 필요
**현재 연결 가능한 WIFI 목록 확인**
```bash
sudo nmcli device wifi list
- 확인 결과 WIFI 목록이 제대로 표출되지 않아 rescan 필요

** WIFI 목록 재검색 및 재확인**
```bash
sudo nmcli device wifi rescan
sudo nmcli device wifi list
```
- 재검색 후 5GHz 대역 WIFI 식별하여 연결 시도

**5GHz 대역 WIFI 연결**
```bash
sudo nmcli device wifi connect "KT_GiGA_5G_EA19" password "패스워드"
```

** 연결되었는지 확인**
```bash
sudo nmcli device wifi list
```
- IN-USE에 5GHz 대역 WIFI가 연결된 것을 확인

**다시 Anaconda 설치 파일 WinSCP 전송 시도**
- 10MB/s 이상 속도로 정상 전송됨을 확인
---

## 2. 설치 파일 실행 및 설치

1. 설치 파일 실행
   ```bash
   bash Anaconda3-2025.06-0-Linux-x86_64.sh
   ```
2. 안내에 따라 [Enter] 키로 진행, 라이선스 동의(y), 설치 경로 지정(기본값 추천)
3. 설치 완료 후, 다음 명령어로 conda 활성화
   ```bash
   source ~/anaconda3/bin/activate
   ```
4. conda 버전 확인
5. ```bash
   conda --version
   ```
   - 25.5.1 버전 확인

---

## 3. 환경 변수 등록 (선택)

1. 설치 마지막에 "conda initialize" 관련 질문이 나오면 yes 입력
2. 만약 생략했다면, 아래 명령어로 수동 등록
   ```bash
   echo 'export PATH="$HOME/anaconda3/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

---

## 4. 설치 확인

1. 아래 명령어로 정상 설치 확인
   ```bash
   conda --version
   ```

---

## 5. (선택) 기본 환경 최신 버전으로 업데이트

```bash
conda update -n base -c defaults conda
```
