# 2025-09-14 | Jetson Nano Jetpack 업데이트 확인

---

# 1. jetson_release 또는 L4T 버전으로 JetPack 버전 확인하기
Jetson Nano에서 현재 설치된 JetPack 버전은 직접적으로 명령어 하나로 확인되는 건 아니고, 보통은 JetPack과 함께 깔리는 L4T(Linux for Tegra) 버전이나 jetson-release 패키지를 통해 확인합니다.

## 2. jetson_release 스크립트로 확인 (가장 간단)
jetson_release

→ JetPack, L4T, CUDA, cuDNN, TensorRT 버전을 한 번에 출력해줍니다.
만약 command not found가 뜨면 아래 방법으로 확인하세요.

## 3. L4T 버전으로 확인
```bash
head -n 1 /etc/nv_tegra_release
```
또는
```bash
cat /etc/nv_tegra_release
```
예시 출력:
# R32 (release), REVISION: 7.4, GCID: 29931747, BOARD: t210ref, EABI: aarch64, DATE: Tue Jun 15 21:13:56 UTC 2021.

## 4. JetPack ↔ L4T 매핑표 일부

- JetPack 4.6.6 → L4T R32.7.4
- JetPack 4.6.4 → L4T R32.7.3
- JetPack 4.5.1 → L4T R32.5.1
- JetPack 4.4 → L4T R32.4.3

---