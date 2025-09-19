# 2025-09-17 | Desktop Ubuntu Git 설치 및 VSCode Git 연동

---

## 1. Git 설치

Ubuntu에서 Git을 설치하려면 아래 명령어를 터미널에 입력하세요.

```bash
sudo apt update
sudo apt install git
```

설치가 완료되면 아래 명령어로 버전을 확인할 수 있습니다.

```bash
git --version
```
---

## 2. Git 사용자 정보 설정

Git을 처음 사용할 때는 사용자 이름과 이메일을 등록해야 합니다.

```bash
git config --global user.name "ubuntu_gyuteak"
git config --global user.email "rlarbxor85@gmail.com"
```

설정 확인:

```bash
git config --list
```

---

## 3. VSCode Remote SSH 접속

1. **VSCode에서 Remote-SSH 확장 설치**
   - VSCode 좌측 Extensions(확장) 아이콘 클릭 → "Remote - SSH" 검색 후 설치

2. **SSH 설정**
   - VSCode 좌측 하단의 녹색 >< 아이콘 클릭 → "Remote-SSH: Connect to Host..." 선택
   - SSH 접속 정보를 입력 (예: `user@192.168.0.10`)
   - 처음 접속 시 비밀번호 또는 SSH 키 인증 필요

3. **접속 성공 시**
   - VSCode 상단에 `[SSH: <hostname>]` 표시
   - 원격 Ubuntu 서버의 파일 탐색, 터미널, Git 등 모든 기능을 로컬처럼 사용 가능

---

## 4. Repository 복제 후 VSCode에서 Git 연동

1. **원격 서버에서 원하는 위치로 이동**
   ```bash
   cd ~/workspace  # 예시: 작업 폴더로 이동
   ```

2. **Git 저장소 복제**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

3. **VSCode에서 Git 연동 확인**
   - VSCode 파일 탐색기에서 복제한 폴더를 열면, 좌측 소스 제어(🔃) 아이콘에 변경 내역이 표시됨
   - 커밋, 푸시, 브랜치 관리 등 모든 Git 기능을 VSCode에서 바로 사용 가능

4. **(선택) SSH 키로 GitHub 연동**
   - SSH 키를 GitHub에 등록하면 비밀번호 없이 푸시/풀 가능
   - SSH 주소로 복제:  
     ```bash
     git clone git@github.com:your-username/your-repo.git
     ```

---