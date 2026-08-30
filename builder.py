import os, math, colorsys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

BASE_DIR = "/home/gr/Escritorio/Kali-Red-Dragon-Suite"
VARIANTS_DIR = os.path.join(BASE_DIR, "variants")
os.makedirs(VARIANTS_DIR, exist_ok=True)

# 8 Color Configurations
COLORS = {
    "red": {
        "name": "Crimson Red",
        "emoji": "🔴",
        "hue": 0.0,
        "primary": "#ff1744",
        "core": "#ec0101",
        "dark": "#8b0015",
        "glow_rgb": (255, 23, 68),
        "dark_rgb": (180, 10, 25),
        "highlight_rgb": (255, 120, 140)
    },
    "orange": {
        "name": "Neon Orange",
        "emoji": "🟠",
        "hue": 0.08,
        "primary": "#ff6d00",
        "core": "#ff5722",
        "dark": "#b73d00",
        "glow_rgb": (255, 109, 0),
        "dark_rgb": (200, 70, 0),
        "highlight_rgb": (255, 175, 80)
    },
    "yellow": {
        "name": "Cyber Yellow",
        "emoji": "🟡",
        "hue": 0.14,
        "primary": "#ffd600",
        "core": "#ffc107",
        "dark": "#b28900",
        "glow_rgb": (255, 214, 0),
        "dark_rgb": (200, 160, 0),
        "highlight_rgb": (255, 240, 120)
    },
    "lime": {
        "name": "Electric Lime",
        "emoji": "🍈",
        "hue": 0.24,
        "primary": "#76ff03",
        "core": "#64dd17",
        "dark": "#439600",
        "glow_rgb": (118, 255, 3),
        "dark_rgb": (80, 190, 10),
        "highlight_rgb": (180, 255, 100)
    },
    "green": {
        "name": "Toxic Green",
        "emoji": "🟢",
        "hue": 0.35,
        "primary": "#00e676",
        "core": "#00c853",
        "dark": "#007a33",
        "glow_rgb": (0, 230, 118),
        "dark_rgb": (0, 160, 60),
        "highlight_rgb": (100, 255, 170)
    },
    "blue": {
        "name": "Plasma Blue",
        "emoji": "🔵",
        "hue": 0.58,
        "primary": "#00b0ff",
        "core": "#2979ff",
        "dark": "#005cb2",
        "glow_rgb": (0, 176, 255),
        "dark_rgb": (20, 100, 220),
        "highlight_rgb": (120, 210, 255)
    },
    "purple": {
        "name": "Neon Purple",
        "emoji": "🟣",
        "hue": 0.77,
        "primary": "#d500f9",
        "core": "#aa00ff",
        "dark": "#6a0080",
        "glow_rgb": (213, 0, 249),
        "dark_rgb": (150, 0, 200),
        "highlight_rgb": (230, 120, 255)
    },
    "pink": {
        "name": "Cyber Pink",
        "emoji": "🌸",
        "hue": 0.90,
        "primary": "#ff4081",
        "core": "#f50057",
        "dark": "#a00037",
        "glow_rgb": (255, 64, 129),
        "dark_rgb": (200, 20, 90),
        "highlight_rgb": (255, 150, 190)
    }
}

