#!/usr/bin/env python3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VARIANTS_DIR = os.path.join(BASE_DIR, "variants")

ALL_COLORS = {
    "red": {"hex": "#ec0101", "primary": "#ff1744", "dark": "#8a0000", "glow": "rgba(255, 23, 68, 0.45)", "rgb": (255, 23, 68)},
    "purple": {"hex": "#aa00ff", "primary": "#d500f9", "dark": "#6a0080", "glow": "rgba(213, 0, 249, 0.45)", "rgb": (213, 0, 249)},
    "green": {"hex": "#00c853", "primary": "#00e676", "dark": "#006020", "glow": "rgba(0, 230, 118, 0.45)", "rgb": (0, 230, 118)},
    "blue": {"hex": "#2979ff", "primary": "#00b0ff", "dark": "#003c99", "glow": "rgba(0, 176, 255, 0.45)", "rgb": (0, 176, 255)},
    "yellow": {"hex": "#ffc107", "primary": "#ffd600", "dark": "#806000", "glow": "rgba(255, 214, 0, 0.45)", "rgb": (255, 214, 0)},
    "orange": {"hex": "#ff5722", "primary": "#ff6d00", "dark": "#802b00", "glow": "rgba(255, 109, 0, 0.45)", "rgb": (255, 109, 0)},
    "lime": {"hex": "#64dd17", "primary": "#76ff03", "dark": "#33691e", "glow": "rgba(118, 255, 3, 0.45)", "rgb": (118, 255, 3)},
    "pink": {"hex": "#f50057", "primary": "#ff4081", "dark": "#880e4f", "glow": "rgba(255, 64, 129, 0.45)", "rgb": (255, 64, 129)},
    "cyan": {"hex": "#00e5ff", "primary": "#18ffff", "dark": "#006080", "glow": "rgba(24, 255, 255, 0.45)", "rgb": (0, 229, 255)},
    "white": {"hex": "#f5f5f5", "primary": "#ffffff", "dark": "#424242", "glow": "rgba(255, 255, 255, 0.50)", "rgb": (245, 245, 245)},
    "gold": {"hex": "#ffd700", "primary": "#ffab00", "dark": "#7f5500", "glow": "rgba(255, 171, 0, 0.45)", "rgb": (255, 215, 0)},
    "indigo": {"hex": "#3d5afe", "primary": "#536dfe", "dark": "#1a237e", "glow": "rgba(83, 109, 254, 0.45)", "rgb": (61, 90, 254)},
    "mint": {"hex": "#00bfa5", "primary": "#64ffda", "dark": "#004d40", "glow": "rgba(100, 255, 218, 0.45)", "rgb": (0, 191, 165)},
    "ruby": {"hex": "#c2185b", "primary": "#e91e63", "dark": "#560027", "glow": "rgba(233, 30, 99, 0.45)", "rgb": (194, 24, 91)},
    "silver": {"hex": "#cfd8dc", "primary": "#eceff1", "dark": "#37474f", "glow": "rgba(236, 239, 241, 0.45)", "rgb": (207, 216, 220)}
}

with open("/usr/share/themes/Kali-Dark/gtk-3.0/gtk.css", "r") as f:
    base_gtk3 = f.read()

with open("/usr/share/themes/Kali-Dark/gtk-4.0/gtk.css", "r") as f:
    base_gtk4 = f.read()

