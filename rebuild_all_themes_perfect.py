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

# 1. REBUILD LOGIN & SCREENSAVER THEMES
screensaver_universal_css = """
/* ==========================================================================
   🐉 UNIVERSAL SCREENSAVER / SUSPEND WAKEUP GLASSMORPHIC DIALOG - {cap_color}
   ========================================================================== */

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
dialog.screensaver-dialog > box,
.screensaver-dialog #login_window,
.screensaver-dialog #login_box,
.screensaver-dialog #content_frame {{
    background-color: rgba(12, 14, 20, 0.94) !important;
    border: 2px solid {primary} !important;
    border-radius: 14px !important;
    box-shadow: 0 0 35px {glow}, 0 0 6px {hex} !important;
    padding: 16px !important;
}}

#auth-face-image,
#user_image_border image,
.screensaver-dialog #user_image {{
    border: 2.5px solid {primary} !important;
    border-radius: 50% !important;
    box-shadow: 0 0 22px {glow} !important;
    background-color: #0c0004 !important;
}}

/* PERMANENTLY REMOVE THE THICK WHITE RECTANGLE ON GTKINFOBAR / GREETER_INFOBAR */
#greeter_infobar,
infobar#greeter_infobar,
infobar,
.infobar,
infobar.info,
infobar.warning,
infobar.error,
infobar.question,
#infobar-content_area,
#auth-prompt-box,
#auth-status-label,
label#auth-status-label,
#status-message-label,
label#status-message-label,
#auth-prompt-label,
label#auth-prompt-label,
#auth-capslock-label,
label#auth-capslock-label,
#auth-realname-label,
#auth-hostname-label,
#auth-date-time-label,
infobar:backdrop > revealer > box,
infobar > revealer > box,
infobar.info > revealer > box,
infobar.info:backdrop > revealer > box {{
    background: transparent !important;
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
}}

#auth-prompt-label,
label#auth-prompt-label {{
    color: #ffffff !important;
    font-weight: bold !important;
    font-size: 11pt !important;
    text-shadow: 0 0 6px {glow} !important;
}}

#auth-status-label,
label#auth-status-label,
#status-message-label,
label#status-message-label {{
    color: {primary} !important;
    font-weight: bold !important;
    font-size: 11pt !important;
    text-shadow: 0 0 12px {glow} !important;
}}

#auth-capslock-label,
label#auth-capslock-label {{
    color: #ffd600 !important;
    font-weight: bold !important;
}}

#auth-realname-label,
#auth-hostname-label,
#auth-date-time-label {{
    color: #ffffff !important;
    font-weight: bold !important;
    text-shadow: 0 0 8px {glow} !important;
}}

#auth-prompt-entry,
entry#auth-prompt-entry,
#prompt_entry,
.screensaver-dialog entry {{
    background-color: rgba(0, 0, 0, 0.70) !important;
    border: 1.5px solid rgba(255, 255, 255, 0.20) !important;
    border-radius: 6px !important;
    color: #ffffff !important;
    caret-color: {primary} !important;
    padding: 7px 12px !important;
}}

#auth-prompt-entry:focus,
entry#auth-prompt-entry:focus,
#prompt_entry:focus,
.screensaver-dialog entry:focus {{
    border: 2px solid {primary} !important;
    box-shadow: 0 0 18px {glow} !important;
}}

/* SCREENSAVER UNLOCK / CONFIRM BUTTON (Force High Contrast Text) */
#auth-unlock-button,
button#auth-unlock-button,
#auth-action-area button.suggested-action,
#auth-action-area button.primary,
.screensaver-dialog button.suggested-action,
.screensaver-dialog button:default,
.screensaver-dialog button:last-child {{
    background-color: {primary} !important;
    background-image: linear-gradient(135deg, {primary} 0%, {circle} 50%, {dark} 100%) !important;
    border: 1.5px solid {primary} !important;
    border-radius: 6px !important;
    color: {fg} !important;
    font-weight: bold !important;
    padding: 7px 20px !important;
    box-shadow: 0 0 16px {glow} !important;
}}

#auth-unlock-button label,
button#auth-unlock-button label,
#auth-action-area button.suggested-action label,
#auth-action-area button.primary label,
.screensaver-dialog button.suggested-action label,
.screensaver-dialog button:default label,
.screensaver-dialog button:last-child label,
#auth-unlock-button *,
button#auth-unlock-button *,
#auth-action-area button.suggested-action *,
.screensaver-dialog button.suggested-action * {{
    color: {fg} !important;
    font-weight: bold !important;
}}

#auth-unlock-button:hover,
button#auth-unlock-button:hover,
#auth-action-area button.suggested-action:hover,
.screensaver-dialog button.suggested-action:hover,
.screensaver-dialog button:default:hover {{
    background-color: {primary} !important;
    background-image: linear-gradient(135deg, #ffffff 0%, {primary} 40%, {circle} 100%) !important;
    box-shadow: 0 0 28px {glow} !important;
    color: {fg} !important;
}}

#auth-unlock-button:hover label,
button#auth-unlock-button:hover label,
#auth-unlock-button:hover *,
button#auth-unlock-button:hover * {{
    color: {fg} !important;
}}

#auth-cancel-button,
#auth-logout-button,
#auth-switch-button,
.screensaver-dialog button:not(.suggested-action):not(#auth-unlock-button) {{
    background-color: rgba(255, 255, 255, 0.08) !important;
    border: 1.5px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 6px !important;
    color: #ffffff !important;
    padding: 6px 14px !important;
}}

#auth-cancel-button label,
#auth-logout-button label,
#auth-switch-button label,
.screensaver-dialog button:not(.suggested-action):not(#auth-unlock-button) label {{
    color: #ffffff !important;
}}

#auth-cancel-button:hover,
#auth-logout-button:hover,
#auth-switch-button:hover,
.screensaver-dialog button:not(.suggested-action):not(#auth-unlock-button):hover {{
    background-color: rgba({r}, {g}, {b}, 0.35) !important;
    border: 2px solid {primary} !important;
    box-shadow: 0 0 16px {glow} !important;
    color: {fg} !important;
}}

#auth-cancel-button:hover label,
#auth-logout-button:hover label,
#auth-switch-button:hover label,
.screensaver-dialog button:not(.suggested-action):not(#auth-unlock-button):hover label {{
    color: {fg} !important;
}}
"""

