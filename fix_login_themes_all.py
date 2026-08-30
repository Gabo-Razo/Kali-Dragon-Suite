#!/usr/bin/env python3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VARIANTS_DIR = os.path.join(BASE_DIR, "variants")

ALL_COLORS = [
    "red", "blue", "green", "yellow", "purple", "orange", "lime", "pink",
    "cyan", "white", "gold", "indigo", "mint", "ruby", "silver"
]

for c in ALL_COLORS:
    cap = c.capitalize()
    t_login = f"Kali-{cap}-Dragon-Login"
    login_theme_dir = os.path.join(VARIANTS_DIR, c, "login", "theme", t_login)
    os.makedirs(os.path.join(login_theme_dir, "gtk-3.0"), exist_ok=True)
    
    # 1. Write index.theme
    with open(os.path.join(login_theme_dir, "index.theme"), "w") as f:
        f.write(f"""[Desktop Entry]
Type=X-GNOME-Metatheme
Name={t_login}
Comment=Kali Dragon Glassmorphism Login Greeter Theme
Encoding=UTF-8

[X-GNOME-Metatheme]
GtkTheme={t_login}
MetacityTheme={t_login}
IconTheme=Flat-Remix-Blue-Dark
""")

    # 2. Add @import to gtk.css if not present
    gtk_css_file = os.path.join(login_theme_dir, "gtk-3.0", "gtk.css")
    if os.path.exists(gtk_css_file):
        with open(gtk_css_file, "r") as f:
            content = f.read()
        if "@import" not in content:
            content = '@import url("/usr/share/themes/Kali-Dark/gtk-3.0/gtk.css");\n\n' + content
            with open(gtk_css_file, "w") as f:
                f.write(content)

print("SUCCESS: Added index.theme and base GTK import to all 15 login themes!")
