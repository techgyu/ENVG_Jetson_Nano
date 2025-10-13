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

## 9. 기존 dts 파일을 제거
    ```bash
       rm -rf extracted.dts
    ```

## 10. 저장 후 다시 WinSCP로 Jetson Nano의 /boot 폴더로 복사
    ```bash
        sudo cp extlinux.conf /boot/extlinux
    ```

## 11. 기존의 내용을 백업
    ```bash
        sudo mv kernel_tegra210-p3448-0000-p3449-0000-b00-user-custom.dtb kernel_tegra210-p3448-0000-p3449-0000-b00-user-custom.dtb.bak
    ```

## 12. 수정된 dts 파일을 dtb로 재변환 및 교체
	```bash
	sudo dtc -I dts -O dtb -o new_tegra210-p3448-0000-p3449-0000-b00.dtb extracted_edited.dts
	```

**출력결과**
    ```bash
        user@ubuntu:/boot$ sudo dtc -I dts -O dtb -o new_tegra210-p3448-0000-p3449-0000-b00.dtb extracted_edited.dts
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /clock has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /reserved-memory/iram-carveout has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /reserved-memory/ramoops_carveout has a reg or ranges property, 
        but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /reserved-memory/fb0_carveout has a reg or ranges property, but 
        no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /reserved-memory/fb1_carveout has a reg or ranges property, but 
        no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /iommu has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /bpmp has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /mc has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /interrupt-controller has a reg or ranges property, but no unit 
        name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /aconnect@702c0000 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /aconnect@702c0000/adsp has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /aconnect@702c0000/ahub has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /aconnect@702c0000/ahub/ope@702d8000/peq@702d8100 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /aconnect@702c0000/ahub/ope@702d8000/mbdrc@702d8200 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /aconnect@702c0000/ahub/ope@702d8400/peq@702d8500 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /aconnect@702c0000/ahub/ope@702d8400/mbdrc@702d8600 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /aconnect@702c0000/ahub/mvc@0x702da200 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /rtc has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /usb_cd has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /host1x has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /host1x/vi has a reg or ranges property, but no unit name       
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /host1x/dsi has a reg or ranges property, but no unit name      
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /host1x/vic has a reg or ranges property, but no unit name      
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /host1x/nvenc has a reg or ranges property, but no unit name    
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /host1x/tsec has a reg or ranges property, but no unit name     
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /host1x/tsecb has a reg or ranges property, but no unit name    
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /host1x/nvdec has a reg or ranges property, but no unit name    
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /host1x/nvjpg has a reg or ranges property, but no unit name    
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /host1x/sor has a reg or ranges property, but no unit name      
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /host1x/sor/dp-display/dp-lt-settings/lt-setting@0 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /host1x/sor/dp-display/dp-lt-settings/lt-setting@1 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /host1x/sor/dp-display/dp-lt-settings/lt-setting@2 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /host1x/sor1 has a reg or ranges property, but no unit name     
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /host1x/dpaux has a reg or ranges property, but no unit name    
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /host1x/dpaux1 has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /host1x/nvcsi/channel@0/ports/port@0/endpoint@0 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /host1x/nvcsi/channel@0/ports/port@1/endpoint@1 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /host1x/nvcsi/channel@1/ports/port@2/endpoint@2 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /host1x/nvcsi/channel@1/ports/port@3/endpoint@3 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /gpu has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /mipical has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /i2c@7000c400/iqs263@44 has a unit name, but no reg property    
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /i2c@7000c500/battery-charger@6b has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /i2c@7000d000/max77620@3c/pinmux@0 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /i2c@7000d000/max77620@3c/fps/fps0 has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /i2c@7000d000/max77620@3c/fps/fps1 has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /i2c@7000d000/max77620@3c/fps/fps2 has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /soctherm@0x700E2000/fuse_war@fuse_rev_0_1 has a unit name, but 
        no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /soctherm@0x700E2000/fuse_war@fuse_rev_2 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /soctherm@0x700E2000/throttle@critical has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /soctherm@0x700E2000/throttle@heavy has a unit name, but no reg 
        property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /soctherm@0x700E2000/throttle_dev@cpu_high has a unit name, but 
        no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /soctherm@0x700E2000/throttle_dev@gpu_high has a unit name, but 
        no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /tegra_cec has a reg or ranges property, but no unit name       
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ptm has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /mselect has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /adma@702e2000 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/admaif@0x702d0000 has a unit name, but no reg property    
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/sfc@702d2000 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/sfc@702d2200 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/sfc@702d2400 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/sfc@702d2600 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/spkprot@702d8c00 has a unit name, but no reg property     
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/amixer@702dbb00 has a unit name, but no reg property      
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/i2s@702d1000 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/i2s@702d1100 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/i2s@702d1200 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/i2s@702d1300 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/i2s@702d1400 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/amx@702d3000 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/amx@702d3100 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/adx@702d3800 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/adx@702d3900 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/dmic@702d4000 has a unit name, but no reg property        
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/dmic@702d4100 has a unit name, but no reg property        
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/dmic@702d4200 has a unit name, but no reg property        
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/afc@702d7000 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/afc@702d7100 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/afc@702d7200 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/afc@702d7300 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/afc@702d7400 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/afc@702d7500 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/mvc@702da000 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/mvc@702da200 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/iqc@702de000 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/iqc@702de200 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/ope@702d8000 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /ahub/ope@702d8400 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /sata@70020000 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /camera-pcl/dpd/csia has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /camera-pcl/dpd/csib has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /camera-pcl/dpd/csic has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /camera-pcl/dpd/csid has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /camera-pcl/dpd/csie has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /camera-pcl/dpd/csif has a reg or ranges property, but no unit name
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /external-memory-controller@7001b000/emc-table@0 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /external-memory-controller@7001b000/emc-table@0/emc-table@204000 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /external-memory-controller@7001b000/emc-table@0/emc-table@1600000 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /external-memory-controller@7001b000/emc-table@0/emc-table-derated@204000 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /external-memory-controller@7001b000/emc-table@0/emc-table-derated@1600000 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /external-memory-controller@7001b000/emc-table@1 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /external-memory-controller@7001b000/emc-table@1/emc-table@204000 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /external-memory-controller@7001b000/emc-table@1/emc-table@1600000 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /external-memory-controller@7001b000/emc-table@1/emc-table-derated@204000 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /external-memory-controller@7001b000/emc-table@1/emc-table-derated@1600000 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /eeprom-manager/bus@0 has a unit name, but no reg property      
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /eeprom-manager/bus@1 has a unit name, but no reg property      
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragement@0 has a unit name, but no reg propertynew_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragement@0/override@0 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragement@0/override@0/_overlay_/channel@0 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragement@0/override@0/_overlay_/channel@1 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment@1 has a unit name, but no reg property 
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment@1/override@0 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment@2 has a unit name, but no reg property 
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment@2/override@0 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment@2/override@1 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment@2/override@2 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment@3 has a unit name, but no reg property 
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment@3/override@0 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment@3/override@1 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment@4 has a unit name, but no reg property 
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment@4/override@0 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment@4/override@1 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment@4/override@2 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment@5 has a unit name, but no reg property 
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment@5/override@0 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment@5/override@1 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment@5/override@2 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragement@6 has a unit name, but no reg propertynew_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragement@6/override@0 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragement@7 has a unit name, but no reg propertynew_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragement@7/override@0 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragement@8 has a unit name, but no reg propertynew_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragement@8/override@0 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragement@9 has a unit name, but no reg propertynew_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragement@9/override@0 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragement@9/override@1 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment@12 has a unit name, but no reg propertynew_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment@12/override@0 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment@12/override@1 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragement@13 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragement@13/override@0 has a unit name, but no 
        reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragement@13/override@1 has a unit name, but no 
        reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragement@13/override@2 has a unit name, but no 
        reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragement@13/override@3 has a unit name, but no 
        reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment-e2614-common@0 has a unit name, but no 
        reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment-e2614-common@0/overrides@0 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment-e2614-common@0/overrides@1 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment-e2614-common@0/overrides@2 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment-e2614-common@0/overrides@3 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment-e2614-common@0/overrides@4 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment-e2614-common@0/overrides@6 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment-e2614-common@0/overrides@7 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment-e2614-common@0/overrides@8 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment-e2614-common@0/overrides@9 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment-e2614-common@0/overrides@10 has a unit 
        name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment-e2614-common@0/overrides@11 has a unit 
        name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment-e2614-common@0/override@12 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment-e2614-a00@1 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment-e2614-a00@1/overrides@0 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment-e2614-a00@1/override@1 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment-e2614-b00@2 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment-e2614-b00@2/overrides@0 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment-e2614-b00@2/override@1 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment-e2614-pins@3 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /plugin-manager/fragment-e2614-pins@3/overrides@0 has a unit name, but no reg property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /dfll-max77621@70110000 has a unit name, but no reg property    
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_vs_reg): Node /lens_imx219@RBPCV2 has a unit name, but no reg property        
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (pci_bridge): Node /pcie@1003000/pci@1,0 missing bus-range for PCI bridge
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (pci_bridge): Node /pcie@1003000/pci@2,0 missing bus-range for PCI bridge
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (unit_address_format): Failed prerequisite 'pci_bridge'
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (pci_device_reg): Failed prerequisite 'pci_bridge'
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (pci_device_bus_num): Failed prerequisite 'pci_bridge'
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (simple_bus_reg): Node /host1x/vi simple-bus unit address format error, expected "54080000" 
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (simple_bus_reg): Node /host1x/vi/ports missing or empty reg/ranges property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (simple_bus_reg): Node /host1x/vi-bypass missing or empty reg/ranges property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (simple_bus_reg): Node /host1x/dsi simple-bus unit address format error, expected "54300000"new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (simple_bus_reg): Node /host1x/vic simple-bus unit address format error, expected "54340000"new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (simple_bus_reg): Node /host1x/nvenc simple-bus unit address format error, expected "544c0000"
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (simple_bus_reg): Node /host1x/tsec simple-bus unit address format error, expected "54500000"
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (simple_bus_reg): Node /host1x/tsecb simple-bus unit address format error, expected "54100000"
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (simple_bus_reg): Node /host1x/nvdec simple-bus unit address format error, expected "54480000"
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (simple_bus_reg): Node /host1x/nvjpg simple-bus unit address format error, expected "54380000"
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (simple_bus_reg): Node /host1x/sor simple-bus unit address format error, expected "54540000"new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (simple_bus_reg): Node /host1x/sor1 simple-bus unit address format error, expected "54580000"
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (simple_bus_reg): Node /host1x/dpaux simple-bus unit address format error, expected "545c0000"
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (simple_bus_reg): Node /host1x/dpaux1 simple-bus unit address format error, expected "54040000"
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (simple_bus_reg): Node /host1x/nvcsi missing or empty reg/ranges property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (simple_bus_reg): Node /extcon/disp-state missing or empty reg/ranges property
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (simple_bus_reg): Node /regulators/regulator@10 simple-bus unit address format error, expected "a"
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (simple_bus_reg): Node /mods-simple-bus/mods-clocks missing or empty reg/ranges property    
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (gpios_property): Missing property '#gpio-cells' in node /thermal-zones/AO-therm/trips/gpu-scaling5 or bad phandle (referred from /plugin-manager/fragment-e2614-pins@3/overrides@0/_overlay_:gpios[0])
        new_tegra210-p3448-0000-p3449-0000-b00.dtb: Warning (gpios_property): property 'gpio' size (15) is invalid, expected multiple of 4 in node /__symbols__
        user@ubuntu:/boot$ 
    ```

