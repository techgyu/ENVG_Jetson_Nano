import tkinter as tk
# apt update
# apt install -y python3-tk
def main():
	root = tk.Tk()
	root.title("Resizable Window Example")
	root.geometry("400x300")  # 초기 크기
	root.minsize(200, 150)     # 최소 크기
	root.maxsize(1000, 800)    # 최대 크기
	root.resizable(True, True) # 상하좌우 모두 조절 가능

	label = tk.Label(root, text="이 창은 상하좌우로 크기 조절이 가능합니다.", font=("Arial", 14))
	label.pack(expand=True)

	root.mainloop()

if __name__ == "__main__":
	main()
