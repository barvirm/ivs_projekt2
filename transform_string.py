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

def modulo(a,b):
    return (a)%(b)

def abx(a):
    if a >= 0:
        return a
    else:
        return -a
def transform_factorial(vstup):
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
        
            z_p=1
            o=0
            i_zac=0
            o_z=0
            while vstup[i_end-i_zac-1]>="0" and vstup[i_end-i_zac-1]<="9":
                if  vstup[i_end-i_zac-1]=="+":
                    i_zac-=1
                i_zac += 1
                print "zacatek",vstup[i_end-i_zac]
                
            if vstup[i_end-z_p] == ")":
                while vstup[i_end-z_p] !="(":
                    if vstup[i_end-z_p] =="+" or vstup[i_end-z_p]=="-":
                        o_z=1
                        
                    z_p +=1
                    print vstup[i_end-z_p]
                #o=1
            #if  vstup[i_end-i_zac-1]=="+":
                #i_zac-=1
            p1 = vstup[:i_end-z_p-i_zac+1-o_z]
            p2 = vstup[i_end-z_p+o-i_zac+1:i_end-o-o_z]
            p3 = vstup[i_end+1:]
            print "o1",p1
            print "o2",p2
            print "o3",p3
            print "vstup:",vstup
       
   
            if p2 == "":
                return False
            
            vstup =  p1 + "factorial(" + p2 + ")" + p3
            #print "p1:",p1
            #print "p2:",p2
            #print "p3:",p3
            if vstup[0] == "+":
                vstup = vstup[1:]
            print vstup
            
      return vstup
def transform_abs(vstup):
    while "|" in vstup:
        if vstup[0] != "+" and vstup[0] != "-":
                vstup = "+" + vstup
        i_max=len(vstup)
        #i=0
        i_abs=0
        i_kr=0
        i_ak=0
        while i_kr<i_max :
            if vstup[i_kr]=="|":
                i_abs+=1
            i_kr+=1
            
        if i_abs% 2 != 0:
            return False
        i_abs=i_abs
        
        while vstup[i_ak]=="|" or i_abs !=0:
            if vstup[i_ak]=="|":
                if vstup[i_ak-1]=="-" or vstup[i_ak-1]=="+" or vstup[i_ak-1]=="("or vstup[i_ak-1]=="*" or vstup[i_ak-1]=="/":
                    zac=vstup[:i_ak]
                    kon=vstup[i_ak+1:]
                    vstup= zac + "abs(" + kon
                    i_abs-=1

                elif vstup[i_ak-1]>="0" and vstup[i_ak-1]<="9" or vstup[i_ak-1]==")":
                    zac1=vstup[:i_ak]
                    kon1=vstup[i_ak+1:]
                    vstup = zac1+ ")"+kon1
                    i_abs-=1
            else:
                i_ak+=1
        
    if vstup[0] == "+":
        vstup = vstup[1:]
     
    return vstup
## Transform entry input to form ready for eval function.
# replace x! --> factorial(x)
# replace a**b --> pow(a,b)
# replace a%b --> modulo(a,b)
# @param vstup string from entry input
# @return String ready for eval funtion
def StrFce(vstup):    
    if type(vstup) == str:        
        # nahrazení řárek za tečku
        vstup = vstup.replace(",", ".")
#        vstup = vstup.replace("(", "")
#        vstup = vstup.replace(")", "")  
        #if vstup.find("m") !=0:
         #   print "sqrt"
        # factorial
        
        vstup=transform_factorial(vstup)
        vstup=transform_abs(vstup)        
        """
        back = 0
        frst = 0
        ten = len(vstup)
        if ten <= 1:
            return False
        while (ten):
            if vstup[ten-1] == ')':
                back += 1
            if vstup[ten-1] == '(':
                frst += 1
            ten -=1
        if back != frst:
            return False
        absolut = 0
        ten = len(vstup)
        while (ten):
            if vstup[ten-1] == '|':
                absolut += 1
            ten -= 1
        if (absolut%2) != 0:
            return False
        """
       
        while "%" in vstup:
        
            i_centr = vstup.find("%")
            i1 = i_centr-1
    
            while vstup[i1] >= '0' and vstup[i1] <= '9' or vstup[i1] == '.':
                if i1 > 0:
                    i1 -= 1
                else:
                    break

            i2 = i_centr+1
            while vstup[i2] >= '0' and vstup[i2] <= '9' or vstup[i2] == '.' or vstup[i2] == '-' or (vstup[i2] == '*' and (vstup[i2+1] == '*' or vstup[i2-1] == '*')):
                if i2 > 0 :
                    i2 += 1
                    if i2 == len(vstup):
                        break
                else:
                    break


            p1 = vstup[:i1+1]
            p2 = vstup[i1+1:i_centr]
            p3 = vstup[i_centr+1:i2]
            p4 = vstup[i2:]
            if p1.find('modulo(') != -1 and p1.endswith(')'):
                p2 = p1
                p1 = ""
            if p4.find('modulo(') != -1 and p4.endswith(')'):
                p3 = p4
                p4 = ""
            if p2 == "" and p1 != "":
                p2 = p1
                p1 = ""
            if p3 == "" and p4 != "":
                p3 = p4
                p4 = ""
#            if p2.startswith('(') and p2.endswith(')'):
#                p2 = p2[+1:-1]
#            if p3.startswith('(') and p3.endswith(')'):
#                p3 = p3[+1:-1]
#            print "p1:",p1
#            print "p2:",p2
#            print "p3:",p3
#            print "p4:",p4

            if p2 == "":
                return False
            if p3 == "0":
                return False
            
            vstup =  p1 + "modulo(" + p2 + "," + p3 + ")" + p4

            if vstup[0] == "+":
                vstup = vstup[1:]


        return vstup
            
    else:
        print "špatná vstupní data"
        

# demo        
txt ="|(3*5)|*|1-2|-(2*5)"
print txt
txt = StrFce(txt)
print "txt:",txt
print eval(txt)
txt ="(5-2)%2"
print txt
txt = StrFce(txt)
print "txt:",txt
print eval(txt)
txt ="(5%2)%2"
print txt
txt = StrFce(txt)
print "txt:",txt
print eval(txt)
txt ="(5)%2"
print txt
txt = StrFce(txt)
print "txt:",txt
print eval(txt)
txt ="2%2+5%3"
print txt
txt = StrFce(txt)
print "txt:",txt
print eval(txt)
