# 2025-09-19 | Jetson Nano Git 설치

---

## 1. Jetson Nano에 Git 설치
```bash
sudo apt update
sudo apt install git
```
## 2. Git 설치 확인
```bash
git --version
```

**출력 결과:**
```bash
(jetson) user@ubuntu:~$ git --version
git version 2.17.1
```

## 3. Git 기본 설정
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**실제 입력 값**
```bash
(jetson) user@ubuntu:~$ git config --global user.name "jetson_nano"
(jetson) user@ubuntu:~$ git config --global user.email "rlarbxor85@gmail.com"
```

## 4. Git 설정 확인
```bash
git config --list
```

**출력 결과:**
```bash
user.name=jetson_nano
user.email=rlarbxor85@gmail.com
```

## 5. git clone 예시
```bash
git clone https://github.com/techgyu/ENVG_Jetson_Nano.git
```

## 6. 변경 사항 commit 방법
1. 변경 사항 확인
    ```bash
    git status
    ```

2. 변경 사항 스테이징
    ```bash
    git add .
    ```

3. 변경 사항 커밋
    ```bash
    git commit -m "Your commit message"
    ```

4. 원격 저장소에 푸시
    ```bash
    git push origin main
    ```

## 7. 원격 저장소 변경 사항 가져오기
```bash
git pull origin main
```

## 8. 만약 원격 저장소가 변경되었는데 로컬에서 이전 시점에 작업 사항이 있다면?

1. 작업 중인 변경 사항 임시 저장
```bash
git stash
```

2. 원격 저장소 변경 사항 가져오기
```bash
git pull origin main
```

3. 임시 저장한 변경 사항 다시 적용
```bash
git stash pop
```

4. 충돌 해결 후 커밋
```bash
git add .
git commit -m "로컬 변경사항 반영"
```

5. 원격 저장소에 푸시
```bash
git push origin main
```