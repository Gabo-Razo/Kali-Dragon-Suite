# 🐉 Kali Dragon Theme Suite (Multi-Color Edition)

<div align="center">

[![Read in English](https://img.shields.io/badge/Language-English-blue?style=for-the-badge&logo=google-translate)](README_EN.md)
[![Leer en Español](https://img.shields.io/badge/Idioma-Español-red?style=for-the-badge&logo=google-translate)](README.md)

![Kali Dragon Preview](assets/preview_red.png)

**Una suite visual completa, 100% modular y cinematográfica para Kali Linux.**  
Transforma toda la experiencia visual en 8 ediciones de color: desde el menú de arranque de **GRUB** con tarjeta *frosted glass* y más de 70 iconos de distros, la animación de carga de **Plymouth**, la pantalla de **Login (LightDM)**, hasta el escritorio **XFCE** con bordes de 2px, iconos de panel y animaciones del dragón volador al abrir y cerrar ventanas.

[![Platform: Kali Linux](https://img.shields.io/badge/Platform-Kali%20Linux%202026.x-red?style=for-the-badge&logo=kalilinux)](https://www.kali.org/)
[![Desktop: XFCE4 / XFWM4](https://img.shields.io/badge/Desktop-XFCE4%20%2F%20XFWM4-blue?style=for-the-badge&logo=xfce)](https://www.xfce.org/)
[![Colors: 8 Editions](https://img.shields.io/badge/Colors-8%20Variants-purple?style=for-the-badge)](#-ediciones-de-color-disponibles)
[![Modular: 100% Granular](https://img.shields.io/badge/Components-Modular-green?style=for-the-badge)](#-instalación-modular-por-componentes-independientes)
[![Engine: PyQt6 Event-Driven](https://img.shields.io/badge/Engine-PyQt6%20%280%25%20CPU%29-green?style=for-the-badge&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-crimson?style=for-the-badge)](LICENSE)

</div>

---

## 🎨 Ediciones de Color Disponibles

| Color | Nombre de la Edición | Tono Principal | Vista Previa |
| :---: | :--- | :---: | :---: |
| 🔴 | **Crimson Red** *(Favorito / Original)* | `#ff1744` / `#ec0101` | [Ver](assets/preview_red.png) |
| 🔵 | **Plasma Blue** *(Cyberpunk Blue)* | `#00b0ff` / `#2979ff` | [Ver](assets/preview_blue.png) |
| 🟢 | **Toxic Green** *(Hacker Green)* | `#00e676` / `#00c853` | [Ver](assets/preview_green.png) |
| 🟡 | **Cyber Yellow** *(Neon Gold)* | `#ffd600` / `#ffc107` | [Ver](assets/preview_yellow.png) |
| 🟣 | **Neon Purple** *(Synthwave)* | `#d500f9` / `#aa00ff` | [Ver](assets/preview_purple.png) |
| 🟠 | **Neon Orange** *(Incandescent)* | `#ff6d00` / `#ff5722` | [Ver](assets/preview_orange.png) |
| 🍈 | **Electric Lime** *(Acid Lime)* | `#76ff03` / `#64dd17` | [Ver](assets/preview_lime.png) |
| 🌸 | **Cyber Pink** *(Arcade Pink)* | `#ff4081` / `#f50057` | [Ver](assets/preview_pink.png) |

---

## 🚀 Guía Rápida de Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/Gabo-Razo/Kali-Dragon-Suite.git
cd Kali-Dragon-Suite

# 2. Ejecutar el menú interactivo
sudo ./install.sh
```

---

## 🧩 Instalación Modular (Por Componentes Independientes)

Puedes instalar **únicamente la parte que tú quieras** sin alterar el resto de tu sistema:

| Componente | Comando de Ejemplo | ¿Qué hace? |
| :--- | :--- | :--- |
| **🌟 Todo el Sistema** | `sudo ./install.sh --color red --all` | Instala GRUB, Plymouth, Login, Bordes, Dragón, Iconos y Terminal. |
| **🎛️ Todo el Arranque** | `sudo ./install.sh --color purple --boot-only` | Instala el Menú GRUB Frosted Glass + la animación de carga de Plymouth. |
| **🔘 Solo Menú GRUB** | `sudo ./install.sh --color green --grub-only` | Solo instala el tema de GRUB con sus 70+ iconos y selectores. |
| **⚡ Solo Animación Carga**| `sudo ./install.sh --color blue --plymouth-only` | Solo instala el logo del dragón palpitante de Plymouth. |
| **🛡️ Solo Pantalla de Login** | `sudo ./install.sh --color purple --login-only` | Instala la tarjeta de cristal de LightDM y el avatar del dragón. |
| **🐉 Solo Dragón Volador** | `sudo ./install.sh --color red --animator-only` | Activa el demonio del dragón al abrir y cerrar ventanas (0% CPU). |
| **🪟 Solo Bordes de Ventana**| `sudo ./install.sh --color lime --borders-only` | Aplica marcos sólidos de 2px a todas las ventanas (XFWM4 y GTK). |
| **🖼️ Solo Fondo de Pantalla**| `sudo ./install.sh --color yellow --wallpaper-only` | Aplica el fondo 1080p del dragón a tu escritorio. |
| **🎨 Solo Iconos de Panel** | `sudo ./install.sh --color orange --icons-only` | Cambia el dragón del menú del panel y los iconos del sistema. |
| **💻 Solo Terminal** | `sudo ./install.sh --color pink --terminal-only` | Cambia el prompt de ZSH/Bash y el cursor al color elegido. |
| **🖥️ Solo Escritorio** | `sudo ./install.sh --color green --desktop-only` | Instala Bordes + Dragón + Fondo + Iconos + Terminal (sin tocar GRUB). |

---

## ⚡ Comandos Rápidos por Consola

```bash
sudo ./install.sh --color red       # 🔴 Todo en Rojo
sudo ./install.sh --color green     # 🟢 Todo en Verde
sudo ./install.sh --color purple    # 🟣 Todo en Morado
sudo ./install.sh --color blue      # 🔵 Todo en Azul
sudo ./install.sh --color yellow    # 🟡 Todo en Amarillo
sudo ./install.sh --color orange    # 🟠 Todo en Naranja
sudo ./install.sh --color lime      # 🍈 Todo en Lima
sudo ./install.sh --color pink      # 🌸 Todo en Rosa
```

---

## 🌐 Compatibilidad Universal de Sistemas Operativos

Incluye más de **70 logotipos vectoriales circulares** en cada uno de los 8 colores para detectar automáticamente:
* **Linux:** Kali, Arch, Garuda, Debian, Ubuntu, Linux Mint, Pop!_OS, Fedora, openSUSE, Gentoo, NixOS, Alpine, Zorin, Void, Parrot, BlackArch, Tails, CentOS, Rocky, etc.
* **Otros Sistemas:** Windows 11/10/7, macOS / Apple, FreeBSD, OpenBSD, Android-x86.
* **Utilidades:** UEFI Firmware / BIOS, Memtest86+, Modo Recuperación, Reiniciar, Apagar.

---

## 🔄 Restauración de Fábrica

Para regresar tu sistema a los valores originales de fábrica:
```bash
sudo ./uninstall.sh
```

---

## 📄 Licencia

Distribuido bajo la Licencia MIT. Consulta `LICENSE` para más información.
