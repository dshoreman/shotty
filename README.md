# Shotty

Simple GUI written in Python to take screenshots with Scrot

## Requirements

Shotty requires Python and PyGObject to run, and Scrot to take screenshots.

To install these on Arch, run `sudo pacman -S python python-gobject scrot`.

## Installation

Shotty can be automatically installed by running `install.sh` in a terminal using curl or wget:

### via curl
```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/dshoreman/shotty/develop/install.sh)"
```

### via wget
```
sh -c "$(wget https://raw.githubusercontent.com/dshoreman/shotty/develop/install.sh -O -)"
```

## Usage

You can call `shotty` manually from a shell, or you can add a keybinding to your window manager.

To use with i3, set the Shotty window to floating mode and optionally bind to the Print Screen key:

```
# ~/.config/i3/config

for_window [class="Shotty"] floating enable
bindsym Print exec shotty
```
