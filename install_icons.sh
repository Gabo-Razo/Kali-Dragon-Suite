#!/bin/bash
# ==============================================================================
#  KALI DRAGON ICONS - STANDALONE MODULAR INSTALLER (15 EDITIONS)
# Independent Icon Theme Installer & Live Desktop Synchronizer
# ==============================================================================

set -e

RED="\033[0;31m"
GREEN="\033[0;32m"
BLUE="\033[0;34m"
YELLOW="\033[1;33m"
PURPLE="\033[0;35m"
CYAN="\033[0;36m"
WHITE="\033[1;37m"
BOLD="\033[1m"
NC="\033[0m"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_USER="${SUDO_USER:-$USER}"
TARGET_HOME=$(getent passwd "$TARGET_USER" | cut -d: -f6)

SELECTED_COLOR=""
SYSTEM_WIDE=false

# CLI Arguments parsing
while [[ $# -gt 0 ]]; do
    case "$1" in
        --color|-c)
            SELECTED_COLOR="$2"
            shift 2
            ;;
        --system|-s)
            SYSTEM_WIDE=true
            shift
            ;;
        red|blue|green|yellow|purple|orange|lime|pink|cyan|teal|gold|indigo|mint|ruby|magenta)
            SELECTED_COLOR="$1"
            shift
            ;;
        --help|-h)
            echo -e "${BOLD}Uso:${NC} ./install_icons.sh [OPCIONES] [COLOR]"
            echo -e "\n${BOLD}Colores disponibles:${NC}"
            echo -e "  red, blue, green, yellow, purple, orange, lime, pink,"
            echo -e "  cyan, teal, gold, indigo, mint, ruby, magenta"
            echo -e "\n${BOLD}Opciones:${NC}"
            echo -e "  -c, --color <nombre>    Especifica el color directamente"
            echo -e "  -s, --system            Instalar globalmente en /usr/share/icons (requiere sudo)"
            echo -e "  -h, --help              Muestra esta ayuda"
            exit 0
            ;;
        *)
            shift
            ;;
    esac
done

# Interactive Menu if no color passed
if [ -z "$SELECTED_COLOR" ]; then
    echo -e "${CYAN}${BOLD}"
    echo "========================================================================"
    echo "       🐉  K A L I   D R A G O N   I C O N S   -   1 5   C O L O R S      "
    echo "              Instalador Independiente de Suite de Iconos               "
    echo "========================================================================"
    echo -e "${NC}"
    echo -e "${BOLD}Elige la edición de color que deseas aplicar:${NC}\n"
    echo -e "  ${RED}[1] 🔴 Crimson Red      (Rojo Carmesí Neón)${NC}"
    echo -e "  ${BLUE}[2] 🔵 Plasma Blue      (Azul Eléctrico Cyberpunk)${NC}"
    echo -e "  ${GREEN}[3] 🟢 Toxic Green      (Verde Hacker Neón)${NC}"
    echo -e "  ${YELLOW}[4] 🟡 Cyber Yellow     (Amarillo Neón Intenso)${NC}"
    echo -e "  ${PURPLE}[5] 🟣 Neon Purple      (Morado Synthwave)${NC}"
    echo -e "  ${YELLOW}[6] 🟠 Neon Orange      (Naranja Incandescente / Lava)${NC}"
    echo -e "  ${GREEN}[7] 🍈 Electric Lime    (Verde Lima Ácido)${NC}"
    echo -e "  ${PURPLE}[8] 🌸 Cyber Pink       (Rosa Neón Arcade)${NC}"
    echo -e "  ${CYAN}[9] 💎 Neon Cyan        (Azul Hielo / Arctic Ice)${NC}"
    echo -e "  ${CYAN}[10] 🌊 Neon Teal       (Turquesa Neón / Cyber Aqua)${NC}"
    echo -e "  ${YELLOW}[11] 🪙 Cyber Gold      (Oro Metálico / Night City Amber)${NC}"
    echo -e "  ${BLUE}[12] 🌌 Royal Indigo    (Azul Índigo / Zafiro Profundo)${NC}"
    echo -e "  ${CYAN}[13] 🧪 Quantum Mint    (Verde Menta Cuántico)${NC}"
    echo -e "  ${RED}[14] 🩸 Blood Ruby      (Rojo Rubí / Dark Wine)${NC}"
    echo -e "  ${PURPLE}[15] 🔮 Cyber Magenta   (Magenta Neón / Retrowave)${NC}"
    echo -e "  [0] Salir sin cambios\n"

    read -rp "Selecciona un color [1-15]: " opt
    case "$opt" in
        1) SELECTED_COLOR="red" ;;
        2) SELECTED_COLOR="blue" ;;
        3) SELECTED_COLOR="green" ;;
        4) SELECTED_COLOR="yellow" ;;
        5) SELECTED_COLOR="purple" ;;
        6) SELECTED_COLOR="orange" ;;
        7) SELECTED_COLOR="lime" ;;
        8) SELECTED_COLOR="pink" ;;
        9) SELECTED_COLOR="cyan" ;;
        10) SELECTED_COLOR="teal" ;;
        11) SELECTED_COLOR="gold" ;;
        12) SELECTED_COLOR="indigo" ;;
        13) SELECTED_COLOR="mint" ;;
        14) SELECTED_COLOR="ruby" ;;
        15) SELECTED_COLOR="magenta" ;;
        0) echo -e "\nCancelado."; exit 0 ;;
        *) echo -e "\n${RED}Opción inválida.${NC}"; exit 1 ;;
    esac
