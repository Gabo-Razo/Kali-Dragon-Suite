#!/bin/bash
# ==============================================================================
#  KALI DRAGON ICONS - RESTORE / UNINSTALL SCRIPT
# Restores Original Factory Icon Theme (Flat-Remix-Blue-Dark) & Cleans Caches
# ==============================================================================

set -e

RED="\033[0;31m"
GREEN="\033[0;32m"
CYAN="\033[0;36m"
YELLOW="\033[1;33m"
BOLD="\033[1m"
NC="\033[0m"

TARGET_USER="${SUDO_USER:-$USER}"
TARGET_HOME=$(getent passwd "$TARGET_USER" | cut -d: -f6)

RESTORE_THEME="Flat-Remix-Blue-Dark"
REMOVE_CUSTOM=false

# CLI args
while [[ $# -gt 0 ]]; do
    case "$1" in
        --theme|-t)
            RESTORE_THEME="$2"
            shift 2
            ;;
        --clean|-c)
            REMOVE_CUSTOM=true
            shift
            ;;
        --help|-h)
            echo -e "${BOLD}Uso:${NC} ./uninstall_icons.sh [OPCIONES]"
            echo -e "\n${BOLD}Opciones:${NC}"
            echo -e "  -t, --theme <nombre>   Tema a restaurar (por defecto: Flat-Remix-Blue-Dark)"
            echo -e "  -c, --clean            Elimina las carpetas de Kali-Dragon-Icons-* instaladas"
            echo -e "  -h, --help             Muestra esta ayuda"
            exit 0
            ;;
        *)
            shift
            ;;
    esac
done

echo -e "${CYAN}${BOLD}[+] Restaurando tema de iconos original: ${RESTORE_THEME}...${NC}"

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

# Apply original theme in desktop
if [ -n "$DBUS_ADDR" ]; then
    echo -e "    -> Aplicando $RESTORE_THEME en XFCE / GNOME..."
    sudo -u "$TARGET_USER" DISPLAY="$USER_DISP" DBUS_SESSION_BUS_ADDRESS="$DBUS_ADDR" xfconf-query -c xsettings -p /Net/IconThemeName -s "$RESTORE_THEME" 2>/dev/null || true
    sudo -u "$TARGET_USER" DISPLAY="$USER_DISP" DBUS_SESSION_BUS_ADDRESS="$DBUS_ADDR" xfdesktop --reload 2>/dev/null || true
    sudo -u "$TARGET_USER" DISPLAY="$USER_DISP" DBUS_SESSION_BUS_ADDRESS="$DBUS_ADDR" xfce4-panel -r 2>/dev/null || true
    sudo -u "$TARGET_USER" DISPLAY="$USER_DISP" DBUS_SESSION_BUS_ADDRESS="$DBUS_ADDR" gsettings set org.gnome.desktop.interface icon-theme "$RESTORE_THEME" 2>/dev/null || true
fi

# Remove custom dragon themes if requested
if [ "$REMOVE_CUSTOM" = true ]; then
    echo -e "    -> Eliminando variantes Kali-Dragon-Icons de ~/.local/share/icons..."
    rm -rf "$TARGET_HOME/.local/share/icons/Kali-Dragon-Icons-"* 2>/dev/null || true
    if [ "$EUID" -eq 0 ]; then
        rm -rf /usr/share/icons/Kali-Dragon-Icons-* 2>/dev/null || true
    fi
fi

# Purge thumbnails
echo -e "    -> Purgando caché de miniaturas..."
rm -rf "$TARGET_HOME/.cache/thumbnails/normal/"* "$TARGET_HOME/.cache/thumbnails/large/"* "$TARGET_HOME/.cache/thumbnails/fail/"* 2>/dev/null || true

# Refresh Thunar
thunar -q 2>/dev/null || true

echo -e "\n${GREEN}${BOLD}========================================================================${NC}"
echo -e "${GREEN}${BOLD}  ✔ ¡TEMA DE ICONOS ORIGINAL RESTAURADO CORRECTAMENTE!                 ${NC}"
echo -e "${GREEN}${BOLD}  Tema Activo: ${RESTORE_THEME}                                         ${NC}"
echo -e "${GREEN}${BOLD}========================================================================${NC}\n"
