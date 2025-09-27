
import os
import cv2
from concurrent.futures import ThreadPoolExecutor

# 입력 프레임 폴더 (예: "output/영상이름/frame_0001.jpg" ...)
input_dir = r"C:\github_personal\ENVG_Jetson_Nano\1_project_preparation\2_single_module_experiment\1_Desktop_YOLO\data\image\yolo_output"
# 저장할 영상 파일 경로
output_video = r"C:\github_personal\ENVG_Jetson_Nano\1_project_preparation\2_single_module_experiment\1_Desktop_YOLO\data\image\yolo_output_video.mp4"
# 프레임 간격(초) - 추출할 때 사용한 interval과 동일하게 맞춰야 함
interval = 1/24  # 예시: 2초마다 추출했다면 2

# 프레임 파일 리스트 정렬
frames = sorted([f for f in os.listdir(input_dir) if f.lower().endswith('.jpg')])

if not frames:
    print("프레임 이미지가 없습니다.")
    exit(1)

# 첫 프레임으로 영상 크기 결정
first_frame = cv2.imread(os.path.join(input_dir, frames[0]))
height, width, _ = first_frame.shape

# 영상 저장 객체 생성 (fps=1/interval)
fps = 1 / interval
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))


# 배치 크기 설정 (메모리 상황에 따라 16~64 사이로 조정)
BATCH_SIZE = 512

def read_frame(frame_name):
    frame_path = os.path.join(input_dir, frame_name)
    img = cv2.imread(frame_path)
    return img

total = len(frames)
for batch_start in range(0, total, BATCH_SIZE):
    batch_frames = frames[batch_start:batch_start+BATCH_SIZE]
    with ThreadPoolExecutor() as executor:
        imgs = list(executor.map(read_frame, batch_frames))
    for i, img in enumerate(imgs):
        idx = batch_start + i
        frame_name = batch_frames[i]
        if img is not None:
            out.write(img)
            print(f"[{idx+1}/{total}] 프레임 영상에 저장 완료: {frame_name}")
        else:
            print(f"[{idx+1}/{total}] 프레임 읽기 실패: {frame_name}")

out.release()
print(f"영상 저장 완료: {output_video}")