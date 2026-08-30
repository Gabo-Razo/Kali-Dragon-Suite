# 🐉 Kali Dragon Theme Suite (Multi-Color Edition)

<div align="center">

[![Leer en Español](https://img.shields.io/badge/Language-Spanish-red?style=for-the-badge&logo=google-translate)](README.md)
[![Read in English](https://img.shields.io/badge/Language-English-blue?style=for-the-badge&logo=google-translate)](README_EN.md)

![Kali Dragon Preview](assets/preview_red.png)

**A complete, modular, and cinematic visual theme suite for Kali Linux.**  
Transforms the entire visual experience across 8 color editions: from the **GRUB** bootloader with a *frosted glass* menu card and 70+ OS icons, the **Plymouth** boot animation, the **LightDM** login screen, to the **XFCE** desktop with 2px solid window borders and flying dragon window animations.

[![Platform: Kali Linux](https://img.shields.io/badge/Platform-Kali%20Linux%202026.x-red?style=for-the-badge&logo=kalilinux)](https://www.kali.org/)
[![Desktop: XFCE4 / XFWM4](https://img.shields.io/badge/Desktop-XFCE4%20%2F%20XFWM4-blue?style=for-the-badge&logo=xfce)](https://www.xfce.org/)
[![Colors: 8 Editions](https://img.shields.io/badge/Colors-8%20Variants-purple?style=for-the-badge)](#-available-color-editions)
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
git clone https://github.com/YOUR-USER/Kali-Dragon-Suite.git
cd Kali-Dragon-Suite

# 2. Run the interactive installer (select color and components)
sudo ./install.sh
```

---

## ⚡ Command-Line Quick Flags

### Install a specific color:
```bash
sudo ./install.sh --color red       # 🔴 Install full suite in Red
sudo ./install.sh --color green     # 🟢 Install full suite in Green
sudo ./install.sh --color blue      # 🔵 Install full suite in Blue
sudo ./install.sh --color purple    # 🟣 Install full suite in Purple
sudo ./install.sh --color yellow    # 🟡 Install full suite in Yellow
sudo ./install.sh --color orange    # 🟠 Install full suite in Orange
sudo ./install.sh --color lime      # 🍈 Install full suite in Lime
sudo ./install.sh --color pink      # 🌸 Install full suite in Pink
```

### Install specific components only (Modular Mode):
If a user only wants specific parts rather than the full OS theme:

```bash
# Only install the GRUB Boot Menu (e.g. in Green)
sudo ./install.sh --color green --grub-only

# Only install the LightDM Login Screen (e.g. in Purple)
sudo ./install.sh --color purple --login-only

# Only install the Desktop (2px window borders and dragon animator)
sudo ./install.sh --color red --desktop-only

# Only install the Plymouth Boot Splash
sudo ./install.sh --color blue --plymouth-only
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
