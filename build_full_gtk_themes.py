#!/usr/bin/env python3
import os, sys, shutil, glob, re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VARIANTS_DIR = os.path.join(BASE_DIR, "variants")

ALL_COLORS = {
    "red": {"hex": "#ec0101", "primary": "#ff1744", "circle": "#d50000", "dark": "#8a0000", "glow": "rgba(255, 23, 68, 0.45)", "rgb": (255, 23, 68)},
    "purple": {"hex": "#aa00ff", "primary": "#d500f9", "circle": "#aa00ff", "dark": "#6a0080", "glow": "rgba(213, 0, 249, 0.45)", "rgb": (213, 0, 249)},
    "green": {"hex": "#00c853", "primary": "#00e676", "circle": "#00c853", "dark": "#006020", "glow": "rgba(0, 230, 118, 0.45)", "rgb": (0, 230, 118)},
    "blue": {"hex": "#2979ff", "primary": "#00b0ff", "circle": "#2979ff", "dark": "#003c99", "glow": "rgba(0, 176, 255, 0.45)", "rgb": (0, 176, 255)},
    "yellow": {"hex": "#ffc107", "primary": "#ffd600", "circle": "#ffd600", "dark": "#806000", "glow": "rgba(255, 214, 0, 0.45)", "rgb": (255, 214, 0)},
    "orange": {"hex": "#ff5722", "primary": "#ff6d00", "circle": "#ff6d00", "dark": "#802b00", "glow": "rgba(255, 109, 0, 0.45)", "rgb": (255, 109, 0)},
    "lime": {"hex": "#64dd17", "primary": "#76ff03", "circle": "#76ff03", "dark": "#33691e", "glow": "rgba(118, 255, 3, 0.45)", "rgb": (118, 255, 3)},
    "pink": {"hex": "#f50057", "primary": "#ff4081", "circle": "#ff4081", "dark": "#880e4f", "glow": "rgba(255, 64, 129, 0.45)", "rgb": (255, 64, 129)},
    "cyan": {"hex": "#00e5ff", "primary": "#18ffff", "circle": "#00e5ff", "dark": "#006080", "glow": "rgba(24, 255, 255, 0.45)", "rgb": (0, 229, 255)},
    "white": {"hex": "#f5f5f5", "primary": "#ffffff", "circle": "#e0e0e0", "dark": "#424242", "glow": "rgba(255, 255, 255, 0.50)", "rgb": (245, 245, 245)},
    "gold": {"hex": "#ffd700", "primary": "#ffab00", "circle": "#ffd700", "dark": "#7f5500", "glow": "rgba(255, 171, 0, 0.45)", "rgb": (255, 215, 0)},
    "indigo": {"hex": "#3d5afe", "primary": "#536dfe", "circle": "#3d5afe", "dark": "#1a237e", "glow": "rgba(83, 109, 254, 0.45)", "rgb": (61, 90, 254)},
    "mint": {"hex": "#00bfa5", "primary": "#64ffda", "circle": "#00bfa5", "dark": "#004d40", "glow": "rgba(100, 255, 218, 0.45)", "rgb": (0, 191, 165)},
    "ruby": {"hex": "#c2185b", "primary": "#e91e63", "circle": "#ad1457", "dark": "#560027", "glow": "rgba(233, 30, 99, 0.45)", "rgb": (194, 24, 91)},
    "silver": {"hex": "#cfd8dc", "primary": "#eceff1", "circle": "#b0bec5", "dark": "#37474f", "glow": "rgba(236, 239, 241, 0.45)", "rgb": (207, 216, 220)}
}

with open("/usr/share/themes/Kali-Dark/gtk-3.0/gtk.css", "r") as f:
    base_gtk3_css = f.read()

with open("/usr/share/themes/Kali-Dark/gtk-4.0/gtk.css", "r") as f:
    base_gtk4_css = f.read()

