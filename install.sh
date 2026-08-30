#!/bin/bash
# ==============================================================================
#  🐉 KALI RED DRAGON SUITE - MASTER INSTALLER
#  Full System Transformation: GRUB, Plymouth, LightDM, XFWM4 & Window Animator
# ==============================================================================

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_USER="${SUDO_USER:-$USER}"
TARGET_HOME=$(getent passwd "$TARGET_USER" | cut -d: -f6)

echo -e "${RED}${BOLD}"
echo "========================================================================"
echo "          🐉  K A L I   R E D   D R A G O N   S U I T E  🐉            "
echo "        Full Visual Overhaul: Boot, Login, Windows & Animations         "
echo "========================================================================"
echo -e "${NC}"

# Check root privileges
if [ "$EUID" -ne 0 ]; then
    echo -e "${YELLOW}[!] Se requieren permisos de administrador (sudo) para instalar en /boot y /etc.${NC}"
    echo -e "    Por favor ejecuta: ${BOLD}sudo ./install.sh${NC}\n"
    exit 1
fi

echo -e "${CYAN}[1/6] Creando respaldos de seguridad del sistema...${NC}"
# Backup GRUB
if [ ! -d "/boot/grub/themes/kali.pristine_backup" ] && [ -d "/boot/grub/themes/kali" ]; then
    cp -r /boot/grub/themes/kali /boot/grub/themes/kali.pristine_backup
    echo "  -> Respaldo de GRUB creado en /boot/grub/themes/kali.pristine_backup"
fi
# Backup Plymouth
if [ ! -d "/usr/share/plymouth/themes/kali.pristine_backup" ] && [ -d "/usr/share/plymouth/themes/kali" ]; then
    cp -r /usr/share/plymouth/themes/kali /usr/share/plymouth/themes/kali.pristine_backup
    echo "  -> Respaldo de Plymouth creado en /usr/share/plymouth/themes/kali.pristine_backup"
fi
# Backup LightDM
if [ ! -f "/etc/lightdm/lightdm-gtk-greeter.conf.pristine_backup" ] && [ -f "/etc/lightdm/lightdm-gtk-greeter.conf" ]; then
    cp /etc/lightdm/lightdm-gtk-greeter.conf /etc/lightdm/lightdm-gtk-greeter.conf.pristine_backup
    echo "  -> Respaldo de LightDM creado en /etc/lightdm/lightdm-gtk-greeter.conf.pristine_backup"
fi

echo -e "\n${CYAN}[2/6] Instalando tema GRUB Frosted Glass Red Dragon...${NC}"
mkdir -p /boot/grub/themes/kali/icons
cp -f "$SCRIPT_DIR/boot/grub/grub-16x9.png" /boot/grub/themes/kali/
cp -f "$SCRIPT_DIR/boot/grub/grub-4x3.png" /boot/grub/themes/kali/
cp -f "$SCRIPT_DIR/boot/grub/select_"*.png /boot/grub/themes/kali/
cp -f "$SCRIPT_DIR/boot/grub/theme.txt" /boot/grub/themes/kali/
cp -rf "$SCRIPT_DIR/boot/grub/icons/"* /boot/grub/themes/kali/icons/
chmod -R 755 /boot/grub/themes/kali

echo -e "\n${CYAN}[3/6] Instalando Plymouth Red Dragon y fondos de traspaso...${NC}"
cp -f "$SCRIPT_DIR/boot/plymouth/"* /usr/share/plymouth/themes/kali/
mkdir -p /usr/share/desktop-base/kali-theme/{grub,login}
cp -f "$SCRIPT_DIR/boot/transition/desktop-grub.png" /usr/share/desktop-base/kali-theme/grub/grub-16x9.png
cp -f "$SCRIPT_DIR/boot/transition/desktop-grub.png" /usr/share/images/desktop-base/desktop-grub.png 2>/dev/null || true
cp -f "$SCRIPT_DIR/boot/transition/login-background.png" /usr/share/desktop-base/kali-theme/login/
cp -f "$SCRIPT_DIR/boot/transition/login-blurred.png" /usr/share/desktop-base/kali-theme/login/

