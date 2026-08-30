#!/bin/bash
# ==============================================================================
#  🐉 KALI DRAGON SUITE - MULTI-COLOR MODULAR MASTER INSTALLER
#  Full Granular Modular Component Support & 8 Color Editions
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
INSTALL_GRUB=false
INSTALL_PLYMOUTH=false
INSTALL_LOGIN=false
INSTALL_BORDERS=false
INSTALL_ANIMATOR=false
INSTALL_WALLPAPER=false
INSTALL_ICONS=false
INSTALL_TERMINAL=false
MODULAR_FLAG_PASSED=false

# Parse CLI Arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --color|-c)
            SELECTED_COLOR="$2"
            shift 2
            ;;
        --all)
            INSTALL_GRUB=true
            INSTALL_PLYMOUTH=true
            INSTALL_LOGIN=true
            INSTALL_BORDERS=true
            INSTALL_ANIMATOR=true
            INSTALL_WALLPAPER=true
            INSTALL_ICONS=true
            INSTALL_TERMINAL=true
            MODULAR_FLAG_PASSED=true
            shift
            ;;
        --boot-only)
            INSTALL_GRUB=true
            INSTALL_PLYMOUTH=true
            MODULAR_FLAG_PASSED=true
            shift
            ;;
        --grub-only)
            INSTALL_GRUB=true
            MODULAR_FLAG_PASSED=true
            shift
            ;;
        --plymouth-only)
            INSTALL_PLYMOUTH=true
            MODULAR_FLAG_PASSED=true
            shift
            ;;
        --login-only)
            INSTALL_LOGIN=true
            MODULAR_FLAG_PASSED=true
            shift
            ;;
        --animator-only)
            INSTALL_ANIMATOR=true
            MODULAR_FLAG_PASSED=true
            shift
            ;;
        --borders-only)
            INSTALL_BORDERS=true
            MODULAR_FLAG_PASSED=true
            shift
            ;;
        --wallpaper-only)
            INSTALL_WALLPAPER=true
            MODULAR_FLAG_PASSED=true
            shift
            ;;
        --icons-only)
            INSTALL_ICONS=true
            MODULAR_FLAG_PASSED=true
            shift
            ;;
        --terminal-only)
            INSTALL_TERMINAL=true
            MODULAR_FLAG_PASSED=true
            shift
            ;;
        --desktop-only)
            INSTALL_BORDERS=true
            INSTALL_ANIMATOR=true
            INSTALL_WALLPAPER=true
            INSTALL_ICONS=true
            INSTALL_TERMINAL=true
            MODULAR_FLAG_PASSED=true
            shift
            ;;
        red|blue|green|yellow|purple|orange|lime|pink)
            SELECTED_COLOR="$1"
            shift
            ;;
        *)
            shift
            ;;
    esac
done

# Default to all if no modular flag passed
if [ "$MODULAR_FLAG_PASSED" = false ]; then
    INSTALL_GRUB=true
    INSTALL_PLYMOUTH=true
    INSTALL_LOGIN=true
    INSTALL_BORDERS=true
    INSTALL_ANIMATOR=true
    INSTALL_WALLPAPER=true
    INSTALL_ICONS=true
    INSTALL_TERMINAL=true
fi

