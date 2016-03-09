#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pygtk
import gtk
import gtk.glade

import numpy
##############
## Graphic library ##
##############
import matplotlib
matplotlib.use('Agg')
from matplotlib.figure import Figure
from matplotlib.axes import Subplot
from matplotlib.backends.backend_gtkagg import FigureCanvasGTK
from matplotlib import cm # colormap
from matplotlib import pylab
pylab.hold(False) # This will avoid memory leak

class plot:
    def __init__(self):
        ###
        # Initialize the gui
        ###
        self.array_size = 1
        self.nbr_dots = 2

        builder = gtk.Builder()
        builder.add_from_file("gtk_test.glade")
        self.window = builder.get_object("main_window")
        # connect signals
        builder.connect_signals(self)

        self.figure = Figure(figsize=(100, 100), dpi=75)
        self.axis = self.figure.add_subplot(110)

        self.canvas = FigureCanvasGTK(self.figure) # a gtk.DrawingArea
        self.canvas.show()

        self.graphview = builder.get_object("plot")
        self.graphview.pack_start(self.canvas, True, True)

    def on_button1_pressed(self, widget):
        self.array_size = int(5)
        self.generate_seed_array()
        self.plot_gride()

    def on_nbr_pix_value_changed(self, widget):
        self.nbr_dots = int(widget.value)
        self.generate_seed_array()
        self.plot_gride()

    def on_gride_destroy(self, widget, data=None):
        gtk.main_quit()

    def main(self):
        self.window.show()
        gtk.main()

    def refresh_plot(self):
        self.canvas.draw_idle()

    def generate_seed_array(self):
        rand_pos = numpy.random.random(self.array_size ** 2)
        rand_pos = rand_pos.argsort()
        rand_pos = rand_pos < self.nbr_dots
        self.seed_array = rand_pos.reshape(self.array_size, self.array_size)

    def plot_gride(self):
        self.axis.pcolor(self.seed_array, cmap=cm.gray)
        self.axis.axis([0, self.seed_array.shape[0],
                        0, self.seed_array.shape[1]])
        self.refresh_plot()

    def on_main_window_destroy(self, widget, data=None):
        gtk.main_quit()

    def main(self):
        self.window.show()
        gtk.main()

    def plot_gride(self):
        self.axis.pcolor(self.seed_array, cmap=cm.gray)
        self.axis.axis([0, self.seed_array.shape[0],
                        0, self.seed_array.shape[1]])
        self.refresh_plot()

        pass

if __name__=='__main__':
    app = plot()
    app.window.show()
    gtk.main()
