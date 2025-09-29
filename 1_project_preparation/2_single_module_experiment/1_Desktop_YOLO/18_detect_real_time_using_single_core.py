from PIL import Image, ImageTk
import tkinter as tk
import pyautogui
import time
import threading
import os
import numpy as np
from ultralytics import YOLO
import torch
import torchvision.utils as vutils
import cv2

def update_window(root, canvas, border_width):  # 윈도우와 테두리를 주기적으로 갱신하는 함수
    canvas.config(width=root.winfo_width(), height=root.winfo_height())  # Canvas 크기 갱신
    # 테두리만 삭제하고 다시 그림 (contour는 삭제하지 않음)
    canvas.delete("border")
    w = root.winfo_width()  # 현재 윈도우 너비
    h = root.winfo_height()  # 현재 윈도우 높이
    canvas.create_rectangle(
        border_width//2, border_width//2, w-border_width//2, h-border_width//2,  # 테두리 좌표
        outline="red", width=border_width, tag="border"  # 빨간색 테두리 그리기
    )
    root.after(30, update_window, root, canvas, border_width)  # 30ms마다 반복 호출

def capture_window_region(save_dir, x, y, w, h, filename="capture_0000.png"):
    """
    지정한 영역을 한 번 캡처하여 저장합니다.

    save_dir: 저장 폴더 경로
    x, y, w, h: 캡처할 영역의 좌표와 크기
    """
    os.makedirs(save_dir, exist_ok=True)
    img = pyautogui.screenshot(region=(x, y, w, h))
    img.save(os.path.join(save_dir, filename))


