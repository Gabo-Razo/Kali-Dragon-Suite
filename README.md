# 🐉 Kali Dragon Theme Suite (15 Color Editions)

<div align="center">

[![Read in English](https://img.shields.io/badge/Language-English-blue?style=for-the-badge&logo=google-translate)](README_EN.md)
[![Leer en Español](https://img.shields.io/badge/Idioma-Español-red?style=for-the-badge&logo=google-translate)](README.md)

![Kali Dragon Preview](assets/preview_red.png)

**Una suite visual cinematográfica, 100% modular y universal para Kali Linux.**  
Transforma toda la experiencia visual en **15 ediciones de color de alta fidelidad**: desde el menú de arranque de **GRUB** con tarjeta *frosted glass* y más de 70 iconos de distros, la animación de carga de **Plymouth**, la **tríada de pantallas de login y bloqueo** (LightDM, pantalla de desbloqueo al suspender y cuadro de cerrar sesión), hasta el escritorio **XFCE** con bordes sólidos de 2px, iconos y animaciones del dragón volador al abrir y cerrar ventanas.

[![Platform: Kali Linux](https://img.shields.io/badge/Platform-Kali%20Linux%202026.x-red?style=for-the-badge&logo=kalilinux)](https://www.kali.org/)
[![Desktop: XFCE4 / XFWM4](https://img.shields.io/badge/Desktop-XFCE4%20%2F%20XFWM4-blue?style=for-the-badge&logo=xfce)](https://www.xfce.org/)
[![Colors: 15 Editions](https://img.shields.io/badge/Colors-15%20Variants-purple?style=for-the-badge)](#-15-ediciones-de-color-disponibles)
[![Modular: 100% Granular](https://img.shields.io/badge/Components-Modular-green?style=for-the-badge)](#-instalación-modular-por-componentes-independientes)
[![Engine: PyQt6 Event-Driven](https://img.shields.io/badge/Engine-PyQt6%20%280%25%20CPU%29-green?style=for-the-badge&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-crimson?style=for-the-badge)](LICENSE)

</div>

---

## 🎨 15 Ediciones de Color Disponibles

| # | Color | Nombre de la Edición | Tono Principal | Vista Previa |
| :-: | :---: | :--- | :---: | :---: |
| **1** | 🔴 | **Crimson Red** *(Original / Favorito)* | `#ff1744` / `#ec0101` | [Ver](assets/preview_red.png) |
| **2** | 🔵 | **Plasma Blue** *(Cyberpunk Blue)* | `#00b0ff` / `#2979ff` | [Ver](assets/preview_blue.png) |
| **3** | 🟢 | **Toxic Green** *(Hacker Green / Matrix)* | `#00e676` / `#00c853` | [Ver](assets/preview_green.png) |
| **4** | 🟡 | **Cyber Yellow** *(Neon Gold)* | `#ffd600` / `#ffc107` | [Ver](assets/preview_yellow.png) |
| **5** | 🟣 | **Neon Purple** *(Synthwave / Vaporwave)* | `#d500f9` / `#aa00ff` | [Ver](assets/preview_purple.png) |
| **6** | 🟠 | **Neon Orange** *(Incandescente / Lava)* | `#ff6d00` / `#ff5722` | [Ver](assets/preview_orange.png) |
| **7** | 🍈 | **Electric Lime** *(Verde Lima Ácido)* | `#76ff03` / `#64dd17` | [Ver](assets/preview_lime.png) |
| **8** | 🌸 | **Cyber Pink** *(Arcade Pink / Magenta)* | `#ff4081` / `#f50057` | [Ver](assets/preview_pink.png) |
| **9** | 💎 | **Neon Cyan** *(Azul Hielo / Arctic Ice)* | `#18ffff` / `#00e5ff` | [Ver](assets/preview_cyan.png) |
| **10** | 🖤 | **Stealth White** *(Blanco Puro Neón / Ghost)* | `#ffffff` / `#f5f5f5` | [Ver](assets/preview_white.png) |
| **11** | 🪙 | **Cyber Gold** *(Oro Metálico / Night City)* | `#ffab00` / `#ffd700` | [Ver](assets/preview_gold.png) |
| **12** | 🌊 | **Royal Indigo** *(Azul Índigo / Zafiro)* | `#536dfe` / `#3d5afe` | [Ver](assets/preview_indigo.png) |
| **13** | 🧪 | **Quantum Mint** *(Verde Menta Cuántico)* | `#64ffda` / `#00bfa5` | [Ver](assets/preview_mint.png) |
| **14** | 🩸 | **Blood Ruby** *(Rojo Rubí / Dark Wine)* | `#e91e63` / `#c2185b` | [Ver](assets/preview_ruby.png) |
| **15** | 🥈 | **Chrome Silver** *(Plata Metalizado / Chrome)* | `#eceff1` / `#cfd8dc` | [Ver](assets/preview_silver.png) |

---

## 🚀 Guía Rápida de Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/Gabo-Razo/Kali-Dragon-Suite.git
cd Kali-Dragon-Suite

# 2. Ejecutar el menú interactivo con las 15 opciones de color
sudo ./install.sh
```

---

## 🧩 Instalación Modular (Por Componentes Independientes)

Puedes instalar **únicamente la parte que tú quieras** sin alterar el resto de tu sistema:

| Componente | Comando de Ejemplo | ¿Qué instala exactamente? |
| :--- | :--- | :--- |
| **🌟 Todo el Sistema** | `sudo ./install.sh --color cyan --all` | Instala GRUB, Plymouth, la tríada de Logins, Bordes, Dragón, Iconos y Terminal. |
| **🎛️ Todo el Arranque** | `sudo ./install.sh --color gold --boot-only` | Instala el Menú GRUB Frosted Glass + la animación de carga de Plymouth. |
| **🔘 Solo Menú GRUB** | `sudo ./install.sh --color white --grub-only` | Solo instala el tema de GRUB con sus 70+ iconos y selectores neón. |
| **⚡ Solo Animación Carga**| `sudo ./install.sh --color indigo --plymouth-only`| Solo instala el logo del dragón palpitante de Plymouth en el arranque. |
| **🛡️ Tríada de Logins** | `sudo ./install.sh --color mint --login-only` | **1)** Pantalla de inicio LightDM con avatar y fondo 1080p.<br>**2)** Pantalla de bloqueo al suspender con avatar, textos y fondo 1080p.<br>**3)** Cuadro de diálogo de cerrar sesión con botones de cristal. |
| **🐉 Solo Dragón Volador** | `sudo ./install.sh --color ruby --animator-only` | Activa el demonio del dragón al abrir y cerrar ventanas (60 FPS / 0% CPU). |
| **🪟 Solo Bordes de Ventana**| `sudo ./install.sh --color silver --borders-only`| Aplica marcos sólidos de 2px a todas las ventanas (XFWM4 y GTK). |
| **🖼️ Solo Fondo de Pantalla**| `sudo ./install.sh --color cyan --wallpaper-only`| Aplica el fondo 1080p del dragón a tu escritorio. |
| **🎨 Solo Iconos de Panel** | `sudo ./install.sh --color gold --icons-only` | Cambia el dragón del menú del panel, los botones de acción y carpetas. |
| **💻 Solo Terminal** | `sudo ./install.sh --color white --terminal-only` | Cambia el prompt de ZSH/Bash y el cursor al color elegido. |
| **🖥️ Solo Escritorio** | `sudo ./install.sh --color indigo --desktop-only` | Instala Bordes + Dragón + Fondo + Iconos + Terminal (sin tocar GRUB). |

---

## ⚡ Comandos Rápidos por Consola

```bash
sudo ./install.sh --color red --all       # 🔴 Crimson Red
sudo ./install.sh --color blue --all      # 🔵 Plasma Blue
sudo ./install.sh --color green --all     # 🟢 Toxic Green
sudo ./install.sh --color yellow --all    # 🟡 Cyber Yellow
sudo ./install.sh --color purple --all    # 🟣 Neon Purple
sudo ./install.sh --color orange --all    # 🟠 Neon Orange
sudo ./install.sh --color lime --all      # 🍈 Electric Lime
sudo ./install.sh --color pink --all      # 🌸 Cyber Pink
sudo ./install.sh --color cyan --all      # 💎 Neon Cyan / Ice
sudo ./install.sh --color white --all     # 🖤 Stealth White
sudo ./install.sh --color gold --all      # 🪙 Cyber Gold
sudo ./install.sh --color indigo --all    # 🌊 Royal Indigo
sudo ./install.sh --color mint --all      # 🧪 Quantum Mint
sudo ./install.sh --color ruby --all      # 🩸 Blood Ruby
sudo ./install.sh --color silver --all    # 🥈 Chrome Silver
```

---

## 🌐 Compatibilidad Universal de Sistemas Operativos

Incluye más de **70 logotipos vectoriales circulares** en cada uno de los 15 colores para detectar automáticamente:
* **Linux:** Kali, Arch, Garuda, Debian, Ubuntu, Linux Mint, Pop!_OS, Fedora, openSUSE, Gentoo, NixOS, Alpine, Zorin, Void, Parrot, BlackArch, Tails, CentOS, Rocky, etc.
* **Otros Sistemas:** Windows 11/10/7, macOS / Apple, FreeBSD, OpenBSD, Android-x86.
* **Utilidades:** UEFI Firmware / BIOS, Memtest86+, Modo Recuperación, Reiniciar, Apagar.

---

## 🔄 Restauración de Fábrica

Para regresar tu sistema a los valores originales de fábrica en cualquier momento:
```bash
sudo ./uninstall.sh
```

---

## 📄 Licencia

Distribuido bajo la Licencia MIT. Consulta `LICENSE` para más información.
