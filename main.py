import my_math
import pygtk
pygtk.require("2.0")

import gtk
import gtk.glade

import numpy as np
from matplotlib.figure as Figure
from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas
import pylab

pylab.hold(False)

class Calculator():
    def __init__(self):
        self.x = []
        self.y = []


        self.gui_init()

    def gui_init(self):
        builder = gtk.Builder()
        builder.add_from_file("main_gui.glade")
        window = builder.get_object("main_window")

        builder.connect_signals()
        self.figure = Figure(figsize=(100,100), dpi=75 )
        self.axis = self.figure.add_subplot(111)

        self.canvas = FigureCanvas(self.figure)
        self.canvas.show()

        self.graphview = builder.get_object("PLOT")
        self.graphview.pack_start(self.canvas,True,True)

    ######################### SIGNALS #####################
    def on_main_window_destroy(self, widget, data = None ):
        gtk.main_quit()

    #######################################################

        def main(self):
            self.window.show()
            gtk.main()


############################ Start app ####################

if __name__ = '__main__':
    app = Calculator()
    app.main()