fi

# Capitalize color name
case "$SELECTED_COLOR" in
    red) CAP_COLOR="Red" ;;
    blue) CAP_COLOR="Blue" ;;
    green) CAP_COLOR="Green" ;;
    yellow) CAP_COLOR="Yellow" ;;
    purple) CAP_COLOR="Purple" ;;
    orange) CAP_COLOR="Orange" ;;
    lime) CAP_COLOR="Lime" ;;
    pink) CAP_COLOR="Pink" ;;
    cyan) CAP_COLOR="Cyan" ;;
    teal) CAP_COLOR="Teal" ;;
    gold) CAP_COLOR="Gold" ;;
    indigo) CAP_COLOR="Indigo" ;;
    mint) CAP_COLOR="Mint" ;;
    ruby) CAP_COLOR="Ruby" ;;
    magenta) CAP_COLOR="Magenta" ;;
    *) echo -e "${RED}[!] Color no reconocido: $SELECTED_COLOR${NC}"; exit 1 ;;
esac

ICON_THEME="Kali-Dragon-Icons-${CAP_COLOR}"
SOURCE_THEME_DIR="$SCRIPT_DIR/variants/$SELECTED_COLOR/desktop/icons/$ICON_THEME"

if [ ! -d "$SOURCE_THEME_DIR" ] && [ -d "$TARGET_HOME/.local/share/icons/$ICON_THEME" ]; then
    SOURCE_THEME_DIR="$TARGET_HOME/.local/share/icons/$ICON_THEME"
fi

if [ ! -d "$SOURCE_THEME_DIR" ]; then
    echo -e "${YELLOW}[*] Compilando iconos mediante generate_dragon_icons.rb...${NC}"
    ruby "$SCRIPT_DIR/generate_dragon_icons.rb"
fi

echo -e "\n${CYAN}${BOLD}[+] Instalando Tema de Iconos: ${ICON_THEME}...${NC}"

if [ "$SYSTEM_WIDE" = true ]; then
    if [ "$EUID" -ne 0 ]; then
        echo -e "${RED}[!] Se requiere sudo para instalación global (--system).${NC}"
        exit 1
    fi
    DEST_DIR="/usr/share/icons/$ICON_THEME"
else
    DEST_DIR="$TARGET_HOME/.local/share/icons/$ICON_THEME"
