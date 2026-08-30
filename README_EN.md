# 🐉 Kali Dragon Theme Suite (Multi-Color Edition)

<div align="center">

[![Leer en Español](https://img.shields.io/badge/Language-Spanish-red?style=for-the-badge&logo=google-translate)](README.md)
[![Read in English](https://img.shields.io/badge/Language-English-blue?style=for-the-badge&logo=google-translate)](README_EN.md)

![Kali Dragon Preview](assets/preview_red.png)

**A complete, 100% modular, and cinematic visual theme suite for Kali Linux.**  
Transforms the entire visual experience across 8 color editions: from the **GRUB** bootloader with a *frosted glass* menu card and 70+ OS icons, the **Plymouth** boot animation, the **LightDM** login screen, to the **XFCE** desktop with 2px solid window borders, panel icons, and flying dragon window animations.

[![Platform: Kali Linux](https://img.shields.io/badge/Platform-Kali%20Linux%202026.x-red?style=for-the-badge&logo=kalilinux)](https://www.kali.org/)
[![Desktop: XFCE4 / XFWM4](https://img.shields.io/badge/Desktop-XFCE4%20%2F%20XFWM4-blue?style=for-the-badge&logo=xfce)](https://www.xfce.org/)
[![Colors: 8 Editions](https://img.shields.io/badge/Colors-8%20Variants-purple?style=for-the-badge)](#-available-color-editions)
[![Modular: 100% Granular](https://img.shields.io/badge/Components-Modular-green?style=for-the-badge)](#-granular-modular-installation-by-component)
[![Engine: PyQt6 Event-Driven](https://img.shields.io/badge/Engine-PyQt6%20%280%25%20CPU%29-green?style=for-the-badge&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-crimson?style=for-the-badge)](LICENSE)

</div>

---

## 🎨 Available Color Editions

| Color | Edition Name | Primary Tone | Preview |
| :---: | :--- | :---: | :---: |
| 🔴 | **Crimson Red** *(Original / Favorite)* | `#ff1744` / `#ec0101` | [View](assets/preview_red.png) |
| 🔵 | **Plasma Blue** *(Cyberpunk Blue)* | `#00b0ff` / `#2979ff` | [View](assets/preview_blue.png) |
| 🟢 | **Toxic Green** *(Hacker Green)* | `#00e676` / `#00c853` | [View](assets/preview_green.png) |
| 🟡 | **Cyber Yellow** *(Neon Gold)* | `#ffd600` / `#ffc107` | [View](assets/preview_yellow.png) |
| 🟣 | **Neon Purple** *(Synthwave)* | `#d500f9` / `#aa00ff` | [View](assets/preview_purple.png) |
| 🟠 | **Neon Orange** *(Incandescent)* | `#ff6d00` / `#ff5722` | [View](assets/preview_orange.png) |
| 🍈 | **Electric Lime** *(Acid Lime)* | `#76ff03` / `#64dd17` | [View](assets/preview_lime.png) |
| 🌸 | **Cyber Pink** *(Arcade Pink)* | `#ff4081` / `#f50057` | [View](assets/preview_pink.png) |

---

## 🚀 Quick Start & Installation

```bash
# 1. Clone the repository
git clone https://github.com/Gabo-Razo/Kali-Dragon-Suite.git
cd Kali-Dragon-Suite

# 2. Run the interactive installer
sudo ./install.sh
```

---

## 🧩 Granular Modular Installation (By Component)

You can install **only the specific components you want** without touching the rest of your system:

| Component | Example Command | Description |
| :--- | :--- | :--- |
| **🌟 Full System** | `sudo ./install.sh --color red --all` | Installs GRUB, Plymouth, Login, Window Borders, Dragon Animator, Icons & Terminal. |
| **🎛️ Full Bootloader** | `sudo ./install.sh --color purple --boot-only` | Installs GRUB Frosted Glass + Plymouth boot animation. |
| **🔘 GRUB Menu Only** | `sudo ./install.sh --color green --grub-only` | Installs only the GRUB boot menu with 70+ OS icons and glowing selectors. |
| **⚡ Plymouth Splash Only**| `sudo ./install.sh --color blue --plymouth-only` | Installs only the pulsating dragon Plymouth boot animation. |
| **🛡️ Login Screen Only** | `sudo ./install.sh --color purple --login-only` | Installs only the LightDM glassmorphism theme and dragon avatar. |
| **🐉 Dragon Animator Only**| `sudo ./install.sh --color red --animator-only` | Activates the flying dragon window spawn & close daemon (0% CPU). |
| **🪟 Window Borders Only** | `sudo ./install.sh --color lime --borders-only` | Applies continuous 2px solid borders to all windows (XFWM4 & GTK). |
| **🖼️ Wallpaper Only** | `sudo ./install.sh --color yellow --wallpaper-only` | Applies the 1080p dragon wallpaper to the desktop. |
| **🎨 Panel & Icons Only** | `sudo ./install.sh --color orange --icons-only` | Changes the Kali application menu icon and system icons. |
| **💻 Terminal Only** | `sudo ./install.sh --color pink --terminal-only` | Updates ZSH/Bash prompt colors and cursor to the selected color. |
| **🖥️ Desktop Only** | `sudo ./install.sh --color green --desktop-only` | Installs Borders + Animator + Wallpaper + Icons + Terminal (without touching GRUB). |

---

## ⚡ Command-Line Quick Flags

```bash
sudo ./install.sh --color red       # 🔴 Install full suite in Red
sudo ./install.sh --color green     # 🟢 Install full suite in Green
sudo ./install.sh --color purple    # 🟣 Install full suite in Purple
sudo ./install.sh --color blue      # 🔵 Install full suite in Blue
sudo ./install.sh --color yellow    # 🟡 Install full suite in Yellow
sudo ./install.sh --color orange    # 🟠 Install full suite in Orange
sudo ./install.sh --color lime      # 🍈 Install full suite in Lime
sudo ./install.sh --color pink      # 🌸 Install full suite in Pink
```

---

## 🌐 Universal OS & Distro Support

Includes **70+ custom vector circular logos** in all 8 colors for automatic icon matching:
* **Linux:** Kali, Arch, Garuda, Debian, Ubuntu, Linux Mint, Pop!_OS, Fedora, openSUSE, Gentoo, NixOS, Alpine, Zorin, Void, Parrot, BlackArch, Tails, CentOS, Rocky, etc.
* **Other OS:** Windows 11/10/7, macOS / Apple, FreeBSD, OpenBSD, Android-x86.
* **Utilities:** UEFI Firmware / BIOS, Memtest86+, Recovery Mode, Reboot, Shutdown.

---

## 🔄 Factory Reset / Uninstall

To restore all default factory settings anytime:
```bash
sudo ./uninstall.sh
```

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
