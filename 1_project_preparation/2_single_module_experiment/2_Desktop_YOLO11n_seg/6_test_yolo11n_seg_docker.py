from ultralytics import YOLO
import torch
import torchvision.utils as vutils
import cv2
import numpy as np

# YOLO segmentation 모델 로드
model = YOLO("1_project_preparation/2_single_module_experiment/1_Desktop_YOLO/data/model/yolo11n-seg.pt")

# 이미지에 대해 예측 수행 (바운딩 박스 비활성화)
results = model("1_project_preparation/2_single_module_experiment/1_Desktop_YOLO/data/6_test_yolo11n_segmentation_docker",
    show_boxes=False
)

# 결과 순회하며 외곽선 그리기
for i, result in enumerate(results):
    if result.masks is not None and result.names is not None:
        # 원본 이미지 불러오기
        img = cv2.imread("1_project_preparation/2_single_module_experiment/1_Desktop_YOLO/data/6_test_yolo11n_segmentation_docker/bus.jpg")
        masks = result.masks.data.cpu().numpy()  # (객체수 x 높이 x 너비) 마스크 배열
        classes = result.boxes.cls.cpu().numpy().astype(int)  # 각 객체의 클래스 인덱스
        names = result.names  # 클래스 인덱스:이름 dict

        for idx, (mask, cls_idx) in enumerate(zip(masks, classes)):
            if names[cls_idx] == "person":
                mask = (mask > 0.5).astype(np.uint8) * 255  # 마스크 이진화

                # 마스크를 원본 이미지 크기로 리사이즈
                mask_resized = cv2.resize(mask, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST)

                # 외곽선 추출
                contours, _ = cv2.findContours(mask_resized, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                # 주황색(BGR) 외곽선 그리기
                cv2.drawContours(img, contours, -1, (0, 140, 255), 2)
    # 결과 이미지 저장 (원본 이미지와 같은 폴더에 저장)
    import os
    img_path = result.path if hasattr(result, 'path') else ""
    output_dir = os.path.dirname(img_path)
    output_path = os.path.join(output_dir, f"output_contour_person_{i}.jpg")
    cv2.imwrite(output_path, img)
    print(f"Saved {output_path}")