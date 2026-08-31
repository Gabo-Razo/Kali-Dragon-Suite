#!/bin/bash
# ==============================================================================
#  KALI DRAGON SUITE - RESTORE / UNINSTALL SCRIPT (MODULAR)
#  Restores Original Factory Settings for Kali Linux (GRUB, Plymouth, LightDM, Icons, GTK)
# ==============================================================================

set -e

RED="\033[0;31m"
GREEN="\033[0;32m"
CYAN="\033[0;36m"
YELLOW="\033[1;33m"
BOLD="\033[1m"
NC="\033[0m"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_USER="${SUDO_USER:-$USER}"
TARGET_HOME=$(getent passwd "$TARGET_USER" | cut -d: -f6)

RESTORE_GRUB=false
RESTORE_PLYMOUTH=false
RESTORE_LOGIN=false
RESTORE_BORDERS=false
RESTORE_ANIMATOR=false
RESTORE_WALLPAPER=false
RESTORE_ICONS=false
RESTORE_TERMINAL=false
MODULAR_FLAG_PASSED=false
REMOVE_CUSTOM_ICONS=false
DEFAULT_ICON_THEME="Flat-Remix-Blue-Dark"
DEFAULT_GTK_THEME="Kali-Dark"

# CLI Arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --all)
            RESTORE_GRUB=true
            RESTORE_PLYMOUTH=true
            RESTORE_LOGIN=true
            RESTORE_BORDERS=true
            RESTORE_ANIMATOR=true
            RESTORE_WALLPAPER=true
            RESTORE_ICONS=true
            RESTORE_TERMINAL=true
            MODULAR_FLAG_PASSED=true
            shift
            ;;
        --boot-only)
            RESTORE_GRUB=true
            RESTORE_PLYMOUTH=true
            MODULAR_FLAG_PASSED=true
            shift
            ;;
        --grub-only)
            RESTORE_GRUB=true
            MODULAR_FLAG_PASSED=true
            shift
            ;;
        --plymouth-only)
            RESTORE_PLYMOUTH=true
            MODULAR_FLAG_PASSED=true
            shift
            ;;
        --login-only)
            RESTORE_LOGIN=true
            MODULAR_FLAG_PASSED=true
            shift
            ;;
        --desktop-only)
            RESTORE_BORDERS=true
            RESTORE_ANIMATOR=true
            RESTORE_WALLPAPER=true
            RESTORE_ICONS=true
            RESTORE_TERMINAL=true
            MODULAR_FLAG_PASSED=true
            shift
            ;;
        --icons-only)
            RESTORE_ICONS=true
            MODULAR_FLAG_PASSED=true
            shift
            ;;
        --borders-only)
            RESTORE_BORDERS=true
            MODULAR_FLAG_PASSED=true
            shift
            ;;
        --wallpaper-only)
            RESTORE_WALLPAPER=true
            MODULAR_FLAG_PASSED=true
            shift
            ;;
        --animator-only)
            RESTORE_ANIMATOR=true
            MODULAR_FLAG_PASSED=true
            shift
            ;;
        --terminal-only)
            RESTORE_TERMINAL=true
            MODULAR_FLAG_PASSED=true
            shift
            ;;
        --clean)
            REMOVE_CUSTOM_ICONS=true
            shift
            ;;
        --icon-theme|-t)
            DEFAULT_ICON_THEME="$2"
            shift 2
            ;;
        --help|-h)
            echo -e "${BOLD}Uso:${NC} sudo ./uninstall.sh [OPCIONES]"
            echo -e "\n${BOLD}Opciones Modulares:${NC}"
            echo -e "  --all             Restaura absolutamente todos los componentes a estado de fabrica"
            echo -e "  --boot-only       Restaura unicamente GRUB y Plymouth"
            echo -e "  --grub-only       Restaura solo el menu de arranque GRUB"
            echo -e "  --plymouth-only   Restaura solo la pantalla de carga Plymouth"
            echo -e "  --login-only      Restaura solo la pantalla de inicio de sesion (LightDM)"
            echo -e "  --desktop-only    Restaura iconos, bordes GTK, fondo de pantalla, terminal y animador"
            echo -e "  --icons-only      Restaura el tema de iconos a Flat-Remix-Blue-Dark"
            echo -e "  --borders-only    Restaura el tema de bordes y ventanas a Kali-Dark"
            echo -e "  --wallpaper-only  Restaura el fondo de pantalla predeterminado de Kali"
            echo -e "  --animator-only   Detiene y desactiva el servicio del animador de ventanas"
            echo -e "  --terminal-only   Restaura los colores originales del prompt ZSH y terminal"
            echo -e "  --clean           Elimina las carpetas de temas Kali-Dragon instaladas"
            echo -e "  --icon-theme <t>  Especifica un tema de iconos alternativo a restaurar"
            echo -e "  -h, --help        Muestra esta ayuda"
            exit 0
            ;;
        *)
            shift
            ;;
    esac
