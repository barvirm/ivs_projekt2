#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# 
# ToDo
# Prog. kalkulačka
# Historie


import my_math
import transform_string
import pygtk
pygtk.require("2.0")

import gtk
import gtk.glade

from numpy import arange, sin
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas
import pylab

pylab.hold(False) # avoid memory leak

class Calculator():

    def __init__(self):
        self.x = []
        self.y = []
        self.history=["","","","","","","","","",""]
        self.gui_init()

    ## Create GUI for .glade file, connect signals, add canvas and figure
    # @param self pointer to class
    # @todo ADD CANVAS AND FIGURE
    def gui_init(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file("Glades.glade")
        self.window = self.builder.get_object("main_window")
        self.window.set_size_request(320,300)
        self.window.set_title("The Calculator")

        # builder.connect_signals(self)
        self.builder.connect_signals({
                                      "switch_page": self.switch_page,
                                      "on_main_window_destroy": self.on_main_window_destroy,
                                      "press_button":self.press_button,
                                      "entry_changed":self.entry_changed,
                                      "num_base_chaged":self.num_base_chaged,
                                      "press_keyboard":self.press_keyboard,
                                      "history_change":self.history_change
                                     })
        self.num_base_chaged(self.builder.get_object("radiobutton1"))   #Switching of programming calculator to Binaries
        
        # figsize -- size of tuple (wight,heigth)
        self.figure = Figure(figsize=(100,100),dpi=150)
        self.axis = self.figure.add_subplot(111)

        t = arange(0.0,3.0,0.01)
        s = sin(2*my_math.pi*t)
        self.axis.plot(t,s)

        self.canvas = FigureCanvas(self.figure)
        self.canvas.show()

        self.graphview = self.builder.get_object("plot")
        self.graphview.pack_start(self.canvas,True,True)



    ######################### GUI funcions #####################
    
    ## Close application after hit X on bar
    # @param self pointer to class
    # @param widget pointer to widget that call this function
    def on_main_window_destroy(self, widget):
        gtk.main_quit()

    # TODO WHAT IS THIS
    def press_keyboard(self, widget,data = None):
        key = gtk.gdk.keyval_name(data.keyval)
        print key
        if key in ["Return","KP_Enter"]:
            notebook=self.builder.get_object("notebook1").get_current_page()
            self.send_to_calculate(self.builder.get_object("entry"+str(notebook)).get_text())


    ## Switching of programming calculator to numeral system of the selected base
    # @param self pointer to class
    # @param widget pointer to widget that call this function
    def num_base_chaged(self,widget):
        print widget.get_label()
        st=0
        buttons=[]
        for i in range(49,65):
            buttons.append(self.builder.get_object("button"+str(i)))
        if widget.get_label() == "BIN":
            st=2
        elif widget.get_label() == "OCT":
            st=8
        elif widget.get_label() == "DEC":
            st=10
        elif widget.get_label() == "HEX":
            st=16
        print st
        for i in range(0,st):
            buttons[i].set_sensitive(True)
        for i in range((st),16):
            buttons[i].set_sensitive(False)

    ## Add number or funcion to Classic and Science calculator entry when id pressed button
    # @param self pointer to class
    # @param widget pointer to widget that call this function
    def press_button(self,widget):
        notebook=self.builder.get_object("notebook1").get_current_page()
        char =  widget.get_label()
        position = self.builder.get_object("entry"+str(notebook)).get_position()
        functions = {"√":"sqrt()","x!":"!","ln":"ln()","abs":"||","sin":"sin()","cos":"cos()","tg":"tg()","cotg":"cotg()"}
        if char in ["0","1","2","3","4","5","6","7","8","9","+","-","/","*",",","e","π","%","^"]:
            self.set_entry(notebook,position,char)
        elif char in functions:
            self.set_entry(notebook,position,functions[char])
        elif char == "CLR":
            self.builder.get_object("entry"+str(notebook)).set_text("")
        elif char == "←":
            if position != 0:
                ent=self.builder.get_object("entry"+str(notebook)).get_text()
                before = ent[:position-1]
                after = ent[(position):]
                ent = before+after
                self.builder.get_object("entry"+str(notebook)).set_text(ent)
                self.builder.get_object("entry"+str(notebook)).grab_focus()
                self.builder.get_object("entry"+str(notebook)).set_position(position-1)
        elif char == "=":
            self.send_to_calculate(self.builder.get_object("entry"+str(notebook)).get_text())
        self.builder.get_object("entry"+str(1-notebook)).set_text(self.builder.get_object("entry"+str(notebook)).get_text())   #Actualization of entry in another notebook

    ## Insert selected expression to current position in Entry
    ##Change the position of the cursor on the most suitable position relative to the last part of expression in entry
    #
    #
    def set_entry(self,notebook,position,data):
        ent = self.builder.get_object("entry"+str(notebook)).get_text()
        before = ent[:position]
        after = ent[(position):]
        ent = before+data+after
        self.builder.get_object("entry"+str(notebook)).set_text(ent)
        if data in ["sqrt()","ln()","||","sin()","cos()","tg()","cotg()"]:
            entry_off_set = len(data)-1
        else:
            entry_off_set = len(data)
        self.builder.get_object("entry"+str(notebook)).grab_focus()
        self.builder.get_object("entry"+str(notebook)).set_position(position+entry_off_set)

    #Update Classic and Science calculators entry when is typed to entry
    def entry_changed(self,widget):
        #TODO FIX IT !! UNREADABLE
        actual_page = self.builder.get_object("notebook1").get_current_page()
        if actual_page == 4:
            actual_page = 1
        text_on_actual_page = self.builder.get_object("entry"+str(actual_page)).get_text()
        self.builder.get_object("entry"+str(1-actual_page)).set_text(text_on_actual_page)
    
    ## Add old calculation to history tab
    # @param self pointer to class
    # TODO DATA PARAM ??
    def history_add(self,data):
        if data != self.history[9]:
            for i in range(0,9):
                self.history[i]=self.history[i+1]
            self.history[9]=data
            for i in range(0,10):
                self.builder.get_object("label"+str(101+i)).set_text(self.history[i])
    
    # TODO WHAT IS THIS ??
    def history_change(self,widget):
        button = gtk.Buildable.get_name(widget)[6:9]
        historical_text = self.builder.get_object("label"+button).get_label()
        print historical_text
        self.builder.get_object("entry0").set_text(historical_text)
        self.builder.get_object("entry1").set_text(historical_text)

    def send_to_calculate(self,eval_string):
        self.history_add(eval_string)
        print eval_string
        print transform_string.calculate(eval_string)


    ## Change window size for each mode of calculator
    # @param self pointer to class
    # @param widget pointer to widget that call this function
    # TODO WHAT THE FUCK IS p1,p2
    def switch_page(self,widget,p1,p2):
        if p2 == 0:
            self.window.set_size_request(320,300)
            self.builder.get_object("entry"+str(p2)).grab_focus()
        elif p2 == 1:
            self.window.set_size_request(515,300)
            self.builder.get_object("entry"+str(p2)).grab_focus()
        elif p2 == 2:
            self.window.set_size_request(475,300)
            self.builder.get_object("entry"+str(p2)).grab_focus()
        elif p2 == 3:
            self.window.set_size_request(800,600)
        elif p2 == 4:
            self.window.set_size_request(480,400)
        elif p2 == 5:
            self.window.set_size_request(320,300)
    
    ## Main loop for GUI
    # @param self pointer to class
    def main(self):
        self.window.show()
        gtk.main()


if __name__ == '__main__':
    app = Calculator()
    app.main()

