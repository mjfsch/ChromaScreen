import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango, GLib, GdkPixbuf

class InfoDialog(Gtk.Dialog):
    def __init__(self,this, _content, isActive= True):
        super().__init__(title="Info Dialog",parent=None ,flags=0)
        
        self.set_size_request(0, 0)
        self.set_default_size(800, 20)

         # Get current position of dialog
        pos = self.get_position()
        # Move dialog to the desired location
        self.move(pos[0] + 125, pos[1] + 225)

        svg_file = "styles/z-bolt/images/bell.svg"
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(svg_file, 40 , 40)

        alertImage = Gtk.Image()       
        alertImage.set_from_pixbuf(pixbuf)
                    
                   


        #alertImage = this._gtk.Image("bell", this._screen.width *.08, this._screen.width *.08)
        
        content = Gtk.Label(_content, name="info-dialog-content-label")
        content.set_line_wrap(True)
        content.set_justify(Gtk.Justification.CENTER)
        
        #closeIcon = this._gtk.Image("blue-close", this._screen.width *.04, this._screen.width *.04)

        svg_file = "styles/z-bolt/images/blue-close.svg"
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(svg_file, 40 , 40)

        closeIcon = Gtk.Image()       
        closeIcon.set_from_pixbuf(pixbuf)

        closeButton = Gtk.Button(name ="numpad-close-button")
        closeButton.set_image(closeIcon)
        closeButton.set_always_show_image(True)
        if(isActive):
            closeButton.connect("clicked", lambda x: self.destroy())



        mainBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=30)
        mainBox.set_halign(Gtk.Align.CENTER)
        mainBox.set_valign(Gtk.Align.CENTER)
        mainBox.pack_start(alertImage, False, False, 0)
        mainBox.pack_start(content, False, False, 0)
        mainBox.pack_start(closeButton, False, False, 0)
        
        box = self.get_content_area()
        box.set_halign(Gtk.Align.CENTER)
        box.set_valign(Gtk.Align.CENTER)
        
        box.add(mainBox)
       
        self.show_all()
        
   