#!/usr/bin/env python
# -*- coding: utf-8 -*-

def factorial(x):
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
## Transform entry input to factorial  for eval
# @param vstup string from entry input
# @return String ready for eval funtion
def transform_factorial(vstup):
      while "!" in vstup:               
            if len(vstup) <= 1: # @brief Test of input string 
                return False
                          
            if vstup[0] != "+" and vstup[0] != "-": # @brief Test the first operand
                vstup = "+" + vstup
            
            i_end = vstup.find("!") # @param First ! in input       
            # Find number
            i = i_end-1    # @param First index before !
            
            while vstup[i] >= '0' and vstup[i] <= '9' or vstup[i] == '.':
                if i > 0:
                    i -= 1
                else:
                    break
        
            z_p=1
            o=0
            i_zac=0
            o_z=0
            a=0
            while vstup[i_end-i_zac-1]>="0" and vstup[i_end-i_zac-1]<="9":  # @brief Find a start index of number before factorial
                if  vstup[i_end-i_zac-1]=="+":
                    i_zac-=1
                i_zac += 1
                print "zacatek",vstup[i_end-i_zac]
                
            if vstup[i_end-z_p] == ")" : # @brief Find a end index of number before factorial
                while vstup[i_end-z_p] !="(":
                    if vstup[i_end-z_p-1]>="a" and vstup[i_end-z_p-1]<="z":
                        z_p +=1
                    if vstup[i_end-z_p] =="+" or vstup[i_end-z_p]=="-" or vstup[i_end-z_p]=="*" or vstup[i_end-z_p]=="/" or vstup[i_end-z_p] == "|":
                        o_z=1
                        
                    z_p +=1
                    print vstup[i_end-z_p]
                while vstup[i_end-z_p-1]>="a" and vstup[i_end-z_p-1]<="z":
                    z_p +=1
                    a=1
                    
                    
           
            p1 = vstup[:i_end-z_p-i_zac+1-o_z]  # @param String before factorial function
            p2 = vstup[i_end-z_p+o-i_zac+1-a:i_end-o-o_z+a] # @param String for factorial function
            p3 = vstup[i_end+1:]    # @param String after factorial function
           
   
            if p2 == "":
                return False
            
            vstup =  p1 + "factorial(" + p2 + ")" + p3  # @brief Compose all strings 
         
            if vstup[0] == "+": # @brief Delete first index,If it's +
                vstup = vstup[1:]
            
      return vstup
      
## Transform entry input to abs  for eval
# @param vstup string from entry input
# @return String ready for eval funtion
def transform_abs(vstup):
    while "|" in vstup:
        if vstup[0] != "+" and vstup[0] != "-":
                vstup = "+" + vstup
        i_max=len(vstup)    # @brief Number of characters in string
        #i=0
        i_abs=0    # @param Number of "|" in string
        i_kr=0     # @param Number of steps
        i_ak=0     # @param Current index in string
        while i_kr<i_max :  # @brief Find a number of "|"
            if vstup[i_kr]=="|":
                i_abs+=1
            i_kr+=1
            
        if i_abs% 2 != 0:   # @brief  If odd number of "|" return False
            return False
        
        while vstup[i_ak]=="|" or i_abs !=0:    # @brief Find "|" and replace it for "abs(" or ")"
            if vstup[i_ak]=="|":
                if vstup[i_ak-1]=="-" or vstup[i_ak-1]=="+" or vstup[i_ak-1]=="("or vstup[i_ak-1]=="*" or vstup[i_ak-1]=="/" or vstup[i_ak+1]=="%":   # @brief If it's a started of abs function.
                    zac=vstup[:i_ak] # @param String berofe abs function
                    kon=vstup[i_ak+1:]  # @param String in param function
                    vstup= zac + "abs(" + kon   # @brief Compose all strings 
                    i_abs-=1

                elif vstup[i_ak-1]>="0" and vstup[i_ak-1]<="9" or vstup[i_ak-1]==")" or vstup[i_ak-1]=="!" :   # @brief If it's a end "|" of abs function.
                    zac1=vstup[:i_ak]   # @param String in param function
                    kon1=vstup[i_ak+1:] #@param String after abs function
                    vstup = zac1+ ")"+kon1  # @brief Compose all strings 
                    i_abs-=1
                elif vstup[i_ak-1]=="!":
                    return False
            else:
                i_ak+=1
        
    if vstup[0] == "+":
        vstup = vstup[1:]
    return vstup
    
def transform_modulo(vstup):
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

        if p2 == "":
            return False
        if p3 == "0":
            return False
            
        vstup =  p1 + "modulo(" + p2 + "," + p3 + ")" + p4
    return vstup


## Transform entry input to form ready for eval function.
# replace x! --> factorial(x)
# replace a**b --> pow(a,b)
# replace a%b --> modulo(a,b)
# @param vstup string from entry input
# @return String ready for eval funtion
def StrFce(vstup):    
    if type(vstup) == str:        
        
        if len(vstup)<=1:
            print "No date for transforming"
            return False
        vstup = vstup.replace(",", ".")
        
        
        vstup=transform_abs(vstup)
        print vstup
        vstup=transform_factorial(vstup)
        print vstup
        #vstup=transform_abs(vstup) 
        vstup=transform_modulo(vstup)
        print vstup
       
    else:
        print "Bad input data"
        return False

        
    return vstup
    
    
def calculate(vstup):
    prevod=StrFce(vstup)
    if prevod==False:
        print "No data for count"
        return False
    
    return eval(prevod)
# demo        
txt ="|(3*5)|*|1-2|!-(2%5!)"
print txt
txt = calculate(txt)
print "txt:",txt
#print eval(txt)
txt ="(5-2)%2"
print txt
txt = calculate(txt)
print "txt:",txt
#print eval(txt)
txt ="(5%2)%2"
print txt
txt = calculate(txt)
print "txt:",txt
#print eval(txt)
txt ="(5)%2"
print txt
txt = calculate(txt)
print "txt:",txt
#print eval(txt)
txt ="2%2+5%3"
print txt
txt = calculate(txt)
print "txt:",txt
#print eval(txt)