suite_addon_template = """
/* ==========================================================================
   🐉 KALI DRAGON SUITE - {cap_color} EXTENSIONS & ENHANCEMENTS
   ========================================================================== */

@define-color theme_selected_bg_color {primary};
@define-color theme_selected_fg_color #ffffff;
@define-color selection_color {primary};

/* 1. SOLID 2PX CONTINUOUS WINDOW BORDERS */
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

/* 2. LAPTOP OSD VOLUME, BRIGHTNESS & NOTIFICATIONS */
.osd,
osd,
XfceNotifyWindow,
#XfceNotifyWindow {{
    background-color: rgba(20, 22, 28, 0.95);
    border: 2px solid {primary};
    border-radius: 10px;
    box-shadow: 0 0 16px {glow};
    color: #ffffff;
}}

.osd progressbar progress,
osd progressbar progress,
.osd levelbar block.filled {{
    background-color: {primary};
    border: none;
}}

.osd label,
osd label {{
    color: #ffffff;
    font-weight: bold;
}}

/* 3. MENUS & CONTEXT POPUPS (GUARANTEED OPAQUE DARK BACKGROUND) */
menu,
.menu,
.context-menu,
popover.background {{
    background-color: #1e2029;
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 6px;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.7);
    color: #ffffff;
    padding: 4px;
}}

menu menuitem,
.menu menuitem {{
    padding: 5px 12px;
    color: #eeeeec;
}}

menu menuitem:hover,
.menu menuitem:hover {{
    background-color: {primary};
    color: #ffffff;
    border-radius: 4px;
}}

menu separator,
.menu separator {{
    background-color: rgba(255, 255, 255, 0.12);
    min-height: 1px;
    margin: 4px 0;
}}

/* 4. TOOLTIPS */
tooltip,
tooltip.background,
.tooltip {{
    background-color: rgba(20, 22, 28, 0.95);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 5px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
    color: #ffffff;
}}

/* 5. LIGHTDM LOGIN GREETER CARD */
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

/* 6. XFCE4 SCREENSAVER LOCK DIALOG */
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

/* 7. XFCE4 SESSION LOGOUT DIALOG */
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

for c_key, c_info in ALL_COLORS.items():
    cap = c_key.capitalize()
    t_login_name = f"Kali-{cap}-Dragon-Login"
    t_desktop_name = f"Kali-{cap}-Dark-Borders"
    v_dir = os.path.join(VARIANTS_DIR, c_key)
    
    t_dir = os.path.join(v_dir, "desktop", "theme", t_desktop_name)
    gtk3_dir = os.path.join(t_dir, "gtk-3.0")
    gtk4_dir = os.path.join(t_dir, "gtk-4.0")
    os.makedirs(gtk3_dir, exist_ok=True)
    os.makedirs(gtk4_dir, exist_ok=True)
    
    # 1. Copy full GTK assets directory
    assets_src = "/usr/share/themes/Kali-Dark/gtk-3.0/assets"
    assets_dst = os.path.join(gtk3_dir, "assets")
    if os.path.exists(assets_dst):
        shutil.rmtree(assets_dst)
    shutil.copytree(assets_src, assets_dst)
    
    # Symlink in gtk-4.0
    gtk4_assets = os.path.join(gtk4_dir, "assets")
    if os.path.exists(gtk4_assets) or os.path.islink(gtk4_assets):
        os.remove(gtk4_assets)
    os.symlink("../gtk-3.0/assets", gtk4_assets)
    
    # 2. Build full GTK-3 stylesheet
    # Replace blue highlights (#2777ff / #06a284) in base theme with target color
    themed_gtk3 = base_gtk3_css.replace("#2777ff", c_info["hex"]).replace("#06a284", c_info["hex"])
    themed_gtk4 = base_gtk4_css.replace("#2777ff", c_info["hex"]).replace("#06a284", c_info["hex"])
    
    r, g, b = c_info["rgb"]
    suite_addon = suite_addon_template.format(
        cap_color=cap,
        hex=c_info["hex"],
        primary=c_info["primary"],
        core=c_info["circle"],
        dark=c_info["dark"],
        glow=c_info["glow"],
        r=r, g=g, b=b
    )
    
    full_gtk3 = themed_gtk3 + "\n" + suite_addon
    full_gtk4 = themed_gtk4 + "\n" + suite_addon
    
    with open(os.path.join(gtk3_dir, "gtk.css"), "w") as f:
        f.write(full_gtk3)
    with open(os.path.join(gtk3_dir, "gtk-dark.css"), "w") as f:
        f.write(full_gtk3)
        
    with open(os.path.join(gtk4_dir, "gtk.css"), "w") as f:
        f.write(full_gtk4)
    with open(os.path.join(gtk4_dir, "gtk-dark.css"), "w") as f:
        f.write(full_gtk4)
        
    # Also save to desktop/gtk-css for user config overrides
    with open(os.path.join(v_dir, "desktop", "gtk-css", "gtk-3.0.css"), "w") as f:
        f.write(suite_addon)
    with open(os.path.join(v_dir, "desktop", "gtk-css", "gtk-4.0.css"), "w") as f:
        f.write(suite_addon)

print("SUCCESS: Generated complete 7,000+ line GTK3/GTK4 dark stylesheets with full assets, OSD volume/brightness, and menu styling for all 15 colors!")
