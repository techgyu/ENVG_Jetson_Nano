# [Done] Step 1. Connect MOSI and MISO of SPI1
MOSI(PIN19 of 40-pin GPIO header)
MISO(PIN21 of 40-pin GPIO header)

# [Done]Step 2. Remove GPIO usage of SPI pins
## 2-1. Check flash log to know which dtb you are using (ex. tegra210-p3448-0000-p3449-0000-b00.dtb)
- my dtb edited by jetson-io : kernel_tegra210-p3448-0000-p3449-0000-b00-user-custom.dtb

## 2-2. Remove GPIO usage in that device tree
### 2-2-1. Method 1 - Remove from source
diff --git a/kernel-dts/porg-platforms/tegra210-porg-gpio-p3448-0000-b00.dtsi b/kernel-dts/porg-platforms/tegra210-porg-gpio-p3448-0000-b00.dtsi
index 1ea952f..49d4196 100644
--- a/kernel-dts/porg-platforms/tegra210-porg-gpio-p3448-0000-b00.dtsi
+++ b/kernel-dts/porg-platforms/tegra210-porg-gpio-p3448-0000-b00.dtsi
@@ -27,11 +27,6 @@
                gpio_default: default {
                        gpio-input = <
                                TEGRA_GPIO(BB, 0)
-                               TEGRA_GPIO(B, 4)
-                               TEGRA_GPIO(B, 5)
-                               TEGRA_GPIO(B, 6)
-                               TEGRA_GPIO(B, 7)
-                               TEGRA_GPIO(DD, 0)
                                TEGRA_GPIO(E, 6)
                                TEGRA_GPIO(S, 5)
                                TEGRA_GPIO(A, 5)
@@ -49,11 +44,6 @@
                                TEGRA_GPIO(J, 7)
                                TEGRA_GPIO(G, 2)
                                TEGRA_GPIO(G, 3)
-                               TEGRA_GPIO(C, 0)
-                               TEGRA_GPIO(C, 1)
-                               TEGRA_GPIO(C, 2)
-                               TEGRA_GPIO(C, 3)
-                               TEGRA_GPIO(C, 4)
                                TEGRA_GPIO(H, 2)
                                TEGRA_GPIO(H, 5)
                                TEGRA_GPIO(H, 6)

### 2-2-2. Method 2 - Remove from decompiled dtb
#### 2-2-2-1 Find you dtb in Linux_for_Tegra/kernel/dtb/tegra210-p3448-0000-p3449-0000-b00.dtb
- my dtb edited by jetson-io : /boot/kernel_tegra210-p3448-0000-p3449-0000-b00-user-custom.dtb
  
#### 2-2-2-2 Dissemble the dtb to dts
dtc -I dtb -O dts -o temp.dts tegra210-p3448-0000-p3449-0000-b00.dtb
- my dtb edited by jetson-io : dtc -I dtb -O dts -o temp.dts kernel_tegra210-p3448-0000-p3449-0000-b00-user-custom.dtb

#### 2-2-2-3 Modify the following line
-        gpio-input = <0xd8 0xc 0xd 0xe 0xf 0xe8 0x26 0x95 0x5 0xbc 0xbd 0xbe 0xc1 0xc2 0xa8 0xc8 0xca 0x4d 0x4e 0x4c 0x4f 0x32 0x33 0x10 0x11 0x12 0x13 0x14 0x3a 0x3d 0x3e 0x41 0xe4>;
+        gpio-input = <0xd8 0x26 0x95 0x5 0xbc 0xbd 0xbe 0xc1 0xc2 0xa8 0xc8 0xca 0x4d 0x4e 0x4c 0x4f 0x32 0x33 0x3a 0x3d 0x3e 0x41 0xe4>;

- my dtb edited by jetson-io :
gpio-input = <0x5 0xbc 0xbd 0xbe 0xc1 0xa9 0xca 0x3a 0x3d 0x3e 0x41 0xe4>;

#### 2-2-2-4 Assemble the dts back to dtb
dtc -I dts -O dtb -o tegra210-p3448-0000-p3449-0000-b00.dtb temp.dts

- my dtb edited by jetson-io : dtc -I dts -O dtb -o kernel_tegra210-p3448-0000-p3449-0000-b00-user-custom.dtb temp.dts

#### 2-2-2-5 Flash the board

# [Done] Step 3. Running Jetson-IO to enable SPI1
## 3-1. Run Jetson IO
```sh
$ sudo /opt/nvidia/jetson-io/jetson-io.py
```
## 3-2. Configure SPI1
Configure Jetson 40pin Header => Configure header pins manually => Select "spi1 (19,21,23,24,26)" => Back -> Save pin changes => Save and reboot to reconfigure pins

**!!!Problem!!!**but my jetson-io.py shows spi0 (19, 21, 23, 24, 26) and spi1 (13, 16, 18, 22, 37) -> Is it correct?

## 3-3. Check pinmux for SPI if the same as following
```sh
$  sudo cat /sys/kernel/debug/tegra_pinctrl_reg | grep -i spi
Bank: 1 Reg: 0x70003050 Val: 0x0000e044 -> spi1_mosi_pc0
Bank: 1 Reg: 0x70003054 Val: 0x0000e044 -> spi1_miso_pc1
Bank: 1 Reg: 0x70003058 Val: 0x0000e044 -> spi1_sck_pc2
Bank: 1 Reg: 0x7000305c Val: 0x0000e048 -> spi1_cs0_pc3
Bank: 1 Reg: 0x70003060 Val: 0x0000e048 -> spi1_cs1_pc4
Bank: 1 Reg: 0x70003064 Val: 0x00006044 -> spi2_mosi_pb4
Bank: 1 Reg: 0x70003068 Val: 0x00006044 -> spi2_miso_pb5
Bank: 1 Reg: 0x7000306c Val: 0x00006044 -> spi2_sck_pb6
Bank: 1 Reg: 0x70003070 Val: 0x00006048 -> spi2_cs0_pb7
Bank: 1 Reg: 0x70003074 Val: 0x00006048 -> spi2_cs1_pdd0
```

my result
```sh
$  sudo cat /sys/kernel/debug/tegra_pinctrl_reg | grep -i spi
Bank: 1 0x70003050 0x0000e044 -> spi1_mosi_pc0
Bank: 1 0x70003054 0x0000e044 -> spi1_miso_pc1
Bank: 1 0x70003058 0x0000e044 -> spi1_sck_pc2
Bank: 1 0x7000305c 0x0000e048 -> spi1_cs0_pc3
Bank: 1 0x70003060 0x0000e048 -> spi1_cs1_pc4
Bank: 1 0x70003064 **0x00006046** -> spi2_mosi_pb4
Bank: 1 0x70003068 **0x00006046** -> spi2_miso_pb5
Bank: 1 0x7000306c **0x00006046** -> spi2_sck_pb6
Bank: 1 0x70003070 **0x00006045** -> spi2_cs0_pb7
Bank: 1 0x70003074 **0x00006045** -> spi2_cs1_pdd0

and there is 

Bank: 1 spi4 mosi
Bank: 1 spi4 sck
Bank: 1 spi4 cs0
Bank: 1 qspi sck pee0
Bank: 1 qspi cs n peel
Bank: 1 qspi io0 pee2
Bank: 1 qspi io1 pee3
Bank: 1 qspi io2 pee4
Bank: 1 qspi io3 pee5

Bank: 0 drive_qspi_comp_control
Bank: 0 drive_qspi_lpbk_control
Bank: 0 drive_qspi_comp

```

# Step 4. Probe SPI driver
```sh
$ sudo modprobe spidev
```

# Step 5. Download/build this test file:
## 5-1 Download
```sh
$ wget https://raw.githubusercontent.com/torvalds/linux/v4.9/tools/spi/spidev_test.c
```
### 5-2 Build on the board
```sh
$ gcc -o spidev_test spidev_test.c
```

# [Done]Step 6. Run the command and check if the result is expected:
```sh
$ sudo ./spidev_test -D /dev/spidev0.0 -v -p "HelloWorld123456789abcdef"
Or 
$ sudo ./spidev_test -D /dev/spidev0.0 -s 10000000 -v
```

# same result TX on but no result on RX