login_template = """/* ==========================================================================
   🐉 KALI DRAGON ULTRA-EPIC GLASSMORPHISM LOGIN & LOCK SUITE - {cap_color}
   ========================================================================== */

@define-color theme_selected_bg_color {primary};
@define-color theme_selected_fg_color {fg};
@define-color selection_color {primary};
@define-color selected_bg_color {primary};
@define-color selected_fg_color {fg};

/* 1. LIGHTDM LOGIN GREETER WINDOW */
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
    background: transparent;
    background-color: transparent;
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

/* 2. UNIVERSAL EPIC SUBMIT / LOGIN BUTTON */
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
    background-image: linear-gradient(135deg, {primary} 0%, {circle} 50%, {dark} 100%) !important;
    border: 1.5px solid {primary} !important;
    border-radius: 6px !important;
    color: {fg} !important;
    font-weight: bold !important;
    padding: 7px 20px !important;
    box-shadow: 0 0 16px {glow} !important;
}}

#login_button label,
button#login_button label,
button.suggested-action label,
.suggested-action label,
button:default label,
button.default label,
#login_window button.suggested-action label,
#login_window button:default label,
#login_button *,
button#login_button *,
button.suggested-action *,
.suggested-action *,
button:default *,
button.default * {{
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
    background-image: linear-gradient(135deg, #ffffff 0%, {primary} 40%, {circle} 100%) !important;
    box-shadow: 0 0 28px {glow} !important;
    color: {fg} !important;
}}

#login_button:hover label,
button#login_button:hover label,
#login_button:hover * {{
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

#panel_window menuitem:hover label,
#panel_window menuitem:hover * {{
    color: {fg} !important;
}}

""" + screensaver_universal_css + """
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

window#logout-dialog button label,
.xfce4-session-logout button label {{
    color: #ffffff;
}}

window#logout-dialog button:hover,
.xfce4-session-logout button:hover {{
    background-color: {primary} !important;
    border: 2px solid {primary} !important;
    box-shadow: 0 0 20px {glow} !important;
    color: {fg} !important;
}}

window#logout-dialog button:hover label,
.xfce4-session-logout button:hover label,
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
    content = login_template.format(
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

# 2. REBUILD DESKTOP THEMES (INCLUDING SCREENSAVER CSS FOR RESUME/SUSPEND SESSIONS)
with open("/usr/share/themes/Kali-Dark/gtk-3.0/gtk.css", "r") as f:
    base_gtk3 = f.read()

with open("/usr/share/themes/Kali-Dark/gtk-4.0/gtk.css", "r") as f:
    base_gtk4 = f.read()

desktop_addon_template = """
/* ==========================================================================
   🐉 KALI DRAGON SUITE - HIGH-CONTRAST SELECTION & SEARCH AUTOCOMPLETE
   ========================================================================== */

@define-color theme_selected_bg_color {primary};
@define-color theme_selected_fg_color {fg};
@define-color selection_color {primary};
@define-color selected_bg_color {primary};
@define-color selected_fg_color {fg};

/* 1. TEXTBOX SELECTION & INLINE AUTOCOMPLETE COMPLETIONS (Search Bar, URL Bar, Inputs) */
entry,
entry:focus,
searchbar entry,
.search-bar entry {{
    color: #ffffff;
}}

entry selection,
entry:focus selection,
entry:selected,
entry:focus:selected,
textview text selection,
textview text:selected,
.view text selection,
.view text:selected,
selection,
*:selected {{
    background-color: {primary} !important;
    color: {fg} !important;
}}

