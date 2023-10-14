import logging
import os
from ks_includes.widgets.checkbuttonbox import CheckButtonBox
import gi

from ks_includes.widgets.initheader import InitHeader
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango, GLib, Gdk, GdkPixbuf

from ks_includes.screen_panel import ScreenPanel


def create_panel(*args):
    return CoPrintPrintingSelectionPort(*args)


class CoPrintPrintingSelectionPort(ScreenPanel):

     
    def __init__(self, screen, title):
        super().__init__(screen, title)
     
       
        initHeader = InitHeader (self, _('Connect Your 3D Printer'), _('Connect your 3D printer to Co Print Smart using a USB cable.'), "yazicibaglama")

         
        self.continueButton = Gtk.Button(_('Continue'),name ="flat-button-blue")
        self.continueButton.connect("clicked", self.on_click_continue_button)
        self.continueButton.set_hexpand(True)
        buttonBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        buttonBox.pack_start(self.continueButton, False, False, 0)


        self.portOne = Gtk.Button("usb-0:1:1.0-port0",name ="flat-button-black")
       
        self.portOne.set_hexpand(True)
        portOneBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        portOneBox.pack_start(self.portOne, False, False, 0)


        self.portTwo = Gtk.Button("usb-0:1:1.0-port1",name ="flat-button-black")
        
        self.portTwo.set_hexpand(True)
        portTwoBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        portTwoBox.pack_start(self.portTwo, False, False, 0)

        backIcon = self._gtk.Image("back-arrow", 35, 35)
        backLabel = Gtk.Label(_("Back"), name="bottom-menu-label")            
        backButtonBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        backButtonBox.set_halign(Gtk.Align.CENTER)
        backButtonBox.set_valign(Gtk.Align.CENTER)
        backButtonBox.pack_start(backIcon, False, False, 0)
        backButtonBox.pack_start(backLabel, False, False, 0)
        self.backButton = Gtk.Button(name ="back-button")
        self.backButton.add(backButtonBox)
        self.backButton.connect("clicked", self.on_click_back_button, 'co_print_printing_selection')
        self.backButton.set_always_show_image (True)       
        mainBackButtonBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        mainBackButtonBox.pack_start(self.backButton, False, False, 0)
        
        main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
       
        main.pack_start(mainBackButtonBox, False, False, 0)
        main.pack_start(initHeader, False, False, 0)
        main.pack_start(portOneBox, False, False, 10)
        main.pack_start(portTwoBox, False, False, 5)
        main.pack_end(buttonBox, False, True, 30)
       
      
        self.content.add(main)
        self._screen.base_panel.visible_menu(False)
       
    def radioButtonSelected(self, button, baudRate):
        self.selected = baudRate
    
    
    def on_click_continue_button(self, continueButton):
        self._screen.show_panel("co_print_printing_brand_selection", "co_print_printing_brand_selection", None, 2)
        
   
    def on_click_back_button(self, button, data):
        
        self._screen.show_panel(data, data, "Language", 1, False)