def shift_hue(img, target_hue):
    if target_hue == 0.0:
        return img.copy()
    img_rgb = img.convert("RGB")
    arr = np.array(img_rgb, dtype=np.float32) / 255.0
    max_c = np.max(arr, axis=-1)
    min_c = np.min(arr, axis=-1)
    delta = max_c - min_c
    h = np.zeros_like(max_c)
    mask = delta > 0.001
    r, g, b = arr[..., 0], arr[..., 1], arr[..., 2]
    mask_r = mask & (max_c == r)
    mask_g = mask & (max_c == g)
    mask_b = mask & (max_c == b)
    h[mask_r] = ((g[mask_r] - b[mask_r]) / delta[mask_r]) % 6.0
    h[mask_g] = ((b[mask_g] - r[mask_g]) / delta[mask_g]) + 2.0
    h[mask_b] = ((r[mask_b] - g[mask_b]) / delta[mask_b]) + 4.0
    h = (h / 6.0 + target_hue) % 1.0
    s = np.zeros_like(max_c)
    s[max_c > 0] = delta[max_c > 0] / max_c[max_c > 0]
    v = max_c
    c = v * s
    x = c * (1.0 - np.abs((h * 6.0) % 2.0 - 1.0))
    m = v - c
    rgb = np.zeros_like(arr)
    cond0 = (0.0 <= h * 6.0) & (h * 6.0 < 1.0)
    cond1 = (1.0 <= h * 6.0) & (h * 6.0 < 2.0)
    cond2 = (2.0 <= h * 6.0) & (h * 6.0 < 3.0)
    cond3 = (3.0 <= h * 6.0) & (h * 6.0 < 4.0)
    cond4 = (4.0 <= h * 6.0) & (h * 6.0 < 5.0)
    cond5 = (5.0 <= h * 6.0) & (h * 6.0 < 6.0)
    rgb[cond0] = np.stack([c[cond0], x[cond0], np.zeros_like(c[cond0])], axis=-1)
    rgb[cond1] = np.stack([x[cond1], c[cond1], np.zeros_like(c[cond1])], axis=-1)
    rgb[cond2] = np.stack([np.zeros_like(c[cond2]), c[cond2], x[cond2]], axis=-1)
    rgb[cond3] = np.stack([np.zeros_like(c[cond3]), x[cond3], c[cond3]], axis=-1)
    rgb[cond4] = np.stack([x[cond4], np.zeros_like(c[cond4]), c[cond4]], axis=-1)
    rgb[cond5] = np.stack([c[cond5], np.zeros_like(c[cond5]), x[cond5]], axis=-1)
    rgb = np.clip((rgb + m[..., np.newaxis]) * 255.0, 0, 255).astype(np.uint8)
    if img.mode == "RGBA":
        res = Image.fromarray(rgb, "RGB").convert("RGBA")
        res.putalpha(img.split()[3])
        return res
    return Image.fromarray(rgb, "RGB")

orig_wp = Image.open(os.path.expanduser("~/Pictures/kali_dragon_official.jpg")).convert("RGB")
orig_sprite = Image.open(os.path.expanduser("~/.local/share/dragon-anim/dragon_sprite.png")).convert("RGBA")

try:
    font_h = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 15)
    font_item = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)
except Exception:
    font_h = font_item = font_small = ImageFont.load_default()

OS_ICONS = {
    "kali": "K", "debian": "D", "ubuntu": "U", "arch": "A", "fedora": "F",
    "windows": "W", "mint": "M", "manjaro": "M", "pop-os": "P", "gentoo": "G",
    "opensuse": "S", "macos": "", "gnu-linux": "L", "linux": "L", "uefi": "⚙", "memtest": "MEM"
}

