import os, shutil

BASE_DIR = "/home/gr/Escritorio/Kali-Red-Dragon-Suite"
VARIANTS_DIR = os.path.join(BASE_DIR, "variants")

COLORS = {
    "red": {"hex": "#ec0101", "glow": "#ff1744", "base_theme": "Kali-Red-Dark", "icon_theme": "Flat-Remix-Red-Dark"},
    "purple": {"hex": "#aa00ff", "glow": "#d500f9", "base_theme": "Kali-Purple-Dark", "icon_theme": "Flat-Remix-Purple-Dark"},
    "green": {"hex": "#00c853", "glow": "#00e676", "base_theme": "Kali-Green-Dark", "icon_theme": "Flat-Remix-Green-Dark"},
    "blue": {"hex": "#2979ff", "glow": "#00b0ff", "base_theme": "Kali-Dark", "icon_theme": "Flat-Remix-Blue-Dark"},
    "yellow": {"hex": "#ffc107", "glow": "#ffd600", "base_theme": "Kali-Yellow-Dark", "icon_theme": "Flat-Remix-Yellow-Dark"},
    "orange": {"hex": "#ff5722", "glow": "#ff6d00", "base_theme": "Kali-Orange-Dark", "icon_theme": "Flat-Remix-Orange-Dark"},
    "pink": {"hex": "#f50057", "glow": "#ff4081", "base_theme": "Kali-Pink-Dark", "icon_theme": "Flat-Remix-Pink-Dark"},
    "lime": {"hex": "#64dd17", "glow": "#76ff03", "base_theme": "Kali-Green-Dark", "icon_theme": "Flat-Remix-Green-Dark"}
}

csd_snippet_tpl = """
/* Continuous 2px Solid Border for Client-Side Decorated Windows */
window.ssd decoration,
window.csd decoration,
window.csd,
decoration {{
    border: 2px solid {hex} !important;
    border-radius: 6px 6px 0px 0px !important;
    box-shadow: 0 0 10px {glow}40, 0 0 2px {hex} !important;
}}

/* Headerbar border matching */
headerbar,
.titlebar {{
    border-top: 2px solid {hex} !important;
    border-left: 2px solid {hex} !important;
    border-right: 2px solid {hex} !important;
}}
"""

for c_key, c_val in COLORS.items():
    cap = c_key.capitalize()
    t_name = f"Kali-{cap}-Dark-Borders"
    v_theme_dir = os.path.join(VARIANTS_DIR, c_key, "desktop", "theme", t_name)
    gtk3_dir = os.path.join(v_theme_dir, "gtk-3.0")
    gtk4_dir = os.path.join(v_theme_dir, "gtk-4.0")
    xfwm_dir = os.path.join(v_theme_dir, "xfwm4")
    
    os.makedirs(gtk3_dir, exist_ok=True)
    os.makedirs(gtk4_dir, exist_ok=True)
    os.makedirs(xfwm_dir, exist_ok=True)
    
    base_theme_name = c_val["base_theme"]
    base_t = f"/usr/share/themes/{base_theme_name}"
    
    if os.path.exists(os.path.join(base_t, "gtk-3.0", "gtk.css")):
        with open(os.path.join(base_t, "gtk-3.0", "gtk.css"), "r") as f:
            gtk3_content = f.read()
    else:
        gtk3_content = ""
        
    if os.path.exists(os.path.join(base_t, "gtk-4.0", "gtk.css")):
        with open(os.path.join(base_t, "gtk-4.0", "gtk.css"), "r") as f:
            gtk4_content = f.read()
    else:
        gtk4_content = ""
        
    csd_css = csd_snippet_tpl.format(hex=c_val["hex"], glow=c_val["glow"])
    
    with open(os.path.join(gtk3_dir, "gtk.css"), "w") as f:
        f.write(gtk3_content + "\n" + csd_css)
    with open(os.path.join(gtk3_dir, "gtk-dark.css"), "w") as f:
        f.write(gtk3_content + "\n" + csd_css)
        
    with open(os.path.join(gtk4_dir, "gtk.css"), "w") as f:
        f.write(gtk4_content + "\n" + csd_css)
    with open(os.path.join(gtk4_dir, "gtk-dark.css"), "w") as f:
        f.write(gtk4_content + "\n" + csd_css)
        
    src_xfwm = os.path.join(VARIANTS_DIR, c_key, "desktop", "xfwm4-theme", f"Kali-{cap}-Dark-Borders", "xfwm4")
    for xf_file in os.listdir(src_xfwm):
        shutil.copy2(os.path.join(src_xfwm, xf_file), os.path.join(xfwm_dir, xf_file))
        
    icon_t = c_val["icon_theme"]
    with open(os.path.join(v_theme_dir, "index.theme"), "w") as f:
        f.write(f"[Desktop Entry]\nType=X-GNOME-Metatheme\nName={t_name}\nComment=Kali {cap} Dark with 2px Continuous Solid Borders\nEncoding=UTF-8\n\n[X-GNOME-Metatheme]\nGtkTheme={t_name}\nMetacityTheme={t_name}\nIconTheme={icon_t}\nXfwmTheme={t_name}\n")

    with open(os.path.join(VARIANTS_DIR, c_key, "desktop", "gtk-css", "gtk-3.0.css"), "w") as f:
        f.write(csd_css)
    with open(os.path.join(VARIANTS_DIR, c_key, "desktop", "gtk-css", "gtk-4.0.css"), "w") as f:
        f.write(csd_css)

print("Generated full standalone GTK3/GTK4/XFWM4 border themes for all 8 colors!")