# Addon ONLY for solid notifications (volume/brightness) and solid logout dialog without touching native window selection
osd_dialog_addon = """
/* ==========================================================================
   🐉 KALI DRAGON SUITE - SOLID NOTIFICATIONS & LOGOUT DIALOG
   ========================================================================== */

/* LAPTOP OSD NOTIFICATIONS (VOLUME, BRIGHTNESS & NOTIFY-OSD) */
#XfceNotifyWindow,
XfceNotifyWindow,
.xfce4-notifyd,
#xfce-notifyd-container,
.osd,
osd {{
    background-color: #1e2029;
    border: 2px solid {primary};
    border-radius: 10px;
    box-shadow: 0 0 16px {glow};
    color: #ffffff;
    padding: 10px 14px;
}}

#XfceNotifyWindow label,
.xfce4-notifyd label,
.osd label {{
    color: #ffffff;
    font-weight: bold;
    text-shadow: 0 0 6px {glow};
}}

#XfceNotifyWindow progressbar,
#XfceNotifyWindow levelbar,
.osd progressbar,
.osd levelbar {{
    min-height: 8px;
    background-color: rgba(255, 255, 255, 0.15);
    border-radius: 4px;
}}

#XfceNotifyWindow progressbar progress,
#XfceNotifyWindow levelbar block.filled,
.osd progressbar progress,
.osd levelbar block.filled {{
    background-color: {primary};
    border-radius: 4px;
    border: none;
}}

/* SOLID DARK MENUS & CONTEXT POPUPS */
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

/* SOLID DARK LOGOUT / POWER OFF DIALOG */
window#logout-dialog,
dialog#logout-dialog,
.xfce4-session-logout,
window.xfce4-session-logout {{
    background-color: #1a1c23;
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
    background-color: rgba(255, 255, 255, 0.08);
    border: 1.5px solid rgba(255, 255, 255, 0.18);
    border-radius: 8px;
    color: #ffffff;
    font-weight: bold;
    padding: 8px 14px;
    margin: 4px;
}}

window#logout-dialog button:hover,
.xfce4-session-logout button:hover {{
    background-color: rgba({r}, {g}, {b}, 0.35);
    border: 2px solid {primary};
    box-shadow: 0 0 16px {glow};
    color: #ffffff;
}}
"""

for c_key, c_info in ALL_COLORS.items():
    cap = c_key.capitalize()
    t_desktop_name = f"Kali-{cap}-Dark-Borders"
    v_dir = os.path.join(VARIANTS_DIR, c_key)
    
    t_dir = os.path.join(v_dir, "desktop", "theme", t_desktop_name)
    gtk3_dir = os.path.join(t_dir, "gtk-3.0")
    gtk4_dir = os.path.join(t_dir, "gtk-4.0")
    os.makedirs(gtk3_dir, exist_ok=True)
    os.makedirs(gtk4_dir, exist_ok=True)
    
    r, g, b = c_info["rgb"]
    
    # Pure clean native color replacement across the whole stylesheet
    themed_gtk3 = (
        base_gtk3
        .replace("#2777ff", c_info["primary"])
        .replace("#005af3", c_info["hex"])
        .replace("#0047c0", c_info["dark"])
        .replace("rgba(0, 90, 243, 0.2)", f"rgba({r}, {g}, {b}, 0.22)")
        .replace("rgba(0, 90, 243, 0.75)", f"rgba({r}, {g}, {b}, 0.75)")
    )
    
    themed_gtk4 = (
        base_gtk4
        .replace("#2777ff", c_info["primary"])
        .replace("#005af3", c_info["hex"])
        .replace("#0047c0", c_info["dark"])
        .replace("rgba(0, 90, 243, 0.2)", f"rgba({r}, {g}, {b}, 0.22)")
        .replace("rgba(0, 90, 243, 0.75)", f"rgba({r}, {g}, {b}, 0.75)")
    )
    
    addon = osd_dialog_addon.format(
        cap_color=cap,
        hex=c_info["hex"],
        primary=c_info["primary"],
        glow=c_info["glow"],
        r=r, g=g, b=b
    )
    
    full_3 = themed_gtk3 + "\n" + addon
    full_4 = themed_gtk4 + "\n" + addon
    
    with open(os.path.join(gtk3_dir, "gtk.css"), "w") as f:
        f.write(full_3)
    with open(os.path.join(gtk3_dir, "gtk-dark.css"), "w") as f:
        f.write(full_3)
        
    with open(os.path.join(gtk4_dir, "gtk.css"), "w") as f:
        f.write(full_4)
    with open(os.path.join(gtk4_dir, "gtk-dark.css"), "w") as f:
        f.write(full_4)
        
    os.makedirs(os.path.join(v_dir, "desktop", "gtk-css"), exist_ok=True)
    with open(os.path.join(v_dir, "desktop", "gtk-css", "gtk-3.0.css"), "w") as f:
        f.write(addon)
    with open(os.path.join(v_dir, "desktop", "gtk-css", "gtk-4.0.css"), "w") as f:
        f.write(addon)

print("SUCCESS: Native zero-artifact rubberband selection restored for all 15 colors!")
