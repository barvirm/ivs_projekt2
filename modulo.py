#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Soubor:    David.py
#email:     d.babek@seznam.cz
#Datum:     6.4.2016
#Popis:     Program ma vzit string ze vstupu a prevest ho na modulo

def Modulo(vstup):
    if type(vstup) != str:
        return False

    vstup = vstup.replace(",",".")
    while "%" in vstup:
        if len(vstup) <= 1:
            return False

        if vstup[0] != "+" and vstup[0] != "-":
            vstup = "+" + vstup

        i_centr = vstup.find("%")
        i1 = i_centr-1
    
        while vstup[i1] >= '0' and vstup[i1] <= '9' or vstup[i1] == '.':
            if i1 > 0:
                i1 -= 1
            else:
                break

        i2 = i_centr+1
        while vstup[i2] >= '0' and vstup[i1] <= '9' or vstup[i2] == '.':
            if i2 > 0:
                i2 += 1
            else:
                break

        p1 = vstup[:i1+1]
        p2 = vstup[i1+1:i_centr]
        p3 = vstup[i_centr+1:i2]
        p4 = vstup[i2:]

        if p2 == "":
            return False
        if p3 == "0":
            return False
            
        vstup =  p1 + "modulo(" + p2 + "," + p3 + ")" + p4

        if vstup[0] == "+":
            vstup = vstup[1:]
    return vstup


#demostrace 
txt = "120+25%20+0123"
print txt
txt = Modulo(txt)
print txt
#print eval(txt)
