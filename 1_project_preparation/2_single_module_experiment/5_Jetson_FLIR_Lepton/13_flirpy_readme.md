# -----------------------------
# 한글 요약/번역
# -----------------------------

## 소개
flirpy는 FLIR 열화상 카메라 및 이미지를 다루는 파이썬 라이브러리입니다. 연구나 논문 등에서 flirpy를 사용할 경우 Zenodo DOI로 인용해 주세요.

### 주요 기능
- 시리얼 통신을 통한 카메라 제어 및 질의
- 원시 이미지 캡처
- FLIR 파일 포맷(예: seq, fff)을 읽기 쉬운 이미지로 변환
- 원시 이미지를 방사선(radiometric) 이미지로 변환

### 테스트된 카메라
- FLIR Tau 2 (시리얼)
- TeAx ThermalCapture Grabber USB (이미지 캡처 및 Tau2 시리얼)
- FLIR Boson (시리얼 및 이미지 캡처)
- FLIR Duo Pro R (이미지 후처리)
- TeAx Fusion Zoom (이미지 후처리)
- FLIR Lepton (PureThermal 보드, 캡처+텔레메트리)

위 목록에 없고 SEQ 파일을 생성하지 않는 카메라는 지원하지 않을 수 있습니다. 많은 FLIR 카메라는 블루투스 등 독점 인터페이스를 사용하며, 공식 API가 없습니다.

### 곧 지원 예정
- FLIR Lepton 저수준(SPI) 지원

### 파이썬 3 권장
카메라 통신 관련 기능은 Python 2/3 모두 동작하도록 했으나, 파일 IO 등은 Python 2에서 일부 제한이 있습니다. Python 2는 사실상 지원 종료 상태이므로 Python 3 사용을 권장합니다.

## 라이브러리 구조
- flirpy.camera: FLIR 카메라 코어와 직접 통신하는 클래스
- flirpy.io: 열화상 이미지 포맷 처리 클래스
- flirpy.util: raw 변환 등 유틸리티 함수

## 유틸리티
split_seqs 스크립트로 FLIR SEQ 파일을 폴더별로 분할할 수 있습니다.

## 설치
가상환경(virtualenv, conda) 사용 권장. pip로 간단히 설치:
```
pip install flirpy
```
ARM(Raspberry Pi 등)에서도 동작하며, opencv-python-headless 등 의존성 필요. Exiftool도 별도 설치 필요할 수 있음.

## 이미지 캡처 예시
```python
from flirpy.camera.lepton import Lepton
camera = Lepton()
image = camera.grab()
camera.close()
```
with문 사용 가능. PureThermal Lepton 사용 시 텔레메트리 정보도 확인 가능.

## 기타
- Windows에서 드라이버 문제 발생 시, 장치 관리자에서 USB Video Device로 수동 변경 필요
- 테스트는 pytest로 가능, 일부 테스트는 실제 카메라 필요

---
이 문서는 flirpy 공식 README의 주요 내용을 한글로 요약/번역한 것입니다.
Introduction
flirpy is a Python library to interact with FLIR thermal imaging cameras and images. If you use flirpy for a research or other publishable application, please cite it using the Zenodo DOI.

It aims to be a one-stop-shop to:

Interact and query cameras via serial
Capture raw images
Convert FLIR file formats (e.g. seq, fff) to geotagged readable images
Convert raw images to radiometric images
The library has been tested with:

FLIR Tau 2 (serial)
TeAx ThermalCapture Grabber USB (image capture and Tau2 serial)
FLIR Boson (serial and image capture)
FLIR Duo Pro R (image post-processing)
TeAx Fusion Zoom (image post-processing)
FLIR Lepton (PureThermal board, capture+telemetry only)
If your camera is not on this list and it does not produce SEQ files, then flirpy probably does not support it. Many of FLIR's cameras use proprietary bluetooth interfaces for control and there are no APIs available.

Coming soon

FLIR Lepton low level (SPI)
Documentation...
It is strongly recommended that you use Python 3. I have tried to ensure that certain functions are portable between Python 2 and 3, mainly those involved with camera communication (for example if you want to use flirpy with ROS, most of the important stuff works). However, some file IO is hit and miss on Python 2 due to differences in regexes. Python 2 is effectively end of life and while I'd like to support both, it's a low priority. Submit a PR if you like!

Library organisation
The library is organised into logical sections:

