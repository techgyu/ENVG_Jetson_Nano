# flirpy를 이용한 FLIR Lepton 3.5 SPI 연결 예제 (Jetson Nano)
#
# 참고사항:
# - Jetson Nano Expansion Header Tool에서 SPI2 활성화 필요 (핀맵: SCK=13, MOSI=37, MISO=22, CS0=18)
# - Breakout Board와의 연결은 문서 상단 표 참고
# - I2C는 보통 제어용, SPI는 영상 데이터용
# - SPI 디바이스 경로는 ls /dev/spidev* 로 확인 가능
# - 실행 전 pip install flirpy opencv-python-headless 필요

from flirpy.camera.lepton import Lepton
import cv2
import numpy as np

# Lepton SPI 디바이스 경로 (Jetson Nano의 SPI2는 일반적으로 /dev/spidev1.0)
# 실제 연결에 따라 /dev/spidev0.0, /dev/spidev1.0 등으로 다를 수 있음
# 본 예제에서는 SPI_2_CS0 (J41 18번) 사용 시 /dev/spidev1.0이 일반적
SPI_DEVICE = "/dev/spidev1.0"

# Lepton 카메라 열기
with Lepton(SPI_DEVICE) as cam:
  print("FLIR Lepton 연결 성공!")
  for i in range(10):
    frame, _ = cam.capture()
    # 16비트 데이터를 8비트로 정규화
    img = np.uint8(255 * (frame - frame.min()) / (frame.ptp() + 1e-6))
    img_color = cv2.applyColorMap(img, cv2.COLORMAP_JET)
    out_path = f"lepton_capture_{i:02d}.png"
    cv2.imwrite(out_path, img_color)
    print(f"Saved: {out_path}")
  print("이미지 저장 완료. (lepton_capture_XX.png)")