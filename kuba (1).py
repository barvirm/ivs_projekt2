# -*- coding: utf-8 -*-
"""
Created on Tue Apr 05 23:02:07 2016

@author: wykys
"""

def faktorial(x):
    if x == 0:
        return 1
    else:
        o = 1
        for i in range(1,x+1):
            o *= i
        return o

def StrFce(vstup):    
    if type(vstup) == str:        
        # nahrazení řárek za tečku
        vstup = vstup.replace(",", ".")        
        # faktorial        
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

            if p2 == "":
                return False
            
            vstup =  p1 + "faktorial(" + p2 + ")" + p3
        if vstup[0] == "+":
            vstup = vstup[1:]
        return vstup
    else:
        print "špatná vstupní data"

# demo        
txt = "4!-5"
print txt
txt = StrFce(txt)
print txt
print eval(txt)