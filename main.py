# -*- coding: utf-8 -*-  

import my_math
import pygtk
pygtk.require("2.0")

import gtk
import gtk.glade

import numpy as np
import  matplotlib.figure as Figure
from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas
import pylab

pylab.hold(False) # avoid memory leak

class Calculator():
    def __init__(self):
        self.x = []
        self.y = []
        self.gui_init()

    def gui_init(self):
        """ Create gui from .glade file
        add canvas and figure for graph and connect signals
        """

        self.builder = gtk.Builder()
        self.builder.add_from_file("Glades.glade")
        self.window = self.builder.get_object("main_window")
        self.window.set_size_request(320,300)

        self.builder.connect_signals({"switch_page": self.switch_page,"on_main_window_destroy": self.on_main_window_destroy,"press_button":self.press_button,"entry_changed":self.entry_changed})

        self.builder.connect_signals(self)
        """
        # figsize -- size of tuple (wight,heigth)
        self.figure = Figure(figsize=(100,100), dpi=75 )
        self.axis = self.figure.add_subplot(111)

        self.canvas = FigureCanvas(self.figure)
        self.canvas.show()

        # pack canvas to "box" with name PLOT
        self.graphview = builder.get_object("PLOT")
        self.graphview.pack_start(self.canvas, expand=True, fill=True)
        """ 

    ######################### SIGNALS #####################

    def on_main_window_destroy(self, widget, data = None ):
        gtk.main_quit()

    def press_button(self,widget):
        char =  widget.get_label()
        print char
        if char == "=":
            print "BUFFER"

    def entry_changed(self,widget):
        print "ENTRY"

    def switch_page(self,widget,p1,p2):
        print "CLASSIC"
        print p2
        if p2 == 0:
            self.window.set_size_request(320,300)
        elif p2 == 1:
            self.window.set_size_request(515,300)
        elif p2 == 2:
            self.window.set_size_request(475,300)
        elif p2 == 3:
            self.window.set_size_request(800,600)
        elif p2 == 4:
            self.window.set_size_request(515,400)
        elif p2 == 5:
            self.window.set_size_request(320,300)

    #######################################################
    def main(self):
        """ mainloop for gui """
        self.window.show()
        gtk.main()

    #def plot(self, widget = None ):
    


############################ Start app ####################
if __name__ == '__main__':
    app = Calculator()
    app.main()

