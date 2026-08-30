#!/usr/bin/env python3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VARIANTS_DIR = os.path.join(BASE_DIR, "variants")

ALL_COLORS = {
    "red": {"hex": "#ec0101", "primary": "#ff1744", "circle": "#d50000", "dark": "#8a0000", "glow": "rgba(255, 23, 68, 0.50)", "rgb": (255, 23, 68), "fg": "#ffffff"},
    "purple": {"hex": "#aa00ff", "primary": "#d500f9", "circle": "#aa00ff", "dark": "#6a0080", "glow": "rgba(213, 0, 249, 0.50)", "rgb": (213, 0, 249), "fg": "#ffffff"},
    "green": {"hex": "#00c853", "primary": "#00e676", "circle": "#00c853", "dark": "#006020", "glow": "rgba(0, 230, 118, 0.50)", "rgb": (0, 230, 118), "fg": "#121317"},
    "blue": {"hex": "#2979ff", "primary": "#00b0ff", "circle": "#2979ff", "dark": "#003c99", "glow": "rgba(0, 176, 255, 0.50)", "rgb": (0, 176, 255), "fg": "#ffffff"},
    "yellow": {"hex": "#ffc107", "primary": "#ffd600", "circle": "#ffd600", "dark": "#806000", "glow": "rgba(255, 214, 0, 0.50)", "rgb": (255, 214, 0), "fg": "#121317"},
    "orange": {"hex": "#ff5722", "primary": "#ff6d00", "circle": "#ff6d00", "dark": "#802b00", "glow": "rgba(255, 109, 0, 0.50)", "rgb": (255, 109, 0), "fg": "#ffffff"},
    "lime": {"hex": "#64dd17", "primary": "#76ff03", "circle": "#76ff03", "dark": "#33691e", "glow": "rgba(118, 255, 3, 0.50)", "rgb": (118, 255, 3), "fg": "#121317"},
    "pink": {"hex": "#f50057", "primary": "#ff4081", "circle": "#ff4081", "dark": "#880e4f", "glow": "rgba(255, 64, 129, 0.50)", "rgb": (255, 64, 129), "fg": "#ffffff"},
    "cyan": {"hex": "#00e5ff", "primary": "#18ffff", "circle": "#00e5ff", "dark": "#006080", "glow": "rgba(24, 255, 255, 0.50)", "rgb": (24, 255, 255), "fg": "#121317"},
    "white": {"hex": "#f5f5f5", "primary": "#ffffff", "circle": "#e0e0e0", "dark": "#424242", "glow": "rgba(255, 255, 255, 0.60)", "rgb": (255, 255, 255), "fg": "#121317"},
    "gold": {"hex": "#ffd700", "primary": "#ffab00", "circle": "#ffd700", "dark": "#7f5500", "glow": "rgba(255, 171, 0, 0.50)", "rgb": (255, 215, 0), "fg": "#121317"},
    "indigo": {"hex": "#3d5afe", "primary": "#536dfe", "circle": "#3d5afe", "dark": "#1a237e", "glow": "rgba(83, 109, 254, 0.50)", "rgb": (61, 90, 254), "fg": "#ffffff"},
    "mint": {"hex": "#00bfa5", "primary": "#64ffda", "circle": "#00bfa5", "dark": "#004d40", "glow": "rgba(100, 255, 218, 0.50)", "rgb": (0, 191, 165), "fg": "#121317"},
    "ruby": {"hex": "#c2185b", "primary": "#e91e63", "circle": "#ad1457", "dark": "#560027", "glow": "rgba(233, 30, 99, 0.50)", "rgb": (194, 24, 91), "fg": "#ffffff"},
    "silver": {"hex": "#cfd8dc", "primary": "#eceff1", "circle": "#b0bec5", "dark": "#37474f", "glow": "rgba(236, 239, 241, 0.50)", "rgb": (207, 216, 220), "fg": "#121317"}
}

