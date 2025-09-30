# -----------------------------
# 한글 요약/번역
# -----------------------------

## pylepton (이 소프트웨어는 더 이상 동작하지 않음)
Lepton을 SPI로(예: 라즈베리파이에서) 이미지를 캡처하는 간단한 파이썬 라이브러리입니다.

### 필요 모듈
- cv2, numpy
- Debian 계열에서는 다음으로 설치:
  $ sudo apt-get install python-opencv python-numpy

### 설치 방법
- 작업 디렉터리에서 예제 실행 가능
- site-packages에 설치하려면:
  $ sudo python setup.py install

### 예제 코드
```python
import numpy as np
import cv2
from pylepton import Lepton

with Lepton() as l:
  a,_ = l.capture()
cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX) # 대비 확장
np.right_shift(a, 8, a) # 8비트로 변환
cv2.imwrite("output.jpg", np.uint8(a)) # 이미지 저장
```
- capture()의 결과는 12비트, 정규화되지 않은 원본 데이터
- 프레임 ID도 함께 반환됨(고유 프레임만 약 9Hz)
- Lepton 생성자에 SPI 디바이스 경로를 인자로 줄 수 있음

### 예제 프로그램
- pylepton_overlay: 라즈베리파이, picamera 필요, 오버레이 투명도 등 옵션 지원
- pylepton_capture: opencv가 지원하는 포맷으로 저장 가능

### 중요 안내
- GroupGets는 코드/펌웨어/소프트웨어 지원을 제공하지 않음
- 저장소는 예시 또는 시작점일 뿐, 동작 보장 없음
- 소프트웨어, 펌웨어, 코드 호환성 문제로 인한 반품/교환 불가
- 소프트웨어는 "있는 그대로(AS IS)" 제공, 어떠한 보증도 없음
pylepton (this software no longer works)
Quick and dirty pure python library for capturing images from the Lepton over SPI (for example, on a Raspberry PI).

Requires cv2 and numpy modules, if you don't have them already. On a Debian-based system you can probably do this:

$ sudo apt-get install python-opencv python-numpy
You can run the examples in the working directory, but a distutils setup is included to install into site-packages for distribution:

$ sudo python setup.py install
Example usage
import numpy as np
import cv2
from pylepton import Lepton

with Lepton() as l:
  a,_ = l.capture()
cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX) # extend contrast
np.right_shift(a, 8, a) # fit data into 8 bits
cv2.imwrite("output.jpg", np.uint8(a)) # write it!
Image data from capture() is 12-bit, non-normalized (raw sensor data). Here we contrast extend it since the bandwidth tends to be narrow.

capture() returns a tuple that includes a unique frame ID, as lepton frames can update at ~27 Hz, but only unique ones are returned at ~9 Hz. Currently, this is just a simple sum, but ideally this will turn into a real frame ID from telemetry once this feature is implemented.

Note also that the Lepton contructor can take as an optional argument the SPI device on which to find the Lepton. If in your system that device is /dev/spidev0.1, you can instantiate lepton as such:

...
with Lepton("/dev/spidev0.1") as l:
  ...
Example programs
pylepton_overlay
Requires python-picamera, a Raspberry PI, and compatible camera such as http://www.adafruit.com/products/1367

$ sudo apt-get install python-picamera

$ pylepton_overlay --help
Usage: pylepton_overlay [options]

Options:
  -h, --help            show this help message and exit
  -f, --flip-vertical   flip the output images vertically
  -a ALPHA, --alpha=ALPHA
                        set lepton overlay opacity
To get a 100% lepton overlay (note camera installation still required):

$ pylepton_overlay -a 255
pylepton_capture
Note that this program will output any image format that opencv knows about, just specify the output file format extension (e.g. output.jpg or output.png)

$ pylepton_capture --help
Usage: pylepton_capture [options] output_file[.format]

Options:
  -h, --help           show this help message and exit
  -f, --flip-vertical  flip the output image vertically
To capture a png file named output.png:

$ pylepton_capture output.png
Important Note
GroupGets does not provide coding, firmware, or software support of any kind and will not respond to related requests. All software and firmware provided by GroupGets are offered solely as examples or potential starting points. These repositories may be outdated and are not guaranteed to function as intended.

We do not accept returns or offer replacements due to issues related to software, firmware, or code compatibility.

The software is provided "AS IS", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and non-infringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.