done

if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}${BOLD}[!] Se requieren permisos de administrador (sudo).${NC}"
    echo -e "    Por favor ejecuta: ${BOLD}sudo ./uninstall.sh${NC}\n"
    exit 1
fi

# If no flags passed, interactive menu
if [ "$MODULAR_FLAG_PASSED" = false ]; then
    echo -e "${CYAN}${BOLD}"
    echo "========================================================================"
    echo "       K A L I   D R A G O N   S U I T E   -   D E S I N S T A L A D O R "
    echo "        Restauracion de configuraciones originales de fabrica          "
    echo "========================================================================"
    echo -e "${NC}"
    echo -e "${BOLD}Elige que componentes deseas restaurar:${NC}\n"
    echo -e "  [1] Restaurar TODO a estado de fabrica original"
    echo -e "  [2] Restaurar solo Arranque (GRUB + Plymouth)"
    echo -e "  [3] Restaurar solo Inicio de Sesion (LightDM)"
    echo -e "  [4] Restaurar solo Entorno de Escritorio (Iconos + Bordes + Wallpaper)"
    echo -e "  [5] Restaurar solo Suite de Iconos (Flat-Remix-Blue-Dark)"
    echo -e "  [6] Salir sin cambios\n"

    read -rp "Selecciona una opcion [1-6]: " opt
    case "$opt" in
        1)
            RESTORE_GRUB=true; RESTORE_PLYMOUTH=true; RESTORE_LOGIN=true
            RESTORE_BORDERS=true; RESTORE_ANIMATOR=true; RESTORE_WALLPAPER=true
            RESTORE_ICONS=true; RESTORE_TERMINAL=true
            ;;
        2) RESTORE_GRUB=true; RESTORE_PLYMOUTH=true ;;
        3) RESTORE_LOGIN=true ;;
        4)
            RESTORE_BORDERS=true; RESTORE_ANIMATOR=true
            RESTORE_WALLPAPER=true; RESTORE_ICONS=true; RESTORE_TERMINAL=true
            ;;
        5) RESTORE_ICONS=true ;;
        6) echo -e "\nCancelado."; exit 0 ;;
        *) echo -e "\n${RED}Opcion invalida.${NC}"; exit 1 ;;
    esac
fi

echo -e "\n${CYAN}${BOLD}=== Iniciando proceso de restauracion ===${NC}\n"

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

