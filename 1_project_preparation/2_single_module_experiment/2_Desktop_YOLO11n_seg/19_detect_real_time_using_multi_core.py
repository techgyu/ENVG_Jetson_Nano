from PIL import Image, ImageTk
import tkinter as tk
import pyautogui
import time
import multiprocessing
import os
import numpy as np
from ultralytics import YOLO
import cv2
import queue
import mss

# 멀티프로세스용 파이프라인 함수
def pipeline_process(gui_info, result_queue, interval_sec=1/60):
    """
    별도 프로세스에서 캡처+YOLO+외곽선 추출을 반복 실행
    gui_info: multiprocessing.Manager().dict() - GUI 정보 공유
    result_queue: multiprocessing.Queue() - 결과 전달용
    """
    import time
    import os
    import numpy as np
    import cv2
    from ultralytics import YOLO
    import pyautogui
    
    # 프로세스 내부에서 사용할 함수들
    def capture_window_region_mp(x, y, w, h):
        with mss.mss() as sct:
            monitor = {"top": int(y), "left": int(x), "width": int(w), "height": int(h)}
            sct_img = sct.grab(monitor)
            img = Image.frombytes("RGB", sct_img.size, sct_img.rgb)
            img_np = np.array(img)
        return img_np

    def detect_person_contours_mp(model, img_np):
        t_yolo0 = time.time()
        result = model(img_np, show_boxes=False)[0]
        t_yolo1 = time.time()
        contours_list = []
        t_contour0 = time.time()
        if result.masks is not None and result.names is not None:
            masks = result.masks.data.cpu().numpy()
            classes = result.boxes.cls.cpu().numpy().astype(int)
            names = result.names
            for idx, (mask, cls_idx) in enumerate(zip(masks, classes)):
                if names[cls_idx] == "person":
                    mask = (mask > 0.5).astype(np.uint8) * 255
                    mask_resized = cv2.resize(mask, (img_np.shape[1], img_np.shape[0]), interpolation=cv2.INTER_NEAREST)
                    contours, _ = cv2.findContours(mask_resized, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    for c in contours:
                        if len(c) > 0:
                            contours_list.append(c.squeeze(1))
        t_contour1 = time.time()
        return contours_list, (t_yolo1-t_yolo0), (t_contour1-t_contour0)
    
    # 메인 파이프라인 루프
    model_path = "1_project_preparation/2_single_module_experiment/1_Desktop_YOLO/data/model/yolo11n-seg.pt"
    model = YOLO(model_path)
    i = 0
    while True:
        try:
            t0 = time.time()
            # GUI 정보 가져오기
            x = gui_info['x']
            y = gui_info['y']
            w = gui_info['w']
            h = gui_info['h']
            t1 = time.time()
            # 캡처
            img_np = capture_window_region_mp(x, y, w, h)
            t2 = time.time()
            # YOLO 추론 및 외곽선 추출 (시간 분리)
            contours, yolo_time, contour_time = detect_person_contours_mp(model, img_np)
            t3 = time.time()
            # 결과를 메인 프로세스로 전달
            result_queue.put((contours, w, h, i))
            t4 = time.time()
            print(f"[Process] Frame {i} | GUI: {(t1-t0)*1000:.1f}ms | Capture: {(t2-t1)*1000:.1f}ms | YOLO: {yolo_time*1000:.1f}ms | Contour: {contour_time*1000:.1f}ms | Queue: {(t4-t3)*1000:.1f}ms | Total: {(t4-t0)*1000:.1f}ms")
            i += 1
            time.sleep(interval_sec)
        except Exception as e:
            print(f"[Process] Error: {e}")
            time.sleep(1)

def update_window(root, canvas, border_width):
    """윈도우와 테두리를 주기적으로 갱신하는 함수"""
    canvas.config(width=root.winfo_width(), height=root.winfo_height())
    canvas.delete("border")
    w = root.winfo_width()
    h = root.winfo_height()
    canvas.create_rectangle(
        border_width//2, border_width//2, w-border_width//2, h-border_width//2,
        outline="red", width=border_width, tag="border"
    )
    root.after(30, update_window, root, canvas, border_width)

def draw_contours_on_window(canvas, contours, canvas_w, canvas_h, tk_img_holder, offset_x=0, offset_y=0):
    img = np.zeros((canvas_h, canvas_w, 4), dtype=np.uint8)
    for contour in contours:
        contour = np.array(contour, dtype=np.int32)
        if len(contour.shape) == 2:
            contour = contour.reshape(-1, 1, 2)
        contour = contour + np.array([[offset_x, offset_y]])
        cv2.drawContours(img, [contour], -1, (0, 120, 255, 255), 2)
    img_rgba = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
    pil_img = Image.fromarray(img_rgba, mode="RGBA")
    tk_img = ImageTk.PhotoImage(pil_img)
    tk_img_holder.clear()
    tk_img_holder.append(tk_img)
    canvas.delete("img")
    canvas.create_image(0, 0, anchor='nw', image=tk_img, tag="img")

def main():
    # 멀티프로세스 시작 방법 설정 (Windows 호환성)
    multiprocessing.set_start_method('spawn', force=True)
    
    # tkinter GUI 설정
    root = tk.Tk()
    root.title("Transparent Border Window - MultiProcess")
    root.geometry("1200x800")
    root.resizable(False, False)
    
    # 완전 투명 배경
    transparent_color = 'magenta'
    root.configure(bg=transparent_color)
    root.attributes('-transparentcolor', transparent_color)
    
    # 테두리 Canvas
    border_width = 2
    canvas = tk.Canvas(root, highlightthickness=0, bg=transparent_color)
    canvas.place(x=0, y=0, relwidth=1, relheight=1)
    
    root.bind("<Configure>", lambda event: update_window(root, canvas, border_width))
    update_window(root, canvas, border_width)
    
    # 프로세스 간 통신 설정
    manager = multiprocessing.Manager()
    gui_info = manager.dict()
    result_queue = multiprocessing.Queue()
    tk_img_holder = []
    
    # GUI 정보 초기화
    def update_gui_info():
        gui_info['x'] = root.winfo_rootx() + border_width
        gui_info['y'] = root.winfo_rooty() + border_width
        gui_info['w'] = root.winfo_width() - 2*border_width
        gui_info['h'] = root.winfo_height() - 2*border_width
        root.after(100, update_gui_info)  # 100ms마다 GUI 정보 갱신
    
    # 초기 GUI 정보 설정
    root.update_idletasks()
    gui_info['x'] = root.winfo_rootx() + border_width
    gui_info['y'] = root.winfo_rooty() + border_width
    gui_info['w'] = root.winfo_width() - 2*border_width
    gui_info['h'] = root.winfo_height() - 2*border_width
    
    # GUI 정보 갱신 시작
    update_gui_info()
    
    # 멀티프로세스 파이프라인 시작
    def start_pipeline():
        p = multiprocessing.Process(
            target=pipeline_process, 
            args=(gui_info, result_queue, 1/10),  # 1/10초 간격
            daemon=True
        )
        p.start()
        print("[Main] Pipeline process started")
        return p
    
    # 결과 큐를 폴링하여 GUI에 반영
    def poll_result_queue():
        try:
            while True:
                contours, w, h, frame_idx = result_queue.get_nowait()
                print(f"[Main] Received result for frame {frame_idx}")
                canvas.delete("img")
                draw_contours_on_window(canvas, contours, w, h, tk_img_holder, offset_x=0, offset_y=0)
        except queue.Empty:
            pass
        except Exception as e:
            print(f"[Main] Error processing result: {e}")
        root.after(50, poll_result_queue)
    
    # 0.5초 후 파이프라인 시작
    def delayed_start():
        pipeline_process_obj = start_pipeline()
        poll_result_queue()
    
    root.after(1, delayed_start)
    
    # GUI 이벤트 루프 시작
    print("[Main] Starting GUI main loop")
    root.mainloop()

if __name__ == "__main__":
    main()