entry selection *,
entry:focus selection *,
entry:selected *,
textview text selection *,
textview text:selected *,
.view text selection *,
.view text:selected *,
selection *,
*:selected * {{
    color: {fg} !important;
}}

/* 2. AUTOCOMPLETE / SEARCH SUGGESTION DROPDOWNS (Below Search Bar) */
popover,
popover.background,
.popover,
.entry-completion,
entry completion,
.autocomplete-popover,
treeview.completion,
#whiskermenu-window treeview,
appfinder treeview {{
    background-color: #1e2029 !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    color: #eeeeec !important;
}}

popover label,
.entry-completion label,
treeview.completion cell,
treeview.completion label {{
    color: #eeeeec !important;
}}

/* Active Search Suggestion Item */
treeview.completion:selected,
treeview.completion:hover,
.entry-completion:selected,
.entry-completion:hover,
popover list row:selected,
popover list row:hover,
popover menuitem:hover,
popover menuitem:focus,
#whiskermenu-window treeview:selected,
appfinder treeview:selected {{
    background-color: {primary} !important;
    color: {fg} !important;
}}

treeview.completion:selected *,
treeview.completion:hover *,
.entry-completion:selected *,
.entry-completion:hover *,
popover list row:selected *,
popover list row:hover *,
popover menuitem:hover *,
popover menuitem:focus *,
#whiskermenu-window treeview:selected *,
appfinder treeview:selected * {{
    color: {fg} !important;
}}

/* 3. PRIMARY & SUGGESTED ACTION BUTTONS (OK / Confirm / Submit) */
button.suggested-action,
button.primary,
button:default,
button.destructive-action {{
    background-color: {primary} !important;
    background-image: none !important;
    border: 1px solid {primary} !important;
    color: {fg} !important;
    font-weight: bold !important;
    box-shadow: 0 0 10px {glow} !important;
}}

button.suggested-action label,
button.primary label,
button:default label,
button.suggested-action *,
button.primary *,
button:default * {{
    color: {fg} !important;
}}

button.suggested-action:hover,
button.primary:hover,
button:default:hover {{
    background-color: {primary} !important;
    color: {fg} !important;
    box-shadow: 0 0 18px {glow} !important;
}}

button.suggested-action:hover label,
button.primary:hover label,
button:default:hover label,
button.suggested-action:hover *,
button.primary:hover * {{
    color: {fg} !important;
}}

/* 4. LAPTOP OSD NOTIFICATIONS (VOLUME, BRIGHTNESS & NOTIFY-OSD) */
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

/* 5. SOLID DARK MENUS & CONTEXT POPUPS */
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
    color: {fg} !important;
    border-radius: 4px;
}}

menu menuitem:hover label,
menu menuitem:hover * {{
    color: {fg} !important;
}}

""" + screensaver_universal_css + """

/* 6. SOLID DARK LOGOUT / POWER OFF DIALOG */
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
    background-color: {primary};
    border: 2px solid {primary};
    box-shadow: 0 0 18px {glow};
    color: {fg} !important;
}}

window#logout-dialog button:hover label,
.xfce4-session-logout button:hover label,
window#logout-dialog button:hover *,
.xfce4-session-logout button:hover * {{
    color: {fg} !important;
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
    fg = c_info["fg"]
    
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
    
    # If foreground is dark (#121317), replace the hardcoded "color: #ffffff;" on selection lines with dark fg
    if fg == "#121317":
        themed_gtk3 = themed_gtk3.replace("entry selection, modelbutton.flat:selected,\n  .menuitem.button.flat:selected, spinbutton:not(.vertical) selection, treeview.view:selected:focus, treeview.view:selected, row:selected, calendar:selected {\n    color: #ffffff;", f"entry selection, modelbutton.flat:selected,\n  .menuitem.button.flat:selected, spinbutton:not(.vertical) selection, treeview.view:selected:focus, treeview.view:selected, row:selected, calendar:selected {{\n    color: {fg};")
        themed_gtk4 = themed_gtk4.replace("entry selection, modelbutton.flat:selected,\n  .menuitem.button.flat:selected, spinbutton:not(.vertical) selection, treeview.view:selected:focus, treeview.view:selected, row:selected, calendar:selected {\n    color: #ffffff;", f"entry selection, modelbutton.flat:selected,\n  .menuitem.button.flat:selected, spinbutton:not(.vertical) selection, treeview.view:selected:focus, treeview.view:selected, row:selected, calendar:selected {{\n    color: {fg};")

    addon = desktop_addon_template.format(
        cap_color=cap,
        hex=c_info["hex"],
        primary=c_info["primary"],
        circle=c_info["circle"],
        dark=c_info["dark"],
        glow=c_info["glow"],
        r=r, g=g, b=b,
        fg=c_info["fg"]
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

print("SUCCESS: Injected screensaver and suspend wakeup rules directly into desktop themes & login themes!")