# Interactive Color Selection if needed
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

    read -rp "Selecciona un color [1-8]: " opt
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

    echo -e "\n${BOLD}¿Qué componentes deseas instalar?${NC}"
    echo -e "  [1] 🌟 Todo completo (GRUB + Plymouth + Login + Bloqueo/Logout + Escritorio)"
    echo -e "  [2] 🎛️  Todo el Arranque (Menú GRUB + Animación Plymouth de carga)"
    echo -e "  [3] 🛡️  Pantallas de Login, Bloqueo (Suspend) y Cerrar Sesión"
    echo -e "  [4] 🐉  Solo Animador del Dragón (Vuelo al abrir/cerrar ventanas)"
    echo -e "  [5] 🪟  Solo Bordes de Ventana de 2px (XFWM4 & GTK)"
    echo -e "  [6] 🖼️  Solo Fondo de Pantalla"
    echo -e "  [7] 🎨  Solo Iconos de Sistema y Menú del Panel"
    echo -e "  [8] 💻  Solo Prompt y Colores de la Terminal"
    
    read -rp "Selecciona una opción [1-8] (Enter para Todo): " comp_opt
    case "$comp_opt" in
        2) INSTALL_GRUB=true; INSTALL_PLYMOUTH=true; INSTALL_LOGIN=false; INSTALL_BORDERS=false; INSTALL_ANIMATOR=false; INSTALL_WALLPAPER=false; INSTALL_ICONS=false; INSTALL_TERMINAL=false ;;
        3) INSTALL_GRUB=false; INSTALL_PLYMOUTH=false; INSTALL_LOGIN=true; INSTALL_BORDERS=false; INSTALL_ANIMATOR=false; INSTALL_WALLPAPER=false; INSTALL_ICONS=false; INSTALL_TERMINAL=false ;;
        4) INSTALL_GRUB=false; INSTALL_PLYMOUTH=false; INSTALL_LOGIN=false; INSTALL_BORDERS=false; INSTALL_ANIMATOR=true; INSTALL_WALLPAPER=false; INSTALL_ICONS=false; INSTALL_TERMINAL=false ;;
        5) INSTALL_GRUB=false; INSTALL_PLYMOUTH=false; INSTALL_LOGIN=false; INSTALL_BORDERS=true; INSTALL_ANIMATOR=false; INSTALL_WALLPAPER=false; INSTALL_ICONS=false; INSTALL_TERMINAL=false ;;
        6) INSTALL_GRUB=false; INSTALL_PLYMOUTH=false; INSTALL_LOGIN=false; INSTALL_BORDERS=false; INSTALL_ANIMATOR=false; INSTALL_WALLPAPER=true; INSTALL_ICONS=false; INSTALL_TERMINAL=false ;;
        7) INSTALL_GRUB=false; INSTALL_PLYMOUTH=false; INSTALL_LOGIN=false; INSTALL_BORDERS=false; INSTALL_ANIMATOR=false; INSTALL_WALLPAPER=false; INSTALL_ICONS=true; INSTALL_TERMINAL=false ;;
        8) INSTALL_GRUB=false; INSTALL_PLYMOUTH=false; INSTALL_LOGIN=false; INSTALL_BORDERS=false; INSTALL_ANIMATOR=false; INSTALL_WALLPAPER=false; INSTALL_ICONS=false; INSTALL_TERMINAL=true ;;
        *) INSTALL_GRUB=true; INSTALL_PLYMOUTH=true; INSTALL_LOGIN=true; INSTALL_BORDERS=true; INSTALL_ANIMATOR=true; INSTALL_WALLPAPER=true; INSTALL_ICONS=true; INSTALL_TERMINAL=true ;;
    esac
fi

SELECTED_COLOR=$(echo "$SELECTED_COLOR" | tr '[:upper:]' '[:lower:]')
VARIANT_PATH="$SCRIPT_DIR/variants/$SELECTED_COLOR"

if [ ! -d "$VARIANT_PATH" ]; then
    echo -e "${RED}[!] Error: Color '$SELECTED_COLOR' no encontrado. Colores válidos: red, blue, green, yellow, purple, orange, lime, pink.${NC}"
    exit 1
fi

CAP_COLOR="$(tr '[:lower:]' '[:upper:]' <<< ${SELECTED_COLOR:0:1})${SELECTED_COLOR:1}"
THEME_NAME="Kali-${CAP_COLOR}-Dark-Borders"
LOGIN_THEME_NAME="Kali-${CAP_COLOR}-Dragon-Login"
ICON_THEME="Flat-Remix-${CAP_COLOR}-Dark"

if [ "$SELECTED_COLOR" == "lime" ]; then
    ICON_THEME="Flat-Remix-Green-Dark"
fi

