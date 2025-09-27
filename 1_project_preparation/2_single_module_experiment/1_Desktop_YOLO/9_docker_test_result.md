# 2025-09-27 | Laptop Docker 환경 기존 코드 작동 확인 결과

---

## 1. 기존 아나콘다 환경에서 돌렸던 코드 정상 작동 확인
6_test_yolo11n_segmentation.py -> 경로 수정 후 정상 작동
7_test_yolo11n_segmentation_in_video.py -> 경로 수정 후 정상 작동
8_intergrate_frame_to_video.py -> Killed 발생


## 2. 8_intergrate_frame_to_video.py Killed 문제
### 1. docker 컨테이너 CPU, 메모리 할당 확인