flirpy.camera contains classes to communicate with FLIR camera cores directly
flirpy.io contains claseses to deal with thermal image formats
flirpy.util contains helper functions e.g. raw conversion
Utilities
Flirpy includes a convenience utility split_seqs for splitting FLIR sequence (SEQ) files.

Once installed, you can run:

python .\scripts\split_seqs -h
usage: split_seqs [-h] [-o OUTPUT] [-i INPUT] [-v VERBOSITY]
                  [--preview_format PREVIEW_FORMAT] [--rgb RGB]
                  [--jpeg_quality JPEG_QUALITY] [--use_gstreamer] [--copy]
                  [--width WIDTH] [--height HEIGHT]
                  [--merge_folders | --no_merge_folders]
                  [--split_filetypes | --no_split_filetypes]
                  [--export_meta | --no_export_meta]
                  [--export_tiff | --no_export_tiff]
                  [--export_raw | --no_export_raw]
                  [--export_preview | --no_export_preview]
                  [--skip_thermal | --no_skip_thermal]
                  [--sync_rgb | --no_sync_rgb]

Split all files in folder

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output folder (default: ./)
  -i INPUT, --input INPUT
                        Input file mask, e.g. "/path/*.SEQ" (default: *.SEQ)
  -v VERBOSITY, --verbosity VERBOSITY
                        Logging level (default: info)
  --preview_format PREVIEW_FORMAT
                        Output preview format (png, jpg, tiff) (default: jpg)
  --rgb RGB             If provided, split videos too e.g. "/path/*.MOV"
                        (default: )
  --jpeg_quality JPEG_QUALITY
                        RGB Output quality (0-100) (default: 80)
  --use_gstreamer       Use Gstreamer for video decoding (default: False)
  --copy                Copy first, instead of move after split (default:
                        False)
  --width WIDTH         Image width (if unspecified flirpy will attempt to
                        infer from FFF files) (default: None)
  --height HEIGHT       Image height (default: None)
  --merge_folders       Merge output folders (and remove intermediates
                        afterwards) (default: True)
  --no_merge_folders    Merge output folders (and remove intermediates
                        afterwards) (default: True)
  --split_filetypes     Split output files by type (make
                        raw/preview/radiometric folders) (default: True)
  --no_split_filetypes  Split output files by type (make
                        raw/preview/radiometric folders) (default: True)
  --export_meta         Export meta information files (also for geotagging)
                        (default: True)
  --no_export_meta      Export meta information files (also for geotagging)
                        (default: True)
  --export_tiff         Export radiometric tiff files (default: True)
  --no_export_tiff      Export radiometric tiff files (default: True)
  --export_raw          Leave raw files (by default copy meta to radiometric)
                        (default: False)
  --no_export_raw       Leave raw files (by default copy meta to radiometric)
                        (default: False)
  --export_preview      Export 8-bit preview png files (default: True)
  --no_export_preview   Export 8-bit preview png files (default: True)
  --skip_thermal        Skip thermal processing (default: False)
  --no_skip_thermal     Skip thermal processing (default: False)
  --sync_rgb            Attempt to synchronise RGB/IR streams (default: False)
  --no_sync_rgb         Attempt to synchronise RGB/IR streams (default: False)
Flirpy includes an experimental FFF interpreter that attempts to load metadata and other information directly from the file headers. If you have trouble splitting your SEQ files, then specify the width and height parameters in this script and it will fall back to using Exiftool.

split_seqs accepts either a directory, a specific filename, or a wildcard string (e.g. "./my/data/flight_*.SEQ"). If you use wildcards, be sure to enclose the argument in quotes, otherwise your shell will expand the wildcard before running the program and confuse it. If you specify a directoy, all SEQ files in that diretory will be used.

Files will be extracted to folders with the same base name as the SEQ file, for example 20180101_1030.SEQ will be extracted to 20180101_1030, etc. By default the splitter will three kinds of files, separated by subfolder.

Raw (FFF) files with metadata text files
Radiometric 16-bit tiff images
Preview 8-bit RGB representations of the radiometric data
By default, the raw folder will be deleted and all the metadata files will be copied to the radiometric folder. This is mostly to save disk space as it's unlikely you need the raw files hanging around. If you do need raw counts for some reason, you can use the --no_export_radiometric flag.

The tiff images will be geotagged if GPS information is present in the raw data.

Output images are numbered sequentially. If SEQ file 1 contains 1800 frames, the first frame from SEQ file 2 will be numbered 1800.