echo -e "\n${GREEN}${BOLD}=== Instalando Kali Dragon Suite - Edición ${CAP_COLOR} ===${NC}"

# Detect active graphical session
USER_PID=$(pgrep -u "$TARGET_USER" xfce4-session | head -n 1 || true)
if [ -n "$USER_PID" ]; then
    DBUS_ADDR=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$USER_PID/environ 2>/dev/null | cut -d= -f2- | tr -d '\0' || true)
    USER_DISP=$(grep -z DISPLAY /proc/$USER_PID/environ 2>/dev/null | cut -d= -f2- | tr -d '\0' || echo ":0")
else
    USER_DISP=":0"
    DBUS_ADDR=""
fi

# 1. GRUB Boot Menu
if [ "$INSTALL_GRUB" = true ]; then
    echo -e "${CYAN}[+] Instalando Menú de Arranque GRUB (${CAP_COLOR} Frosted Glass + Selectores + 70+ Iconos)...${NC}"
    mkdir -p /boot/grub/themes/kali/icons
    cp -f "$VARIANT_PATH/boot/grub/grub-16x9.png" /boot/grub/themes/kali/
    cp -f "$VARIANT_PATH/boot/grub/grub-4x3.png" /boot/grub/themes/kali/
    cp -f "$VARIANT_PATH/boot/grub/select_"*.png /boot/grub/themes/kali/
    cp -f "$VARIANT_PATH/boot/grub/slider_"*.png /boot/grub/themes/kali/ 2>/dev/null || true
    cp -f "$VARIANT_PATH/boot/grub/theme.txt" /boot/grub/themes/kali/
    cp -rf "$VARIANT_PATH/boot/grub/icons/"* /boot/grub/themes/kali/icons/
    chmod -R 755 /boot/grub/themes/kali
fi

# 2. Plymouth & Boot Handoff
if [ "$INSTALL_PLYMOUTH" = true ]; then
    echo -e "${CYAN}[+] Instalando Pantalla de Carga Plymouth y fondos de traspaso limpios...${NC}"
    cp -f "$VARIANT_PATH/boot/plymouth/"* /usr/share/plymouth/themes/kali/
    mkdir -p /usr/share/desktop-base/kali-theme/{grub,login,lockscreen,wallpaper/contents/images}
    mkdir -p /usr/share/grub/themes/kali
    mkdir -p /usr/share/images/desktop-base
    
    cp -f "$VARIANT_PATH/boot/transition/desktop-grub.png" /usr/share/desktop-base/kali-theme/grub/grub-16x9.png
    cp -f "$VARIANT_PATH/boot/transition/desktop-grub.png" /usr/share/desktop-base/kali-theme/grub/grub-4x3.png 2>/dev/null || true
    cp -f "$VARIANT_PATH/boot/transition/desktop-grub.png" /usr/share/grub/themes/kali/grub-16x9.png 2>/dev/null || true
    cp -f "$VARIANT_PATH/boot/transition/desktop-grub.png" /usr/share/grub/themes/kali/grub-4x3.png 2>/dev/null || true
    cp -f "$VARIANT_PATH/boot/transition/desktop-grub.png" /usr/share/images/desktop-base/desktop-grub.png 2>/dev/null || true
fi

