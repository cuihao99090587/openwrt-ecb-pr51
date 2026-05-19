#!/usr/bin/env python3
"""Add Lenovo ECB-PR51 device entry to OpenWrt armv8.mk."""
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "target/linux/rockchip/image/armv8.mk"

with open(path) as f:
    content = f.read()

if "lenovo_ecb-pr51" in content:
    print("Already configured, skipping")
    sys.exit(0)

insert = """define Device/lenovo_ecb-pr51
  $(Device/rk3568)
  DEVICE_VENDOR := Lenovo
  DEVICE_MODEL := ECB-PR51
  DEVICE_DTS := rk3568-ecb-pr51
  UBOOT_DEVICE_NAME := rock-3a-rk3568
  DEVICE_PACKAGES := kmod-r8169 blkdiscard
endef
TARGET_DEVICES += lenovo_ecb-pr51"""

lines = content.split('\n')
out = []
done = False

for i, line in enumerate(lines):
    out.append(line)
    if not done and 'Device/rk3568' in line and 'define' in line:
        # look ahead for the closing endef
        depth = 1
        for j in range(i+1, len(lines)):
            if 'define' in lines[j] and 'Device/' in lines[j]:
                depth += 1
            if lines[j].strip() == 'endef':
                depth -= 1
                if depth == 0:
                    # insert after this endef
                    out.append('')
                    out.append(insert)
                    done = True
                    break

with open(path, 'w') as f:
    f.write('\n'.join(out) + '\n')

print("Image config updated" if done else "ERROR: could not find rk3568 block")
sys.exit(0 if done else 1)