fi

mkdir -p "$DEST_DIR"
cp -rf "$SOURCE_THEME_DIR/"* "$DEST_DIR/"

# Synchronize custom shared MIME definitions
MIME_PACKAGES="$TARGET_HOME/.local/share/mime/packages"
mkdir -p "$MIME_PACKAGES"
if [ -f "$SCRIPT_DIR/custom-cyber-dragon.xml" ] && [ "$SCRIPT_DIR/custom-cyber-dragon.xml" != "$MIME_PACKAGES/custom-cyber-dragon.xml" ]; then
    cp -f "$SCRIPT_DIR/custom-cyber-dragon.xml" "$MIME_PACKAGES/"
fi
update-mime-database "$TARGET_HOME/.local/share/mime" 2>/dev/null || true

# Update GTK Icon Cache
echo -e "    -> Actualizando caché de iconos GTK..."
gtk-update-icon-cache -f -q "$DEST_DIR" 2>/dev/null || true

# Purge Thumbnail Cache
echo -e "    -> Purgando caché de miniaturas residuales..."
rm -rf "$TARGET_HOME/.cache/thumbnails/normal/"* "$TARGET_HOME/.cache/thumbnails/large/"* "$TARGET_HOME/.cache/thumbnails/fail/"* 2>/dev/null || true

# Detect active graphical session and DBus
USER_PID=$(pgrep -u "$TARGET_USER" xfce4-session | head -n 1 || true)
if [ -n "$USER_PID" ]; then
    DBUS_ADDR=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$USER_PID/environ 2>/dev/null | cut -d= -f2- | tr -d "\0" || true)
    USER_DISP=$(grep -z DISPLAY /proc/$USER_PID/environ 2>/dev/null | cut -d= -f2- | tr -d "\0" || echo ":0")
else
    USER_DISP=":0"
    DBUS_ADDR=""
fi

if [ -z "$DBUS_ADDR" ]; then
    TARGET_UID=$(id -u "$TARGET_USER" 2>/dev/null || echo "1000")
    if [ -S "/run/user/$TARGET_UID/bus" ]; then
        DBUS_ADDR="unix:path=/run/user/$TARGET_UID/bus"
    fi
fi

# Live Desktop Switch
echo -e "    -> Aplicando tema ${ICON_THEME} en el entorno de escritorio..."
if [ -n "$DBUS_ADDR" ]; then
    sudo -u "$TARGET_USER" DISPLAY="$USER_DISP" DBUS_SESSION_BUS_ADDRESS="$DBUS_ADDR" xfconf-query -c xsettings -p /Net/IconThemeName -s "$ICON_THEME" 2>/dev/null || true
    sudo -u "$TARGET_USER" DISPLAY="$USER_DISP" DBUS_SESSION_BUS_ADDRESS="$DBUS_ADDR" xfdesktop --reload 2>/dev/null || true
    sudo -u "$TARGET_USER" DISPLAY="$USER_DISP" DBUS_SESSION_BUS_ADDRESS="$DBUS_ADDR" xfce4-panel -r 2>/dev/null || true
    sudo -u "$TARGET_USER" DISPLAY="$USER_DISP" DBUS_SESSION_BUS_ADDRESS="$DBUS_ADDR" gsettings set org.gnome.desktop.interface icon-theme "$ICON_THEME" 2>/dev/null || true
fi

# Reload File Managers
thunar -q 2>/dev/null || true

echo -e "\n${GREEN}${BOLD}========================================================================${NC}"
echo -e "${GREEN}${BOLD}  ✔ ¡TEMA DE ICONOS INSTALADO Y APLICADO CON ÉXITO!                     ${NC}"
echo -e "${GREEN}${BOLD}  Edición Activa: ${CAP_COLOR^^} (${ICON_THEME})                          ${NC}"
echo -e "${GREEN}${BOLD}========================================================================${NC}\n"
