<div align="center">

# 🐉 KALI DRAGON SUITE
### *The Ultimate Cyberpunk & Neon Transformation for Kali Linux (XFCE)*

[![OS: Kali Linux](https://img.shields.io/badge/OS-Kali%20Linux%20%2F%20Debian-557C94?style=for-the-badge&logo=kalilinux&logoColor=white)](https://www.kali.org/)
[![Desktop: XFCE4](https://img.shields.io/badge/Desktop-XFCE4-00A4E4?style=for-the-badge&logo=xfce&logoColor=white)](https://www.xfce.org/)
[![Editions: 15 Colors](https://img.shields.io/badge/Editions-15%20Neon%20Colors-FF1744?style=for-the-badge&logo=palette&logoColor=white)](#-15-available-color-editions)
[![Performance: 60 FPS](https://img.shields.io/badge/Performance-60%20FPS%20Native-00E676?style=for-the-badge&logo=speedtest&logoColor=white)](#-technical-features--performance)
[![License: MIT](https://img.shields.io/badge/License-MIT-FAD02C?style=for-the-badge)](LICENSE)

<br/>

> **A complete, modular, and ultra-optimized customization suite transforming every inch of your system:**  
> 1080p GRUB bootloader menu, Plymouth boot splash, LightDM login greeter, glassmorphism lock screen, 2px neon borders, 60 FPS cinematic dragon window animator, high-contrast GTK3/4 themes, Flat-Remix icons, and custom ZSH terminal prompt.

</div>

---

## 💬 Creator's Note

> *"This is my first project built for Linux and I wanted to share it with the community. The goal was to give Kali Linux a visually epic cyberpunk/neon aesthetic while keeping it extremely lightweight and resource-friendly.*  
> *Several base textures and wallpapers were generated with the help of Gemini. If you run into any visual bug or have suggestions for improvements, feel free to open an [Issue](https://github.com/Gabo-Razo/Kali-Dragon-Suite/issues) and I'll do my best to address it promptly. Hope you find it useful and enjoy it!"*  
> — **Gabo Razo** ([@Gabo-Razo](https://github.com/Gabo-Razo))

---

## 📸 Visual Showcase & Previews

<div align="center">

### 🐉 1. Cinematic Dragon Window Animator (60 FPS Flight)
*The dragon orbits window perimeters with plasma trails and glowing illumination upon application launch.*

![Dragon Window Animation](assets/previews/5_dragon_window_animation.gif)

<br/>

### 🖥️ 2. GRUB Boot Menu (1080p Crystal Glass)
*Dark carbon background with neon aura, cybernetic brackets, and over 70 recolored OS icons.*

![GRUB Boot Menu](assets/previews/1_grub_boot_menu.png)

<br/>

### ⏳ 3. Plymouth Boot Splash (Neon Loading)
*Clean, smooth boot animation on pure OLED black.*

![Plymouth Animation](assets/previews/3_plymouth_animation.png)

<br/>

### 🔒 4. Lockscreen / Suspend Dialog (`xfce4-screensaver`)
*Glassmorphic card with glowing circular avatar, password input, and responsive action buttons.*

![Lockscreen Dialog](assets/previews/2_lockscreen_dialog.png)

<br/>

### 🪟 5. 2px Neon Window Borders & Desktop Theme (GTK3 & GTK4)
*Windows featuring crisp 2px neon borders, arcade circular buttons, and 100% solid, opaque dark backgrounds.*

![Desktop Window Borders](assets/previews/4_desktop_window_borders.png)

</div>

---

## 🎨 15 Available Color Editions

Every single color is calibrated for high neon saturation on pitch-dark backdrops, guaranteeing crystal-clear readability and contrast:

| # | Edition | CLI Flag | Primary Color | Aesthetic / Vibe |
| :-: | :--- | :--- | :--- | :--- |
| 1 | **🔴 Crimson Red** | `red` | `#ff1744` / `#ec0101` | Crimson Neon Red (Original Suite Theme) |
| 2 | **🔵 Plasma Blue** | `blue` | `#00b0ff` / `#2979ff` | Electric Plasma Cyberpunk Blue |
| 3 | **🟢 Toxic Green** | `green` | `#00e676` / `#00c853` | Matrix Hacker Toxic Green |
| 4 | **🟡 Cyber Yellow** | `yellow` | `#ffd600` / `#ffc107` | High-Voltage Cyber Yellow |
| 5 | **🟣 Neon Purple** | `purple` | `#d500f9` / `#aa00ff` | Synthwave Purple / Retro City |
| 6 | **🟠 Neon Orange** | `orange` | `#ff6d00` / `#ff5722` | Incandescent Lava Orange |
| 7 | **🍈 Electric Lime** | `lime` | `#76ff03` / `#64dd17` | Acid Electric Lime |
| 8 | **🌸 Cyber Pink** | `pink` | `#ff4081` / `#f50057` | Arcade Neon Pink |
| 9 | **💎 Neon Cyan** | `cyan` | `#18ffff` / `#00e5ff` | Arctic Ice / Neon Cyan |
| 10 | **🌊 Neon Teal** | `teal` | `#00f2fe` / `#00b4d8` | Cyberpunk Aqua / Neon Teal |
| 11 | **🪙 Cyber Gold** | `gold` | `#ffab00` / `#ffd700` | Night City Amber / Metallic Gold |
| 12 | **🌌 Royal Indigo** | `indigo` | `#536dfe` / `#3d5afe` | Deep Sapphire / Royal Indigo |
| 13 | **🧪 Quantum Mint** | `mint` | `#64ffda` / `#00bfa5` | Quantum Mint Green |
| 14 | **🩸 Blood Ruby** | `ruby` | `#e91e63` / `#c2185b` | Dark Wine / Blood Ruby |
| 15 | **🔮 Cyber Magenta** | `magenta` | `#ff007f` / `#e00070` | Retrowave 80s Cyber Magenta |

---

## 📦 Granular Modular Architecture

You don't need to change your whole setup; choose the **complete suite** or install **only what you need**:

| Module | CLI Flag | Functionality |
| :--- | :--- | :--- |
| **🌟 Complete Suite** | `--all` | Installs all 8 visual and animator components. |
| **🎛️ Boot Only** | `--boot-only` | Configures both the GRUB menu and Plymouth splash. |
| **🖥️ GRUB Only** | `--grub-only` | Deploys the 1080p GRUB theme with 70+ OS icons. |
| **⏳ Plymouth Only** | `--plymouth-only` | Installs the dragon boot animation. |
| **🛡️ Login & Lock Only** | `--login-only` | LightDM Greeter, screensaver lockscreen, and logout dialog. |
| **🪟 Window Borders Only** | `--borders-only` | 2px thin borders (XFWM4 & GTK) with solid backgrounds. |
| **🐉 Animator Only** | `--animator-only` | 60 FPS daemon for cinematic dragon window flight. |
| **🖼️ Wallpaper Only** | `--wallpaper-only` | 1080p Dragon wallpaper in the selected color edition. |
| **🎨 System Icons Only** | `--icons-only` | Panel, app menu, and lockscreen icons synchronized. |
| **💻 Terminal Only** | `--terminal-only` | 2-line ZSH prompt and matching neon cursor. |
| **🎛️ Desktop Only** | `--desktop-only` | Borders, animator, wallpaper, icons, and terminal. |

---

## 🚀 Quick Installation

### Prerequisites
* **Operating System:** Kali Linux (or any Debian-based distribution with XFCE).
* **Desktop Environment:** XFCE4.
* **Dependencies:** Python 3, PyQt6 (`python3-pyqt6`), `xprop`, `xdotool` (installer checks automatically).

```bash
# 1. Clone repository
git clone https://github.com/Gabo-Razo/Kali-Dragon-Suite.git
cd Kali-Dragon-Suite

# 2. Grant execute permissions
chmod +x install.sh
```

### Option A: Interactive Menu (Recommended)
Run the script to select your color edition and desired modules from a guided numerical menu:
```bash
sudo ./install.sh
```

### Option B: Direct Command-Line Flags
```bash
# Install everything in Crimson Red:
sudo ./install.sh --color red --all

# Install everything in Cyber Gold:
sudo ./install.sh --color gold --all

# Install only 2px window borders in Toxic Green:
sudo ./install.sh --color green --borders-only

# Install only the boot components (GRUB + Plymouth) in Plasma Blue:
sudo ./install.sh --color blue --boot-only

# Install only the Dragon Animator in Neon Cyan:
sudo ./install.sh --color cyan --animator-only
```

---

## ⚙️ Technical Features & Performance

* 🚀 **Near-Zero Idle Consumption (0.0% CPU):** The window animator operates as a native `systemd --user` background daemon, awakening strictly upon X11 window mapping events.
* 🛡️ **100% Solid Dark Backgrounds (`#23252e`):** Problematic GTK transparencias were eliminated to guarantee full text contrast in Thunar, browsers, and terminal emulators.
* 📐 **1:1 Natural Aspect Ratio Preserved:** The dragon sprite orbits with exact mathematical proportions without squishing or distortion.
* 🔄 **Suspend & Reboot Resilient:** Services restore themselves seamlessly across reboots and screen lock states.

---

## 🤝 Support & Contributions

Encountered an issue or have an idea for a new animation/palette?
* Open an **[Issue](https://github.com/Gabo-Razo/Kali-Dragon-Suite/issues)** describing your suggestion or open a Pull Request.
* If you enjoyed the project and found it useful, consider giving it a **⭐ Star** on GitHub to support it!

---

## 💖 Support & Donations

If you enjoy this project and wish to support its ongoing development, new themes, and animation enhancements:

<div align="center">

[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/Gabo-Razo)

*Any sponsorship or support is deeply appreciated and fuels future open-source Linux projects! ☕🐉*

</div>

---

<div align="center">

Crafted with ❤️ by **[Gabo Razo](https://github.com/Gabo-Razo)** for the **Kali Linux & Open Source** community.

</div>
