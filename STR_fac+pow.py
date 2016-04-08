#!/usr/bin/env python
# -*- coding: utf-8 -*-

def faktorial(x):
    if x == 0:
        return 1
    else:
        o = 1
        for i in range(1,x+1):
            o *= i
        return o
        
def sqrt(a,n=2):
    """ return sqrt of a """
    if (a < 0):
        return None
    return a**(1./ (n) )

def pow_(a,n):
    """ return pow of a """
    return (a)**(n)


## Transform entry input to form ready for eval function.
# replace x! --> factorial(x)
# replace a**b --> pow(a,b)
# @param vstup string from entry input
# @return String ready for eval funtion
def StrFce(vstup):    
    if type(vstup) == str:        
        # nahrazení řárek za tečku
        vstup = vstup.replace(",", ".")  
        vstup=vstup.replace("*","m")
        #if vstup.find("m") !=0:
         #   print "sqrt"
        # factorial    
        while "!" in vstup:               
            if len(vstup) <= 1:
                return False
                          
            if vstup[0] != "+" and vstup[0] != "-":
                vstup = "+" + vstup
            
            i_end = vstup.find("!")        
            # hledáme číslo
            i = i_end-1           
            while vstup[i] >= '0' and vstup[i] <= '9' or vstup[i] == '.':
                if i > 0:
                    i -= 1
                else:
                    break
            
            p1 = vstup[:i+1]
            p2 = vstup[i+1:i_end]
            p3 = vstup[i_end+1:]
            #print "p1:",p1
            #print "p2:",p2
            #print "p3:",p3

            if p2 == "":
                return False
            
            vstup =  p1 + "faktorial(" + p2 + ")" + p3
            #print "p1:",p1
            #print "p2:",p2
            #print "p3:",p3
            if vstup[0] == "+":
                vstup = vstup[1:]
            print vstup
        
           
        while "mm" in vstup:
            print "pow_"
            if len(vstup) <= 1:
                return False
                          
            if vstup[0] != "+" and vstup[0] != "-":
                vstup = "+" + vstup
            
            i_end = vstup.find("m")        
            # find number
            i = i_end-1          
            while vstup[i] >= '0' and vstup[i] <= '9' or vstup[i] == '.':
                if i > 0:
                    i -= 1
                else:
                    break
            
            o1 = vstup[:i+2]
            o2 = vstup[i+5:]
            o3 = vstup[i_end+2:i_end+3]
            o4 = vstup[:i+1]
            #print i_end
            #print "p1:",o1
            #print "p2:",o2
            #print "p3:",o3
            #print "p4:",o4
            vstup= o4 + "pow_(" + o1 + "," + o3 + ")" +o2
            
            
            
            if vstup[0] == "+":
                vstup = vstup[1:]
            
        return vstup
            
    else:
        print "špatná vstupní data"
        

# demo        
txt ="5**2+4!+4!"
print txt
txt = StrFce(txt)
print "txt:",txt
print eval(txt)