## 13. 새 dtb를 /boot 또는 플래싱 경로에 복사
	```sh
	sudo cp new_tegra210-p3448-0000-p3449-0000-b00.dtb kernel_tegra210-p3448-0000-p3449-0000-b00-user-custom.dtb
	```
	- 필요시 재부팅 또는 플래싱 진행

## 14. 복사 확인
    ```sh
    ls -l kernel_tegra210-p3448-0000-p3449-0000-b00-user-custom.dtb
    ```

## 15. 재부팅
    ```sh
    sudo reboot
    ```

## 16. Jetson-IO로 SPI1 활성화
40핀 헤더 수동 설정 → SPI1(19,21,23,24,26) 선택 → 저장 후 재부팅
    ```sh
    sudo /opt/nvidia/jetson-io/jetson-io.py
    ```

## 17. 핀 설정 확인
MOSI/MISO/SCK/CS 핀이 모두 spi1_xxx로 설정되어 있는지 확인
``` sh
user@ubuntu:~/Desktop$ sudo grep . /sys/kernel/debug/gpio
gpiochip0: GPIOs 0-255, parent: platform/6000d000.gpio, tegra-gpio:
    gpio-0   (                    )
    gpio-1   (                    )
    gpio-2   (                    |pcie_wake           ) in  hi
    gpio-3   (                    )
    gpio-4   (                    )
    gpio-5   (                    )
    gpio-6   (                    |system-suspend-gpio ) out hi
    gpio-7   (                    )
    gpio-8   (                    )
    gpio-9   (                    )
    gpio-10  (                    )
    gpio-11  (                    )
    gpio-12  (SPI1_MOSI           )
    gpio-13  (SPI1_MISO           )
    gpio-14  (SPI1_SCK            )
    gpio-15  (SPI1_CS0            )
    gpio-16  (SPI0_MOSI           )
    gpio-17  (SPI0_MISO           )
    gpio-18  (SPI0_SCK            )
    gpio-19  (SPI0_CS0            )
    gpio-20  (SPI0_CS1            )
    gpio-21  (                    )
    gpio-22  (                    )
    gpio-23  (                    )
    gpio-24  (                    )
    gpio-25  (                    )
    gpio-26  (                    )
    gpio-27  (                    )
    gpio-28  (                    )
    gpio-29  (                    )
    gpio-30  (                    )
    gpio-31  (                    )
    gpio-32  (                    )
    gpio-33  (                    )
    gpio-34  (                    )
    gpio-35  (                    )
    gpio-36  (                    )
    gpio-37  (                    )
    gpio-38  (GPIO13              )
    gpio-39  (                    )
    gpio-40  (                    )
    gpio-41  (                    )
    gpio-42  (                    )
    gpio-43  (                    )
    gpio-44  (                    )
    gpio-45  (                    )
    gpio-46  (                    )
    gpio-47  (                    )
    gpio-48  (                    )
    gpio-49  (                    )
    gpio-50  (UART1_RTS           )
    gpio-51  (UART1_CTS           )
    gpio-52  (                    )
    gpio-53  (                    )
    gpio-54  (                    )
    gpio-55  (                    )
    gpio-56  (                    )
    gpio-57  (                    )
    gpio-58  (                    )
    gpio-59  (                    )
    gpio-60  (                    )
    gpio-61  (                    )
    gpio-62  (                    )
    gpio-63  (                    )
    gpio-64  (                    |i2c-mux-gpio        ) out hi
    gpio-65  (                    |?                   ) out hi
    gpio-66  (                    )
    gpio-67  (                    )
    gpio-68  (                    )
    gpio-69  (                    )
    gpio-70  (                    )
    gpio-71  (                    )
    gpio-72  (                    )
    gpio-73  (                    )
    gpio-74  (                    )
    gpio-75  (                    )
    gpio-76  (I2S0_FS             )
    gpio-77  (I2S0_DIN            )
    gpio-78  (I2S0_DOUT           )
    gpio-79  (I2S0_SCLK           )
    gpio-80  (                    )
    gpio-81  (                    )
    gpio-82  (                    )
    gpio-83  (                    )
    gpio-84  (                    )
    gpio-85  (                    )
    gpio-86  (                    )
    gpio-87  (                    )
    gpio-88  (                    )
    gpio-89  (                    )
    gpio-90  (                    )
    gpio-91  (                    )
    gpio-92  (                    )
    gpio-93  (                    )
    gpio-94  (                    )
    gpio-95  (                    )
    gpio-96  (                    )
    gpio-97  (                    )
    gpio-98  (                    )
    gpio-99  (                    )
    gpio-100 (                    )
    gpio-101 (                    )
    gpio-102 (                    )
    gpio-103 (                    )
    gpio-104 (                    )
    gpio-105 (                    )
    gpio-106 (                    )
    gpio-107 (                    )
    gpio-108 (                    )
    gpio-109 (                    )
    gpio-110 (                    )
    gpio-111 (                    )
    gpio-112 (                    )
    gpio-113 (                    )
    gpio-114 (                    )
    gpio-115 (                    )
    gpio-116 (                    )
    gpio-117 (                    )
    gpio-118 (                    )
    gpio-119 (                    )
    gpio-120 (                    )
    gpio-121 (                    )
    gpio-122 (                    )
    gpio-123 (                    )
    gpio-124 (                    )
    gpio-125 (                    )
    gpio-126 (                    )
    gpio-127 (                    )
    gpio-128 (                    )
    gpio-129 (                    )
    gpio-130 (                    )
    gpio-131 (                    )
    gpio-132 (                    )
    gpio-133 (                    )
    gpio-134 (                    )
    gpio-135 (                    )
    gpio-136 (                    )
    gpio-137 (                    )
    gpio-138 (                    )
    gpio-139 (                    )
    gpio-140 (                    )
    gpio-141 (                    )
    gpio-142 (                    )
    gpio-143 (                    )
    gpio-144 (                    )
    gpio-145 (                    )
    gpio-146 (                    )
    gpio-147 (                    )
    gpio-148 (                    )
    gpio-149 (GPIO01              )
    gpio-150 (                    )
    gpio-151 (                    )
    gpio-152 (                    )
    gpio-153 (                    )
    gpio-154 (                    )
    gpio-155 (                    )
    gpio-156 (                    )
    gpio-157 (                    )
    gpio-158 (                    )
    gpio-159 (                    )
    gpio-160 (                    )
    gpio-161 (                    )
    gpio-162 (                    )
    gpio-163 (                    )
    gpio-164 (                    )
    gpio-165 (                    )
    gpio-166 (                    )
    gpio-167 (                    )
    gpio-168 (GPIO07              )
    gpio-169 (                    )
    gpio-170 (                    )
    gpio-171 (                    )
    gpio-172 (                    )
    gpio-173 (                    )
    gpio-174 (                    )
    gpio-175 (                    )
    gpio-176 (                    )
    gpio-177 (                    )
    gpio-178 (                    )
    gpio-179 (                    )
    gpio-180 (                    )
    gpio-181 (                    )
    gpio-182 (                    )
    gpio-183 (                    )
    gpio-184 (                    )
    gpio-185 (                    )
    gpio-186 (                    )
    gpio-187 (                    )
    gpio-188 (                    )
    gpio-189 (                    |Power               ) in  hi IRQ
    gpio-190 (                    |Forcerecovery       ) in  hi IRQ
    gpio-191 (                    )
    gpio-192 (                    )
    gpio-193 (                    )
    gpio-194 (GPIO12              )
    gpio-195 (                    )
    gpio-196 (                    )
    gpio-197 (                    )
    gpio-198 (                    )
    gpio-199 (                    )
    gpio-200 (GPIO11              )
    gpio-201 (                    |cd                  ) in  lo IRQ
    gpio-202 (                    |pwm-fan-tach        ) in  hi IRQ
    gpio-203 (                    |vdd-3v3-sd          ) out hi
    gpio-204 (                    )
    gpio-205 (                    )
    gpio-206 (                    )
    gpio-207 (                    )
    gpio-208 (                    )
    gpio-209 (                    )
    gpio-210 (                    )
    gpio-211 (                    )
    gpio-212 (                    )
    gpio-213 (                    )
    gpio-214 (                    )
    gpio-215 (                    )
    gpio-216 (GPIO09              )
    gpio-217 (                    )
    gpio-218 (                    )
    gpio-219 (                    )
    gpio-220 (                    )
    gpio-221 (                    )
    gpio-222 (                    )
    gpio-223 (                    )
    gpio-224 (                    )
    gpio-225 (                    |hdmi2.0_hpd         ) in  hi IRQ
    gpio-226 (                    )
    gpio-227 (                    )
    gpio-228 (                    |extcon:extcon@1     ) in  hi IRQ
    gpio-229 (                    )
    gpio-230 (                    )
    gpio-231 (                    |?                   ) out hi
    gpio-232 (SPI1_CS1            )
    gpio-233 (                    )
    gpio-234 (                    )
    gpio-235 (                    )
    gpio-236 (                    )
    gpio-237 (                    )
    gpio-238 (                    )
    gpio-239 (                    )
    gpiochip1: GPIOs 504-511, parent: platform/max77620-gpio, max77620-gpio, can sleep:
    gpio-505 (                    |spmic-default-output) out hi
    gpio-507 (                    |vdd-3v3-sys         ) out hi
    gpio-510 (                    |enable              ) out lo
    gpio-511 (                    |avdd-io-edp-1v05    ) out lo
```
## . SPI 드라이버 로드
## . 테스트 프로그램 다운로드 및 빌드
## . SPI 루프백 테스트 실행
TX와 RX가 동일하게 나오면 성공!
```
    user@ubuntu:~/Desktop$ sudo ./spidev_test -D /dev/spidev0.0 -v -p "hello"
    spi mode: 0x0
    bits per word: 8
    max speed: 500000 Hz (500 KHz)
    TX | 68 65 6C 6C 6F __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __  | hello
    RX | 00 00 00 00 00 __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __  | .....
    user@ubuntu:~/Desktop$
```

요약:

MOSI/MISO 점퍼 연결
dtb/dts에서 SPI 핀 GPIO 기능 제거
Jetson-IO로 SPI1 활성화
핀 설정 확인
spidev 드라이버 로드
테스트 프로그램 빌드
루프백 테스트 실행