#!/usr/bin/env python3
import os, glob, re
import numpy as np
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VARIANTS_DIR = os.path.join(BASE_DIR, "variants")
RED_XFWM4 = os.path.join(VARIANTS_DIR, "red", "desktop", "theme", "Kali-Red-Dark-Borders", "xfwm4")

ALL_COLORS = {
    "red": {"hex": "#ec0101", "primary": "#ff1744", "circle": "#d50000", "dark": "#8a0000", "glow": "rgba(255, 23, 68, 0.45)", "rgb": (255, 23, 68), "target_hue": 0.0, "sat_mult": 1.0, "is_mono": False},
    "purple": {"hex": "#aa00ff", "primary": "#d500f9", "circle": "#aa00ff", "dark": "#6a0080", "glow": "rgba(213, 0, 249, 0.45)", "rgb": (213, 0, 249), "target_hue": 280.0/360.0, "sat_mult": 1.0, "is_mono": False},
    "green": {"hex": "#00c853", "primary": "#00e676", "circle": "#00c853", "dark": "#006020", "glow": "rgba(0, 230, 118, 0.45)", "rgb": (0, 230, 118), "target_hue": 140.0/360.0, "sat_mult": 1.0, "is_mono": False},
    "blue": {"hex": "#2979ff", "primary": "#00b0ff", "circle": "#2979ff", "dark": "#003c99", "glow": "rgba(0, 176, 255, 0.45)", "rgb": (0, 176, 255), "target_hue": 215.0/360.0, "sat_mult": 1.0, "is_mono": False},
    "yellow": {"hex": "#ffc107", "primary": "#ffd600", "circle": "#ffd600", "dark": "#806000", "glow": "rgba(255, 214, 0, 0.45)", "rgb": (255, 214, 0), "target_hue": 48.0/360.0, "sat_mult": 1.0, "is_mono": False},
    "orange": {"hex": "#ff5722", "primary": "#ff6d00", "circle": "#ff6d00", "dark": "#802b00", "glow": "rgba(255, 109, 0, 0.45)", "rgb": (255, 109, 0), "target_hue": 24.0/360.0, "sat_mult": 1.0, "is_mono": False},
    "lime": {"hex": "#64dd17", "primary": "#76ff03", "circle": "#76ff03", "dark": "#33691e", "glow": "rgba(118, 255, 3, 0.45)", "rgb": (118, 255, 3), "target_hue": 95.0/360.0, "sat_mult": 1.0, "is_mono": False},
    "pink": {"hex": "#f50057", "primary": "#ff4081", "circle": "#ff4081", "dark": "#880e4f", "glow": "rgba(255, 64, 129, 0.45)", "rgb": (255, 64, 129), "target_hue": 335.0/360.0, "sat_mult": 1.0, "is_mono": False},
    "cyan": {"hex": "#00e5ff", "primary": "#18ffff", "circle": "#00e5ff", "dark": "#006080", "glow": "rgba(24, 255, 255, 0.45)", "rgb": (0, 229, 255), "target_hue": 185.0/360.0, "sat_mult": 1.0, "is_mono": False},
    "white": {"hex": "#f5f5f5", "primary": "#ffffff", "circle": "#e0e0e0", "dark": "#424242", "glow": "rgba(255, 255, 255, 0.50)", "rgb": (245, 245, 245), "target_hue": 0.0, "sat_mult": 0.02, "is_mono": True, "mono_tint": (255, 255, 255)},
    "gold": {"hex": "#ffd700", "primary": "#ffab00", "circle": "#ffd700", "dark": "#7f5500", "glow": "rgba(255, 171, 0, 0.45)", "rgb": (255, 215, 0), "target_hue": 42.0/360.0, "sat_mult": 1.1, "is_mono": False},
    "indigo": {"hex": "#3d5afe", "primary": "#536dfe", "circle": "#3d5afe", "dark": "#1a237e", "glow": "rgba(83, 109, 254, 0.45)", "rgb": (61, 90, 254), "target_hue": 232.0/360.0, "sat_mult": 1.0, "is_mono": False},
    "mint": {"hex": "#00bfa5", "primary": "#64ffda", "circle": "#00bfa5", "dark": "#004d40", "glow": "rgba(100, 255, 218, 0.45)", "rgb": (0, 191, 165), "target_hue": 165.0/360.0, "sat_mult": 1.0, "is_mono": False},
    "ruby": {"hex": "#c2185b", "primary": "#e91e63", "circle": "#ad1457", "dark": "#560027", "glow": "rgba(233, 30, 99, 0.45)", "rgb": (194, 24, 91), "target_hue": 338.0/360.0, "sat_mult": 0.85, "is_mono": False},
    "silver": {"hex": "#cfd8dc", "primary": "#eceff1", "circle": "#b0bec5", "dark": "#37474f", "glow": "rgba(236, 239, 241, 0.45)", "rgb": (207, 216, 220), "target_hue": 0.0, "sat_mult": 0.10, "is_mono": True, "mono_tint": (207, 216, 220)}
}

