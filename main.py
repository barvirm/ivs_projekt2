#!/usr/bin/env python
# -*- coding: utf-8 -*-  

"""
License: GPL-3.0+
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 .
 This package is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 .
 You should have received a copy of the GNU General Public License
 along with this program. If not, see <http://www.gnu.org/licenses/>.
 .
 On Debian systems, the complete text of the GNU General
 Public License version 3 can be found in "/usr/share/common-licenses/GPL-3".
"""

import re
import my_math
import transform_string
import pygtk
import pango
import exceptions
pygtk.require("2.0")

import gtk
import gtk.glade

from numpy import arange, array, sin
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas
import pylab

pylab.hold(False) # avoid memory leak

class Calculator():

    def __init__(self):
        self.x = []
        self.y = []
        self.history=["","","","","","","","","",""]
        self.history_pages=[6,6,6,6,6,6,6,6,6,6]
        self.gui_init()

    ######################### GUI INIT #####################

    ## Create GUI for .glade file, connect signals, add canvas and figure
    # @param self pointer to class
    def gui_init(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file("Glades.glade")
        self.window = self.builder.get_object("main_window")
        self.window.set_size_request(320,320)
        self.window.set_title("The Calculator")
        self.window.set_icon_from_file("thecalculator-icon.png")
        #self.window.set_icon_from_file("/usr/share/pixmaps/thecalculator-icon.png")
        self.builder.get_object("entry0").grab_focus()

        #set font type and size for all entries
        for i in range(0,7):
            self.builder.get_object("entry"+str(i)).modify_font(pango.FontDescription("serif,monospace bold condensed 14"))
        for i in range(101,111):
            self.builder.get_object("label"+str(i)).modify_font(pango.FontDescription("serif,monospace bold condensed 14"))

        # builder.connect_signals(self)
        self.builder.connect_signals({
                                      "switch_page": self.switch_page,
                                      "on_main_window_destroy": self.on_main_window_destroy,
                                      "press_button":self.press_button,
                                      "entry_changed":self.entry_changed,
                                      "num_base_changed":self.num_base_changed,
                                      "press_keyboard":self.press_keyboard,
                                      "history_change":self.history_change,
                                      "plot":self.plot,
                                      "help_about":self.help
                                     })

        self.num_base_changed(self.builder.get_object("radiobutton1"))   #Switching of programming calculator to Binaries
    
    ######################### PLOT funcions #####################
    
        # figsize -- size of tuple (wight,heigth)
        self.figure = Figure(figsize=(100,100),dpi=150)
        self.axis = self.figure.add_subplot(111)

        t = arange(0.0,3.0,0.01)
        s = sin(2*my_math.pi*t)
        self.axis.plot(t,s)
        self.axis.grid(True)

        gridlines = self.axis.get_xgridlines() + self.axis.get_ygridlines()
        for line in gridlines:
            line.set_linewidth(0.1)
            line.set_linestyle('-')

        self.canvas = FigureCanvas(self.figure)
        self.canvas.show()

        self.graphview = self.builder.get_object("plot")
        self.graphview.pack_start(self.canvas,True,True)


    def plot(self,widget=None,from_x=-10,to_x=10):
        orig_string = self.builder.get_object("entry6").get_text()
        self.x = []
        self.y = []
        self.x = arange(from_x,to_x,0.01)
        for x in self.x:
            try:
                string = orig_string.replace("x",str("(%f)"%(x)))
                tmp_number = transform_string.calculate(string)
                if ( type(tmp_number) != str ):
                    self.y.append(tmp_number)
                else:
                    self.y.append(None)
                    continue
            except:
                entry = self.builder.get_object("entry6")
                entry.set_text("Invalid synatax, use variable x")
        self.y = array(self.y)
        self.axis.plot(self.x,self.y)
        self.axis.grid(True)

        gridlines = self.axis.get_xgridlines() + self.axis.get_ygridlines()
        for line in gridlines:
            line.set_linewidth(0.1)
            line.set_linestyle('-')

        self.canvas.draw_idle()


    ## Show help window
    # @param self pointer to class
    # @param widget which launch this
    def help(self,widget):
        self.about = gtk.AboutDialog()
        self.about.set_program_name("TheCalculator")
        self.about.set_comments("v 1.12\nYou can change bookmarks between:\nClassic, Science, Programming, Plot, History and Autors.\n\nIn history you can look on the previous calculation or you \nreturn on page where was this example solve, with history text in input.\nYou can use keyboard or click on button in calculator.\n\nPlot - Solve equation on with one unknown,\nthis parameters must be named x.")
        self.about.set_logo(gtk.gdk.pixbuf_new_from_file("logo/team_logo_80x50.png"))
        self.about.run()
        self.about.destroy()

    ######################### PROG funcions ####################

    
    ## Evaluate string from prog. entry from engaged base to entry
    # @param self pointer to class
    # @param base_string raw string from entry
    def prog_calc(self,base_string):

        try:
            base_dictionary = {"BIN":2,"OCT":8,"DEC":10,"HEX":16}
            if len(base_string)<=0:
                return "No input"
            base_string=base_string.replace("xor","^")
            for i in range(0,len(base_string)):
                if base_string[i] not in ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","~","^","&","|","+","-","/","*"," ",]:
                    return "Invalid input syntax"

            base_to = self.get_radio_state(0)
            insert_base = base_dictionary[self.builder.get_object("radiobutton"+str(base_to+1)).get_label()]

            base_string = self.prog_transfer(base_string,insert_base)
        
            output = eval(base_string, {"__builtins__":None})
        
            if self.get_radio_state(1) == insert_base:
                output = output
            elif self.get_radio_state(1) == 0:
                output = bin(int(str(output)))[2:]
            elif self.get_radio_state(1) == 1:
                output = oct(int(str(output)))[1:]
            elif self.get_radio_state(1) == 2:
                output = int(int(str(output)))
            elif self.get_radio_state(1) == 3:
                output = hex(int(str(output)))[2:]

            return str(output).upper()

        except exceptions.SyntaxError:
            return "Invalid input syntax"
        except exceptions.ValueError:
            return "Invalid base"
        except :
            return "Some Error"
        

    ## Transform string to format prepared for eval
    # @param self pointer to class
    # @param prog_string string which is transformed to form prepared for eval
    # @param base numeral base of string
    def prog_transfer(self,prog_string,base):
        prog_string = prog_string.replace(" ","")
        numerals = re.split(r'[\^\&\|\+\-\*\/]+', prog_string)
        operators = re.split(r'[0123456789ABCDEF~]+', prog_string)
        for i in range(0,len(numerals)):
            leg=len(numerals[i])
            if "~" in numerals[i]:
                numerals[i]=bin(int(numerals[i][1:],base))
                numerals[i]=numerals[i][2:].zfill(leg-1)
                numerals[i]="~0b"+numerals[i]
            else:
                numerals[i]=bin(int(numerals[i],base))
                numerals[i]=numerals[i][2:].zfill(leg)
                numerals[i]="0b"+numerals[i]

        while "" in operators:
            operators.remove("")
        output = ""
        for i in range(0,len(numerals)-1):
            output +=str(numerals[i])
            output +=str(operators[i])
        output += str(numerals[len(numerals)-1])
        output = self.negation(output)
        return output


    ## Transform string by using negation
    # @param self pointer to class
    # @param string string which is transformed by negation(~)
    def negation(self,string):
        letters = '|&^+-/ *)'
        while ( string.find('~') != -1 ):
            after_neg=string[string.find('~'):]
            lowerest_index = 1500000
            for i in letters:
                if ( after_neg.find(i) < lowerest_index and after_neg.find(i) !=-1 ):
                    lowerest_index=after_neg.find(i)
            if ( i == ')' ):
                if ( lowerest_index == 1500000):
                    lowerest_index=len(after_neg)
                cuted_string=after_neg[:lowerest_index]

                a=cuted_string[3:]
                v=''
                for i in a:
                    r=str(not(int(i))).replace('False', '0').replace('True', '1')
                    v+=r
                string=string.replace('~0b'+a,'0b'+v)
        return string

    ## Get posion of radio button in group of radio buttons
    # @param self pointer to class
    # @param group of radio button
    def get_radio_state(self,group): #group 0 is input group, 1 is output group
        if group == 0:
            group += 1
        elif group == 1:
            group +=4
        for i in [0,1,2,3]:
            if self.builder.get_object("radiobutton"+str(group)).get_group()[i].get_active() == True:
                return abs(i-3)


    ######################### GUI funcions #####################
    
    ## Close application after hit X on bar
    # @param self pointer to class
    # @param widget pointer to widget that call this function
    def on_main_window_destroy(self, widget):
        gtk.main_quit()

    ## Performs same function as button '=' on GUI
    # @param self pointer to class
    # @param widget pointer to widget that call this function
    # @param data indentificator of pressed key
    def press_keyboard(self, widget,data = None):
        key = gtk.gdk.keyval_name(data.keyval)
        if key in ["Return","KP_Enter"]:
            notebook=self.builder.get_object("notebook1").get_current_page()
            if notebook == 3:
                self.plot()
            else:
                self.send_to_calculate(self.builder.get_object("entry"+str(notebook)).get_text())

    ## Switching of programming calculator to numeral system of the selected base
    # @param self pointer to class
    # @param widget pointer to widget that call this function
    def num_base_changed(self,widget):
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
        if char in ["0","1","2","3","4","5","6","7","8","9","+","-","/","*",",","e","π","%","^","&","|","xor","~","A","B","C","D","E","F"]:
            self.set_entry(notebook,position,char)
        elif char in functions:
            self.set_entry(notebook,position,functions[char])
        elif char == "CLR":
            if notebook in [0,1]:
                for i in [0,1,3,4]:
                    self.builder.get_object("entry"+str(i)).set_text("")
            elif notebook == 2:
                self.builder.get_object("entry2").set_text("")
                self.builder.get_object("entry5").set_text("")
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
        #self.builder.get_object("entry"+str(1-notebook)).set_text(self.builder.get_object("entry"+str(notebook)).get_text())   #Actualization of entry in another notebook

    ## Insert selected expression to current position in Entry
    ## Change the position of the cursor on the most suitable position relative to the last part of expression in entry
    # @param self pointer to class
    # @param notebook pointer to widget that call this function
    # @param position actual position in entry on page 0 or 1
    # @param data actual string in entry on page 0 or 1
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

    ##Synchronize Classic and Science calculators entries when is typed to one of thies entry
    # @param self pointer to class
    # @param widget pointer to widget that call this function
    def entry_changed(self,widget):
        actual_page = self.builder.get_object("notebook1").get_current_page()
        if actual_page == 4:
            actual_page =0
        if actual_page in [0,1]:
            text_on_actual_page = self.builder.get_object("entry"+str(actual_page)).get_text()
            self.builder.get_object("entry0").set_text(text_on_actual_page)
            self.builder.get_object("entry1").set_text(text_on_actual_page)
    
    ## Add old calculation to history tab at first position, shit another
    # @param self pointer to class
    # @param data last calculated string 
    def history_add(self,data):
        actual_page = self.builder.get_object("notebook1").get_current_page()
        if data != self.history[9]:
            for i in range(0,9):                        #shif of list (records and pages)
                self.history[i]=self.history[i+1]
                self.history_pages[i]=self.history_pages[i+1]
            self.history[9]=data                        #save new historical record to 0.position on list
            self.history_pages[9]=actual_page           #save actual page linked to record in list 
            for i in range(0,10):
                self.builder.get_object("label"+str(101+i)).set_text(self.history[i]) #actualize the label by the list od records

    ## When is pressed button right side of history record, this record is return to entry on page 0 or 1
    # @param self pointer to class
    # @param widget pointer to widget that call this function
    def history_change(self,widget):
        button = gtk.Buildable.get_name(widget)[6:9]
        historical_text = self.builder.get_object("label"+button).get_label()
        final_page = self.history_pages[int(button)-101]
        if final_page in [0,1]:
            self.builder.get_object("entry0").set_text(historical_text)
            self.builder.get_object("entry3").set_text("")
            self.builder.get_object("entry4").set_text("")
        elif final_page == 2:
            self.builder.get_object("entry2").set_text(historical_text)
            self.builder.get_object("entry5").set_text("")
        self.builder.get_object("notebook1").set_current_page(final_page)


    ## Send input from calc. display to calculation
    # @param self pointer to class
    # @param eval_string data from calc entry
    def send_to_calculate(self,eval_string):
        actual_page = self.builder.get_object("notebook1").get_current_page()
        self.history_add(eval_string) 
        if actual_page in [0,1]:
            ev = str(transform_string.calculate(eval_string))
            self.builder.get_object("entry3").set_text("= "+ev)
            self.builder.get_object("entry4").set_text("= "+ev)
        elif actual_page == 2:
            ev = str(self.prog_calc(eval_string)) 
            self.builder.get_object("entry5").set_text(ev)

    ## Change window size for each mode of calculator
    # @param self pointer to class
    # @param widget pointer to widget that call this function
    # @param p1 previous page in notebook
    # @param p2 actual page in notebook
    def switch_page(self,widget,p1,p2):
        if p2 == 0:         #Classic
            self.window.set_size_request(320,320)
            self.builder.get_object("entry"+str(p2)).grab_focus()
        elif p2 == 1:       #Science
            self.window.set_size_request(515,320)
            self.builder.get_object("entry"+str(p2)).grab_focus()
        elif p2 == 2:       #Prog.
            self.window.set_size_request(450,320)
            self.builder.get_object("entry"+str(p2)).grab_focus()
        elif p2 == 3:       #PLOT
            self.window.set_size_request(800,600)
        elif p2 == 4:       #History
            self.window.set_size_request(480,330)
        elif p2 == 5:       #Authors
            self.window.set_size_request(320,300)
    
    ## Main loop for GUI
    # @param self pointer to class
    def main(self):
        self.window.show()
        gtk.main()

if __name__ == '__main__':
    app = Calculator()
    app.main()