# 3. Login, Lock Screen (Screensaver/Suspend) & Logout Dialog (Unified Glassmorphism & Wallpaper)
if [ "$INSTALL_LOGIN" = true ]; then
    echo -e "${CYAN}[+] Instalando Pantallas de Login (LightDM), Bloqueo (Suspend) y Cuadro de Cerrar Sesión (${CAP_COLOR})...${NC}"
    mkdir -p "/usr/share/themes/$LOGIN_THEME_NAME/gtk-3.0"
    mkdir -p /usr/share/desktop-base/kali-theme/{login,lockscreen}
    mkdir -p /usr/share/backgrounds/kali
    mkdir -p /var/lib/AccountsService/icons
    
    # 3.1 LightDM Theme & Greeter
    cp -rf "$VARIANT_PATH/login/theme/$LOGIN_THEME_NAME/"* "/usr/share/themes/$LOGIN_THEME_NAME/"
    cp -f "$VARIANT_PATH/login/dragon-avatar.png" /usr/share/desktop-base/kali-theme/login/
    cp -f "$VARIANT_PATH/login/lightdm-gtk-greeter.conf" /etc/lightdm/lightdm-gtk-greeter.conf
    cp -f "$VARIANT_PATH/boot/transition/login-background.png" /usr/share/desktop-base/kali-theme/login/
    cp -f "$VARIANT_PATH/boot/transition/login-blurred.png" /usr/share/desktop-base/kali-theme/login/
    
    # 3.2 Lockscreen (xfce4-screensaver / Suspend Wake-up) Wallpaper, XML & Avatar
    cp -f "$VARIANT_PATH/lockscreen/lockscreen.png" /usr/share/desktop-base/kali-theme/lockscreen/
    cp -f "$VARIANT_PATH/lockscreen/gnome-background.xml" /usr/share/desktop-base/kali-theme/lockscreen/
    cp -f "$VARIANT_PATH/lockscreen/dragon-avatar.png" /usr/share/desktop-base/kali-theme/lockscreen/
    
    # Overwrite default blue backgrounds so lockscreen never bleeds blue
    cp -f "$VARIANT_PATH/lockscreen/lockscreen.png" /usr/share/backgrounds/kali/kali-cubes2-16x9.jpg 2>/dev/null || true
    cp -f "$VARIANT_PATH/lockscreen/lockscreen.png" /usr/share/backgrounds/kali/kali-cubes-16x9.jpg 2>/dev/null || true
    cp -f "$VARIANT_PATH/lockscreen/gnome-background.xml" /usr/share/backgrounds/kali/kali-cubes2.xml 2>/dev/null || true
    cp -f "$VARIANT_PATH/boot/transition/login-blurred.png" /usr/share/backgrounds/kali/login-blurred 2>/dev/null || true
    
    # User Profile Avatar in target color (for lockscreen and accounts service)
    cp -f "$VARIANT_PATH/login/dragon-avatar.png" "$TARGET_HOME/.face" 2>/dev/null || true
    cp -f "$VARIANT_PATH/login/dragon-avatar.png" "$TARGET_HOME/.face.icon" 2>/dev/null || true
    cp -f "$VARIANT_PATH/login/dragon-avatar.png" "/var/lib/AccountsService/icons/$TARGET_USER" 2>/dev/null || true
    chown "$TARGET_USER:$TARGET_USER" "$TARGET_HOME/.face" "$TARGET_HOME/.face.icon" 2>/dev/null || true
    
    # 3.3 Lockscreen & Logout GTK CSS in user & system themes
    mkdir -p "$TARGET_HOME/.config/gtk-3.0" "$TARGET_HOME/.themes/$THEME_NAME/gtk-3.0"
    cp -f "$VARIANT_PATH/desktop/gtk-css/gtk-3.0.css" "$TARGET_HOME/.config/gtk-3.0/gtk.css"
    cp -f "$VARIANT_PATH/desktop/gtk-css/gtk-3.0.css" "$TARGET_HOME/.themes/$THEME_NAME/gtk-3.0/gtk.css" 2>/dev/null || true
    
    chmod 644 /etc/lightdm/lightdm-gtk-greeter.conf 2>/dev/null || true
    chmod -R 755 "/usr/share/themes/$LOGIN_THEME_NAME"
fi

