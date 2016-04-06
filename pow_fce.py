# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 20:39:25 2016

@author: kuba
"""
def pow(a,n):
    """ return pow of a """
    return (a)**(n)

def StrFce(vstup):    
    if type(vstup) == str:        
        # nahrazení řárek za tečku
        vstup = vstup.replace(",", ".")  
        vstup=vstup.replace("*","m")
        while "mm" in vstup:
            print "sqrt "
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
            o2 = vstup[i_end:i-1]
            o3 = vstup[i_end+2:i_end+3]
            o4 = vstup[:i+1]
            print i_end
            print "p1:",o1
            print "p2:",o2
            print "p3:",o3
            print "p4:",o4
            vstup= o4 + "pow_(" + o1 + "," + o3 + ")"
            
            if o2 == "":
                return False
            
            if vstup[0] == "+":
                vstup = vstup[1:]
            
            return vstup
            
        print "špatná vstupní data"

# demo        
txt = "4**2"
print txt
txt = StrFce(txt)
print txt
print eval(txt)