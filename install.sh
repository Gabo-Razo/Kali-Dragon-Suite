#!/bin/bash
# ==============================================================================
#  🐉 KALI DRAGON SUITE - MULTI-COLOR MASTER INSTALLER
#  Supports 8 Color Editions: Red, Blue, Green, Yellow, Purple, Orange, Lime, Pink
# ==============================================================================

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_USER="${SUDO_USER:-$USER}"
TARGET_HOME=$(getent passwd "$TARGET_USER" | cut -d: -f6)

if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}${BOLD}[!] Se requieren permisos de administrador (sudo).${NC}"
    echo -e "    Por favor ejecuta: ${BOLD}sudo ./install.sh${NC}\n"
    exit 1
fi

SELECTED_COLOR=""

# Check CLI argument: ./install.sh --color <name> or ./install.sh <name>
if [ "$1" == "--color" ] && [ -n "$2" ]; then
    SELECTED_COLOR="$2"
elif [ -n "$1" ] && [ "$1" != "--color" ]; then
    SELECTED_COLOR="$1"
fi

if [ -z "$SELECTED_COLOR" ]; then
    echo -e "${CYAN}${BOLD}"
    echo "========================================================================"
    echo "       🐉  K A L I   D R A G O N   S U I T E  -  M U L T I C O L O R    "
    echo "    Transformación completa de GRUB, Plymouth, Login y Escritorio       "
    echo "========================================================================"
    echo -e "${NC}"
    echo -e "${BOLD}Elige la edición de color que deseas instalar:${NC}\n"
    echo -e "  ${RED}[1] 🔴 Crimson Red    (Rojo Neón Carmesí - Favorito)${NC}"
    echo -e "  ${BLUE}[2] 🔵 Plasma Blue    (Azul Eléctrico Cyberpunk)${NC}"
    echo -e "  ${GREEN}[3] 🟢 Toxic Green    (Verde Hacker Neón)${NC}"
    echo -e "  ${YELLOW}[4] 🟡 Cyber Yellow   (Amarillo Neón Intenso)${NC}"
    echo -e "  ${PURPLE}[5] 🟣 Neon Purple    (Morado Synthwave)${NC}"
    echo -e "  ${YELLOW}[6] 🟠 Neon Orange    (Naranja Incandescente)${NC}"
    echo -e "  ${GREEN}[7] 🍈 Electric Lime  (Lima Eléctrico)${NC}"
    echo -e "  ${PURPLE}[8] 🌸 Cyber Pink     (Rosa Neón Arcade)${NC}"
    echo -e "  [0] Salir sin cambios\n"

    read -rp "Selecciona una opción [1-8]: " opt
    case "$opt" in
        1) SELECTED_COLOR="red" ;;
        2) SELECTED_COLOR="blue" ;;
        3) SELECTED_COLOR="green" ;;
        4) SELECTED_COLOR="yellow" ;;
        5) SELECTED_COLOR="purple" ;;
        6) SELECTED_COLOR="orange" ;;
        7) SELECTED_COLOR="lime" ;;
        8) SELECTED_COLOR="pink" ;;
        0) echo -e "\nCancelado."; exit 0 ;;
        *) echo -e "\n${RED}Opción inválida.${NC}"; exit 1 ;;
    esac
fi

SELECTED_COLOR=$(echo "$SELECTED_COLOR" | tr '[:upper:]' '[:lower:]')
VARIANT_PATH="$SCRIPT_DIR/variants/$SELECTED_COLOR"

if [ ! -d "$VARIANT_PATH" ]; then
    echo -e "${RED}[!] Error: Color '$SELECTED_COLOR' no encontrado. Colores válidos: red, blue, green, yellow, purple, orange, lime, pink.${NC}"
    exit 1
fi

CAP_COLOR="$(tr '[:lower:]' '[:upper:]' <<< ${SELECTED_COLOR:0:1})${SELECTED_COLOR:1}"

echo -e "\n${GREEN}${BOLD}=== Instalando Kali Dragon Suite - Edición ${CAP_COLOR} ===${NC}"

# 1. Backups
echo -e "${CYAN}[1/6] Comprobando respaldos de seguridad...${NC}"
if [ ! -d "/boot/grub/themes/kali.pristine_backup" ] && [ -d "/boot/grub/themes/kali" ]; then
    cp -r /boot/grub/themes/kali /boot/grub/themes/kali.pristine_backup
fi
if [ ! -d "/usr/share/plymouth/themes/kali.pristine_backup" ] && [ -d "/usr/share/plymouth/themes/kali" ]; then
    cp -r /usr/share/plymouth/themes/kali /usr/share/plymouth/themes/kali.pristine_backup
fi
if [ ! -f "/etc/lightdm/lightdm-gtk-greeter.conf.pristine_backup" ] && [ -f "/etc/lightdm/lightdm-gtk-greeter.conf" ]; then
    cp /etc/lightdm/lightdm-gtk-greeter.conf /etc/lightdm/lightdm-gtk-greeter.conf.pristine_backup
fi

# 2. GRUB
echo -e "${CYAN}[2/6] Instalando Menú de Arranque GRUB (${CAP_COLOR} Frosted Glass)...${NC}"
mkdir -p /boot/grub/themes/kali/icons
cp -f "$VARIANT_PATH/boot/grub/grub-16x9.png" /boot/grub/themes/kali/
cp -f "$VARIANT_PATH/boot/grub/grub-4x3.png" /boot/grub/themes/kali/
cp -f "$VARIANT_PATH/boot/grub/select_"*.png /boot/grub/themes/kali/
cp -f "$VARIANT_PATH/boot/grub/theme.txt" /boot/grub/themes/kali/
cp -rf "$VARIANT_PATH/boot/grub/icons/"* /boot/grub/themes/kali/icons/
chmod -R 755 /boot/grub/themes/kali