for c_key, c_val in COLORS.items():
    name = c_val["name"]
    emoji = c_val["emoji"]
    print(f"Building variant: {emoji} {name} ({c_key})...")
    
    v_dir = os.path.join(VARIANTS_DIR, c_key)
    boot_grub = os.path.join(v_dir, "boot", "grub")
    boot_icons = os.path.join(boot_grub, "icons")
    boot_plymouth = os.path.join(v_dir, "boot", "plymouth")
    boot_trans = os.path.join(v_dir, "boot", "transition")
    login_dir = os.path.join(v_dir, "login")
    login_theme = os.path.join(login_dir, "theme", f"Kali-{c_key.capitalize()}-Dragon-Login", "gtk-3.0")
    desktop_xfwm = os.path.join(v_dir, "desktop", "xfwm4-theme", f"Kali-{c_key.capitalize()}-Dark-Borders", "xfwm4")
    desktop_css = os.path.join(v_dir, "desktop", "gtk-css")
    desktop_anim = os.path.join(v_dir, "desktop", "animator")
    assets_dir = os.path.join(v_dir, "assets")
    
    for d in [boot_grub, boot_icons, boot_plymouth, boot_trans, login_dir, login_theme, desktop_xfwm, desktop_css, desktop_anim, assets_dir]:
        os.makedirs(d, exist_ok=True)
        
    # 1. Base Wallpaper
    c_wp = shift_hue(orig_wp, c_val["hue"])
    c_wp_1080 = c_wp.resize((1920, 1080), Image.Resampling.LANCZOS)
    c_wp_1080.save(os.path.join(assets_dir, f"wallpaper_{c_key}.png"), "PNG")
    c_wp_1080.save(os.path.join(boot_trans, "desktop-grub.png"), "PNG")
    c_wp_1080.save(os.path.join(boot_trans, "login-background.png"), "PNG")
    c_wp_1080.filter(ImageFilter.GaussianBlur(radius=16)).save(os.path.join(boot_trans, "login-blurred.png"), "PNG")
    
    # 2. Dragon Sprite
    c_sprite = shift_hue(orig_sprite, c_val["hue"])
    c_sprite.save(os.path.join(assets_dir, "dragon_sprite.png"), "PNG")
    c_sprite.save(os.path.join(desktop_anim, "dragon_sprite.png"), "PNG")
    
    # 3. GRUB Frosted Glass Wallpaper
    card_w, card_h = 980, 520
    card_x, card_y = (1920 - card_w) // 2, 250
    blur_crop = c_wp_1080.crop((card_x, card_y, card_x + card_w, card_y + card_h)).filter(ImageFilter.GaussianBlur(radius=28))
    tint_layer = Image.new("RGBA", (card_w, card_h), (8, 2, 4, 215))
    tinted_card = Image.alpha_composite(blur_crop.convert("RGBA"), tint_layer)
    cdraw = ImageDraw.Draw(tinted_card)
    
    g_col = c_val["glow_rgb"] + (235,)
    cdraw.rounded_rectangle([0, 0, card_w - 1, card_h - 1], radius=10, outline=g_col, width=2)
    cdraw.rounded_rectangle([3, 3, card_w - 4, card_h - 4], radius=8, outline=c_val["highlight_rgb"] + (70,), width=1)
    
    blen = 28
    cdraw.line([6, 6, 6 + blen, 6], fill=(255, 255, 255, 240), width=3)
    cdraw.line([6, 6, 6, 6 + blen], fill=(255, 255, 255, 240), width=3)
    cdraw.line([card_w - 7 - blen, 6, card_w - 7, 6], fill=(255, 255, 255, 240), width=3)
    cdraw.line([card_w - 7, 6, card_w - 7, 6 + blen], fill=(255, 255, 255, 240), width=3)
    cdraw.line([6, card_h - 7, 6 + blen, card_h - 7], fill=(255, 255, 255, 240), width=3)
    cdraw.line([6, card_h - 7 - blen, 6, card_h - 7], fill=(255, 255, 255, 240), width=3)
    cdraw.line([card_w - 7 - blen, card_h - 7, card_w - 7, card_h - 7], fill=(255, 255, 255, 240), width=3)
    cdraw.line([card_w - 7, card_h - 7 - blen, card_w - 7, card_h - 7], fill=(255, 255, 255, 240), width=3)
    
    hdr_txt = "◈  K A L I   L I N U X   B O O T   M A N A G E R  ◈"
    cdraw.text((card_w // 2 - 200, 22), hdr_txt, fill=c_val["glow_rgb"] + (240,), font=font_h)
    cdraw.line([40, 52, card_w - 40, 52], fill=c_val["glow_rgb"] + (130,), width=1)
    
    grub_16x9 = c_wp_1080.convert("RGBA")
    grub_16x9.paste(tinted_card, (card_x, card_y), tinted_card)
    grub_16x9.convert("RGB").save(os.path.join(boot_grub, "grub-16x9.png"), "PNG")
    
    target_w = int(1080 * (4.0/3.0))
    left_x = (1920 - target_w) // 2
    grub_4x3 = grub_16x9.crop((left_x, 0, left_x + target_w, 1080)).resize((1440, 1080), Image.Resampling.LANCZOS)
    grub_4x3.convert("RGB").save(os.path.join(boot_grub, "grub-4x3.png"), "PNG")
    
    # 4. Selection Pills
    pill_h = 38
    fpill = Image.new("RGBA", (128, pill_h), (0, 0, 0, 0))
    pdraw = ImageDraw.Draw(fpill)
    pdraw.rounded_rectangle([0, 0, 127, pill_h - 1], radius=6, fill=c_val["dark_rgb"] + (225,), outline=c_val["glow_rgb"] + (255,), width=2)
    pdraw.line([4, 2, 123, 2], fill=c_val["highlight_rgb"] + (190,), width=1)
    pdraw.line([4, pill_h - 3, 123, pill_h - 3], fill=c_val["glow_rgb"] + (220,), width=1)
    
    fpill.crop((0, 0, 6, pill_h)).save(os.path.join(boot_grub, "select_w.png"), "PNG")
    fpill.crop((60, 0, 68, pill_h)).save(os.path.join(boot_grub, "select_c.png"), "PNG")
    fpill.crop((121, 0, 128, pill_h)).save(os.path.join(boot_grub, "select_e.png"), "PNG")
    
    # 5. OS Icons
    for iname, itxt in OS_ICONS.items():
        iimg = Image.new("RGBA", (24, 24), (0, 0, 0, 0))
        idraw = ImageDraw.Draw(iimg)
        idraw.ellipse([1, 1, 22, 22], fill=(20, 3, 6, 235), outline=c_val["glow_rgb"] + (230,), width=1)
        idraw.text((6, 4), itxt, fill=c_val["glow_rgb"] + (255,))
        iimg.save(os.path.join(boot_icons, f"{iname}.png"), "PNG")
        
    # 6. theme.txt
    theme_txt = f"""# Kali Linux {name} GRUB Theme
title-text: ""
desktop-image: "grub-16x9.png"
desktop-color: "#060103"
terminal-left: "0"
terminal-top: "0"
terminal-width: "100%"
terminal-height: "100%"
terminal-border: "0"

+ boot_menu {{
  left = 26%
  top = 30%
  width = 48%
  height = 42%
  item_color = "#dcdcdc"
  selected_item_color = "#ffffff"
  icon_width = 20
  icon_height = 20
  item_icon_space = 12
  item_height = 38
  item_padding = 4
  item_spacing = 7
  selected_item_pixmap_style = "select_*.png"
}}

+ label {{
  top = 84%
  left = 25%
  width = 50%
  align = "center"
  id = "__timeout__"
  text = "◈ Iniciando automáticamente en %d segundos... ◈"
  color = "{c_val["primary"]}"
}}

+ label {{
  top = 94%
  left = 20%
  width = 60%
  align = "center"
  text = "Usa las teclas ↑ y ↓ para seleccionar  •  Presiona ENTER para iniciar"
  color = "#888888"
}}
"""
    with open(os.path.join(boot_grub, "theme.txt"), "w") as f:
        f.write(theme_txt)
        
    # 7. Plymouth Theme
    for fname in os.listdir("/usr/share/plymouth/themes/kali/"):
        spath = os.path.join("/usr/share/plymouth/themes/kali/", fname)
        if fname.endswith(".png"):
            pimg = Image.open(spath).convert("RGBA")
            lum = ImageOps.grayscale(pimg)
            ptinted = ImageOps.colorize(lum, black="#050002", white=c_val["primary"], mid=c_val["core"])
            ptinted.putalpha(pimg.split()[3])
            ptinted.save(os.path.join(boot_plymouth, fname), "PNG")
        elif fname.endswith(".script") or fname.endswith(".plymouth"):
            with open(spath, "r") as f:
                fcontent = f.read()
            with open(os.path.join(boot_plymouth, fname), "w") as f:
                f.write(fcontent)
                
    # 8. User Avatar
    avatar = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
    avdraw = ImageDraw.Draw(avatar)
    for r, a in [(126, 40), (124, 70), (122, 110), (120, 160)]:
        avdraw.ellipse([128 - r, 128 - r, 128 + r, 128 + r], outline=c_val["glow_rgb"] + (a,), width=2)
    avdraw.ellipse([14, 14, 242, 242], fill=(16, 2, 5, 235), outline=c_val["glow_rgb"] + (255,), width=3)
    c_sprite_scaled = c_sprite.resize((210, 144), Image.Resampling.LANCZOS)
    avatar.paste(c_sprite_scaled, ((256 - 210) // 2, (256 - 144) // 2), c_sprite_scaled)
    avatar.save(os.path.join(login_dir, "dragon-avatar.png"), "PNG")
    
    # 9. LightDM GTK CSS
    gtk_css = f"""/* Kali {name} Login GTK3 Theme */
@define-color bg_dark rgba(14, 2, 5, 0.92);
@define-color color_neon {c_val["primary"]};
@define-color color_core {c_val["core"]};
@define-color text_light #ffffff;

window {{ background-color: transparent; color: @text_light; }}
#panel_window {{ background-color: rgba(10, 1, 3, 0.88); border-bottom: 1.5px solid @color_core; color: @text_light; }}
#panel_window menuitem:hover {{ background-color: rgba({c_val["glow_rgb"][0]}, {c_val["glow_rgb"][1]}, {c_val["glow_rgb"][2]}, 0.25); color: @color_neon; }}
#content_frame, #panel_window + window {{
    background-color: @bg_dark;
    border: 2px solid @color_core;
    border-radius: 14px;
    box-shadow: 0 10px 35px rgba({c_val["glow_rgb"][0]}, {c_val["glow_rgb"][1]}, {c_val["glow_rgb"][2]}, 0.4);
    padding: 24px;
}}
#user_image {{ border: 2px solid @color_neon; border-radius: 9999px; box-shadow: 0 0 16px rgba({c_val["glow_rgb"][0]}, {c_val["glow_rgb"][1]}, {c_val["glow_rgb"][2]}, 0.6); }}
entry {{
    background-color: rgba(25, 3, 7, 0.85);
    border: 1.5px solid rgba({c_val["glow_rgb"][0]}, {c_val["glow_rgb"][1]}, {c_val["glow_rgb"][2]}, 0.45);
    border-radius: 8px; color: @text_light; padding: 8px 12px;
}}
entry:focus {{ border-color: @color_neon; box-shadow: 0 0 12px rgba({c_val["glow_rgb"][0]}, {c_val["glow_rgb"][1]}, {c_val["glow_rgb"][2]}, 0.85); }}
button {{
    background: linear-gradient(135deg, {c_val["primary"]} 0%, {c_val["dark"]} 100%);
    border: 1px solid {c_val["primary"]}; border-radius: 8px; color: @text_light; font-weight: bold; padding: 8px 16px;
}}
button:hover {{ box-shadow: 0 5px 18px rgba({c_val["glow_rgb"][0]}, {c_val["glow_rgb"][1]}, {c_val["glow_rgb"][2]}, 0.75); }}
"""
    with open(os.path.join(login_theme, "gtk.css"), "w") as f:
        f.write(gtk_css)
        
    with open(os.path.join(login_dir, "theme", f"Kali-{c_key.capitalize()}-Dragon-Login", "index.theme"), "w") as f:
        f.write(f"[Desktop Entry]\nType=X-GNOME-Metatheme\nName=Kali-{c_key.capitalize()}-Dragon-Login\n")
        
    icon_theme_val = "Flat-Remix-Red-Dark" if c_key == "red" else f"Flat-Remix-{c_key.capitalize()}-Dark"
    greeter_conf = f"""[greeter]
background = /usr/share/desktop-base/kali-theme/login/login-background.png
theme-name = Kali-{c_key.capitalize()}-Dragon-Login
icon-theme-name = {icon_theme_val}
font-name = Cantarell 11
indicators = ~host;~spacer;~clock;~spacer;~session;~a11y;~power;
clock-format = %A %d de %B  •  %H:%M
default-user-image = /usr/share/desktop-base/kali-theme/login/dragon-avatar.png
round-user-image = true
position = 50%,center 50%,center
"""
    with open(os.path.join(login_dir, "lightdm-gtk-greeter.conf"), "w") as f:
        f.write(greeter_conf)
        
    # 10. XFWM4 Theme
    xfwm_src = os.path.expanduser("~/.themes/Kali-Red-Dark-Borders/xfwm4")
    for xf_file in os.listdir(xfwm_src):
        src_f = os.path.join(xfwm_src, xf_file)
        dst_f = os.path.join(desktop_xfwm, xf_file)
        if xf_file.endswith(".png"):
            xp = Image.open(src_f).convert("RGBA")
            xp_shift = shift_hue(xp, c_val["hue"])
            xp_shift.save(dst_f, "PNG")
        elif xf_file == "themerc":
            with open(src_f, "r") as f:
                tmc = f.read()
            with open(dst_f, "w") as f:
                f.write(tmc)
                
    # 11. GTK CSS
    gtk_csd = f"""window.ssd decoration, window.csd decoration {{
    border: 2px solid {c_val["core"]};
    border-radius: 6px 6px 0px 0px;
    box-shadow: 0 0 10px rgba({c_val["glow_rgb"][0]}, {c_val["glow_rgb"][1]}, {c_val["glow_rgb"][2]}, 0.4);
}}
"""
    with open(os.path.join(desktop_css, "gtk-3.0.css"), "w") as f:
        f.write(gtk_csd)
    with open(os.path.join(desktop_css, "gtk-4.0.css"), "w") as f:
        f.write(gtk_csd)
        
    # 12. Preview Image for README
    prev_bg = grub_16x9.copy()
    p_draw = ImageDraw.Draw(prev_bg)
    menu_x, menu_y = 500, 324
    item_w, item_h = 920, 38
    sel_w = Image.open(os.path.join(boot_grub, "select_w.png")).convert("RGBA")
    sel_c = Image.open(os.path.join(boot_grub, "select_c.png")).convert("RGBA")
    sel_e = Image.open(os.path.join(boot_grub, "select_e.png")).convert("RGBA")
    sbar = Image.new("RGBA", (item_w, item_h), (0, 0, 0, 0))
    sbar.paste(sel_w, (0, 0))
    cw = item_w - sel_w.width - sel_e.width
    for cx in range(sel_w.width, sel_w.width + cw, sel_c.width):
        pw = min(sel_c.width, sel_w.width + cw - cx)
        sbar.paste(sel_c.crop((0, 0, pw, item_h)), (cx, 0))
    sbar.paste(sel_e, (item_w - sel_e.width, 0))
    prev_bg.paste(sbar, (menu_x, menu_y), sbar)
    
    p_draw.text((menu_x + 35, menu_y + 8), f"★ Kali GNU/Linux ({name} Edition)", fill=(255, 255, 255), font=font_item)
    p_draw.text((menu_x + 35, menu_y + item_h + 15), "  Opciones avanzadas para Kali GNU/Linux", fill=(210, 210, 210), font=font_small)
    p_draw.text((menu_x + 35, menu_y + (item_h + 7)*2 + 8), "  Windows Boot Manager / Otra Distribución", fill=(190, 190, 190), font=font_small)
    p_draw.text((menu_x + 35, menu_y + (item_h + 7)*3 + 8), "  Configuración de Firmware UEFI", fill=(170, 170, 170), font=font_small)
    p_draw.text((1920//2 - 210, int(1080 * 0.84)), "◈ Iniciando automáticamente en 5 segundos... ◈", fill=c_val["glow_rgb"], font=font_item)
    
    prev_bg.save(os.path.join(assets_dir, f"preview_{c_key}.png"), "PNG")
    prev_bg.save(os.path.join(BASE_DIR, "assets", f"preview_{c_key}.png"), "PNG")

print("\nSUCCESS: All 8 Color Variants Fully Generated and Pre-built!")
