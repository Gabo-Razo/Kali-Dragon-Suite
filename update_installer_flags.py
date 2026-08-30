#!/usr/bin/env python3
import os

with open("/home/gr/Escritorio/Kali-Red-Dragon-Suite/install.sh", "r") as f:
    code = f.read()

# Make sure --all installs all visual components cleanly
# and removes the background autostart if disabled
old_default = """# Default to all if no modular flag passed
if [ "$MODULAR_FLAG_PASSED" = false ]; then
    INSTALL_GRUB=true
    INSTALL_PLYMOUTH=true
    INSTALL_LOGIN=true
    INSTALL_BORDERS=true
    INSTALL_ANIMATOR=true
    INSTALL_WALLPAPER=true
    INSTALL_ICONS=true
    INSTALL_TERMINAL=true
fi"""

new_default = """# Default to all stable core components if no modular flag passed
if [ "$MODULAR_FLAG_PASSED" = false ]; then
    INSTALL_GRUB=true
    INSTALL_PLYMOUTH=true
    INSTALL_LOGIN=true
    INSTALL_BORDERS=true
    INSTALL_ANIMATOR=false
    INSTALL_WALLPAPER=true
    INSTALL_ICONS=true
    INSTALL_TERMINAL=true
fi"""

code = code.replace(old_default, new_default)

with open("/home/gr/Escritorio/Kali-Red-Dragon-Suite/install.sh", "w") as f:
    f.write(code)

print("Updated install.sh with rock-solid defaults!")
