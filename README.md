# OpenWrt for Lenovo ECB-PR51 (Leez SBC PR51 / RK3568)

[![Build OpenWrt](https://github.com/cuihao99090587/openwrt-ecb-pr51/actions/workflows/build-openwrt.yml/badge.svg)](https://github.com/cuihao99090587/openwrt-ecb-pr51/actions/workflows/build-openwrt.yml)

OpenWrt firmware for the **Lenovo ECB-PR51** single board computer, based on Rockchip RK3568.

## Specs

| Component | Detail |
|-----------|--------|
| SoC | Rockchip RK3568, 4×Cortex-A55 @ 2.0GHz |
| GPU | Mali-G52 |
| NPU | 0.8 TOPS |
| RAM | 2/4/8 GB DDR4 |
| Storage | eMMC 16/32/64/128 GB + MicroSD + SATA×1 |
| Network | **Dual Gigabit Ethernet** + WiFi 5 (AP6256) + BT 5.0 |
| USB | 2×USB 2.0, 1×USB 3.0, Type-C |
| PCIe | PCIe 2.1 x2 slot |
| Display | HDMI, eDP, LVDS, MIPI-DSI |
| GPIO | 40-pin header |
| Size | 85mm × 85mm |

## Usage

### Build firmware

Go to **Actions** → **Build OpenWrt** → **Run workflow**.

Or push changes to trigger auto-build.

### Flash

1. Download artifacts from a successful build
2. Extract `sysupgrade.img.gz` → `.img`
3. Write to TF card or eMMC:
   ```bash
   # On Linux/Mac
   gunzip -k openwrt-*-sysupgrade.img.gz
   sudo dd if=openwrt-*-sysupgrade.img of=/dev/sdX bs=4M status=progress
   ```
4. Insert card and boot

### First boot

- Default IP: `192.168.1.1`
- No password set (set via `passwd` or LuCI)
- Connect to LAN port (eth0)

## ⚠️ Notes

- U-Boot: Currently uses **rock-3a** U-Boot config (generic RK3568 DDR4). If boot issues occur, use the existing U-Boot from Armbian/Android and flash only the kernel+rootfs.
- WiFi/BT: AP6256 (BCM4356) support requires additional firmware blobs (not included due to licensing).

## References

- [Lenovo ECB-PR51 Hardware Specs](docs/Lenovo_ECB-PR51_RK3568_硬件规格书V1.0.pdf)
- [OpenWrt Rockchip Target](https://github.com/openwrt/openwrt/tree/main/target/linux/rockchip)
- [Rockchip RK3568 Datasheet](https://www.rock-chips.com/)
