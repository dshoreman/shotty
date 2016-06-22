#!/usr/bin/python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from datetime import datetime
from subprocess import call

class Shotty(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Shotty")
        self.set_border_width(10)

        header = Gtk.HeaderBar()
        header.set_show_close_button(True)
        header.props.title = "Take a Screenshot"
        self.set_titlebar(header)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        target_row = Gtk.Box(spacing=6)
        vbox.add(target_row)

        self.target_label = Gtk.Label()
        self.set_target("/tmp")
        self.target_label.set_justify(Gtk.Justification.LEFT)
        target_row.add(self.target_label)

        target_button = Gtk.Button("Change")
        target_button.connect("clicked", self.select_directory)
        target_row.pack_end(target_button, False, True, 0)

        action_box = Gtk.Box(spacing=6)
        vbox.add(action_box)

        button = Gtk.Button.new_with_label("Full screen")
        button.connect("clicked", self.take_fullscreen_screenshot)
        action_box.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("Selected window")
        button.connect("clicked", self.take_window_screenshot)
        action_box.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("Cancel")
        button.connect("clicked", self.quit)
        action_box.pack_start(button, True, True, 0)

    def set_default_name(self):
        timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
        self.default_filename = timestamp + ".png"

    def set_target(self, target):
        if target == "/tmp":
            self.set_default_name()
            target += "/" + self.default_filename

        self.path = target
        self.target_label.set_markup("<b>Saving to:</b> " + self.path)
        print("Save path is now " + self.path)

    def select_directory(self, button):
        dialog = Gtk.FileChooserDialog("Please choose a folder", self,
                Gtk.FileChooserAction.SAVE, (
                    Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                    "Select", Gtk.ResponseType.OK
                )
        )
        self.set_default_name()
        dialog.set_default_size(800, 400)
        dialog.set_current_name(self.default_filename)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.set_target(dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Path selection aborted")

        dialog.destroy()

    def take_fullscreen_screenshot(self, button):
        print("Taking full-screen screenshot...")
        call("scrot -q85 " + self.path, shell=True)

    def take_window_screenshot(self, button):
        print("Taking windowed screenshot...")
        call("sleep 2; scrot -sq85 " + self.path, shell=True)

    def quit(self, button):
        print("Cancelled by user, closing.")
        Gtk.main_quit()

win = Shotty()
win.connect("delete-event", Gtk.main_quit)
win.show_all()

Gtk.main()
