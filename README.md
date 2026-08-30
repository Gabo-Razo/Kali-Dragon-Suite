# 🐉 Kali Dragon Suite (15 Ediciones de Color)

> **Suite Integral y Modular de Personalización para Kali Linux (XFCE)**  
> Transforma por completo el arranque (GRUB), la pantalla de carga (Plymouth), la pantalla de inicio de sesión (LightDM), la pantalla de bloqueo (Screensaver), el cuadro de apagado/cierre de sesión, los bordes de ventana de 2px, el animador cinemático del dragón (60 FPS), los iconos del sistema y el prompt de la terminal.

---

## 🎨 15 Ediciones de Color Disponibles

| Edición | Color Primario | Nombre Clave |
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

## 📦 Módulos Independientes y Granulares

Puedes instalar la suite completa o **únicamente el módulo que necesites**:

| Módulo | Flag CLI | Descripción |
| :--- | :--- | :--- |
| **🌟 Suite Completa** | `--all` | Instala todos los componentes visuales y el animador. |
| **🎛️ Arranque Completo** | `--boot-only` | Menú de arranque GRUB + Pantalla de carga Plymouth. |
| **🖥️ Solo GRUB** | `--grub-only` | Menú de arranque estilo cristal oscuro con 70+ iconos de SOs. |
| **⏳ Solo Plymouth** | `--plymouth-only` | Animación de carga del dragón con resplandor neón. |
| **🛡️ Solo Login & Bloqueo** | `--login-only` | LightDM Greeter, pantalla de bloqueo (Screensaver) y cuadro de apagar/cerrar sesión. |
| **🪟 Solo Bordes de Ventana** | `--borders-only` | Bordes finos de 2px (XFWM4 y GTK) con fondos 100% sólidos y opacos. |
| **🐉 Solo Animador** | `--animator-only` | Vuelo orbital, resplandor y materialización cinemática a 60 FPS al abrir y cerrar ventanas. |
| **🖼️ Solo Fondo** | `--wallpaper-only` | Fondo de pantalla 1080p del Dragón en el color elegido. |
| **🎨 Solo Iconos** | `--icons-only` | Iconos del panel, menú de aplicaciones y botones de bloqueo/apagado sincronizados. |
| **💻 Solo Terminal** | `--terminal-only` | Prompt de dos líneas de ZSH y cursor a juego sin transparencias. |
| **🎛️ Solo Escritorio** | `--desktop-only` | Bordes, animador, wallpaper, iconos y terminal. |

---

## 🚀 Instalación Rápida

### 1. Menú Interactivo (Te pregunta qué color y qué módulos instalar)
```bash
sudo ./install.sh
```

### 2. Instalación Directa por Línea de Comandos
```bash
# Instalar todo en Cyber Gold:
sudo ./install.sh --color gold --all

# Instalar solo los bordes de ventana en Toxic Green:
sudo ./install.sh --color green --borders-only

# Instalar solo el arranque (GRUB + Plymouth) en Crimson Red:
sudo ./install.sh --color red --boot-only

# Instalar solo el Login y Bloqueo en Neon Purple:
sudo ./install.sh --color purple --login-only

# Instalar solo el Animador del Dragón en Plasma Blue:
sudo ./install.sh --color blue --animator-only
```

---

## 🛡️ Estabilidad y Características Técnicas

* **Fondos 100% Sólidos y Opacos (`#23252e`):** Cero problemas de transparencia o elementos invisibles en Thunar, terminales y cuadros de diálogo.
* **Proporciones 1:1 Preservadas:** El dragón vuela con su relación de aspecto natural exacta sin aplanarse ni deformarse.
* **Trayectoria Confinada:** El dragón se desplaza estrictamente dentro del marco de la ventana sin invadir el resto de la pantalla.
* **Cero Bucles Infinitos:** El daemon del animador utiliza `X11BypassWindowManagerHint` e ignorado de PID propio para un consumo de 0.0% de CPU en reposo.
* **100% Portátil:** Funciona en cualquier equipo con Kali Linux / XFCE sin rutas fijas.

---