def recolor_image(src_path, c_info):
    img = Image.open(src_path)
    has_alpha = (img.mode == "RGBA")
    if has_alpha:
        rgba = np.array(img, dtype=np.float32)
        rgb = rgba[:, :, :3]
        alpha = rgba[:, :, 3:4]
    else:
        rgb = np.array(img, dtype=np.float32)
        alpha = None
        
    r, g, b = rgb[:, :, 0]/255.0, rgb[:, :, 1]/255.0, rgb[:, :, 2]/255.0
    cmax = np.maximum(np.maximum(r, g), b)
    cmin = np.minimum(np.minimum(r, g), b)
    delta = cmax - cmin
    
    v = cmax
    s = np.zeros_like(v)
    mask = cmax > 1e-5
    s[mask] = delta[mask] / cmax[mask]
    
    if c_info.get("is_mono", False):
        s = s * c_info.get("sat_mult", 0.05)
        tr, tg, tb = c_info.get("mono_tint", (255,255,255))
        tr, tg, tb = tr/255.0, tg/255.0, tb/255.0
        r_out = v * (1.0 - s + s * tr)
        g_out = v * (1.0 - s + s * tg)
        b_out = v * (1.0 - s + s * tb)
    else:
        target_hue = c_info["target_hue"]
        h = np.zeros_like(v)
        h.fill(target_hue)
        s = np.clip(s * c_info.get("sat_mult", 1.0), 0.0, 1.0)
        
        c = v * s
        x = c * (1.0 - np.abs((h * 6.0) % 2.0 - 1.0))
        m = v - c
        
        hi = (np.floor(h * 6.0) % 6).astype(int)
        
        r_out = np.zeros_like(v)
        g_out = np.zeros_like(v)
        b_out = np.zeros_like(v)
        
        cond0 = (hi == 0)
        r_out[cond0], g_out[cond0], b_out[cond0] = c[cond0], x[cond0], 0
        cond1 = (hi == 1)
        r_out[cond1], g_out[cond1], b_out[cond1] = x[cond1], c[cond1], 0
        cond2 = (hi == 2)
        r_out[cond2], g_out[cond2], b_out[cond2] = 0, c[cond2], x[cond2]
        cond3 = (hi == 3)
        r_out[cond3], g_out[cond3], b_out[cond3] = 0, x[cond3], c[cond3]
        cond4 = (hi == 4)
        r_out[cond4], g_out[cond4], b_out[cond4] = x[cond4], 0, c[cond4]
        cond5 = (hi == 5)
        r_out[cond5], g_out[cond5], b_out[cond5] = c[cond5], 0, x[cond5]
        
        r_out += m
        g_out += m
        b_out += m

    out_rgb = (np.clip(np.stack([r_out, g_out, b_out], axis=-1), 0, 1) * 255.0).astype(np.uint8)
    if has_alpha:
        out_rgba = np.concatenate([out_rgb, alpha.astype(np.uint8)], axis=-1)
        return Image.fromarray(out_rgba, "RGBA")
    else:
        return Image.fromarray(out_rgb, "RGB")

# Recolor all XFWM4 PNGs for all 15 colors
for c_key, c_info in ALL_COLORS.items():
    cap = c_key.capitalize()
    t_desktop_name = f"Kali-{cap}-Dark-Borders"
    xfwm_dst = os.path.join(VARIANTS_DIR, c_key, "desktop", "theme", t_desktop_name, "xfwm4")
    os.makedirs(xfwm_dst, exist_ok=True)
    
    # 1. themerc
    with open(os.path.join(RED_XFWM4, "themerc"), "r") as f:
        themerc = f.read()
    themerc = re.sub(r"active_border_color=#[0-9a-fA-F]{6}", f"active_border_color={c_info['hex']}", themerc)
    themerc = re.sub(r"active_text_color=#[0-9a-fA-F]{6}", f"active_text_color={c_info['primary']}", themerc)
    with open(os.path.join(xfwm_dst, "themerc"), "w") as f:
        f.write(themerc)
        
    # 2. Recolor all PNGs
    for png_f in glob.glob(os.path.join(RED_XFWM4, "*.png")):
        b_name = os.path.basename(png_f)
        recolored_img = recolor_image(png_f, c_info)
        recolored_img.save(os.path.join(xfwm_dst, b_name), "PNG")

print("SUCCESS: Recolored all XFWM4 border and titlebar PNGs for all 15 colors!")
