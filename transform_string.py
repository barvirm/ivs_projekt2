#!/usr/bin/env python
# -*- coding: utf-8 -*-

import my_math
## Transform entry input to factorial  for eval
# @param vstup string from entry input
# @return String ready for eval funtion
def transform_factorial(vstup):
      while "!" in vstup:               
            if len(vstup) <= 1: #Test of input string 
                return False
                          
            if vstup[0] != "+" and vstup[0] != "-": #Test the first operand
                vstup = "+" + vstup
            
            i_end = vstup.find("!") #First ! in input       
            i = i_end-1    #First index before !
            
            while vstup[i] >= '0' and vstup[i] <= '9' or vstup[i] == '.':
                if i > 0:
                    i -= 1
                else:
                    break
        
            z_p=1   #First index on bracket
            o=0
            i_zac=0 #First index of factorial string
            o_z=0   #Index of operand
            a=0
            #Find number for factorial
            while vstup[i_end-i_zac-1]>="0" and vstup[i_end-i_zac-1]<="9":  #Find a start index of number before factorial
                if  vstup[i_end-i_zac-1]=="+":
                    i_zac-=1
                i_zac += 1
                print "zacatek",vstup[i_end-i_zac]
                
            if vstup[i_end-z_p] == ")" : # Find a end index of number before factorial
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
                    
                    
           
            p1 = vstup[:i_end-z_p-i_zac+1-o_z]  # String before factorial function
            p2 = vstup[i_end-z_p+o-i_zac+1-a:i_end-o-o_z+a] #String for factorial function
            p3 = vstup[i_end+1:]    #String after factorial function
           
   
            if p2 == "":
                return False
            
            vstup =  p1 + "factorial(" + p2 + ")" + p3  #Compose all strings 
         
            if vstup[0] == "+": #Delete first index,If it's +
                vstup = vstup[1:]
            
      return vstup
      
## Transform entry input to abs  for eval
# @param vstup string from entry input
# @return String ready for eval funtion
def transform_abs(vstup):
    while "|" in vstup:
        if vstup[0] != "+" and vstup[0] != "-":
                vstup = "+" + vstup
        
        i_max=len(vstup)    #Number of characters in string
        #i=0
        i_abs=0    # Number of "|" in string
        i_kr=0     # Number of steps
        i_ak=0     #Current index in string
        while i_kr<i_max :  # Find a number of "|"
            if vstup[i_kr]=="|":
                i_abs+=1
            i_kr+=1
            
        if i_abs% 2 != 0:   #If odd number of "|" return False
            return False
        
        while vstup[i_ak]=="|" or i_abs !=0:    # Find "|" and replace it for "abs(" or ")"
            if vstup[i_ak]=="|":
                if vstup[i_ak-1]=="-" or vstup[i_ak-1]=="+" or vstup[i_ak-1]=="("or vstup[i_ak-1]=="*" or vstup[i_ak-1]=="/" :   #If it's a started of abs function.
                    zac=vstup[:i_ak] # String berofe abs function
                    kon=vstup[i_ak+1:]  # String in param function
                    vstup= zac + "abs(" + kon   # Compose all strings 
                    i_abs-=1

                elif vstup[i_ak-1]>="0" and vstup[i_ak-1]<="9" or vstup[i_ak-1]==")" or vstup[i_ak-1]=="!" :   # @brief If it's a end "|" of abs function.
                    zac1=vstup[:i_ak]   # String in param function
                    kon1=vstup[i_ak+1:] #String after abs function
                    vstup = zac1+ ")"+kon1  # Compose all strings 
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
    
## Calculate input string.
# @param vstup input string for eval
# @return Counted string
def calculate(vstup):
    output=StrFce(vstup)
    if output==False:
        print "No data for count"
        return False
    
    return eval(output)