# 1. Restore GRUB
if [ "$RESTORE_GRUB" = true ]; then
    echo -e "${CYAN}[*] Restaurando tema original de GRUB...${NC}"
    if [ -d "/boot/grub/themes/kali.pristine_backup" ]; then
        cp -rf /boot/grub/themes/kali.pristine_backup/* /boot/grub/themes/kali/
    fi
    echo -e "    ${GREEN}[OK] Menu de arranque GRUB restaurado.${NC}"
fi

# 2. Restore Plymouth
if [ "$RESTORE_PLYMOUTH" = true ]; then
    echo -e "${CYAN}[*] Restaurando tema original de Plymouth...${NC}"
    if [ -d "/usr/share/plymouth/themes/kali.pristine_backup" ]; then
        cp -rf /usr/share/plymouth/themes/kali.pristine_backup/* /usr/share/plymouth/themes/kali/
    fi
    echo -e "    ${GREEN}[OK] Pantalla de carga Plymouth restaurada.${NC}"
fi

# 3. Restore LightDM
if [ "$RESTORE_LOGIN" = true ]; then
    echo -e "${CYAN}[*] Restaurando configuracion original de LightDM...${NC}"
    if [ -f "/etc/lightdm/lightdm-gtk-greeter.conf.pristine_backup" ]; then
        cp -f /etc/lightdm/lightdm-gtk-greeter.conf.pristine_backup /etc/lightdm/lightdm-gtk-greeter.conf
    fi
    echo -e "    ${GREEN}[OK] Pantalla de inicio de sesion restaurada.${NC}"
fi

# 4. Restore Desktop Borders & GTK
if [ "$RESTORE_BORDERS" = true ]; then
    echo -e "${CYAN}[*] Restaurando tema de ventanas GTK y bordes a $DEFAULT_GTK_THEME...${NC}"
    if [ -n "$DBUS_ADDR" ]; then
        sudo -u "$TARGET_USER" DISPLAY="$USER_DISP" DBUS_SESSION_BUS_ADDRESS="$DBUS_ADDR" xfconf-query -c xsettings -p /Net/ThemeName -s "$DEFAULT_GTK_THEME" 2>/dev/null || true
        sudo -u "$TARGET_USER" DISPLAY="$USER_DISP" DBUS_SESSION_BUS_ADDRESS="$DBUS_ADDR" xfconf-query -c xfwm4 -p /general/theme -s "$DEFAULT_GTK_THEME" 2>/dev/null || true
    fi
    echo -e "    ${GREEN}[OK] Tema GTK restaurado a $DEFAULT_GTK_THEME.${NC}"
fi

# 5. Stop & Disable Window Animator
if [ "$RESTORE_ANIMATOR" = true ]; then
    echo -e "${CYAN}[*] Deteniendo y desactivando animador orbital de ventanas...${NC}"
    if [ -n "$DBUS_ADDR" ]; then
        sudo -u "$TARGET_USER" DBUS_SESSION_BUS_ADDRESS="$DBUS_ADDR" systemctl --user stop dragon-animator.service 2>/dev/null || true
        sudo -u "$TARGET_USER" DBUS_SESSION_BUS_ADDRESS="$DBUS_ADDR" systemctl --user disable dragon-animator.service 2>/dev/null || true
    fi
    echo -e "    ${GREEN}[OK] Animador de ventanas desactivado.${NC}"
fi

# 6. Restore Wallpaper
if [ "$RESTORE_WALLPAPER" = true ]; then
    echo -e "${CYAN}[*] Restaurando fondo de pantalla predeterminado de Kali...${NC}"
    DEFAULT_WALL="/usr/share/backgrounds/kali/kali-cube.png"
    if [ ! -f "$DEFAULT_WALL" ]; then
        DEFAULT_WALL=$(find /usr/share/backgrounds/kali/ -type f 2>/dev/null | head -n 1 || true)
    fi
    if [ -n "$DEFAULT_WALL" ] && [ -n "$DBUS_ADDR" ]; then
        for prop in $(sudo -u "$TARGET_USER" DISPLAY="$USER_DISP" DBUS_SESSION_BUS_ADDRESS="$DBUS_ADDR" xfconf-query -c xfce4-desktop -l 2>/dev/null | grep "last-image" || true); do
            sudo -u "$TARGET_USER" DISPLAY="$USER_DISP" DBUS_SESSION_BUS_ADDRESS="$DBUS_ADDR" xfconf-query -c xfce4-desktop -p "$prop" -s "$DEFAULT_WALL" 2>/dev/null || true
        done
    fi
    echo -e "    ${GREEN}[OK] Fondo de pantalla restaurado.${NC}"
fi

# 7. Restore Icon Theme
if [ "$RESTORE_ICONS" = true ]; then
    echo -e "${CYAN}[*] Restaurando suite de iconos a $DEFAULT_ICON_THEME...${NC}"
    if [ -n "$DBUS_ADDR" ]; then
        sudo -u "$TARGET_USER" DISPLAY="$USER_DISP" DBUS_SESSION_BUS_ADDRESS="$DBUS_ADDR" xfconf-query -c xsettings -p /Net/IconThemeName -s "$DEFAULT_ICON_THEME" 2>/dev/null || true
        sudo -u "$TARGET_USER" DISPLAY="$USER_DISP" DBUS_SESSION_BUS_ADDRESS="$DBUS_ADDR" gsettings set org.gnome.desktop.interface icon-theme "$DEFAULT_ICON_THEME" 2>/dev/null || true
        sudo -u "$TARGET_USER" DISPLAY="$USER_DISP" DBUS_SESSION_BUS_ADDRESS="$DBUS_ADDR" xfdesktop --reload 2>/dev/null || true
        sudo -u "$TARGET_USER" DISPLAY="$USER_DISP" DBUS_SESSION_BUS_ADDRESS="$DBUS_ADDR" xfce4-panel -r 2>/dev/null || true
    fi

    if [ "$REMOVE_CUSTOM_ICONS" = true ]; then
        echo -e "    -> Eliminando variantes Kali-Dragon-Icons de ~/.local y /usr/share..."
        rm -rf "$TARGET_HOME/.local/share/icons/Kali-Dragon-Icons-"* 2>/dev/null || true
        rm -rf /usr/share/icons/Kali-Dragon-Icons-* 2>/dev/null || true
    fi

    rm -rf "$TARGET_HOME/.cache/thumbnails/normal/"* "$TARGET_HOME/.cache/thumbnails/large/"* "$TARGET_HOME/.cache/thumbnails/fail/"* 2>/dev/null || true
    thunar -q 2>/dev/null || true
    echo -e "    ${GREEN}[OK] Tema de iconos restaurado a $DEFAULT_ICON_THEME.${NC}"
fi

# 8. Restore Terminal Prompt
if [ "$RESTORE_TERMINAL" = true ]; then
    echo -e "${CYAN}[*] Restaurando colores de la terminal...${NC}"
    ZSHRC_FILE="$TARGET_HOME/.zshrc"
    if [ -f "$ZSHRC_FILE" ]; then
        sed -i -E "s/%F\{[0-9]+\}┌──/%F{196}┌──/g" "$ZSHRC_FILE" 2>/dev/null || true
        sed -i -E "s/%F\{[0-9]+\}%n/%F{160}%n/g" "$ZSHRC_FILE" 2>/dev/null || true
        sed -i -E "s/\)%b%F\{[0-9]+\}\]/\)%b%F{196}\]/g" "$ZSHRC_FILE" 2>/dev/null || true
    fi
    QTERM_CFG="$TARGET_HOME/.config/qterminal.org/qterminal.ini"
    if [ -f "$QTERM_CFG" ]; then
        sed -i -E "s/ColorCursor=.*/ColorCursor=#ff1744/g" "$QTERM_CFG" 2>/dev/null || true
    fi
    echo -e "    ${GREEN}[OK] Terminal restaurada.${NC}"
fi

# Rebuild Bootloader & Initramfs if boot components were restored
if [ "$RESTORE_GRUB" = true ] || [ "$RESTORE_PLYMOUTH" = true ]; then
    echo -e "\n${CYAN}[*] Recompilando GRUB e Initramfs...${NC}"
    if [ "$RESTORE_GRUB" = true ]; then
        update-grub
    fi
    if [ "$RESTORE_PLYMOUTH" = true ]; then
        plymouth-set-default-theme -R kali 2>/dev/null || update-initramfs -u
    fi
fi

echo -e "\n${GREEN}${BOLD}========================================================================${NC}"
echo -e "${GREEN}${BOLD}  [OK] CONFIGURACION ORIGINAL RESTAURADA CON EXITO                      ${NC}"
echo -e "${GREEN}${BOLD}========================================================================${NC}\n"
