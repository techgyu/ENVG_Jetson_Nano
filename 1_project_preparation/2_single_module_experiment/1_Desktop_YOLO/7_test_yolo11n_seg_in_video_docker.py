import os
from ultralytics import YOLO
import torch
import torchvision.utils as vutils
import cv2
import numpy as np

# YOLO segmentation 모델 로드
model = YOLO("1_project_preparation/2_single_module_experiment/1_Desktop_YOLO/data/model/yolo11n-seg.pt")

# 입력 이미지 폴더 경로
img_dir = "1_project_preparation/2_single_module_experiment/1_Desktop_YOLO/data/7_test_yolo11n_seg_in_video_docker/input"
# 결과 저장 폴더 경로
out_dir = "1_project_preparation/2_single_module_experiment/1_Desktop_YOLO/data/7_test_yolo11n_seg_in_video_docker/yolo_output"

os.makedirs(out_dir, exist_ok=True)

# 폴더 내 모든 jpg 파일 처리
for img_name in os.listdir(img_dir):
    if img_name.lower().endswith('.jpg'):
        img_path = os.path.join(img_dir, img_name)
        results = model(img_path, show_boxes=False)
        for i, result in enumerate(results):
            if result.masks is not None and result.names is not None:
                img = cv2.imread(img_path)
                masks = result.masks.data.cpu().numpy()
                classes = result.boxes.cls.cpu().numpy().astype(int)
                names = result.names
                for idx, (mask, cls_idx) in enumerate(zip(masks, classes)):
                    if names[cls_idx] == "person":
                        mask = (mask > 0.5).astype(np.uint8) * 255

                        # 마스크를 원본 이미지 크기로 리사이즈
                        mask_resized = cv2.resize(mask, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST)

                        # 블러 또는 모폴로지 연산으로 외곽선 부드럽게
                        mask_blur = cv2.GaussianBlur(mask_resized, (5, 5), 0)
                        # 또는 (둘 중 하나만 사용)
                        # kernel = np.ones((5, 5), np.uint8)
                        # mask_blur = cv2.morphologyEx(mask_resized, cv2.MORPH_CLOSE, kernel)

                        contours, _ = cv2.findContours(mask_blur, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                        cv2.drawContours(img, contours, -1, (0, 140, 255), 7)
                # 결과 이미지 저장 (yolo_output 폴더에 저장)
                out_path = os.path.join(out_dir, f"{os.path.splitext(img_name)[0]}_contour.jpg")
                cv2.imwrite(out_path, img)