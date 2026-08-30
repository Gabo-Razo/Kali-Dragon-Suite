#!/usr/bin/env python3
import os

with open("/home/gr/Escritorio/Kali-Red-Dragon-Suite/build_all_15_variants.py", "r") as f:
    code = f.read()

# Make sure XFWM4 recolors PNGs
old_xfwm = """                safe_copy(os.path.join(xfwm_src, xf_f), os.path.join(xfwm_dst, xf_f))"""
new_xfwm = """                if xf_f.endswith(".png"):
                    recolored_xf = recolor_image(os.path.join(xfwm_src, xf_f), c_info)
                    recolored_xf.save(os.path.join(xfwm_dst, xf_f), "PNG")
                else:
                    safe_copy(os.path.join(xfwm_src, xf_f), os.path.join(xfwm_dst, xf_f))"""

if old_xfwm in code:
    code = code.replace(old_xfwm, new_xfwm)
    with open("/home/gr/Escritorio/Kali-Red-Dragon-Suite/build_all_15_variants.py", "w") as f:
        f.write(code)
    print("Updated build_all_15_variants.py successfully!")
else:
    print("Pattern not found or already updated.")
