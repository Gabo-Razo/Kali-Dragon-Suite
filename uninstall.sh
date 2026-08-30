#!/bin/bash
# ==============================================================================
#  🐉 KALI RED DRAGON SUITE - RESTORE / UNINSTALL SCRIPT
#  Restores Original Factory Settings for GRUB, Plymouth & LightDM
# ==============================================================================

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}[!] Se requieren permisos de administrador (sudo).${NC}"
    echo -e "    Por favor ejecuta: ${BOLD}sudo ./uninstall.sh${NC}\n"
    exit 1
fi

echo -e "${CYAN}=== Restaurando configuración original de fábrica ===${NC}"

# Restore GRUB
if [ -d "/boot/grub/themes/kali.pristine_backup" ]; then
    echo "Restaurando tema original de GRUB..."
    cp -rf /boot/grub/themes/kali.pristine_backup/* /boot/grub/themes/kali/
fi

# Restore Plymouth
if [ -d "/usr/share/plymouth/themes/kali.pristine_backup" ]; then
    echo "Restaurando tema original de Plymouth..."
    cp -rf /usr/share/plymouth/themes/kali.pristine_backup/* /usr/share/plymouth/themes/kali/
fi

# Restore LightDM
if [ -f "/etc/lightdm/lightdm-gtk-greeter.conf.pristine_backup" ]; then
    echo "Restaurando configuración original de LightDM..."
    cp -f /etc/lightdm/lightdm-gtk-greeter.conf.pristine_backup /etc/lightdm/lightdm-gtk-greeter.conf
fi

echo "Recompilando GRUB e Initramfs..."
update-grub
update-initramfs -u

echo -e "\n${GREEN}${BOLD}✅ ¡Configuración original de fábrica restaurada con éxito!${NC}\n"
