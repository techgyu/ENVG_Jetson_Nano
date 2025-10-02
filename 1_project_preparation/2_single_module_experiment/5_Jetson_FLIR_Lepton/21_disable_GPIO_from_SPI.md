# 2025-10-01 | SPI 핀에서 GPIO 비활성화
[Jetson Nano SPI Bus Not Working](https://forums.developer.nvidia.com/t/jetson-nano-spi-bus-not-working/249482/9)

---

## 1. SPI1 MOSI/MISO 핀 연결
Jetson Nano 40핀 헤더에서
MOSI: 19번
MISO: 21번
두 핀을 점퍼선으로 직접 연결 (루프백 테스트용)

## 2. dtb 파일 직접 수정을 위해 /boot 폴더로 이동
    ```bash
        user@ubuntu:/boot$ ls
        dtb                                                                       tegra210-p3448-0000-p3449-0000-a01-mcp251x.dtbo
        extlinux                                                                  tegra210-p3448-0000-p3449-0000-a01-respeaker-4-mic-array.dtbo
        grub                                                                      tegra210-p3448-0000-p3449-0000-a01-respeaker-4-mic-lin-array.dtbo
        Image                                                                     tegra210-p3448-0000-p3449-0000-a02-adafruit-sph0645lm4h.dtbo
        initrd                                                                    tegra210-p3448-0000-p3449-0000-a02-adafruit-uda1334a.dtbo
        initrd.img                                                                tegra210-p3448-0000-p3449-0000-a02.dtb
        initrd.img-4.9.337-tegra                                                  tegra210-p3448-0000-p3449-0000-a02-fe-pi-audio.dtbo
        kernel_tegra210-p3448-0000-p3449-0000-b00.dtb                             tegra210-p3448-0000-p3449-0000-a02-hdr40.dtbo
        kernel_tegra210-p3448-0000-p3449-0000-b00-user-custom.dtb                 tegra210-p3448-0000-p3449-0000-a02-m2ke.dtbo
        tegra210-jetson-tx1-p2597-2180-a01-devkit-adafruit-sph0645lm4h.dtbo       tegra210-p3448-0000-p3449-0000-a02-mcp251x.dtbo
        tegra210-jetson-tx1-p2597-2180-a01-devkit-adafruit-uda1334a.dtbo          tegra210-p3448-0000-p3449-0000-a02-respeaker-4-mic-array.dtbo
        tegra210-jetson-tx1-p2597-2180-a01-devkit-csi.dtbo                        tegra210-p3448-0000-p3449-0000-a02-respeaker-4-mic-lin-array.dtbo
        tegra210-jetson-tx1-p2597-2180-a01-devkit.dtb                             tegra210-p3448-0000-p3449-0000-b00.dtb
        tegra210-jetson-tx1-p2597-2180-a01-devkit-fe-pi-audio.dtbo                tegra210-p3448-0002-p3449-0000-a02.dtb
        tegra210-jetson-tx1-p2597-2180-a01-devkit-hdr30.dtbo                      tegra210-p3448-0002-p3449-0000-b00.dtb
        tegra210-jetson-tx1-p2597-2180-a01-devkit-hdr40.dtbo                      tegra210-p3448-0003-p3542-0000-adafruit-sph0645lm4h.dtbo
        tegra210-jetson-tx1-p2597-2180-a01-devkit-m2ke.dtbo                       tegra210-p3448-0003-p3542-0000-adafruit-uda1334a.dtbo
        tegra210-jetson-tx1-p2597-2180-a01-devkit-respeaker-4-mic-array.dtbo      tegra210-p3448-0003-p3542-0000.dtb
        tegra210-jetson-tx1-p2597-2180-a01-devkit-respeaker-4-mic-lin-array.dtbo  tegra210-p3448-0003-p3542-0000-fe-pi-audio.dtbo
        tegra210-jetson-tx1-p2597-2180-a02-devkit-24x7.dtb                        tegra210-p3448-0003-p3542-0000-hdr40.dtbo
        tegra210-p3448-0000-p3449-0000-a00.dtb                                    tegra210-p3448-0003-p3542-0000-respeaker-4-mic-array.dtbo
        tegra210-p3448-0000-p3449-0000-a01-adafruit-sph0645lm4h.dtbo              tegra210-p3448-0003-p3542-0000-respeaker-4-mic-lin-array.dtbo
        tegra210-p3448-0000-p3449-0000-a01-adafruit-uda1334a.dtbo                 tegra210-p3448-all-p3449-0000-camera-imx219-dual.dtbo
        tegra210-p3448-0000-p3449-0000-a01.dtb                                    tegra210-p3448-all-p3449-0000-camera-imx477-dual.dtbo
        tegra210-p3448-0000-p3449-0000-a01-fe-pi-audio.dtbo                       tegra210-p3448-all-p3449-0000-camera-imx477-imx219.dtbo
        tegra210-p3448-0000-p3449-0000-a01-hdr40.dtbo                             tegra210-p3448-common-imx219.dtbo
        tegra210-p3448-0000-p3449-0000-a01-m2ke.dtbo                              tegra210-p3448-common-imx477.dtbo
    ```
### 2.1 주요 파일 설명
**.dtb (Device Tree Blob)**
    Jetson Nano의 하드웨어 설정 정보를 담은 바이너리 파일입니다.
    부팅 시 커널이 하드웨어를 인식하고 설정하는 데 사용됩니다.
    예시:
    tegra210-p3448-0000-p3449-0000-b00.dtb: 기본 Jetson Nano(2GB/4GB) + 기본 carrier board 조합의 표준 디바이스 트리.
    tegra210-p3448-0000-p3449-0000-a01.dtb, a02.dtb, b00.dtb, b00-user-custom.dtb: 하드웨어 리비전, 커스텀 설정, 또는 특정 보드 조합에 따라 다름.

**.dtbo (Device Tree Overlay)**
    기존 dtb 위에 추가로 적용되는 설정 파일.
    특정 센서, 오디오, 카메라, GPIO 확장 등 추가 하드웨어를 사용할 때 적용.
    예시:
    tegra210-p3448-0000-p3449-0000-a01-mcp251x.dtbo: MCP251x CAN 컨트롤러용 오버레이.
    tegra210-p3448-0000-p3449-0000-a01-respeaker-4-mic-array.dtbo: ReSpeaker 4-Mic Array 오디오 보드용 오버레이.
    tegra210-p3448-all-p3449-0000-camera-imx219-dual.dtbo: 듀얼 IMX219 카메라용 오버레이.
    tegra210-p3448-0000-p3449-0000-a02-adafruit-sph0645lm4h.dtbo: Adafruit SPH0645LM4H I2S 마이크용 오버레이.

**Image**
    리눅스 커널 바이너리 파일.

**initrd, initrd.img, initrd.img-4.9.337-tegra**
    부팅 시 사용하는 초기 램디스크 이미지.

**extlinux, grub**
    부트로더 관련 설정 폴더.

## 3. 현재 사용 중인 Jetson Nano 버전 확인
    ```bash
        user@ubuntu:/boot$ sudo cat /proc/device-tree/model
        NVIDIA Jetson Nano Developer Kit
        user@ubuntu:/boot$ sudo jetson_release
        Software part of jetson-stats 4.3.2 - (c) 2024, Raffaello Bonghi
        Model: NVIDIA Jetson Nano Developer Kit - Jetpack 4.6.6 [L4T 32.7.6]
        NV Power Mode[0]: MAXN
        Serial Number: [XXX Show with: jetson_release -s XXX]
        Hardware:
        - P-Number: p3448-0000
        - Module: NVIDIA Jetson Nano (4 GB ram)
        Platform:
        - Distribution: Ubuntu 18.04 Bionic Beaver
        - Release: 4.9.337-tegra
        jtop:
        - Version: 4.3.2
        - Service: Active
        Libraries:
        - CUDA: 10.2.300
        - cuDNN: 8.2.1.32
        - TensorRT: 8.2.1.9
        - VPI: 1.2.3
        - Vulkan: 1.2.70
        - OpenCV: 4.1.1 - with CUDA: NO
        user@ubuntu:/boot$ 
    ```

## 4. 현재 사용 중인 dtb 파일 확인
    ```bash
    user@ubuntu:/boot$ cat /boot/extlinux/extlinux.conf | grep FDT
    FDT /boot/kernel_tegra210-p3448-0000-p3449-0000-b00-user-custom.dtb
    ```
## 5. 수정할 dtb 파일 선택
    ```bash
    /boot/kernel_tegra210-p3448-0000-p3449-0000-b00-user-custom.dtb
    ```

## 6. dtb → dts 변환
    ```bash
	sudo dtc -I dtb -O dts -o extracted.dts /boot/kernel_tegra210-p3448-0000-p3449-0000-b00-user-custom.dtb
    ```

## 7. 생성된 extracted.dts 파일을 WinSCP를 이용하여 Laptop으로 복사


## 8. extracted.dts 파일에서 SPI 핀 GPIO 기능 제거 
1. dts 파일에서 `gpio-input = < ... >;` 부분에서 SPI 관련 값(0xc0~0xc4 등) 삭제
	
    - vscode로 `extracted.dts` 파일을 열어 아래와 같이 수정

    **아래의 값을 변경**
    ```bash
  		default {
			gpio-input = <0xd8 0xc 0xd 0xe 0xf 0xe8 0x26 0x95 0x5 0xbc 0xbd 0xbe "0xc1" "0xc2" 0xa8 0xc8 0xca 0x4d 0x4e 0x4c 0x4f 0x32 0x33 0x10 0x11 0x12 0x13 0x14 0x3a 0x3d 0x3e 0x41 0xe4>;
			gpio-output-low = <0x97 0x98 0xcb 0x38 0x3b 0x3c 0x3f 0x40 0x42>;
			gpio-output-high = <0x6 0xbb 0xe7>;
			linux,phandle = <0x41>;
			phandle = <0x41>;
		};
    ```

    **아래의 값을 다음과 같이 변경**
    ```bash
  		default {
            gpio-input = <0xd8 0x26 0x95 0x5 0xbc 0xbd 0xbe 0xc1 0xc2 0xa8 0xc8 0xca 0x4d 0x4e 0x4c 0x4f 0x32 0x33 0x3a 0x3d 0x3e 0x41 0xe4>;
			gpio-output-low = <0x97 0x98 0xcb 0x38 0x3b 0x3c 0x3f 0x40 0x42>;
			gpio-output-high = <0x6 0xbb 0xe7>;
			linux,phandle = <0x41>;
			phandle = <0x41>;
		};
    ```
## 9. 저장 후 다시 WinSCP로 Jetson Nano의 /boot 폴더로 복사

## 10. 수정된 dts 파일을 dtb로 재변환 및 교체
	```bash
	dtc -I dts -O dtb -o new_tegra210-p3448-0000-p3449-0000-b00.dtb extracted.dts
	```
1. 새 dtb를 /boot 또는 플래싱 경로에 복사
	```sh
	sudo cp new_tegra210-p3448-0000-p3449-0000-b00.dtb /boot/tegra210-p3448-0000-p3449-0000-b00.dtb
	# 또는
	sudo cp new_tegra210-p3448-0000-p3449-0000-b00.dtb Linux_for_Tegra/kernel/dtb/
	```
	- 필요시 재부팅 또는 플래싱 진행
## 3. Jetson-IO로 SPI1 활성화
40핀 헤더 수동 설정 → SPI1(19,21,23,24,26) 선택 → 저장 후 재부팅

## 4. 핀 설정 확인
MOSI/MISO/SCK/CS 핀이 모두 spi1_xxx로 설정되어 있는지 확인

## 5. SPI 드라이버 로드
## 6. 테스트 프로그램 다운로드 및 빌드
## 7. SPI 루프백 테스트 실행
TX와 RX가 동일하게 나오면 성공!


요약:

MOSI/MISO 점퍼 연결
dtb/dts에서 SPI 핀 GPIO 기능 제거
Jetson-IO로 SPI1 활성화
핀 설정 확인
spidev 드라이버 로드
테스트 프로그램 빌드
루프백 테스트 실행