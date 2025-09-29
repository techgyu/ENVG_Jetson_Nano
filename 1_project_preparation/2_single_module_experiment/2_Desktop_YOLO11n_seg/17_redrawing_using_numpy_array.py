
import numpy as np
import cv2
import os

# 경로 설정
contour_path = "1_project_preparation/2_single_module_experiment/1_Desktop_YOLO/data/real_time_yolo11n_seg_detection/16_yolo11n_seg_detection/contours_person.npy"
img_path = "1_project_preparation/2_single_module_experiment/1_Desktop_YOLO/data/real_time_yolo11n_seg_detection/15_capture_image_using_window/captured_image/bus.jpg"
save_dir = "1_project_preparation/2_single_module_experiment/1_Desktop_YOLO/data/real_time_yolo11n_seg_detection/17_redrawing_using_numpy"
os.makedirs(save_dir, exist_ok=True)

# 외곽선 좌표 불러오기
contours_list = np.load(contour_path, allow_pickle=True)

# 이미지 불러오기
img = cv2.imread(img_path)

# 외곽선 그리기 (주황색)
for contour in contours_list:
	if len(contour.shape) == 2:
		contour = contour.reshape(-1, 1, 2)
	cv2.drawContours(img, [contour], -1, (0, 140, 255), 2)

# 결과 이미지 저장
output_path = os.path.join(save_dir, "bus_with_contours.jpg")
cv2.imwrite(output_path, img)
print(f"Saved: {output_path}")
