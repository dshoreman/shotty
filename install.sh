#!/bin/bash

Grey='\033[0;37m'
Cyan='\033[0;36m'
Green='\033[0;32m'
Purple='\033[0;35m'
Yellow='\033[0;33m'
BRed='\033[1;31m'    # Bold Red
BYellow='\033[1;33m' # Bold Yellow
NC='\033[0m'         # Reset

function fail_install {
    echo
    echo -e "${BRed}Install failed!"
    echo -e "${Yellow}Make sure Shotty hasn't already been installed.${NC}"
    exit 1
}

clear
echo
echo
echo "     .-. .        .  .      "
echo "    (   )|       _|__|_     "
echo "     \`-. |--. .-. |  |  .  ."
echo "    (   )|  |(   )|  |  |  |"
echo "     \`-' '  \`-\`-' \`-'\`-'\`--|"
echo "     Preparing to install  ;"
echo "                        \`-' "
echo

cd /usr/local
sudo git clone -b develop https://github.com/dshoreman/shotty.git src/shotty || fail_install
sudo ln -s ../src/shotty/shotty.py bin/shotty || fail_install

echo
echo -e "${Green}Install complete!"
echo
echo -e "${Yellow}If you use i3, add the following to your i3 config:"
echo -e "${Grey}for_window [class="Shotty"] floating enable"
echo
echo -e "${Yellow}To run manually, call ${BYellow}shotty ${Yellow}from a terminal."
echo "To bind to the Print Screen key, add this too:"
echo -e "${Grey}bindsym Print exec shotty${NC}"
echo
