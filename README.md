<div align="center">

# KALI DRAGON SUITE
### *Transformacion Cyberpunk y Neon Modular para Kali Linux (XFCE)*

[![OS: Kali Linux](https://img.shields.io/badge/OS-Kali%20Linux%20%2F%20Debian-557C94?style=for-the-badge&logo=kalilinux&logoColor=white)](https://www.kali.org/)
[![Desktop: XFCE4](https://img.shields.io/badge/Desktop-XFCE4-00A4E4?style=for-the-badge&logo=xfce&logoColor=white)](https://www.xfce.org/)
[![Editions: 15 Colors](https://img.shields.io/badge/Editions-15%20Neon%20Colors-FF1744?style=for-the-badge&logo=palette&logoColor=white)](#ediciones-de-color)
[![Performance: 60 FPS](https://img.shields.io/badge/Performance-60%20FPS%20Native-00E676?style=for-the-badge&logo=speedtest&logoColor=white)](#caracteristicas-tecnicas)
[![License: MIT](https://img.shields.io/badge/License-MIT-FAD02C?style=for-the-badge)](LICENSE)

<br/>

> **Una suite completa, modular y ligera disenada para transformar la apariencia visual de Kali Linux:**  
> Menu de arranque GRUB 1080p, pantalla de carga Plymouth, inicio de sesion LightDM, bloqueo de pantalla glassmorphic, bordes neon de 2px, animador cinematico del dragon (60 FPS), temas GTK3/4 de alto contraste, suite de iconos wireframe neon con cero fallbacks y prompt para la terminal ZSH.

</div>

---

## Tabla de Contenido
1. [Nota del Creador](#nota)
2. [Inicio Rapido](#inicio-rapido-instalacion-en-1-paso)
3. [Componentes del Proyecto](#que-hace-este-proyecto)
4. [Galeria Visual](#galeria-visual)
5. [Suite de Iconos: Arquitectura y Familias](#suite-de-iconos-wireframe-neon)
6. [Ediciones de Color (15 Variantes)](#ediciones-de-color)
7. [Modulos de Instalacion](#modulos-disponibles)
8. [Guias de Instalacion](#guias-de-instalacion)
9. [Restauracion y Desinstalacion](#restauracion-y-desinstalacion-cero-riesgos)
10. [Estructura del Repositorio](#estructura-del-proyecto)
11. [Caracteristicas Tecnicas](#caracteristicas-tecnicas)
12. [Soporte y Donaciones](#soporte-y-contribuciones)

---

## NOTA

> *"Este es mi primer proyecto que desarrollo para Linux y quise compartirlo con la comunidad. La idea nacio para darle a Kali Linux una estetica neon / cyberpunk visualmente destacada, manteniendolo ligero y sin sobrecargar los recursos de la maquina.*  
> *Varias de las texturas y artes base se generaron con ayuda de Gemini. Si llegan a encontrar algun detalle, fallo visual o tienen alguna propuesta de mejora, con toda confianza abran un [Issue](https://github.com/Gabo-Razo/Kali-Dragon-Suite/issues) y tratare de responder y solucionarlo lo antes posible. Ojala les sea de gran utilidad y lo disfruten."*  
> — **Gabo Razo** ([@Gabo-Razo](https://github.com/Gabo-Razo))

---

## Inicio Rapido (Instalacion en 1 Paso)

Si deseas probar la suite completa de inmediato en tu equipo:

```bash
git clone https://github.com/Gabo-Razo/Kali-Dragon-Suite.git
cd Kali-Dragon-Suite
sudo ./install.sh
```
*El instalador abrira un menu interactivo numerado para que elijas tu color favorito y que partes deseas instalar.*

---

## ¿Que hace este proyecto?

Kali Dragon Suite transforma de manera segura y modular los componentes visuales del sistema operativo:

* **Menu de Arranque (GRUB):** La pantalla de inicio 1080p en alta definicion con marco cibernetico y mas de 70 iconos tematicos para cada sistema operativo instalado.
* **Pantalla de Carga (Plymouth):** La animacion fluida del dragon sobre fondo negro puro que aparece mientras arranca el sistema antes de iniciar sesion.
* **Pantalla de Login (LightDM):** La interfaz de bienvenida y acceso con tarjeta glassmorphic y selector circular de usuario iluminado.
* **Pantalla de Bloqueo (Screensaver):** Tarjeta de autenticacion con avatar y campo de contrasena para desbloqueo rapido.
* **Bordes de Ventana (XFWM4 y GTK3/4):** Marcos delgados de 2px con resplandor neon, sin transparencias defectuosas y con fondos oscuros profundos (`#16191f` y `#23252e`) que garantizan perfecta legibilidad.
* **Animador del Dragon (60 FPS):** Un daemon nativo en segundo plano que detecta la apertura de ventanas y lanza un dragon con estela de plasma recorriendo sus bordes.
* **Suite de Iconos Wireframe Neon (Kali Dragon Icons):** Mas de 1000+ iconos vectoriales SVG con diseno de planos ciberneticos blueprint, papelera independiente y organizacion por familias tecnologicas con 100% de coincidencia y cero iconos genericos perdidos.
* **Prompt de Terminal (ZSH):** Diseno de dos lineas con colores coordinados y cursor solido sin latencia.

---

## Galeria Visual

<div align="center">

### 1. Suite de Iconos Wireframe Neon (Blueprint Cyberpunk & Familias Tecnologicas)
*Iconos vectoriales en alta definicion con doble contorno neon, halo de resplandor exterior, papelera cibernetica y organizacion exhaustiva por ecosistemas.*

![Iconos Wireframe Neon](assets/previews/6_icons_wireframe_showcase.png)

<br/>

### 2. Animador Cinematico del Dragon (Vuelo en Ventanas a 60 FPS)
*El dragon recorre el perimetro de cada ventana abierta con particulas de plasma a 60 cuadros por segundo.*

![Dragon Window Animation](assets/previews/5_dragon_window_animation.gif)

<br/>

### 3. Menu de Arranque GRUB (1080p Crystal Glass)
*Fondo oscuro con aura neon, panel traslucido y 70+ iconos de distribuciones y sistemas operativos.*

![GRUB Boot Menu](assets/previews/1_grub_boot_menu.png)

<br/>

### 4. Pantalla de Carga Plymouth (Neon Splash)
*Animacion de carga limpia y optimizada sobre lienzo negro puro.*

![Plymouth Animation](assets/previews/3_plymouth_animation.png)

<br/>

### 5. Pantalla de Bloqueo y Suspension (xfce4-screensaver)
*Dialogo glassmorphic con avatar de usuario iluminado y botones de sesion.*

![Lockscreen Dialog](assets/previews/2_lockscreen_dialog.png)

<br/>

### 6. Bordes Finos de 2px y Tema de Escritorio (GTK3 & GTK4)
*Ventanas con contorno neon de 2px, botones circulares estilo terminal y fondos solidos de alto contraste.*

![Desktop Window Borders](assets/previews/4_desktop_window_borders.png)

</div>

---

## Suite de Iconos: Wireframe Neon

La suite de iconos **Kali-Dragon-Icons** fue generada mediante un motor vectorial en Ruby 3.3, garantizando que cada archivo, carpeta y dispositivo este disenado como un plano blueprint cibernetico con halo de brillo exterior (`feGaussianBlur`), doble contorno fino y caja de identificacion inferior.

### 1. Directorios del Sistema y Elementos Modificados

| Directorio | Tipo de Elemento | Descripcion de los Cambios |
| :--- | :--- | :--- |
| `scalable/places/` | Carpetas del Sistema | Home, Escritorio, Descargas, Documentos, Musica, Imagenes, Videos, Plantillas, Publico, Proyectos de Codigo, Repositorios Git y Entornos Virtuales Python (`venv`). |
| `scalable/status/` | Papelera de Reciclaje | Papelera independiente en estado Vacio y Lleno con senal de advertencia cibernetica y nucleo de plasma. |
| `scalable/devices/` | Dispositivos y Red | Discos duros, memorias flash USB, medios extraibles, equipos locales y servidores de red. |
| `scalable/apps/` | Lanzadores y Binarios | Accesos directos `.desktop`, ejecutables de Windows `.exe` y paquetes ejecutables Linux `.appimage`. |
| `scalable/mimetypes/` | Archivos y Documentos | Mas de 1000+ definiciones MIME de codigo fuente, datos cientificos, multimedia y ofimatica. |
| `symbolic/` | Barras Laterales | Iconos monocromaticos de 16x16 para la barra lateral de Thunar y los paneles de XFCE. |

---

### 2. Relacion de Familias Tecnologicas Unificadas

Para evitar incoherencias visuales, los archivos pertenecientes a una misma tecnologia comparten su emblema geometrico central caracteristico y se diferencian por el texto de su banner inferior:

| Familia Tecnologica | Formatos y Extensiones Incluidas | Emblema Visual |
| :--- | :--- | :--- |
| **Familia Ruby** | `.rb`, `.erb`, `.rake`, `Gemfile`, `Rakefile` | Diamante facetado con cortes geometricos. |
| **Familia Python** | `.py`, `.pyw`, `.pyx`, `.pyi`, `.ipynb` | Serpientes ciberneticas duales / Orbitas cuanticas. |
| **Familia C y C++** | `.c`, `.h`, `.cpp`, `.hpp`, `.hh`, `.hxx`, `.inl`, `.tpp` | Hexagono blindado con identificador tipografico central. |
| **Familia C# y .NET** | `.cs`, `.vb`, `.fs` | Hexagono blindado con nucleo de lenguaje. |
| **Familia JavaScript y TypeScript** | `.js`, `.jsx`, `.ts`, `.tsx`, `.mjs`, `.cjs` | Badge rectangular de desarrollo de alta densidad. |
| **Familia Hojas de Estilo Web** | `.css`, `.scss`, `.sass`, `.less`, `.styl` | Escudo angular `#` de estilizacion web. |
| **Familia Servicios Systemd** | `.service`, `.timer`, `.socket`, `.target`, `.mount`, `.swap` | Anillo orbital con rayo central de ejecucion de procesos. |
| **Familia Videojuegos (Game Dev)** | `.gd`, `.tscn`, `.tres`, `.godot`, `.unity`, `.prefab` | Mando retrofuturista con cruceta y botones de accion. |
| **Familia Bases de Datos** | `.sql`, `.sqlite`, `.db`, `.s3db` | Cilindro de almacenamiento de tres niveles jerarquicos. |
| **Familia DevOps e Infraestructura** | `Dockerfile`, `docker-compose.yml`, `Chart.yaml` / K8s, `.tf`, `.tfvars`, `Makefile`, `CMakeLists.txt`, `Jenkinsfile` | Contenedor de carga estibado, timon Kubernetes e insignias CI. |
| **Familia Ciberseguridad y Forense** | `.pcap`, `.pcapng`, `.cap` (Wireshark), `.key`, `.pem`, `.crt`, `.kdbx` (KeePass), `.yar` (YARA), `.ovpn` (VPN) | Aleta de captura de paquetes, llave maestra y candado criptografico. |
| **Familia Hardware y EDA** | `.ino` (Arduino), `.hex`, `.bin`, `.vhd` (VHDL), `.v` / `.sv` (Verilog) | Bucle infinito con polaridad +/- y compuertas logicas. |
| **Familia Documentos Ofimaticos** | `.doc`, `.docx`, `.odt`, `.rtf`, `.pages` | Pagina de texto estructurado. |
| **Familia Hojas de Calculo** | `.xls`, `.xlsx`, `.ods`, `.csv`, `.tsv` | Matriz cuadriculada de filas y columnas. |
| **Familia Presentaciones** | `.ppt`, `.pptx`, `.odp`, `.key` | Proyector con grafica circular de sectores. |
| **Familia Lectura Digital y Comics** | `.epub`, `.mobi`, `.djvu`, `.cbr`, `.cbz` | Libro isometrico abierto con lomo iluminado. |
| **Familia 3D y Diseno CAD** | `.3ds`, `.blend`, `.obj`, `.stl`, `.gltf`, `.glb`, `.dxf`, `.step`, `.stp` | Poliedro tridimensional isometrico con aristas wireframe. |
| **Familia Shells y Scripts** | `.sh`, `.bash`, `.zsh`, `.ps1`, `.bat`, `.cmd` | Pantalla de consola interactiva con prompt `>_`. |
| **Familia Subtitulos** | `.srt`, `.vtt`, `.ass`, `.sub` | Marco CC de subtitulado sincronizado. |
| **Familia Multimedia** | Vector (`.svg`), Imagen (`.png`, `.jpg`, `.webp`, `.gif`), Audio (`.mp3`, `.wav`, `.flac`), Video (`.mp4`, `.mkv`, `.avi`) | Trazado de nodos, paisaje geometrico, ecualizador de ondas y reproductor. |
| **Otros Lenguajes Integrados** | `.java`, `.kt`, `.swift`, `.dart`, `.rs`, `.go`, `.lua`, `.php`, `.vue`, `.svelte`, `.astro`, `.zig`, `.sol`, `.mat`, `.r`, `.jl`, `.nim`, `.asm`, `.tex` | Emblemas nativos estilizados en alambre neón con sus tipografias oficiales. |

---

## Ediciones de Color

La suite incluye 15 ediciones de color calculadas para mantener una saturacion neón brillante sin fatiga visual:

| # | Edicion | Flag CLI | Color Primario | Color Secundario | Estilo y Ambientacion |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 1 | **Crimson Red** | `red` | `#ff1744` | `#ec0101` | Rojo Neon Carmesi (Edicion Original de Kali Dragon) |
| 2 | **Plasma Blue** | `blue` | `#00b0ff` | `#2979ff` | Azul Electrico Cyberpunk / Alta Tension |
| 3 | **Toxic Green** | `green` | `#00e676` | `#00c853` | Verde Hacker Matrix / Terminal Clasica |
| 4 | **Cyber Yellow** | `yellow` | `#ffd600` | `#ffc107` | Amarillo Neon Intenso / Alerta Industrial |
| 5 | **Neon Purple** | `purple` | `#d500f9` | `#aa00ff` | Morado Synthwave / Ciudad Nocturna |
| 6 | **Neon Orange** | `orange` | `#ff6d00` | `#ff5722` | Naranja Incandescente / Fuego y Lava |
| 7 | **Electric Lime** | `lime` | `#76ff03` | `#64dd17` | Verde Lima Acido / Radiacion Cyber |
| 8 | **Cyber Pink** | `pink` | `#ff4081` | `#f50057` | Rosa Neon Arcade / Neon City |
| 9 | **Neon Cyan** | `cyan` | `#18ffff` | `#00e5ff` | Azul Hielo / Glaciar Artico |
| 10 | **Neon Teal** | `teal` | `#00f2fe` | `#00b4d8` | Turquesa Neon / Cyber Aqua |
| 11 | **Cyber Gold** | `gold` | `#ffab00` | `#ffd700` | Oro Metalico / Ambar Night City |
| 12 | **Royal Indigo** | `indigo` | `#536dfe` | `#3d5afe` | Azul Indigo / Zafiro Profundo |
| 13 | **Quantum Mint** | `mint` | `#64ffda` | `#00bfa5` | Verde Menta Cuantico / Cristal de Plasma |
| 14 | **Blood Ruby** | `ruby` | `#e91e63` | `#c2185b` | Rojo Rubi / Vino Oscuro Cyber |
| 15 | **Cyber Magenta** | `magenta` | `#ff007f` | `#e00070` | Magenta Neon / Retrowave Anos 80 |

---

## Modulos Disponibles

Puedes instalar o desinstalar selectivamente componentes mediante flags de linea de comandos:

| Modulo | Flag CLI | Componentes que Abarca |
| :--- | :--- | :--- |
| **Suite Completa** | `--all` | Despliega los 8 componentes al mismo tiempo. |
| **Todo el Arranque** | `--boot-only` | Menu de arranque GRUB 1080p + Pantalla de carga Plymouth. |
| **Solo GRUB** | `--grub-only` | Menu de inicio GRUB con 70+ iconos de sistemas operativos. |
| **Solo Plymouth** | `--plymouth-only` | Animacion de carga del dragon antes del inicio de sesion. |
| **Solo Login y Bloqueo** | `--login-only` | LightDM Greeter, pantalla de bloqueo y cuadro de apagado. |
| **Solo Bordes de Ventana** | `--borders-only` | Bordes de 2px (XFWM4 & GTK3/4) con fondos solidos oscuros. |
| **Solo Animador** | `--animator-only` | Daemon orbital a 60 FPS con vuelo del dragon en ventanas. |
| **Solo Fondo de Pantalla** | `--wallpaper-only` | Wallpaper 1080p del Dragon en la edicion seleccionada. |
| **Solo Suite de Iconos** | `--icons-only` | Mas de 1000+ iconos wireframe neon con cero fallbacks. |
| **Solo Terminal** | `--terminal-only` | Prompt ZSH de dos lineas y colores del cursor de consola. |
| **Solo Escritorio** | `--desktop-only` | Bordes, animador, fondo, suite de iconos y terminal. |

---

## Guias de Instalacion

### 1. Instalador Maestro Modular (`install.sh`)
Permite instalar cualquier color y combinar componentes:

```bash
# Instalar toda la suite en Crimson Red:
sudo ./install.sh --color red --all

# Instalar unicamente la suite de iconos en Neon Purple:
sudo ./install.sh --color purple --icons-only

# Instalar todo el entorno de escritorio en Cyber Gold:
sudo ./install.sh --color gold --desktop-only

# Instalar solo el arranque (GRUB + Plymouth) en Plasma Blue:
sudo ./install.sh --color blue --boot-only
```

---

### 2. Instalador de Iconos Independiente (`install_icons.sh`)
Diseñado para instalar o alternar entre las 15 variantes de iconos de forma instantanea sin necesidad de `sudo`:

```bash
# Aplicar directamente un color por nombre:
./install_icons.sh red
./install_icons.sh purple
./install_icons.sh cyan
./install_icons.sh gold

# Abrir el menu interactivo numerado:
./install_icons.sh

# Instalacion global multiusuario (en /usr/share/icons):
sudo ./install_icons.sh --system -c green
```

---

## Restauracion y Desinstalacion (Cero Riesgos)

El proyecto incluye scripts modulares para regresar a la configuracion original de fabrica de Kali Linux en cualquier momento:

### 1. Desinstalador Modular Maestro (`uninstall.sh`)
```bash
# Restaurar absolutamente TODO a estado de fabrica original:
sudo ./uninstall.sh --all

# Restaurar solo los iconos originales de Kali (Flat-Remix-Blue-Dark):
sudo ./uninstall.sh --icons-only

# Restaurar solo el arranque original (GRUB + Plymouth):
sudo ./uninstall.sh --boot-only

# Restaurar solo la pantalla de inicio de sesion (LightDM):
sudo ./uninstall.sh --login-only

# Restaurar solo el entorno de escritorio (Iconos, Bordes GTK, Wallpaper y Terminal):
sudo ./uninstall.sh --desktop-only

# Restaurar todo y eliminar carpetas de temas instaladas:
sudo ./uninstall.sh --all --clean
```

---

### 2. Desinstalador de Iconos Independiente (`uninstall_icons.sh`)
Para volver a los iconos originales sin permisos de administrador:

```bash
# Restaurar tema de iconos original de Kali:
./uninstall_icons.sh

# Restaurar y borrar las carpetas de iconos personalizadas:
./uninstall_icons.sh --clean

# Restaurar hacia un tema alternativo especifico instalado en el sistema:
./uninstall_icons.sh -t "Papirus-Dark"
```

---

### 3. Desde la Interfaz Grafica de XFCE
1. Ve a **Menu de Aplicaciones -> Configuracion -> Apariencia** y selecciona `Kali-Dark`.
2. Ve a **Configuracion -> Gestor de Ventanas** y selecciona `Kali-Dark`.
3. Ve a **Configuracion -> Iconos** y selecciona `Flat-Remix-Blue-Dark`.

---

## Estructura del Proyecto

```text
Kali-Dragon-Suite/
├── install.sh                  # Instalador modular maestro de la suite
├── install_icons.sh            # Instalador independiente de la suite de iconos
├── uninstall.sh                # Desinstalador modular de fábrica
├── uninstall_icons.sh          # Desinstalador independiente de iconos
├── generate_dragon_icons.rb    # Motor compilador vectorial de iconos en Ruby
├── custom-cyber-dragon.xml     # Base de datos compartida de tipos MIME
├── assets/                     # Wallpapers, texturas, sprites y capturas
│   └── previews/               # Imagenes de muestra para la documentacion
├── variants/                   # Arbol de las 15 ediciones de color
│   ├── red/                    # Variantes Crimson Red (GRUB, Plymouth, GTK, Iconos)
│   ├── blue/                   # Variantes Plasma Blue
│   └── ...                     # (15 carpetas con recursos completos)
├── README.md                   # Documentacion oficial en Espanol
├── README_EN.md                # Documentacion oficial en Ingles
└── LICENSE                     # Licencia de codigo abierto MIT
```

---

## Caracteristicas Tecnicas

* **Consumo Ultrabajo (0.0% CPU en reposo):** El animador corre como daemon nativo con `systemd --user`, activandose exclusivamente cuando se crea una ventana mediante eventos X11.
* **Fondos 100% Solidos y Opacos (`#16191f` / `#23252e`):** Se eliminaron transparencias defectuosas para asegurar que Thunar, editores de codigo y terminales sean perfectamente legibles.
* **Arquitectura Vectorial SVG:** Todos los iconos conservan nitidez absoluta en monitores 1080p, 2K, 4K y pantallas HiDPI.
* **Relacion de Aspecto 1:1 Preservada:** El sprite del dragon vuela con sus proporciones matematicas reales, sin deformarse.
* **Tolerante a Reinicios y Suspension:** Los servicios se restauran automaticamente tras suspender o reiniciar el equipo.

---

## Soporte y Contribuciones

En caso de encontrar un fallo o tener propuestas de nuevos iconos o colores:
* Abre un **[Issue](https://github.com/Gabo-Razo/Kali-Dragon-Suite/issues)** detallando tu entorno o envia un Pull Request.
* Si el proyecto te resulto util, considera dejar una **Star** en el repositorio.

---

## Patrocinio y Donaciones

Si este proyecto te ha sido de utilidad y deseas apoyar su mantenimiento continuo:

<div align="center">

[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/Gabo-Razo)

*Cualquier apoyo o patrocinio es enormemente apreciado.*

</div>

---

<div align="center">

Desarrollado con dedicacion por **[Gabo Razo](https://github.com/Gabo-Razo)** para la comunidad de **Kali Linux & Open Source**.

</div>