epic_login_template = """/* ==========================================================================
   🐉 KALI DRAGON ULTRA-EPIC GLASSMORPHISM LOGIN & LOCK SUITE - {cap_color}
   ========================================================================== */

/* 1. LIGHTDM LOGIN GREETER WINDOW (Glowing Glassmorphic Card) */
#login_window,
#panel_window,
window#login_window,
window#panel_window {{
    background-color: rgba(12, 14, 20, 0.92);
    border: 2px solid {primary};
    border-radius: 14px;
    box-shadow: 0 0 35px {glow}, 0 0 6px {hex};
}}

#user_image,
image#user_image {{
    border: 2.5px solid {primary};
    border-radius: 50%;
    box-shadow: 0 0 20px {glow};
    background-color: #0c0004;
}}

#prompt_label,
#message_label,
#user_label,
label#prompt_label,
label#message_label,
label#user_label {{
    color: {primary};
    font-weight: bold;
    text-shadow: 0 0 10px {glow};
}}

#entry,
entry#entry,
#login_window entry,
#user_combobox entry {{
    background-color: rgba(0, 0, 0, 0.65);
    border: 1.5px solid rgba(255, 255, 255, 0.20);
    border-radius: 6px;
    color: #ffffff;
    caret-color: {primary};
    padding: 7px 12px;
}}

#entry:focus,
entry#entry:focus,
#login_window entry:focus {{
    border: 2px solid {primary};
    box-shadow: 0 0 18px {glow};
}}

/* 2. UNIVERSAL EPIC SUBMIT / LOGIN BUTTON (Neon Gradient + Outer Glow + High Contrast Text) */
#login_button,
button#login_button,
button.suggested-action,
.suggested-action,
button:default,
button.default,
#panel_window button.suggested-action,
#login_window button.suggested-action,
#login_window button.image-button,
#login_window button:default,
#login_window button:last-child {{
    background-image: linear-gradient(135deg, {primary} 0%, {circle} 50%, {dark} 100%);
    border: 1.5px solid {primary};
    border-radius: 6px;
    color: {fg} !important;
    font-weight: bold;
    padding: 7px 20px;
    box-shadow: 0 0 16px {glow};
}}

#login_button *,
button#login_button *,
button.suggested-action *,
.suggested-action *,
button:default *,
button.default *,
#login_window button.suggested-action *,
#login_window button:default * {{
    color: {fg} !important;
}}

#login_button:hover,
button#login_button:hover,
button.suggested-action:hover,
.suggested-action:hover,
button:default:hover,
button.default:hover,
#login_window button.suggested-action:hover,
#login_window button:default:hover,
#login_window button.image-button:hover,
#login_window button:last-child:hover {{
    background-image: linear-gradient(135deg, #ffffff 0%, {primary} 40%, {circle} 100%);
    box-shadow: 0 0 28px {glow};
    color: {fg} !important;
}}

/* 3. LIGHTDM TOP PANEL & INDICATORS */
#panel_window menubar,
#panel_window menuitem {{
    color: #ffffff;
    font-weight: bold;
}}

#panel_window menuitem:hover {{
    background-color: {primary};
    color: {fg} !important;
    border-radius: 4px;
}}

#panel_window menuitem:hover * {{
    color: {fg} !important;
}}

/* 4. XFCE4 SCREENSAVER LOCK DIALOG (Lock / Suspend Wake-up) */
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
    background-color: rgba(12, 14, 20, 0.94);
    border: 2px solid {primary};
    border-radius: 14px;
    box-shadow: 0 0 35px {glow}, 0 0 6px {hex};
    padding: 20px;
}}

#auth-face-image {{
    border: 2.5px solid {primary};
    border-radius: 50%;
    box-shadow: 0 0 22px {glow};
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
    text-shadow: 0 0 12px {glow};
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
    border: 1.5px solid rgba(255, 255, 255, 0.20);
    border-radius: 6px;
    color: #ffffff;
    caret-color: {primary};
    padding: 7px 12px;
}}

#auth-prompt-entry:focus,
entry#auth-prompt-entry:focus {{
    border: 2px solid {primary};
    box-shadow: 0 0 18px {glow};
}}

#auth-unlock-button,
#auth-action-area button.suggested-action,
#auth-action-area button.primary {{
    background-image: linear-gradient(135deg, {primary} 0%, {circle} 50%, {dark} 100%);
    border: 1.5px solid {primary};
    border-radius: 6px;
    color: {fg} !important;
    font-weight: bold;
    padding: 7px 20px;
    box-shadow: 0 0 16px {glow};
}}

#auth-unlock-button *,
#auth-action-area button.suggested-action * {{
    color: {fg} !important;
}}

#auth-unlock-button:hover,
#auth-action-area button.suggested-action:hover {{
    background-image: linear-gradient(135deg, #ffffff 0%, {primary} 40%, {circle} 100%);
    box-shadow: 0 0 28px {glow};
    color: {fg} !important;
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
    background-color: rgba({r}, {g}, {b}, 0.35);
    border: 2px solid {primary};
    box-shadow: 0 0 16px {glow};
    color: #ffffff;
}}

/* 5. XFCE4 SESSION LOGOUT DIALOG */
window#logout-dialog,
dialog#logout-dialog,
.xfce4-session-logout,
window.xfce4-session-logout {{
    background-color: rgba(12, 14, 20, 0.95);
    border: 2px solid {primary};
    border-radius: 14px;
    box-shadow: 0 0 35px {glow}, 0 0 6px {hex};
    padding: 16px;
}}

window#logout-dialog label,
.xfce4-session-logout label {{
    color: #ffffff;
    font-weight: bold;
    text-shadow: 0 0 8px {glow};
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
    box-shadow: 0 0 20px {glow};
    color: {fg} !important;
}}

window#logout-dialog button:hover *,
.xfce4-session-logout button:hover * {{
    color: {fg} !important;
}}
"""

for c_key, c_info in ALL_COLORS.items():
    cap = c_key.capitalize()
    t_login_name = f"Kali-{cap}-Dragon-Login"
    v_dir = os.path.join(VARIANTS_DIR, c_key)
    
    t_dir = os.path.join(v_dir, "login", "theme", t_login_name, "gtk-3.0")
    os.makedirs(t_dir, exist_ok=True)
    
    r, g, b = c_info["rgb"]
    content = epic_login_template.format(
        cap_color=cap,
        hex=c_info["hex"],
        primary=c_info["primary"],
        circle=c_info["circle"],
        dark=c_info["dark"],
        glow=c_info["glow"],
        r=r, g=g, b=b,
        fg=c_info["fg"]
    )
    
    with open(os.path.join(t_dir, "gtk.css"), "w") as f:
        f.write(content)

print("SUCCESS: Restored ultra-epic glassmorphic glows, gradients, and frames across all 15 login themes!")
