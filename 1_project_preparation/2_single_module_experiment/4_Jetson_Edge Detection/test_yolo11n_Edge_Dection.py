import cv2
import numpy as np
from ultralytics import YOLO

if not hasattr(np, 'bool'):
    np.bool = bool

# 1. 모델 로드
model = YOLO("./data/model/yolo11n.pt")

# 2. 이미지 경로 변수로 지정
img_path = "./data/image/bus.jpg"

# 3. 이미지 추론
results = model(img_path)

# 4. 원본 이미지 읽기
img = cv2.imread(img_path)

for r in results[0].boxes.xyxy.cpu().numpy():
    x1, y1, x2, y2 = map(int, r[:4])
    roi = img[y1:y2, x1:x2]

    # 5. 외곽선 추출
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 6. 원본에 그리기
    cv2.drawContours(img[y1:y2, x1:x2], contours, -1, (0,140,255), 1)

cv2.imwrite("./data/image/bus_with_contours.jpg", img)