RGB extraction options are experimental. Generally it's difficult to sync the two streams because they do not start simultaneously and when the IR camera flat fields, it can cause odd discontinuities in the data. If you are familiar with multi-modal video synchronisation, we'd love to hear from you!

Installation
Flirpy has been tested with Python 3 and may work on Python 2. It is always recommended that you install packages inside a virtualenv or Conda environment.

Simply install using pip:

pip install flirpy
Or you can clone the repository and run:

pip install .
Or:

python setup.py install
Using pip is preferable, as it will let you uninstall the package if you need.

flirpy is distributed with a copy of Exiftool which is used to extract metadata from certain file formats.

For a fast local pip install, e.g. from the repository:

python setup.py bdist_wheel
pip install flirpy --no-index --find-links ./dist
This will disable pip looking up stuff online and tell it to look in the dist folder for wheels. This is a useful command for testing!

Installation on ARM (e.g. Raspberry Pi)
Flirpy mostly works well, and has been tested, on the Raspberry Pi. If you're building from scratch, you need to install a few things manually. Try to use Python 3 if you can.

It's recommended that you first install the Python dependencies using pip in combination with piwheels. For whatever reason, setuptools does not find these files, so it will fail if e.g. OpenCV isn't installed already. Once you've set up piwheels (it should be automatic on Raspbian if you've installed pip3) run:

pip3 install -r requirements.txt
You may need to install some dependencies for OpenCV, for example libjasper-dev.

You should also install Exiftool manually with sudo apt install exiftool.

Nowadays opencv-python-headless should exist on most ARM platforms, including aarch64.

Grab images
Here's a very simple example of grabbing an image using a Boson or Lepton:

from flirpy.camera.lepton import Lepton

camera = Lepton()
image = camera.grab()
camera.close()
If you're using a PureThermal Lepton you can also check frame telemetry if enabled:

camera.major_version
camera.minor_version
camera.uptime_ms
camera.status # see datasheet
camera.revision
camera.frame_count
camera.frame_mean # too low?
camera.fpa_temp_k
camera.ffc_temp_k
camera.ffc_elapsed_ms
camera.agc_roi
camera.clip_high
camera.clip_low
camera.video_format
Flirpy automatically locates your camera and captures a 16-bit (raw) image:

from flirpy.camera.boson import Boson

camera = Boson()
image = camera.grab()
camera.close()
If you have a Tau with TeAx's USB grabbing back, then you can grab radiometric images directly:

from flirpy.camera.tau import TeaxGrabber

camera = TeaxGrabber()
image = camera.grab()
camera.close()
These radiometric images are returned as 64-bit Numpy arrays in units of Celsius. This assumes a conversion factor of 0.04 K per count.

Conveniently, TeaxGrabber subclasses the Tau driver so you also have access to all the internal information from the camera, for example:

camera = TeaxGrabber()
camera.get_fpa_temperature()
Cameras support the Python with interface to ensure that interfaces are properly closed when the resource is no longer needed (swap in Lepton or TeaxGraber):

import cv2
from flirpy.camera.boson import Boson

with Boson() as camera:
    while True:
        img = camera.grab().astype(np.float32)

        # Rescale to 8 bit
        img = 255*(img - img.min())/(img.max()-img.min())
        
        # Apply colourmap - try COLORMAP_JET if INFERNO doesn't work.
        # You can also try PLASMA or MAGMA
        img_col = cv2.applyColorMap(img.astype(np.uint8), cv2.COLORMAP_INFERNO)

        cv2.imshow('Boson', img_col)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
        
cv2.destroyAllWindows()
Driver problems on Windows
Occasionally Windows can do some bizarre things and forget that USB devices are cameras. This will stop the camera from being discoverable by flirpy (and usable by software including OpenCV).

You can solve this by going to device manager, right clicking on the USB device and selecting "Update Driver". Choose "Browse my computer ... " and then "Let me pick ... ". Choose the "USB Video Device" driver.

Tests
To run the test suite:

pip install pytest pytest-cov
python -m pytest --cov=flirpy
Some tests are hardware dependent, e.g. for cameras, so expect them to fail unless you own and have a camera to try them with. Hardware tests are skipped by default if the requisite camera is not plugged in.

The repository includes some small representative examples of image files (e.g. SEQ). It is tested and is routinely used with flight data from FLIR Duo cameras, so larger files aren't a problem, but they're too large to include in the repository.

If you're testing on Python 2:

pip install pytest pytest-cov backports.tempfile
pytest --cov=flirpy test
