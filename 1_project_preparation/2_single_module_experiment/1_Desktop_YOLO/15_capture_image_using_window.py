
import tkinter as tk
import pyautogui
import time
import threading
import os


def main():
	# 캡처 이미지 저장 폴더 지정
	save_dir = "1_project_preparation/2_single_module_experiment/1_Desktop_YOLO/data/real_time_yolo11n_seg_detection/15_capture_image_using_window"  # 원하는 경로로 변경 가능
	os.makedirs(save_dir, exist_ok=True)
	root = tk.Tk()
	root.title("Transparent Border Window")
	root.geometry("1200x800")
	root.resizable(False, False)  # 창 크기 고정 (조절 불가)

	# 완전 투명 배경 (윈도우에서만 동작)
	transparent_color = 'magenta'
	root.configure(bg=transparent_color)
	root.attributes('-transparentcolor', transparent_color)

	# 테두리만 Canvas로 그림 (내부는 완전 투명)
	border_width = 2
	canvas = tk.Canvas(root, highlightthickness=0, bg=transparent_color)
	canvas.place(x=0, y=0, relwidth=1, relheight=1)
	def draw_border(event=None):
		canvas.config(width=root.winfo_width(), height=root.winfo_height())
		canvas.delete("all")
		w = root.winfo_width()
		h = root.winfo_height()
		canvas.create_rectangle(
			border_width//2, border_width//2, w-border_width//2, h-border_width//2,
			outline="red", width=border_width
		)
	root.bind("<Configure>", draw_border)
	draw_border()

	# 캡처 주기(fps) 설정
	fps = 1  # 초당 1프레임
	interval = 1 / fps
	capturing = True

	def capture_loop():
		idx = 0
		while capturing:
			# 윈도우의 절대 위치와 크기 얻기
			root.update_idletasks()
			x = root.winfo_rootx() + border_width
			y = root.winfo_rooty() + border_width
			w = root.winfo_width() - 2*border_width
			h = root.winfo_height() - 2*border_width
			# 화면 캡처
			img = pyautogui.screenshot(region=(x, y, w, h))
			img.save(os.path.join(save_dir, f"capture_{idx:04d}.png"))
			idx += 1
			time.sleep(interval)

	# 캡처 스레드 시작
	t = threading.Thread(target=capture_loop, daemon=True)
	t.start()

	root.mainloop()

if __name__ == "__main__":
	main()