# 4. Window Borders (XFWM4 & GTK3/4 CSD)
if [ "$INSTALL_BORDERS" = true ]; then
    echo -e "${CYAN}[+] Instalando Bordes de Ventana de 2px (XFWM4 & GTK)...${NC}"
    mkdir -p "$TARGET_HOME/.themes/$THEME_NAME"
    mkdir -p "$TARGET_HOME/.local/share/themes/$THEME_NAME"
    mkdir -p "/usr/share/themes/$THEME_NAME"
    
    cp -rf "$VARIANT_PATH/desktop/theme/$THEME_NAME/"* "$TARGET_HOME/.themes/$THEME_NAME/"
    cp -rf "$VARIANT_PATH/desktop/theme/$THEME_NAME/"* "$TARGET_HOME/.local/share/themes/$THEME_NAME/"
    cp -rf "$VARIANT_PATH/desktop/theme/$THEME_NAME/"* "/usr/share/themes/$THEME_NAME/"
    
    mkdir -p "$TARGET_HOME/.config/gtk-3.0" "$TARGET_HOME/.config/gtk-4.0"
    cp -f "$VARIANT_PATH/desktop/gtk-css/gtk-3.0.css" "$TARGET_HOME/.config/gtk-3.0/gtk.css"
    cp -f "$VARIANT_PATH/desktop/gtk-css/gtk-4.0.css" "$TARGET_HOME/.config/gtk-4.0/gtk.css"
    
    if [ -n "$DBUS_ADDR" ]; then
        sudo -u "$TARGET_USER" DISPLAY="$USER_DISP" DBUS_SESSION_BUS_ADDRESS="$DBUS_ADDR" xfconf-query -c xfwm4 -p /general/theme -s "$THEME_NAME" 2>/dev/null || true
        sudo -u "$TARGET_USER" DISPLAY="$USER_DISP" DBUS_SESSION_BUS_ADDRESS="$DBUS_ADDR" xfconf-query -c xsettings -p /Net/ThemeName -s "$THEME_NAME" 2>/dev/null || true
    fi
fi

# 5. Dragon Window Animator Daemon
if [ "$INSTALL_ANIMATOR" = true ]; then
    echo -e "${CYAN}[+] Configurando Animador del Dragón Volador...${NC}"
    mkdir -p "$TARGET_HOME/.local/share/dragon-anim" "$TARGET_HOME/.local/bin" "$TARGET_HOME/.config/autostart"
    cp -f "$SCRIPT_DIR/desktop/animator/dragon-window-animator.py" "$TARGET_HOME/.local/bin/"
    cp -f "$VARIANT_PATH/desktop/animator/dragon_sprite.png" "$TARGET_HOME/.local/share/dragon-anim/"
    cp -f "$VARIANT_PATH/desktop/animator/color_config.json" "$TARGET_HOME/.local/share/dragon-anim/"
    cp -f "$SCRIPT_DIR/desktop/animator/dragon-animator.desktop" "$TARGET_HOME/.config/autostart/"
    chmod +x "$TARGET_HOME/.local/bin/dragon-window-animator.py"

    pkill -f dragon-window-animator.py 2>/dev/null || true
    sleep 0.2
    su - "$TARGET_USER" -c "DISPLAY=$USER_DISP nohup $TARGET_HOME/.local/bin/dragon-window-animator.py --no-fork >/dev/null 2>&1 &" 2>/dev/null || true
fi

# 6. Desktop Wallpaper
if [ "$INSTALL_WALLPAPER" = true ]; then
    echo -e "${CYAN}[+] Aplicando Fondo de Pantalla del Dragón 1080p...${NC}"
    WALLPAPER_FILE="$VARIANT_PATH/assets/wallpaper_${SELECTED_COLOR}.png"
    if [ -n "$DBUS_ADDR" ]; then
        for prop in $(sudo -u "$TARGET_USER" DISPLAY="$USER_DISP" DBUS_SESSION_BUS_ADDRESS="$DBUS_ADDR" xfconf-query -c xfce4-desktop -l 2>/dev/null | grep "last-image" || true); do
            sudo -u "$TARGET_USER" DISPLAY="$USER_DISP" DBUS_SESSION_BUS_ADDRESS="$DBUS_ADDR" xfconf-query -c xfce4-desktop -p "$prop" -s "$WALLPAPER_FILE" 2>/dev/null || true
        done
    fi
fi