echo -e "\n${CYAN}[4/6] Instalando Tema de Login (LightDM) y Avatar del Dragón...${NC}"
mkdir -p /usr/share/themes/Kali-Red-Dragon-Login/gtk-3.0
cp -rf "$SCRIPT_DIR/login/theme/Kali-Red-Dragon-Login/"* /usr/share/themes/Kali-Red-Dragon-Login/
cp -f "$SCRIPT_DIR/login/dragon-avatar.png" /usr/share/desktop-base/kali-theme/login/
cp -f "$SCRIPT_DIR/login/lightdm-gtk-greeter.conf" /etc/lightdm/lightdm-gtk-greeter.conf
chmod 644 /etc/lightdm/lightdm-gtk-greeter.conf
chmod -R 755 /usr/share/themes/Kali-Red-Dragon-Login

echo -e "\n${CYAN}[5/6] Instalando Tema de Ventanas XFWM4 (Bordes Rojos) y Animador de Ventanas...${NC}"
# User home themes & autostart
mkdir -p "$TARGET_HOME/.themes/Kali-Red-Dark-Borders/xfwm4"
mkdir -p "$TARGET_HOME/.local/share/themes/Kali-Red-Dark-Borders/xfwm4"
mkdir -p "$TARGET_HOME/.local/share/dragon-anim"
mkdir -p "$TARGET_HOME/.local/bin"
mkdir -p "$TARGET_HOME/.config/autostart"
mkdir -p "$TARGET_HOME/.config/gtk-3.0"
mkdir -p "$TARGET_HOME/.config/gtk-4.0"

# Copy XFWM4 theme
cp -rf "$SCRIPT_DIR/desktop/xfwm4-theme/Kali-Red-Dark-Borders/xfwm4/"* "$TARGET_HOME/.themes/Kali-Red-Dark-Borders/xfwm4/"
cp -rf "$SCRIPT_DIR/desktop/xfwm4-theme/Kali-Red-Dark-Borders/xfwm4/"* "$TARGET_HOME/.local/share/themes/Kali-Red-Dark-Borders/xfwm4/"
# Global theme directory
mkdir -p /usr/share/themes/Kali-Red-Dark-Borders/xfwm4
cp -rf "$SCRIPT_DIR/desktop/xfwm4-theme/Kali-Red-Dark-Borders/xfwm4/"* /usr/share/themes/Kali-Red-Dark-Borders/xfwm4/

# Copy GTK CSS
cp -f "$SCRIPT_DIR/desktop/gtk-css/gtk-3.0/gtk.css" "$TARGET_HOME/.config/gtk-3.0/" 2>/dev/null || true
cp -f "$SCRIPT_DIR/desktop/gtk-css/gtk-4.0/gtk.css" "$TARGET_HOME/.config/gtk-4.0/" 2>/dev/null || true

# Copy Animator
cp -f "$SCRIPT_DIR/desktop/animator/dragon-window-animator.py" "$TARGET_HOME/.local/bin/"
cp -f "$SCRIPT_DIR/desktop/animator/dragon_sprite.png" "$TARGET_HOME/.local/share/dragon-anim/"
cp -f "$SCRIPT_DIR/desktop/animator/dragon-animator.desktop" "$TARGET_HOME/.config/autostart/"
chmod +x "$TARGET_HOME/.local/bin/dragon-window-animator.py"

# Fix ownership for user files
chown -R "$TARGET_USER:$TARGET_USER" "$TARGET_HOME/.themes" "$TARGET_HOME/.local" "$TARGET_HOME/.config"

echo -e "\n${CYAN}[6/6] Recompilando GRUB e Initramfs...${NC}"
update-grub
update-initramfs -u

# Restart animator for active session
pkill -f dragon-window-animator.py 2>/dev/null || true
if [ -n "$SUDO_USER" ]; then
    su - "$TARGET_USER" -c "nohup $TARGET_HOME/.local/bin/dragon-window-animator.py --no-fork >/dev/null 2>&1 &" 2>/dev/null || true
fi

echo -e "\n${GREEN}${BOLD}"
echo "========================================================================"
echo "  ✅  ¡INSTALACIÓN COMPLETADA EXITOSAMENTE!                              "
echo "  La suite Kali Red Dragon está 100% activa en tu sistema.              "
echo "========================================================================"
echo -e "${NC}"
