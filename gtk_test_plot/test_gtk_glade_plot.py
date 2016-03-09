#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pygtk
import gtk
import gtk.glade

from numpy import arange, sin, pi
##############
## Graphic library ##
##############
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas
import pylab

pylab.hold(False) # This will avoid memory leak

class plot:
    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file("gtk_test.glade")
        self.window = builder.get_object("main_window")
        # connect signals
        builder.connect_signals(self)

        self.figure = Figure(figsize=(100, 100), dpi=75)
        self.axis = self.figure.add_subplot(111)

        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        self.axis.plot(t, s)

        self.canvas = FigureCanvas(self.figure) # a gtk.DrawingArea
        self.canvas.show()

        self.graphview = builder.get_object("plot")
        self.graphview.pack_start(self.canvas, True, True)

    def on_button1_pressed(self, widget):
        t = arange(-5, 3.0, 0.01)
        s = sin(3*pi*t)
        self.axis.plot(t, s)
        self.canvas.draw_idle()


    def on_main_window_destroy(self, widget, data=None):
        gtk.main_quit()

    def main(self):
        self.window.show()
        gtk.main()

if __name__=='__main__':
    app = plot()
    app.window.show()
    gtk.main()
