# 🐉 Kali Dragon Theme Suite (Multi-Color Edition)

<div align="center">

[![Read in English](https://img.shields.io/badge/Language-English-blue?style=for-the-badge&logo=google-translate)](README_EN.md)
[![Leer en Español](https://img.shields.io/badge/Idioma-Español-red?style=for-the-badge&logo=google-translate)](README.md)

![Kali Dragon Preview](assets/preview_red.png)

**Una suite visual completa, modular y cinematográfica para Kali Linux.**  
Transforma toda la experiencia visual en 8 ediciones de color: desde el menú de arranque de **GRUB** con tarjeta *frosted glass* y más de 70 iconos de distros, la animación de carga de **Plymouth**, la pantalla de **Login (LightDM)**, hasta el escritorio **XFCE** con bordes de 2px y animaciones del dragón al abrir y cerrar ventanas.

[![Platform: Kali Linux](https://img.shields.io/badge/Platform-Kali%20Linux%202026.x-red?style=for-the-badge&logo=kalilinux)](https://www.kali.org/)
[![Desktop: XFCE4 / XFWM4](https://img.shields.io/badge/Desktop-XFCE4%20%2F%20XFWM4-blue?style=for-the-badge&logo=xfce)](https://www.xfce.org/)
[![Colors: 8 Editions](https://img.shields.io/badge/Colors-8%20Variants-purple?style=for-the-badge)](#-ediciones-de-color-disponibles)
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
git clone https://github.com/TU-USUARIO/Kali-Dragon-Suite.git
cd Kali-Dragon-Suite

# 2. Ejecutar el menú interactivo (puedes elegir color y componentes)
sudo ./install.sh
```

---

## ⚡ Comandos Rápidos por Consola

### ¿Quieres un color específico?
```bash
sudo ./install.sh --color red       # 🔴 Instalar todo en Rojo
sudo ./install.sh --color green     # 🟢 Instalar todo en Verde
sudo ./install.sh --color blue      # 🔵 Instalar todo en Azul
sudo ./install.sh --color purple    # 🟣 Instalar todo en Morado
sudo ./install.sh --color yellow    # 🟡 Instalar todo en Amarillo
sudo ./install.sh --color orange    # 🟠 Instalar todo en Naranja
sudo ./install.sh --color lime      # 🍈 Instalar todo en Lima
sudo ./install.sh --color pink      # 🌸 Instalar todo en Rosa
```

### ¿Solo quieres partes específicas? (Instalación Modular)
Si no quieres cambiar todo tu sistema y prefieres solo una parte:

```bash
# Solo el menú de arranque GRUB (por ejemplo en Verde)
sudo ./install.sh --color green --grub-only

# Solo la pantalla de Login (LightDM) (por ejemplo en Morado)
sudo ./install.sh --color purple --login-only

# Solo el escritorio (Bordes de ventana de 2px y animador del dragón)
sudo ./install.sh --color red --desktop-only

# Solo la animación de carga de arranque (Plymouth)
sudo ./install.sh --color blue --plymouth-only
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