def detect_person_contours(
    model_path,
    img_path,
    save_dir,
    save_name="contours_person.npy"
):
    """
    YOLO segmentation 모델로 'person' 객체의 외곽선 좌표를 추출하여 저장합니다.

    model_path: YOLO 세그멘테이션 모델 경로
    img_path: 예측할 이미지 경로
    save_dir: 외곽선 좌표 저장 폴더
    save_name: 저장 파일명 (기본값: contours_person.npy)
    """
    model = YOLO(model_path)
    os.makedirs(save_dir, exist_ok=True)
    result = model(img_path, show_boxes=False)[0]

    contours_list = []
    if result.masks is not None and result.names is not None:
        masks = result.masks.data.cpu().numpy()
        classes = result.boxes.cls.cpu().numpy().astype(int)
        names = result.names

        for idx, (mask, cls_idx) in enumerate(zip(masks, classes)):
            if names[cls_idx] == "person":
                mask = (mask > 0.5).astype(np.uint8) * 255
                img = cv2.imread(img_path)
                mask_resized = cv2.resize(mask, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST)
                contours, _ = cv2.findContours(mask_resized, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                for c in contours:
                    if len(c) > 0:
                        print("contour min y (detect):", c[:,0,1].min(), "max y:", c[:,0,1].max())
                        contours_list.append(c.squeeze(1))

    contour_save_path = os.path.join(save_dir, save_name)
    np.save(contour_save_path, np.array(contours_list, dtype=object), allow_pickle=True)
    print(f"Saved contours: {len(contours_list)} objects -> {contour_save_path}")


def draw_contours_on_window(canvas, npy_path, canvas_w, canvas_h, tk_img_holder, offset_x=0, offset_y=0):
    """
    투명 배경 위에 외곽선만 OpenCV로 그려 tkinter Canvas에 PhotoImage로 띄움

    canvas: tkinter Canvas 객체
    npy_path: 외곽선 좌표가 저장된 .npy 파일 경로
    canvas_w, canvas_h: 캔버스 크기 (윈도우 크기)
    tk_img_holder: tkinter PhotoImage 객체를 참조로 유지할 리스트(메모리 해제 방지)
    offset_x, offset_y: 좌표 보정값 (윈도우 위치 등)
    """
    if not os.path.exists(npy_path):
        print(f"Contour file not found: {npy_path}")
        return
    contours = np.load(npy_path, allow_pickle=True)
    # 투명 배경(RGBA)
    img = np.zeros((canvas_h, canvas_w, 4), dtype=np.uint8)
    for contour in contours:
        if len(contour.shape) == 2:
            contour = contour.reshape(-1, 1, 2)
        # 좌표 보정
        contour = contour + np.array([[offset_x, offset_y]])
        cv2.drawContours(img, [contour], -1, (0, 255, 0, 255), 2)  # 초록색, 불투명
    pil_img = Image.fromarray(img, mode="RGBA")
    tk_img = ImageTk.PhotoImage(pil_img)
    tk_img_holder.clear()
    tk_img_holder.append(tk_img)  # 참조 유지
    canvas.delete("img")
    canvas.create_image(0, 0, anchor='nw', image=tk_img, tag="img")

def main():  # 메인 함수 정의
    root = tk.Tk()  # Tkinter 루트 윈도우 생성
    root.title("Transparent Border Window")  # 윈도우 제목 설정
    root.geometry("1200x800")  # 윈도우 크기 설정
    root.resizable(False, False)  # 창 크기 고정 (조절 불가)

    # 완전 투명 배경 (윈도우에서만 동작)
    transparent_color = 'magenta'  # 투명색으로 사용할 색상 지정
    root.configure(bg=transparent_color)  # 배경색을 투명색으로 설정
    root.attributes('-transparentcolor', transparent_color)  # 해당 색상을 투명하게 만듦

    # 테두리만 Canvas로 그림 (내부는 완전 투명)
    border_width = 2  # 테두리 두께 설정
    canvas = tk.Canvas(root, highlightthickness=0, bg=transparent_color)  # 투명 배경의 Canvas 생성
    canvas.place(x=0, y=0, relwidth=1, relheight=1)  # Canvas를 윈도우 전체에 배치

    root.bind("<Configure>", lambda event: update_window(root, canvas, border_width))  # 윈도우 크기 변경 시 테두리 다시 그림
    update_window(root, canvas, border_width)  # 최초 1회 및 주기적 테두리 그림

    # 캡처 스레드 시작



    def start_capture_thread():
        interval_sec = 1  # 캡처 간격(초)
        tk_img_holder = []  # tkinter PhotoImage 참조 유지용


        def capture_detect_and_draw_loop():
            i = 0
            while True:
                # 윈도우 위치와 크기 얻기 (매번 최신값)
                root.update_idletasks()
                x = root.winfo_rootx() + border_width
                y = root.winfo_rooty() + border_width
                w = root.winfo_width() - 2*border_width
                h = root.winfo_height() - 2*border_width
                save_dir = "1_project_preparation/2_single_module_experiment/1_Desktop_YOLO/data/real_time_yolo11n_seg_detection/15_capture_image_using_window"
                img_path = os.path.join(save_dir, f"capture_{i:04d}.png")

                # 캡처 직전 외곽선(이미지) 삭제 (메인 스레드에서 실행)
                def clear_contour_img():
                    canvas.delete("img")
                root.after(0, clear_contour_img)

                # 캡처
                filename = f"capture_{i:04d}.png"
                capture_window_region(save_dir, x, y, w, h, filename=filename)

                # 캡처 직후 기존 외곽선 다시 그리기 (최신 npy가 있으면)
                if i > 0:
                    prev_npy_path = os.path.join(
                        "1_project_preparation/2_single_module_experiment/1_Desktop_YOLO/data/real_time_yolo11n_seg_detection/16_yolo11n_seg_detection",
                        f"contours_person_{i-1:04d}.npy"
                    )
                    def redraw_prev_contour():
                        canvas.delete("img")
                        draw_contours_on_window(canvas, prev_npy_path, w, h, tk_img_holder, offset_x=0, offset_y=0)
                    root.after(0, redraw_prev_contour)

                # 외곽선 추출
                model_path = "1_project_preparation/2_single_module_experiment/1_Desktop_YOLO/data/model/yolo11n-seg.pt"
                contour_save_dir = "1_project_preparation/2_single_module_experiment/1_Desktop_YOLO/data/real_time_yolo11n_seg_detection/16_yolo11n_seg_detection"
                # 저장 파일명도 구분
                save_name = f"contours_person_{i:04d}.npy"
                detect_person_contours(model_path, img_path, contour_save_dir, save_name=save_name)

                # 외곽선 갱신 직전 외곽선(이미지) 삭제 후, 새로운 외곽선으로 갱신 (메인 스레드에서 실행)
                npy_path = os.path.join(contour_save_dir, save_name)
                def draw_on_canvas():
                    canvas.delete("img")  # 외곽선 이미지 삭제
                    print("Drawing contours on transparent canvas...")
                    draw_contours_on_window(canvas, npy_path, w, h, tk_img_holder, offset_x=0, offset_y=0)
                root.after(0, draw_on_canvas)

                i += 1
                time.sleep(interval_sec)

        t = threading.Thread(target=capture_detect_and_draw_loop, daemon=True)
        t.start()

    root.after(500, start_capture_thread)  # 0.5초 후 캡처 스레드 시작

    root.mainloop()  # 이벤트 루프 시작

if __name__ == "__main__":  # 메인 함수 실행 조건
    main()  # 메인 함수 호출
