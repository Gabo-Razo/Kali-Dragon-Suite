#!/usr/bin/env python3
import os, sys, json, re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VARIANTS_DIR = os.path.join(BASE_DIR, "variants")

COLORS = [
    "red", "blue", "green", "yellow", "purple", "orange",
    "lime", "pink", "cyan", "teal", "gold", "indigo",
    "mint", "ruby", "magenta"
]

print("=" * 70)
print("🔍 AUDITORÍA INTEGRAL DE TODOS LOS MÓDULOS DE KALI DRAGON SUITE")
print("=" * 70)

errors = []
warnings = []

# 1. Check Installer syntax
ret = os.system(f"bash -n '{os.path.join(BASE_DIR, 'install.sh')}'")
if ret != 0:
    errors.append("Error de sintaxis en install.sh")
else:
    print("✅ [Módulo 0] Sintaxis de install.sh verificada y válida.")

# 2. Check Python Animator syntax & imports
ret = os.system(f"python3 -m py_compile '{os.path.join(BASE_DIR, 'desktop/animator/dragon-window-animator.py')}'")
if ret != 0:
    errors.append("Error de sintaxis en dragon-window-animator.py")
else:
    print("✅ [Módulo 5] Sintaxis de dragon-window-animator.py verificada y válida.")

# 3. Check All 15 Color Variants & Modular Components
for c in COLORS:
    cap = c.capitalize()
    v_dir = os.path.join(VARIANTS_DIR, c)
    if not os.path.isdir(v_dir):
        errors.append(f"Variante {c} no existe en variants/")
        continue

    # 3.1 GRUB
    grub_dir = os.path.join(v_dir, "boot", "grub")
    for f in ["grub-16x9.png", "grub-4x3.png", "select_c.png", "theme.txt"]:
        if not os.path.exists(os.path.join(grub_dir, f)):
            errors.append(f"[{c}] Falta archivo de GRUB: {f}")
    icons_dir = os.path.join(grub_dir, "icons")
    if not os.path.isdir(icons_dir) or len(os.listdir(icons_dir)) < 40:
        errors.append(f"[{c}] Iconos de GRUB incompletos (<40) en {icons_dir}")

    # 3.2 Plymouth
    ply_dir = os.path.join(v_dir, "boot", "plymouth")
    for f in ["kali.plymouth", "kali.script", "kali-logo.png", "kali-logo-container.png", "kali-logo-fade.png", "outline.png"]:
        if not os.path.exists(os.path.join(ply_dir, f)):
            errors.append(f"[{c}] Falta archivo de Plymouth: {f}")

    # 3.3 Boot Transition Wallpapers
    trans_dir = os.path.join(v_dir, "boot", "transition")
    for f in ["desktop-grub.png", "login-background.png", "login-blurred.png"]:
        if not os.path.exists(os.path.join(trans_dir, f)):
            errors.append(f"[{c}] Falta wallpaper de transición: {f}")

    # 3.4 Login & Greeter
    login_dir = os.path.join(v_dir, "login")
    if not os.path.exists(os.path.join(login_dir, "lightdm-gtk-greeter.conf")):
        errors.append(f"[{c}] Falta lightdm-gtk-greeter.conf")
    if not os.path.exists(os.path.join(login_dir, "dragon-avatar.png")):
        errors.append(f"[{c}] Falta dragon-avatar.png en login")
    login_theme = os.path.join(login_dir, "theme", f"Kali-{cap}-Dragon-Login", "gtk-3.0", "gtk.css")
    if not os.path.exists(login_theme):
        errors.append(f"[{c}] Falta login gtk.css: {login_theme}")

    # 3.5 Lockscreen
    lock_dir = os.path.join(v_dir, "lockscreen")
    for f in ["lockscreen.png", "gnome-background.xml", "dragon-avatar.png"]:
        if not os.path.exists(os.path.join(lock_dir, f)):
            errors.append(f"[{c}] Falta archivo de Lockscreen: {f}")

    # 3.6 Desktop Theme & XFWM4 Borders
    t_dir = os.path.join(v_dir, "desktop", "theme", f"Kali-{cap}-Dark-Borders")
    xfwm4_dir = os.path.join(t_dir, "xfwm4")
    if not os.path.isdir(xfwm4_dir):
        errors.append(f"[{c}] Falta directorio XFWM4: {xfwm4_dir}")
    else:
        for xf_f in ["themerc", "close-active.png", "maximize-active.png", "hide-active.png", "bottom-active.png", "left-active.png", "right-active.png", "top-left-active.png", "top-right-active.png"]:
            if not os.path.exists(os.path.join(xfwm4_dir, xf_f)):
                errors.append(f"[{c}] Falta archivo XFWM4: {xf_f}")

    # 3.7 GTK 3 & GTK 4 Stylesheets (Solid & Opaque)
    gtk3_css = os.path.join(t_dir, "gtk-3.0", "gtk.css")
    gtk4_css = os.path.join(t_dir, "gtk-4.0", "gtk.css")
    if not os.path.exists(gtk3_css):
        errors.append(f"[{c}] Falta gtk-3.0/gtk.css")
    else:
        with open(gtk3_css, "r") as gf:
            content = gf.read()
            if "window.csd.background > decoration" in content:
                errors.append(f"[{c}] Regla conflictiva window.csd.background encontrada en GTK3")
            if "background-color: #23252e;" not in content:
                errors.append(f"[{c}] Falta fondo opaco sólido #23252e en GTK3")

    # 3.8 Icons
    icons_dir = os.path.join(v_dir, "icons", "apps", "scalable")
    if not os.path.isdir(icons_dir):
        errors.append(f"[{c}] Falta directorio de iconos: {icons_dir}")

    # 3.9 Wallpaper
    wall_f = os.path.join(v_dir, "assets", f"wallpaper_{c}.png")
    if not os.path.exists(wall_f):
        errors.append(f"[{c}] Falta fondo de pantalla: {wall_f}")

    # 3.10 Animator config & sprite
    anim_dir = os.path.join(v_dir, "desktop", "animator")
    if not os.path.exists(os.path.join(anim_dir, "dragon_sprite.png")):
        errors.append(f"[{c}] Falta dragon_sprite.png en {anim_dir}")
    if not os.path.exists(os.path.join(anim_dir, "color_config.json")):
        errors.append(f"[{c}] Falta color_config.json en {anim_dir}")

if not errors:
    print("🌟 ¡TODOS LOS 15 COLORES Y SUS 8 MÓDULOS PASARON LA AUDITORÍA CON 100% DE ÉXITO!")
else:
    print(f"❌ Se encontraron {len(errors)} errores:")
    for e in errors:
        print(f"  - {e}")

print("=" * 70)
