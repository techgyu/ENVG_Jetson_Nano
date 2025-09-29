# 2. **객체 인식 및 외곽선 탐지**
# 	- 캡처된 이미지를 YOLO11n-seg 모델에 입력하여 객체 검출 및 마스크(외곽선) 추출
# 	- CPU 환경에서도 동작하도록 모델 경량화 및 추론 최적화
# 	- `6_test_yolo11n_seg_docker.py` 참고

import os
from ultralytics import YOLO
import torch
import torchvision.utils as vutils
import cv2
import numpy as np

# YOLO segmentation 모델 로드
model = YOLO("1_project_preparation/2_single_module_experiment/1_Desktop_YOLO/data/model/yolo11n-seg.pt")


# 1장만 예측
img_path = "1_project_preparation/2_single_module_experiment/1_Desktop_YOLO/data/real_time_yolo11n_seg_detection/15_capture_image_using_window/captured_image/bus.jpg"

# 외곽선 좌표 저장 폴더 지정
save_dir = "1_project_preparation/2_single_module_experiment/1_Desktop_YOLO/data/real_time_yolo11n_seg_detection/16_yolo11n_seg_detection"  # 원하는 경로로 변경 가능
os.makedirs(save_dir, exist_ok=True)

result = model(img_path, show_boxes=False)[0]

contours_list = []  # 모든 person 객체의 외곽선 좌표 저장
if result.masks is not None and result.names is not None:
    masks = result.masks.data.cpu().numpy()  # (객체수 x 높이 x 너비) 마스크 배열
    classes = result.boxes.cls.cpu().numpy().astype(int)  # 각 객체의 클래스 인덱스
    names = result.names  # 클래스 인덱스:이름 dict

    for idx, (mask, cls_idx) in enumerate(zip(masks, classes)):
        if names[cls_idx] == "person":
            mask = (mask > 0.5).astype(np.uint8) * 255  # 마스크 이진화
            # 원본 이미지 크기로 리사이즈
            img = cv2.imread(img_path)
            mask_resized = cv2.resize(mask, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST)
            # 외곽선 추출
            contours, _ = cv2.findContours(mask_resized, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            # contours: [array([[x1, y1], [x2, y2], ...], dtype=int32), ...]
            for c in contours:
                if len(c) > 0:
                    contours_list.append(c.squeeze(1))  # (N,2)로 저장

# numpy 배열로 저장 (다른 py에서 불러올 수 있음)
contour_save_path = os.path.join(save_dir, "contours_person.npy")
np.save(contour_save_path, np.array(contours_list, dtype=object), allow_pickle=True)
print(f"Saved contours: {len(contours_list)} objects -> {contour_save_path}")