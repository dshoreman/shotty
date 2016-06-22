#!/usr/bin/python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from subprocess import call

class Shotty(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Shotty")
        self.set_border_width(10)

        header = Gtk.HeaderBar()
        header.set_show_close_button(True)
        header.props.title = "Take a Screenshot"
        self.set_titlebar(header)

        box = Gtk.Box(spacing=6)
        self.add(box)

        button = Gtk.Button.new_with_label("Full screen")
        button.connect("clicked", self.take_fullscreen_screenshot)
        box.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("Selected window")
        button.connect("clicked", self.take_window_screenshot)
        box.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("Cancel")
        button.connect("clicked", self.quit)
        box.pack_start(button, True, True, 0)

    def take_fullscreen_screenshot(self, button):
        print("Taking full-screen screenshot...")
        call("scrot -q85 /tmp/shotty.png", shell=True)

    def take_window_screenshot(self, button):
        print("Taking windowed screenshot...")
        call("sleep 2; scrot -sq85 /tmp/shotty.png", shell=True)

    def quit(self, button):
        print("Cancelled by user, closing.")
        Gtk.main_quit()

win = Shotty()
win.connect("delete-event", Gtk.main_quit)
win.show_all()

Gtk.main()
