# 🐉 Kali Dragon Suite (15 Color Editions)

> **Comprehensive & Granular Modular Customization Suite for Kali Linux (XFCE)**  
> Completely transforms boot (GRUB), splash loading (Plymouth), login screen (LightDM), lock screen (Screensaver), logout/shutdown dialog, 2px window borders, cinematic dragon window animator (60 FPS), system icons, and terminal prompt.

---

## 🎨 15 Available Color Editions

| Edition | Primary Color | CLI Name |
| :--- | :--- | :--- |
| **Crimson Red** | `#ff1744` / `#ec0101` | `red` |
| **Plasma Blue** | `#00b0ff` / `#2979ff` | `blue` |
| **Toxic Green** | `#00e676` / `#00c853` | `green` |
| **Cyber Yellow** | `#ffd600` / `#ffc107` | `yellow` |
| **Neon Purple** | `#d500f9` / `#aa00ff` | `purple` |
| **Neon Orange** | `#ff6d00` / `#ff5722` | `orange` |
| **Electric Lime** | `#76ff03` / `#64dd17` | `lime` |
| **Cyber Pink** | `#ff4081` / `#f50057` | `pink` |
| **Neon Cyan** | `#18ffff` / `#00e5ff` | `cyan` |
| **Neon Teal** | `#00f2fe` / `#00b4d8` | `teal` |
| **Cyber Gold** | `#ffab00` / `#ffd700` | `gold` |
| **Royal Indigo** | `#536dfe` / `#3d5afe` | `indigo` |
| **Quantum Mint** | `#64ffda` / `#00bfa5` | `mint` |
| **Blood Ruby** | `#e91e63` / `#c2185b` | `ruby` |
| **Cyber Magenta** | `#ff007f` / `#e00070` | `magenta` |

---

## 📦 Granular Modular Components

You can install the entire suite or **only the specific module you want**:

| Module | CLI Flag | Description |
| :--- | :--- | :--- |
| **🌟 Full Suite** | `--all` | Installs all visual components and the window animator. |
| **🎛️ Boot Only** | `--boot-only` | GRUB bootloader menu + Plymouth boot splash animation. |
| **🖥️ GRUB Only** | `--grub-only` | Dark glass GRUB theme with 70+ OS icons. |
| **⏳ Plymouth Only** | `--plymouth-only` | Neon glowing dragon boot animation. |
| **🛡️ Login & Lock Only** | `--login-only` | LightDM Greeter, screensaver/lockscreen, and logout dialog. |
| **🪟 Window Borders Only**| `--borders-only` | 2px window borders (XFWM4 & GTK) with 100% solid opaque backgrounds. |
| **🐉 Animator Only** | `--animator-only` | 60 FPS orbital flight, tangent banking & resplandor window crystallization. |
| **🖼️ Wallpaper Only** | `--wallpaper-only` | 1080p Dragon wallpaper in the selected color. |
| **🎨 Icons Only** | `--icons-only` | Panel menu and system power icons synchronized with the theme. |
| **💻 Terminal Only** | `--terminal-only` | Two-line ZSH prompt and cursor color matching the color palette. |
| **🎛️ Desktop Only** | `--desktop-only` | Borders, animator, wallpaper, icons, and terminal prompt. |

---

## 🚀 Quick Start

### 1. Interactive Installer
```bash
sudo ./install.sh
```

### 2. Direct CLI Installation
```bash
# Install everything in Cyber Gold:
sudo ./install.sh --color gold --all

# Install only window borders in Toxic Green:
sudo ./install.sh --color green --borders-only

# Install only Boot components (GRUB + Plymouth) in Crimson Red:
sudo ./install.sh --color red --boot-only

# Install only Login & Lockscreen in Neon Purple:
sudo ./install.sh --color purple --login-only

# Install only the Dragon Window Animator in Plasma Blue:
sudo ./install.sh --color blue --animator-only
```

---
