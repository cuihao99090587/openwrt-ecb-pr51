#!/usr/bin/env python3
"""Add Lenovo ECB-PR51 device entry to OpenWrt armv8.mk."""
import sys

path = sys.argv[1]

with open(path) as f:
    lines = f.readlines()

if any("lenovo_ecb-pr51" in l for l in lines):
    print("Already configured")
    sys.exit(0)

insert_block = [
    "\n",
    "define Device/lenovo_ecb-pr51\n",
    "  $(Device/rk3568)\n",
    "  DEVICE_VENDOR := Lenovo\n",
    "  DEVICE_MODEL := ECB-PR51\n",
    "  DEVICE_DTS := rk3568-ecb-pr51\n",
    "  UBOOT_DEVICE_NAME := rock-3a-rk3568\n",
    "  DEVICE_PACKAGES := kmod-r8169 blkdiscard\n",
    "endef\n",
    "TARGET_DEVICES += lenovo_ecb-pr51\n",
]

out = []
inserted = False
i = 0

while i < len(lines):
    line = lines[i]
    if not inserted and "Device/rk3568" in line and "define" in line:
        out.append(line)
        i += 1
        while i < len(lines):
            out.append(lines[i])
            if lines[i].strip() == "endef":
                out.extend(insert_block)
                inserted = True
                i += 1
                break
            i += 1
    else:
        out.append(line)
    i += 1

with open(path, "w") as f:
    f.writelines(out)

print("OK" if inserted else "FAIL")
sys.exit(0 if inserted else 1)