# 7. System & Panel Icons
if [ "$INSTALL_ICONS" = true ]; then
    echo -e "${CYAN}[+] Actualizando Iconos de Sistema y Menú del Panel (${ICON_THEME})...${NC}"
    if [ -n "$DBUS_ADDR" ]; then
        sudo -u "$TARGET_USER" DISPLAY="$USER_DISP" DBUS_SESSION_BUS_ADDRESS="$DBUS_ADDR" xfconf-query -c xsettings -p /Net/IconThemeName -s "$ICON_THEME" 2>/dev/null || true
    fi
fi

# 8. Terminal Prompt & Colors
if [ "$INSTALL_TERMINAL" = true ]; then
    echo -e "${CYAN}[+] Configurando Prompt y Colores de la Terminal...${NC}"
    ZSHRC_FILE="$TARGET_HOME/.zshrc"
    if [ -f "$ZSHRC_FILE" ]; then
        case "$SELECTED_COLOR" in
            red) Z_HI="196"; Z_LO="160" ;;
            purple) Z_HI="165"; Z_LO="135" ;;
            green) Z_HI="46"; Z_LO="34" ;;
            blue) Z_HI="39"; Z_LO="27" ;;
            yellow) Z_HI="226"; Z_LO="214" ;;
            orange) Z_HI="208"; Z_LO="202" ;;
            lime) Z_HI="118"; Z_LO="112" ;;
            pink) Z_HI="207"; Z_LO="198" ;;
            *) Z_HI="196"; Z_LO="160" ;;
        esac
        sed -i -E "s/%F\{[0-9]+\}┌──/%F{$Z_HI}┌──/g" "$ZSHRC_FILE" 2>/dev/null || true
        sed -i -E "s/%F\{[0-9]+\}%n/%F{$Z_LO}%n/g" "$ZSHRC_FILE" 2>/dev/null || true
        sed -i -E "s/\)─\[%B%F\{15\}%\(6~.%-1~\/…\/%4~.%5~\)%b%F\{[0-9]+\}\]/\)─[%B%F{15}%(6~.%-1~\/…\/%4~.%5~)%b%F{$Z_HI}\]/g" "$ZSHRC_FILE" 2>/dev/null || true
    fi

    QTERM_CFG="$TARGET_HOME/.config/qterminal.org/qterminal.ini"
    if [ -f "$QTERM_CFG" ]; then
        case "$SELECTED_COLOR" in
            red) CURSOR_HEX="#ff1744" ;;
            purple) CURSOR_HEX="#d500f9" ;;
            green) CURSOR_HEX="#00e676" ;;
            blue) CURSOR_HEX="#00b0ff" ;;
            yellow) CURSOR_HEX="#ffd600" ;;
            orange) CURSOR_HEX="#ff6d00" ;;
            lime) CURSOR_HEX="#76ff03" ;;
            pink) CURSOR_HEX="#ff4081" ;;
            *) CURSOR_HEX="#ff1744" ;;
        esac
        sed -i -E "s/ColorCursor=.*/ColorCursor=$CURSOR_HEX/g" "$QTERM_CFG" 2>/dev/null || true
    fi
fi

chown -R "$TARGET_USER:$TARGET_USER" "$TARGET_HOME/.themes" "$TARGET_HOME/.local" "$TARGET_HOME/.config" 2>/dev/null || true

# Rebuild Bootloader if needed
if [ "$INSTALL_GRUB" = true ] || [ "$INSTALL_PLYMOUTH" = true ]; then
    echo -e "${CYAN}[*] Compilando GRUB e Initramfs...${NC}"
    if [ "$INSTALL_GRUB" = true ]; then
        update-grub
    fi
    if [ "$INSTALL_PLYMOUTH" = true ]; then
        update-initramfs -u
    fi
fi

echo -e "\n${GREEN}${BOLD}"
echo "========================================================================"
echo "  ✅  ¡INSTALACIÓN COMPLETADA CON ÉXITO!                                "
echo "  Temática activa: ${CAP_COLOR^^}                                      "
echo "========================================================================"
echo -e "${NC}"
