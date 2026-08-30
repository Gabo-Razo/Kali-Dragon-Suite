# 🐉 Kali Dragon Theme Suite (Multi-Color Edition)

<div align="center">

![Kali Dragon Preview](assets/preview_red.png)

**Una suite visual completa, cinematográfica y multi-color para Kali Linux.**  
Transforma toda la experiencia visual de inicio a fin en 8 espectaculares ediciones de color: desde el menú de arranque de **GRUB** con tarjeta *frosted glass*, pasando por la animación de carga de **Plymouth**, la pantalla de **Login (LightDM)**, hasta el escritorio **XFCE** con bordes de ventana de 2px y animaciones dinámicas del dragón al abrir y cerrar aplicaciones.

[![Platform: Kali Linux](https://img.shields.io/badge/Platform-Kali%20Linux%202026.x-red?style=for-the-badge&logo=kalilinux)](https://www.kali.org/)
[![Desktop: XFCE4 / XFWM4](https://img.shields.io/badge/Desktop-XFCE4%20%2F%20XFWM4-blue?style=for-the-badge&logo=xfce)](https://www.xfce.org/)
[![Colors: 8 Editions](https://img.shields.io/badge/Colors-8%20Variants-purple?style=for-the-badge)](README.md#palette-ediciones-de-color-disponibles)
[![Engine: PyQt6 Event-Driven](https://img.shields.io/badge/Engine-PyQt6%20%280%25%20CPU%29-green?style=for-the-badge&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-crimson?style=for-the-badge)](LICENSE)

</div>

---

## 🎨 Ediciones de Color Disponibles

La suite incluye soporte nativo y pre-renderizado en alta resolución para **8 colores**:

| Color | Nombre de la Edición | Código HEX Primario | Vista Previa |
| :---: | :--- | :---: | :---: |
| 🔴 | **Crimson Red** *(Original / Favorito)* | `#ff1744` / `#ec0101` | [Ver Captura](assets/preview_red.png) |
| 🔵 | **Plasma Blue** *(Cyberpunk Blue)* | `#00b0ff` / `#2979ff` | [Ver Captura](assets/preview_blue.png) |
| 🟢 | **Toxic Green** *(Hacker Green)* | `#00e676` / `#00c853` | [Ver Captura](assets/preview_green.png) |
| 🟡 | **Cyber Yellow** *(Neon Gold)* | `#ffd600` / `#ffc107` | [Ver Captura](assets/preview_yellow.png) |
| 🟣 | **Neon Purple** *(Synthwave)* | `#d500f9` / `#aa00ff` | [Ver Captura](assets/preview_purple.png) |
| 🟠 | **Neon Orange** *(Incandescent)* | `#ff6d00` / `#ff5722` | [Ver Captura](assets/preview_orange.png) |
| 🍈 | **Electric Lime** *(Acid Lime)* | `#76ff03` / `#64dd17` | [Ver Captura](assets/preview_lime.png) |
| 🌸 | **Cyber Pink** *(Arcade Pink)* | `#ff4081` / `#f50057` | [Ver Captura](assets/preview_pink.png) |

---

## ⚡ Componentes Incluidos en Cada Color

### 1. 🎛️ Menú de Arranque GRUB (Frosted Glass & Cyberpunk)
* **Tarjeta Flotante con Desenfoque Gaussiano (*Blur*):** Contenedor oscuro ahumado de cristal que permite leer las opciones con máxima nitidez sobre el fondo del dragón.
* **Borde Neón de 2px & Esquinas Cyberpunk:** Con corchetes en las 4 esquinas y cabecera iluminada `◈ KALI LINUX BOOT MANAGER ◈`.
* **Cápsula de Selección Luminosa:** Barra de selección activa con resplandor neón en el color elegido.
* **Soporte Universal de Sistemas Operativos:** Incluye iconos circulares para **Kali Linux, Debian, Ubuntu, Arch, Fedora, Windows, Linux genérico, UEFI Firmware, Memtest y más**.

### 2. ⚡ Pantalla de Carga de Arranque (Plymouth)
* **Logo del Dragón de Kali Tintado:** Logo oficial palpitante en el color seleccionado durante el arranque.
* **Traspaso de Video Limpio:** Fondos de transición de 1080p que eliminan pantallas intermedias.

### 3. 🛡️ Pantalla de Inicio de Sesión (LightDM Greeter)
* **Avatar del Dragón de Kali:** Disco de cristal oscuro con el emblema del dragón y halo de energía circular en el color elegido.
* **Tarjeta Central Flotante (*Glassmorphism*):** Cuadro de login con marco de 2px neón y sombra exterior difuminada.
* **Caja de Contraseña Reactiva:** Resplandor de enfoque neón al escribir tu contraseña.
* **Botón de Iniciar Sesión con Degradado:** Estilo moderno con iluminación al pasar el ratón.

### 4. 🪟 Bordes de Ventana Continuos XFWM4 (2px Solid Color)
* **Bordes Perfectos de 2px:** Bordes en color activo e inactivo en los cuatro costados de las ventanas.
* **Botones con Transparencia 100%:** Elimina cualquier corte o hueco en el borde superior de la barra de título.
* **Compatibilidad CSD (GTK-3 y GTK-4):** Bordes aplicados a aplicaciones cliente como Firefox, Mousepad, QTerminal, Thunar, etc.

### 5. 🐉 Animador Dinámico de Ventanas (0% CPU Idle)
* **Animación de Apertura:** El dragón vuela en una órbita espiral inclinada dejando una estela de plasma y fuego, se clava en el centro y se expande en el marco de la ventana mientras la aplicación aparece en fundido suave.
* **Animación Inversa de Cierre:** El marco de la ventana implosiona hacia su centro en un vórtice, liberando al dragón que despega en espiral hacia el fondo.
* **Dimensionamiento Automático (`960x620`):** Todas las aplicaciones se abren de forma consistente y centradas.
* **Motor Basado en Eventos Nativos X11:** Uso de procesador en reposo: **0.0%**.

---

## 🚀 Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU-USUARIO/Kali-Dragon-Suite.git
cd Kali-Dragon-Suite

# 2. Ejecutar el menú interactivo de instalación
sudo ./install.sh
```

### ⚡ Instalación Rápida por Línea de Comandos:
También puedes especificar directamente el color deseado:

```bash
sudo ./install.sh --color red      # 🔴 Crimson Red
sudo ./install.sh --color blue     # 🔵 Plasma Blue
sudo ./install.sh --color green    # 🟢 Toxic Green
sudo ./install.sh --color yellow   # 🟡 Cyber Yellow
sudo ./install.sh --color purple   # 🟣 Neon Purple
sudo ./install.sh --color orange   # 🟠 Neon Orange
sudo ./install.sh --color lime     # 🍈 Electric Lime
sudo ./install.sh --color pink     # 🌸 Cyber Pink
```

---

## 🔄 Restauración / Desinstalación

Si en cualquier momento deseas restaurar la configuración original de fábrica de Kali Linux:

```bash
sudo ./uninstall.sh
```

---

## 📁 Estructura del Repositorio

```text
Kali-Dragon-Suite/
├── README.md                          # Documentación completa
├── LICENSE                            # Licencia MIT
├── install.sh                         # Menú interactivo de instalación multi-color
├── uninstall.sh                       # Restaurador de fábrica
├── builder.py                         # Motor de renderizado y generador de variantes
├── assets/                            # Wallpapers y previews de los 8 colores
└── variants/                          # Suites completas pre-renderizadas:
    ├── red/                           # 🔴 Crimson Red
    ├── blue/                          # 🔵 Plasma Blue
    ├── green/                         # 🟢 Toxic Green
    ├── yellow/                        # 🟡 Cyber Yellow
    ├── purple/                        # 🟣 Neon Purple
    ├── orange/                        # 🟠 Neon Orange
    ├── lime/                          # 🍈 Electric Lime
    └── pink/                          # 🌸 Cyber Pink
```

---

## 📄 Licencia

Distribuido bajo la Licencia MIT. Consulta `LICENSE` para más información.
