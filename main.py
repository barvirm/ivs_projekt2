# -*- coding: utf-8 -*-  
# 
# ToDo
# Prog. kalkulačka
# Historie


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
        self.history=["","","","","","","","","",""]

    def gui_init(self):
        """ Create gui from .glade file
        add canvas and figure for graph and connect signals
        """

        self.builder = gtk.Builder()
        self.builder.add_from_file("Glades.glade")
        self.window = self.builder.get_object("main_window")
        self.window.set_size_request(320,300)

        self.builder.connect_signals({"switch_page": self.switch_page,"on_main_window_destroy": self.on_main_window_destroy,"press_button":self.press_button,"entry_changed":self.entry_changed,"num_base_chaged":self.num_base_chaged,"press_keyboard":self.press_keyboard,"history_change":self.history_change})
        self.num_base_chaged(self.builder.get_object("radiobutton1"))   #Switching of programming calculator to Binaries
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

    ######################### GUI funcions #####################

    def on_main_window_destroy(self, widget, data = None ):
        gtk.main_quit()

    def press_keyboard(self, widget,data):
        key = gtk.gdk.keyval_name(data.keyval)
        if key == "Return":
            notebook=self.builder.get_object("notebook1").get_current_page()
            eval_string = self.builder.get_object("entry"+str(notebook)).get_text() #To to bude předáváno do funkce zpracovávající string
            self.history_add(eval_string)
            print eval_string


    #Switching of programming calculator to numeral system of the selected base
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

    #Add number or funcion to Classic and Science calculator entry when id pressed button
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
            eval_string = self.builder.get_object("entry"+str(notebook)).get_text() #To to bude předáváno do funkce zpracovávající string
            self.history_add(eval_string)
            print eval_string
        self.builder.get_object("entry"+str(1-notebook)).set_text(self.builder.get_object("entry"+str(notebook)).get_text())                                                                                                                     

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

    #Update Classic and Science calculator entry when is typed to entry
    def entry_changed(self,widget):
        self.builder.get_object("entry"+str(1-(self.builder.get_object("notebook1").get_current_page()))).set_text(self.builder.get_object("entry"+str(self.builder.get_object("notebook1").get_current_page())).get_text())

    def history_add(self,data):
        if data != self.history[9]:
            for i in range(0,9):
                self.history[i]=self.history[i+1]
            self.history[9]=data
            for i in range(0,10):
                self.builder.get_object("label"+str(101+i)).set_text(self.history[i])

    def history_change(self,widget):
        print widget
        print widget.get_tooltip()

    #change window size for each mode of calculator
    def switch_page(self,widget,p1,p2):
        if p2 == 0:
            self.window.set_size_request(320,300)
        elif p2 == 1:
            self.window.set_size_request(515,300)
        elif p2 == 2:
            self.window.set_size_request(475,300)
        elif p2 == 3:
            self.window.set_size_request(800,600)
        elif p2 == 4:
            self.window.set_size_request(480,400)
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