# 3. Plymouth & Transitions
echo -e "${CYAN}[3/6] Instalando Pantalla de Carga Plymouth y fondos de traspaso...${NC}"
cp -f "$VARIANT_PATH/boot/plymouth/"* /usr/share/plymouth/themes/kali/
mkdir -p /usr/share/desktop-base/kali-theme/{grub,login}
cp -f "$VARIANT_PATH/boot/transition/desktop-grub.png" /usr/share/desktop-base/kali-theme/grub/grub-16x9.png
cp -f "$VARIANT_PATH/boot/transition/desktop-grub.png" /usr/share/images/desktop-base/desktop-grub.png 2>/dev/null || true
cp -f "$VARIANT_PATH/boot/transition/login-background.png" /usr/share/desktop-base/kali-theme/login/
cp -f "$VARIANT_PATH/boot/transition/login-blurred.png" /usr/share/desktop-base/kali-theme/login/

# 4. Login (LightDM)
echo -e "${CYAN}[4/6] Instalando Pantalla de Login (LightDM ${CAP_COLOR} Theme & Avatar)...${NC}"
mkdir -p "/usr/share/themes/Kali-${CAP_COLOR}-Dragon-Login/gtk-3.0"
cp -rf "$VARIANT_PATH/login/theme/Kali-${CAP_COLOR}-Dragon-Login/"* "/usr/share/themes/Kali-${CAP_COLOR}-Dragon-Login/"
cp -f "$VARIANT_PATH/login/dragon-avatar.png" /usr/share/desktop-base/kali-theme/login/
cp -f "$VARIANT_PATH/login/lightdm-gtk-greeter.conf" /etc/lightdm/lightdm-gtk-greeter.conf
chmod 644 /etc/lightdm/lightdm-gtk-greeter.conf
chmod -R 755 "/usr/share/themes/Kali-${CAP_COLOR}-Dragon-Login"

# 5. Desktop (XFWM4, GTK CSS, Animator)
echo -e "${CYAN}[5/6] Configurando Bordes de Ventana (XFWM4) y Animador del Dragón...${NC}"
mkdir -p "$TARGET_HOME/.themes/Kali-${CAP_COLOR}-Dark-Borders/xfwm4"
mkdir -p "$TARGET_HOME/.local/share/themes/Kali-${CAP_COLOR}-Dark-Borders/xfwm4"
mkdir -p "/usr/share/themes/Kali-${CAP_COLOR}-Dark-Borders/xfwm4"
mkdir -p "$TARGET_HOME/.local/share/dragon-anim"
mkdir -p "$TARGET_HOME/.local/bin"
mkdir -p "$TARGET_HOME/.config/autostart"
mkdir -p "$TARGET_HOME/.config/gtk-3.0"
mkdir -p "$TARGET_HOME/.config/gtk-4.0"

cp -rf "$VARIANT_PATH/desktop/xfwm4-theme/Kali-${CAP_COLOR}-Dark-Borders/xfwm4/"* "$TARGET_HOME/.themes/Kali-${CAP_COLOR}-Dark-Borders/xfwm4/"
cp -rf "$VARIANT_PATH/desktop/xfwm4-theme/Kali-${CAP_COLOR}-Dark-Borders/xfwm4/"* "$TARGET_HOME/.local/share/themes/Kali-${CAP_COLOR}-Dark-Borders/xfwm4/"
cp -rf "$VARIANT_PATH/desktop/xfwm4-theme/Kali-${CAP_COLOR}-Dark-Borders/xfwm4/"* "/usr/share/themes/Kali-${CAP_COLOR}-Dark-Borders/xfwm4/"

cp -f "$VARIANT_PATH/desktop/gtk-css/gtk-3.0.css" "$TARGET_HOME/.config/gtk-3.0/gtk.css"
cp -f "$VARIANT_PATH/desktop/gtk-css/gtk-4.0.css" "$TARGET_HOME/.config/gtk-4.0/gtk.css"

cp -f "$SCRIPT_DIR/desktop/animator/dragon-window-animator.py" "$TARGET_HOME/.local/bin/"
cp -f "$VARIANT_PATH/desktop/animator/dragon_sprite.png" "$TARGET_HOME/.local/share/dragon-anim/"
cp -f "$SCRIPT_DIR/desktop/animator/dragon-animator.desktop" "$TARGET_HOME/.config/autostart/"
chmod +x "$TARGET_HOME/.local/bin/dragon-window-animator.py"

chown -R "$TARGET_USER:$TARGET_USER" "$TARGET_HOME/.themes" "$TARGET_HOME/.local" "$TARGET_HOME/.config"

# 6. Rebuild Bootloader
echo -e "${CYAN}[6/6] Compilando GRUB e Initramfs...${NC}"
update-grub
update-initramfs -u

# Restart animator
pkill -f dragon-window-animator.py 2>/dev/null || true
if [ -n "$SUDO_USER" ]; then
    su - "$TARGET_USER" -c "nohup $TARGET_HOME/.local/bin/dragon-window-animator.py --no-fork >/dev/null 2>&1 &" 2>/dev/null || true
fi

echo -e "\n${GREEN}${BOLD}"
echo "========================================================================"
echo "  ✅  ¡EDICIÓN ${CAP_COLOR^^} INSTALADA CON ÉXITO!                       "
echo "  GRUB, Plymouth, Login y tu escritorio ahora tienen la temática ${CAP_COLOR}. "
echo "========================================================================"
echo -e "${NC}"
