#!/usr/bin/env python3
import os, sys, shutil, glob, re
import numpy as np
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VARIANTS_DIR = os.path.join(BASE_DIR, "variants")
RED_VARIANT_DIR = os.path.join(VARIANTS_DIR, "red")

def safe_copy(src, dst):
    if os.path.abspath(src) != os.path.abspath(dst):
        shutil.copyfile(src, dst)

ALL_COLORS = {
    # 1. Classic 8 Colors
    "red": {
        "hex": "#ec0101", "primary": "#ff1744", "circle": "#d50000", "dark": "#8a0000",
        "glow": "rgba(255, 23, 68, 0.45)", "rgb": (255, 23, 68),
        "target_hue": 0.0, "sat_mult": 1.0, "is_mono": False,
        "z_hi": "196", "z_lo": "160", "cursor": "#ff1744",
        "base_theme": "Kali-Red-Dark", "icon_theme": "Flat-Remix-Red-Dark"
    },
    "purple": {
        "hex": "#aa00ff", "primary": "#d500f9", "circle": "#aa00ff", "dark": "#6a0080",
        "glow": "rgba(213, 0, 249, 0.45)", "rgb": (213, 0, 249),
        "target_hue": 280.0/360.0, "sat_mult": 1.0, "is_mono": False,
        "z_hi": "165", "z_lo": "135", "cursor": "#d500f9",
        "base_theme": "Kali-Purple-Dark", "icon_theme": "Flat-Remix-Purple-Dark"
    },
    "green": {
        "hex": "#00c853", "primary": "#00e676", "circle": "#00c853", "dark": "#006020",
        "glow": "rgba(0, 230, 118, 0.45)", "rgb": (0, 230, 118),
        "target_hue": 140.0/360.0, "sat_mult": 1.0, "is_mono": False,
        "z_hi": "46", "z_lo": "34", "cursor": "#00e676",
        "base_theme": "Kali-Green-Dark", "icon_theme": "Flat-Remix-Green-Dark"
    },
    "blue": {
        "hex": "#2979ff", "primary": "#00b0ff", "circle": "#2979ff", "dark": "#003c99",
        "glow": "rgba(0, 176, 255, 0.45)", "rgb": (0, 176, 255),
        "target_hue": 215.0/360.0, "sat_mult": 1.0, "is_mono": False,
        "z_hi": "39", "z_lo": "27", "cursor": "#00b0ff",
        "base_theme": "Kali-Dark", "icon_theme": "Flat-Remix-Blue-Dark"
    },
    "yellow": {
        "hex": "#ffc107", "primary": "#ffd600", "circle": "#ffd600", "dark": "#806000",
        "glow": "rgba(255, 214, 0, 0.45)", "rgb": (255, 214, 0),
        "target_hue": 48.0/360.0, "sat_mult": 1.0, "is_mono": False,
        "z_hi": "226", "z_lo": "214", "cursor": "#ffd600",
        "base_theme": "Kali-Yellow-Dark", "icon_theme": "Flat-Remix-Yellow-Dark"
    },
    "orange": {
        "hex": "#ff5722", "primary": "#ff6d00", "circle": "#ff6d00", "dark": "#802b00",
        "glow": "rgba(255, 109, 0, 0.45)", "rgb": (255, 109, 0),
        "target_hue": 24.0/360.0, "sat_mult": 1.0, "is_mono": False,
        "z_hi": "208", "z_lo": "202", "cursor": "#ff6d00",
        "base_theme": "Kali-Orange-Dark", "icon_theme": "Flat-Remix-Orange-Dark"
    },
    "lime": {
        "hex": "#64dd17", "primary": "#76ff03", "circle": "#76ff03", "dark": "#33691e",
        "glow": "rgba(118, 255, 3, 0.45)", "rgb": (118, 255, 3),
        "target_hue": 95.0/360.0, "sat_mult": 1.0, "is_mono": False,
        "z_hi": "118", "z_lo": "112", "cursor": "#76ff03",
        "base_theme": "Kali-Green-Dark", "icon_theme": "Flat-Remix-Green-Dark"
    },
    "pink": {
        "hex": "#f50057", "primary": "#ff4081", "circle": "#ff4081", "dark": "#880e4f",
        "glow": "rgba(255, 64, 129, 0.45)", "rgb": (255, 64, 129),
        "target_hue": 335.0/360.0, "sat_mult": 1.0, "is_mono": False,
        "z_hi": "207", "z_lo": "198", "cursor": "#ff4081",
        "base_theme": "Kali-Pink-Dark", "icon_theme": "Flat-Remix-Pink-Dark"
    },
    # 2. Brand New 7 Colors
    "cyan": {
        "hex": "#00e5ff", "primary": "#18ffff", "circle": "#00e5ff", "dark": "#006080",
        "glow": "rgba(24, 255, 255, 0.45)", "rgb": (0, 229, 255),
        "target_hue": 185.0/360.0, "sat_mult": 1.0, "is_mono": False,
        "z_hi": "51", "z_lo": "45", "cursor": "#18ffff",
        "base_theme": "Kali-Dark", "icon_theme": "Flat-Remix-Teal-Dark"
    },
    "teal": {
        "hex": "#00b4d8", "primary": "#00f2fe", "circle": "#00b4d8", "dark": "#0077b6",
        "glow": "rgba(0, 242, 254, 0.45)", "rgb": (0, 242, 254),
        "target_hue": 182.0/360.0, "sat_mult": 1.15, "is_mono": False,
        "z_hi": "45", "z_lo": "38", "cursor": "#00f2fe",
        "base_theme": "Kali-Dark", "icon_theme": "Flat-Remix-Teal-Dark"
    },
    "gold": {
        "hex": "#ffd700", "primary": "#ffab00", "circle": "#ffd700", "dark": "#7f5500",
        "glow": "rgba(255, 171, 0, 0.45)", "rgb": (255, 215, 0),
        "target_hue": 42.0/360.0, "sat_mult": 1.1, "is_mono": False,
        "z_hi": "220", "z_lo": "214", "cursor": "#ffab00",
        "base_theme": "Kali-Yellow-Dark", "icon_theme": "Flat-Remix-Yellow-Dark"
    },
    "indigo": {
        "hex": "#3d5afe", "primary": "#536dfe", "circle": "#3d5afe", "dark": "#1a237e",
        "glow": "rgba(83, 109, 254, 0.45)", "rgb": (61, 90, 254),
        "target_hue": 232.0/360.0, "sat_mult": 1.0, "is_mono": False,
        "z_hi": "63", "z_lo": "57", "cursor": "#536dfe",
        "base_theme": "Kali-Dark", "icon_theme": "Flat-Remix-Blue-Dark"
    },
    "mint": {
        "hex": "#00bfa5", "primary": "#64ffda", "circle": "#00bfa5", "dark": "#004d40",
        "glow": "rgba(100, 255, 218, 0.45)", "rgb": (0, 191, 165),
        "target_hue": 165.0/360.0, "sat_mult": 1.0, "is_mono": False,
        "z_hi": "49", "z_lo": "43", "cursor": "#64ffda",
        "base_theme": "Kali-Green-Dark", "icon_theme": "Flat-Remix-Teal-Dark"
    },
    "ruby": {
        "hex": "#c2185b", "primary": "#e91e63", "circle": "#ad1457", "dark": "#560027",
        "glow": "rgba(233, 30, 99, 0.45)", "rgb": (194, 24, 91),
        "target_hue": 338.0/360.0, "sat_mult": 0.85, "is_mono": False,
        "z_hi": "161", "z_lo": "125", "cursor": "#e91e63",
        "base_theme": "Kali-Pink-Dark", "icon_theme": "Flat-Remix-Red-Dark"
    },
    "magenta": {
        "hex": "#e00070", "primary": "#ff007f", "circle": "#d80064", "dark": "#7a0038",
        "glow": "rgba(255, 0, 127, 0.45)", "rgb": (255, 0, 127),
        "target_hue": 320.0/360.0, "sat_mult": 1.15, "is_mono": False,
        "z_hi": "198", "z_lo": "162", "cursor": "#ff007f",
        "base_theme": "Kali-Pink-Dark", "icon_theme": "Flat-Remix-Pink-Dark"
    }
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

# GTK CSS Templates
login_css_template = """
/* ==========================================================================
   🐉 KALI DRAGON GLASSMORPHISM LOGIN & LOCK SUITE - {cap_color} EDITION
   ========================================================================== */

/* 1. LIGHTDM LOGIN GREETER */
#login_window,
#panel_window {{
    background-color: rgba(14, 3, 8, 0.93);
    border: 2px solid {primary};
    border-radius: 12px;
    box-shadow: 0 0 25px {glow}, 0 0 4px {hex};
}}

#user_image {{
    border: 2px solid {primary};
    border-radius: 50%;
    box-shadow: 0 0 16px {glow};
    background-color: #0c0004;
}}

#prompt_label,
#message_label {{
    color: {primary};
    font-weight: bold;
    text-shadow: 0 0 8px {glow};
}}

#entry {{
    background-color: rgba(0, 0, 0, 0.65);
    border: 1.5px solid rgba(255, 255, 255, 0.15);
    border-radius: 6px;
    color: #ffffff;
    caret-color: {primary};
    padding: 6px 12px;
}}

#entry:focus {{
    border: 2px solid {primary};
    box-shadow: 0 0 14px {glow};
}}

#login_button {{
    background-image: linear-gradient(135deg, {primary} 0%, {core} 50%, {dark} 100%);
    border: 1.5px solid {primary};
    border-radius: 6px;
    color: #ffffff;
    font-weight: bold;
    padding: 6px 16px;
    box-shadow: 0 0 12px {glow};
}}

#login_button:hover {{
    background-image: linear-gradient(135deg, #ffffff 0%, {primary} 40%, {core} 100%);
    box-shadow: 0 0 20px {glow};
}}

/* 2. XFCE4 SCREENSAVER LOCK DIALOG (Lock / Suspend Wake-up) */
window.screensaver-dialog,
dialog.screensaver-dialog,
.screensaver-dialog {{
    background-color: #0c0205;
    background-image: url("/usr/share/desktop-base/kali-theme/lockscreen/lockscreen.png");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

.lock-dialog,
.screensaver-dialog > box,
dialog.screensaver-dialog > box {{
    background-color: rgba(12, 3, 7, 0.94);
    border: 2px solid {primary};
    border-radius: 14px;
    box-shadow: 0 0 30px {glow}, 0 0 4px {hex};
    padding: 20px;
}}

#auth-face-image {{
    border: 2px solid {primary};
    border-radius: 50%;
    box-shadow: 0 0 18px {glow};
    background-color: #0c0004;
}}

#auth-prompt-label,
label#auth-prompt-label {{
    color: #ffffff;
    font-weight: bold;
    font-size: 11pt;
    text-shadow: 0 0 6px {glow};
}}

#auth-status-label,
label#auth-status-label {{
    color: {primary};
    font-weight: bold;
    font-size: 11pt;
    text-shadow: 0 0 10px {glow};
}}

#auth-capslock-label,
label#auth-capslock-label {{
    color: #ffd600;
    font-weight: bold;
}}

#auth-realname-label,
#auth-hostname-label,
#auth-date-time-label {{
    color: #ffffff;
    font-weight: bold;
    text-shadow: 0 0 8px {glow};
}}

#auth-prompt-entry,
entry#auth-prompt-entry {{
    background-color: rgba(0, 0, 0, 0.65);
    border: 1.5px solid rgba(255, 255, 255, 0.15);
    border-radius: 6px;
    color: #ffffff;
    caret-color: {primary};
    padding: 6px 12px;
}}

#auth-prompt-entry:focus,
entry#auth-prompt-entry:focus {{
    border: 2px solid {primary};
    box-shadow: 0 0 14px {glow};
}}

#auth-unlock-button,
#auth-action-area button.suggested-action {{
    background-image: linear-gradient(135deg, {primary} 0%, {core} 50%, {dark} 100%);
    border: 1.5px solid {primary};
    border-radius: 6px;
    color: #ffffff;
    font-weight: bold;
    padding: 6px 18px;
    box-shadow: 0 0 12px {glow};
}}

#auth-unlock-button:hover,
#auth-action-area button.suggested-action:hover {{
    background-image: linear-gradient(135deg, #ffffff 0%, {primary} 40%, {core} 100%);
    box-shadow: 0 0 20px {glow};
}}

#auth-cancel-button,
#auth-logout-button,
#auth-switch-button {{
    background-color: rgba(255, 255, 255, 0.08);
    border: 1.5px solid rgba(255, 255, 255, 0.15);
    border-radius: 6px;
    color: #ffffff;
    padding: 6px 12px;
}}

#auth-cancel-button:hover,
#auth-logout-button:hover,
#auth-switch-button:hover {{
    background-color: rgba({r}, {g}, {b}, 0.3);
    border: 2px solid {primary};
    box-shadow: 0 0 14px {glow};
    color: #ffffff;
}}

/* 3. XFCE4 SESSION LOGOUT DIALOG */
window#logout-dialog,
dialog#logout-dialog,
.xfce4-session-logout,
window.xfce4-session-logout {{
    background-color: rgba(12, 3, 7, 0.95);
    border: 2px solid {primary};
    border-radius: 14px;
    box-shadow: 0 0 30px {glow}, 0 0 4px {hex};
    padding: 16px;
}}

window#logout-dialog label,
.xfce4-session-logout label {{
    color: #ffffff;
    font-weight: bold;
    text-shadow: 0 0 6px {glow};
}}

window#logout-dialog button,
.xfce4-session-logout button {{
    background-color: rgba(255, 255, 255, 0.05);
    border: 1.5px solid rgba(255, 255, 255, 0.12);
    border-radius: 8px;
    color: #ffffff;
    font-weight: 500;
    padding: 8px 14px;
    margin: 4px;
}}

window#logout-dialog button:hover,
.xfce4-session-logout button:hover {{
    background-color: rgba({r}, {g}, {b}, 0.25);
    border: 2px solid {primary};
    box-shadow: 0 0 16px {glow};
    color: #ffffff;
}}
"""

desktop_borders_css_template = """
/* 4. SOLID 2PX CONTINUOUS WINDOW BORDERS */
window.ssd > decoration,
window.csd > decoration,
window.csd.background > decoration {{
    border: 2px solid {hex};
    border-radius: 6px 6px 0px 0px;
    box-shadow: 0 0 10px {glow}, 0 0 2px {hex};
}}

headerbar,
.titlebar {{
    border-top: 2px solid {hex};
    border-left: 2px solid {hex};
    border-right: 2px solid {hex};
}}

tooltip,
tooltip.background,
.tooltip {{
    background-color: rgba(20, 22, 28, 0.95);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 5px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
    color: #ffffff;
}}
"""

lock_svg_template = """<svg width="512" height="512" version="1.1" viewBox="0 0 384 384" xmlns="http://www.w3.org/2000/svg">
 <path d="m360 189c0 92.785-75.215 168-168 168s-168-75.215-168-168 75.215-168 168-168 168 75.215 168 168z" fill="{circle}"/>
 <path d="m192 87.75c-40.385 7.91e-4 -72.901 32.51-72.901 72.895v31.941h-12.981c-3.2654 0-5.915 2.7397-5.915 6.1143v98.288c0 3.7322 3.0281 6.7544 6.7603 6.7544h12.136v7e-3h16.201v-7e-3h113.4v7e-3h16.2v-7e-3h12.142c3.7322 0 6.7544-3.0222 6.7544-6.7544v-98.288c0-3.3745-2.6438-6.1143-5.9092-6.1143h-12.987v-31.941c0-40.386-32.514-72.894-72.899-72.895zm1e-3 18.841h1e-3c27.485 8.2e-4 49.608 22.863 49.608 51.261v34.734h-99.218v-34.734c0-28.397 22.123-51.26 49.608-51.261zm0 109.36c7.4574 0 13.5 6.0426 13.5 13.5-7e-3 5.3673-1.6839 10.215-6.5962 12.362v38.936h-13.808v-38.936c-4.9123-2.1469-6.5891-6.9943-6.5962-12.362 0-7.4574 6.0427-13.5 13.5-13.5z" opacity=".3"/>
 <path d="m192 80.25c-40.385 7.91e-4 -72.901 32.51-72.901 72.895v31.941h-12.981c-3.2654 0-5.915 2.7397-5.915 6.1143v98.288c0 3.7322 3.0281 6.7544 6.7603 6.7544h12.136v7e-3h16.201v-7e-3h113.4v7e-3h16.2v-7e-3h12.142c3.7322 0 6.7544-3.0222 6.7544-6.7544v-98.288c0-3.3745-2.6438-6.1143-5.9092-6.1143h-12.987v-31.941c0-40.386-32.514-72.894-72.899-72.895zm1e-3 18.841h1e-3c27.485 8.21e-4 49.608 22.863 49.608 51.261v34.734h-99.218v-34.734c0-28.397 22.123-51.26 49.608-51.261zm0 109.36c7.4574 0 13.5 6.0426 13.5 13.5-7e-3 5.3673-1.6839 10.215-6.5962 12.362v38.936h-13.808v-38.936c-4.9123-2.1469-6.5891-6.9943-6.5962-12.362 0-7.4574 6.0427-13.5 13.5-13.5z" fill="#fff"/>
 <path transform="scale(.75)" d="m32.062 247c-0.036438 1.6631-0.0625 3.3282-0.0625 5 0 123.71 100.29 224 224 224s224-100.29 224-224c0-1.6718-0.02606-3.3369-0.0625-5-2.66 121.4-101.9 219-223.94 219s-221.28-97.597-223.94-219z" opacity=".3" stroke-width="1.3333"/>
 <path transform="scale(.75)" d="m256 28c-123.71 0-224 100.29-224 224 0 1.6718 0.026062 3.3369 0.0625 5 2.66-121.4 101.9-219 223.94-219s221.28 97.597 223.94 219c0.03644-1.6631 0.0625-3.3282 0.0625-5 0-123.71-100.29-224-224-224z" fill="#fafafa" opacity=".3" stroke-width="1.3333"/>
</svg>"""

logout_svg_template = """<svg width="512" height="512" version="1.1" viewBox="0 0 384 384" xmlns="http://www.w3.org/2000/svg">
 <path d="m360 192c0 92.785-75.215 168-168 168s-168-75.215-168-168 75.215-168 168-168 168 75.215 168 168z" fill="{circle}"/>
 <path d="m192 91.5c59.648 0 108 48.352 108 108s-48.352 108-108 108-108-48.352-108-108 48.352-108 108-108zm0 24c-46.391 0-84 37.609-84 84s37.609 84 84 84 84-37.609 84-84-37.609-84-84-84zm0 48 23.789 18.469 24.215 17.531-24.203 17.531-23.797 18.469 0.28907-24h-36.289c-6.6484 0-12-5.3516-12-12s5.3516-12 12-12h36.281l-0.28125-24z" fill="#000205" opacity=".31"/>
 <path d="m192 84c59.648 0 108 48.352 108 108s-48.352 108-108 108-108-48.352-108-108 48.352-108 108-108zm0 24c-46.391 0-84 37.609-84 84s37.609 84 84 84 84-37.609 84-84-37.609-84-84-84zm0 48 23.789 18.469 24.215 17.531-24.203 17.531-23.797 18.469 0.28906-24h-36.289c-6.6484 0-12-5.3516-12-12s5.3516-12 12-12h36.281l-0.28125-24z" fill="#fff"/>
 <path transform="scale(.75)" d="m32.062 251c-0.036438 1.6631-0.0625 3.3282-0.0625 5 0 123.71 100.29 224 224 224s224-100.29 224-224c0-1.6718-0.02606-3.3369-0.0625-5-2.66 121.4-101.9 219-223.94 219s-221.28-97.597-223.94-219z" fill="#000b1d" opacity=".3" stroke-width="1.3333"/>
 <path transform="scale(.75)" d="m256 32c-123.71 0-224 100.29-224 224 0 1.6718 0.026062 3.3369 0.0625 5 2.66-121.4 101.9-219 223.94-219s221.28 97.597 223.94 219c0.03644-1.6631 0.0625-3.3282 0.0625-5 0-123.71-100.29-224-224-224z" fill="#fff" opacity=".1" stroke-width="1.3333"/>
</svg>"""

with open("/usr/share/icons/Flat-Remix-Blue-Dark/apps/scalable/kali-menu.svg", "r") as f:
    base_menu_svg = f.read()

xml_template = """<background>
  <static>
    <duration>8640000.0</duration>
    <file>
      <size width="1920" height="1080">/usr/share/desktop-base/kali-theme/lockscreen/lockscreen.png</size>
    </file>
  </static>
</background>
"""

print(f"Building complete assets for {len(ALL_COLORS)} color variants...")

for c_key, c_info in ALL_COLORS.items():
    cap = c_key.capitalize()
    t_login_name = f"Kali-{cap}-Dragon-Login"
    t_desktop_name = f"Kali-{cap}-Dark-Borders"
    v_dir = os.path.join(VARIANTS_DIR, c_key)
    
    # Create subdirectories
    os.makedirs(os.path.join(v_dir, "assets"), exist_ok=True)
    os.makedirs(os.path.join(v_dir, "boot", "grub", "icons"), exist_ok=True)
    os.makedirs(os.path.join(v_dir, "boot", "plymouth"), exist_ok=True)
    os.makedirs(os.path.join(v_dir, "boot", "transition"), exist_ok=True)
    os.makedirs(os.path.join(v_dir, "login", "theme", t_login_name, "gtk-3.0"), exist_ok=True)
    os.makedirs(os.path.join(v_dir, "lockscreen"), exist_ok=True)
    os.makedirs(os.path.join(v_dir, "desktop", "animator"), exist_ok=True)
    os.makedirs(os.path.join(v_dir, "desktop", "gtk-css"), exist_ok=True)
    os.makedirs(os.path.join(v_dir, "desktop", "theme", t_desktop_name, "gtk-3.0"), exist_ok=True)
    os.makedirs(os.path.join(v_dir, "desktop", "theme", t_desktop_name, "gtk-4.0"), exist_ok=True)
    os.makedirs(os.path.join(v_dir, "desktop", "theme", t_desktop_name, "xfwm4"), exist_ok=True)
    os.makedirs(os.path.join(v_dir, "icons", "apps", "scalable"), exist_ok=True)
    
    # 1. Recolor Images
    # 1.1 Wallpaper
    wp_path = os.path.join(v_dir, "assets", f"wallpaper_{c_key}.png")
    recolored_wp = recolor_image(os.path.join(RED_VARIANT_DIR, "assets", "wallpaper_red.png"), c_info)
    recolored_wp.save(wp_path, "PNG")
    recolored_wp.save(os.path.join(BASE_DIR, "assets", f"dragon_wallpaper_{c_key}.png"), "PNG")
    
    # Preview
    recolored_wp.resize((640, 360), Image.Resampling.LANCZOS).save(os.path.join(v_dir, "assets", f"preview_{c_key}.png"), "PNG")
    recolored_wp.resize((640, 360), Image.Resampling.LANCZOS).save(os.path.join(BASE_DIR, "assets", f"preview_{c_key}.png"), "PNG")

    # 1.2 Lockscreen & Transition
    recolored_wp.save(os.path.join(v_dir, "lockscreen", "lockscreen.png"), "PNG")
    recolored_wp.save(os.path.join(v_dir, "boot", "transition", "login-background.png"), "PNG")
    
    # Blurred login
    blurred_img = recolor_image(os.path.join(RED_VARIANT_DIR, "boot", "transition", "login-blurred.png"), c_info)
    blurred_img.save(os.path.join(v_dir, "boot", "transition", "login-blurred.png"), "PNG")
    
    # Desktop GRUB
    desktop_grub = recolor_image(os.path.join(RED_VARIANT_DIR, "boot", "transition", "desktop-grub.png"), c_info)
    desktop_grub.save(os.path.join(v_dir, "boot", "transition", "desktop-grub.png"), "PNG")
    
    # 1.3 Avatar
    avatar_img = recolor_image(os.path.join(RED_VARIANT_DIR, "login", "dragon-avatar.png"), c_info)
    avatar_img.save(os.path.join(v_dir, "login", "dragon-avatar.png"), "PNG")
    avatar_img.save(os.path.join(v_dir, "lockscreen", "dragon-avatar.png"), "PNG")
    
    # 1.4 Dragon Sprite
    sprite_img = recolor_image(os.path.join(RED_VARIANT_DIR, "desktop", "animator", "dragon_sprite.png"), c_info)
    sprite_img.save(os.path.join(v_dir, "desktop", "animator", "dragon_sprite.png"), "PNG")
    sprite_img.save(os.path.join(v_dir, "assets", "dragon_sprite.png"), "PNG")
    
    # 1.5 GRUB Images & Theme
    for grub_f in ["grub-16x9.png", "grub-4x3.png", "select_c.png", "select_e.png", "select_w.png", "slider_bottom.png", "slider_middle.png", "slider_top.png"]:
        src_g = os.path.join(RED_VARIANT_DIR, "boot", "grub", grub_f)
        if os.path.exists(src_g):
            g_img = recolor_image(src_g, c_info)
            g_img.save(os.path.join(v_dir, "boot", "grub", grub_f), "PNG")
            
    # GRUB theme.txt
    with open(os.path.join(RED_VARIANT_DIR, "boot", "grub", "theme.txt"), "r") as f:
        grub_txt = f.read()
    grub_txt = re.sub(r"#[0-9a-fA-F]{6}", c_info["hex"], grub_txt)
    with open(os.path.join(v_dir, "boot", "grub", "theme.txt"), "w") as f:
        f.write(grub_txt)
        
    # GRUB 70+ OS icons
    for icon_f in glob.glob(os.path.join(RED_VARIANT_DIR, "boot", "grub", "icons", "*.png")):
        b_name = os.path.basename(icon_f)
        i_img = recolor_image(icon_f, c_info)
        i_img.save(os.path.join(v_dir, "boot", "grub", "icons", b_name), "PNG")
        
    # 1.6 Plymouth Images & Script
    for ply_f in glob.glob(os.path.join(RED_VARIANT_DIR, "boot", "plymouth", "*.png")):
        b_name = os.path.basename(ply_f)
        p_img = recolor_image(ply_f, c_info)
        p_img.save(os.path.join(v_dir, "boot", "plymouth", b_name), "PNG")
        
    safe_copy(os.path.join(RED_VARIANT_DIR, "boot", "plymouth", "kali.script"), os.path.join(v_dir, "boot", "plymouth", "kali.script"))
    safe_copy(os.path.join(RED_VARIANT_DIR, "boot", "plymouth", "kali.plymouth"), os.path.join(v_dir, "boot", "plymouth", "kali.plymouth"))

    # 2. Config & Text Files
    # Lockscreen XML
    with open(os.path.join(v_dir, "lockscreen", "gnome-background.xml"), "w") as f:
        f.write(xml_template)
        
    # LightDM Conf
    with open(os.path.join(v_dir, "login", "lightdm-gtk-greeter.conf"), "w") as f:
        f.write(f"""[greeter]
background = /usr/share/desktop-base/kali-theme/login/login-background.png
theme-name = {t_login_name}
icon-theme-name = {c_info['icon_theme']}
font-name = Cantarell 11
xft-antialias = true
xft-dpi = 96
xft-hintstyle = slight
xft-rgba = rgb
indicators = ~host;~spacer;~clock;~spacer;~session;~power
clock-format = %a %d %b, %H:%M
user-background = false
default-user-image = /usr/share/desktop-base/kali-theme/login/dragon-avatar.png
hide-user-image = false
""")

    # Animator Color Config JSON
    r, g, b = c_info["rgb"]
    with open(os.path.join(v_dir, "desktop", "animator", "color_config.json"), "w") as f:
        f.write(f'{{"primary": "{c_info["primary"]}", "glow": "{c_info["glow"]}", "hex": "{c_info["hex"]}", "rgb": [{r}, {g}, {b}]}}\n')

    # CSS Generation
    login_css = login_css_template.format(
        cap_color=cap,
        hex=c_info["hex"],
        primary=c_info["primary"],
        core=c_info["circle"],
        dark=c_info["dark"],
        glow=c_info["glow"],
        r=r, g=g, b=b
    )
    borders_css = desktop_borders_css_template.format(
        hex=c_info["hex"],
        glow=c_info["glow"]
    )
    full_desktop_css = login_css + "\n" + borders_css
    
    with open(os.path.join(v_dir, "login", "theme", t_login_name, "gtk-3.0", "gtk.css"), "w") as f:
        f.write(login_css)
    with open(os.path.join(v_dir, "desktop", "theme", t_desktop_name, "gtk-3.0", "gtk.css"), "w") as f:
        f.write(full_desktop_css)
    with open(os.path.join(v_dir, "desktop", "gtk-css", "gtk-3.0.css"), "w") as f:
        f.write(full_desktop_css)
    with open(os.path.join(v_dir, "desktop", "gtk-css", "gtk-4.0.css"), "w") as f:
        f.write(full_desktop_css)
        
    # XFWM4 Themes
    xfwm_dst = os.path.join(v_dir, "desktop", "theme", t_desktop_name, "xfwm4")
    xfwm_src = os.path.join(RED_VARIANT_DIR, "desktop", "theme", "Kali-Red-Dark-Borders", "xfwm4")
    if os.path.exists(xfwm_src):
        for xf_f in os.listdir(xfwm_src):
            if xf_f == "themerc":
                with open(os.path.join(xfwm_src, xf_f), "r") as f:
                    tm = f.read()
                tm = re.sub(r"active_border_color=#[0-9a-fA-F]{6}", f"active_border_color={c_info['hex']}", tm)
                tm = re.sub(r"active_text_color=#[0-9a-fA-F]{6}", f"active_text_color={c_info['primary']}", tm)
                with open(os.path.join(xfwm_dst, xf_f), "w") as f:
                    f.write(tm)
            else:
                if xf_f.endswith(".png"):
                    recolored_xf = recolor_image(os.path.join(xfwm_src, xf_f), c_info)
                    recolored_xf.save(os.path.join(xfwm_dst, xf_f), "PNG")
                else:
                    safe_copy(os.path.join(xfwm_src, xf_f), os.path.join(xfwm_dst, xf_f))
                
    # Index.theme
    with open(os.path.join(v_dir, "desktop", "theme", t_desktop_name, "index.theme"), "w") as f:
        f.write(f"[Desktop Entry]\nType=X-GNOME-Metatheme\nName={t_desktop_name}\nComment=Kali {cap} Dark with 2px Continuous Solid Borders\nEncoding=UTF-8\n\n[X-GNOME-Metatheme]\nGtkTheme={t_desktop_name}\nMetacityTheme={t_desktop_name}\nIconTheme={c_info['icon_theme']}\nXfwmTheme={t_desktop_name}\n")

    # Action & Menu SVGs
    # Lock
    lock_svg = lock_svg_template.format(circle=c_info["circle"])
    with open(os.path.join(v_dir, "icons", "apps", "scalable", "system-lock-screen.svg"), "w") as f:
        f.write(lock_svg)
    with open(os.path.join(v_dir, "icons", "apps", "scalable", "lock-screen.svg"), "w") as f:
        f.write(lock_svg)
        
    # Logout / Shutdown
    logout_svg = logout_svg_template.format(circle=c_info["circle"])
    for name in ["system-log-out.svg", "system-shutdown.svg", "xfsm-logout.svg", "xfsm-shutdown.svg", "gnome-logout.svg", "computer-log-out.svg", "org.xfce.panel.actions.svg"]:
        with open(os.path.join(v_dir, "icons", "apps", "scalable", name), "w") as f:
            f.write(logout_svg)
            
    # Menu Dragon
    menu_svg = re.sub(r"fill=\"#[0-9a-fA-F]+\"", "fill=\"" + c_info["hex"] + "\"", base_menu_svg)
    with open(os.path.join(v_dir, "icons", "apps", "scalable", "kali-menu.svg"), "w") as f:
        f.write(menu_svg)
    with open(os.path.join(v_dir, "icons", "apps", "scalable", "distributor-logo-kali.svg"), "w") as f:
        f.write(menu_svg)
    with open(os.path.join(v_dir, "icons", "apps", "scalable", "distributor-logo.svg"), "w") as f:
        f.write(menu_svg)

print("SUCCESS: Successfully built complete asset suites for all 15 color editions!")
