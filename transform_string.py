#!/usr/bin/env python
# -*- coding: utf-8 -*-

import exceptions
from my_math import *
pi = 3.14159265359
## Convert the input string with "!" on name of factorial function
# @param coming_in string from entry input
# @return String ready for eval funtion
# @return False if it's no number before "!"
def transform_factorial(coming_in):
      while "!" in coming_in:               
            if len(coming_in) <= 1: #Test of input string 
                return False
           
            i_end = coming_in.find("!") # First ! in input      
            i = i_end-1    # First index before !
            c_bracket = 0   # Number of bracket in !
            while coming_in[i] not in "(/*-+!%" or c_bracket != 0: #find a string for factorial function
                if i == 0:
                    i-=1
                    break
                elif coming_in[i] == ")":   #Counts a number of brackets.
                    c_bracket += 1
                elif coming_in[i] == "(":   #Counts a number of brackets.
                    c_bracket -= 1
                i-=1
            i+=1
      
            p1 = coming_in[:i]  # String before factorial function
            p2 = coming_in[i:i_end] #String for factorial function
            p3 = coming_in[i_end+1:]    #String after factorial function
           
   
            if p2 == "":
                return False
            
            coming_in =  p1 + "factorial(" + p2 + ")" + p3  #Compose all section of strings 
         
            if coming_in[0] == "+": #Delete first index,If it's +
                coming_in = coming_in[1:]
            
      return coming_in
      
## Converts the input string "|" on name of the " abs "
# @param coming_in string from entry input
# @return Converted characters "|" to name of abs function
# @return False if it's a odd number of "|"
def transform_abs(coming_in):
    while "|" in coming_in:
        if coming_in[0] != "+" and coming_in[0] != "-":
                coming_in = "+" + coming_in
        
        i_max=len(coming_in)    #Number of characters in string
        #i=0
        i_abs=0    # Number of "|" in string
        i_kr=0     # Number of steps
        i_ak=0     #Current index in string
        while i_kr<i_max :  # Find a number of "|"
            if coming_in[i_kr]=="|":
                i_abs+=1
            i_kr+=1
            
        if i_abs% 2 != 0:   #If odd number of "|" return False
            return False
        
        while coming_in[i_ak]=="|" or i_abs !=0:    # Find "|" and replace it for "abs(" or ")"
            if coming_in[i_ak]=="|":
                if coming_in[i_ak-1]=="-" or coming_in[i_ak-1]=="+" or coming_in[i_ak-1]=="("or coming_in[i_ak-1]=="*" or coming_in[i_ak-1]=="/" :   #If it's a started of abs function.
                    zac=coming_in[:i_ak] # String berofe abs function
                    kon=coming_in[i_ak+1:]  # String in param function
                    coming_in= zac + "abs(" + kon   # Compose all strings 
                    i_abs-=1

                elif coming_in[i_ak-1]>="0" and coming_in[i_ak-1]<="9" or coming_in[i_ak-1]==")" or coming_in[i_ak-1]=="!" :   # @brief If it's a end "|" of abs function.
                    zac1=coming_in[:i_ak]   # String in param function
                    kon1=coming_in[i_ak+1:] #String after abs function
                    coming_in = zac1+ ")"+kon1  # Compose all strings 
                    i_abs-=1
                elif coming_in[i_ak-1]=="!":
                    return False
            else:
                i_ak+=1
        
    if coming_in[0] == "+":
        coming_in = coming_in[1:]
    return coming_in

## Prevede % na modulo()
# @param Input coming_inni string
# @return Preformovany string pro eval
def transform_modulo(Input):
    while "%" in Input: 
        CharModulo = Input.find("%") # Nalezení znaku %

        BeforeModulo = CharModulo - 1 # @param BeforeModulo Deklarace znaku pred %
    
        # Pocet znaku pred %
        while Input[BeforeModulo] >= '0' and Input[BeforeModulo] <= '9' or Input[BeforeModulo] == '.' or Input[BeforeModulo] == '-' or (Input[BeforeModulo] == '*' and (Input[BeforeModulo+1] == '*' or Input[BeforeModulo-1] == '*')):
            if BeforeModulo >= 0:
                BeforeModulo -= 1
            else:
                break

        AfterModulo = CharModulo + 1 # @param AfterModulo Deklarace znaku za %

        # Pocet znaku za %
        while Input[AfterModulo] >= '0' and Input[AfterModulo] <= '9' or Input[AfterModulo] == '.' or Input[AfterModulo] == '-' or (Input[AfterModulo] == '*' and (Input[AfterModulo+1] == '*' or Input[AfterModulo-1] == '*')):
            AfterModulo += 1
            if AfterModulo == len(Input):
                break


        String_1 = Input[: BeforeModulo + 1] # @param String_1 String pred Modulo()
        String_2 = Input[BeforeModulo + 1:CharModulo] # @param String_2 Prvni parametr Modulo()
        String_3 = Input[CharModulo + 1:AfterModulo] # @param String_3 Druhy parametr Modulo()
        String_4 = Input[AfterModulo:] # @param String_4 String za Modulo()
        # Presunuti modula do modulo prvniho parametru
        if String_1.find('modulo(') != -1 and String_1.endswith(')'):
            String_2 = String_1
            String_1 = ""
        # Presunuti modula do modulo druheho parametru
        if String_4.find('modulo(') != -1 and String_4.endswith(')'):
            String_3 = String_4
            String_4 = ""
        # Osetreni, aby prvni parametr nebyl prazdny
        if String_2 == "" and String_1 != "":
            String_2 = String_1
            String_1 = ""
        # Osetreni, aby druhy paramtr nebyl prazdny
        if String_3 == "" and String_4 != "":
            String_3 = String_4
            String_4 = ""

        # Kontrola prazdneho pole v prvnim parametru Modulo
        if String_2 == "":
            return False
        # Kontrola prazdneho pole druheho parametru a kontrola
        if String_3 == "0" or String_3 == "":
            return False
            
        # Poskladani vystupniho retezce
        Input =  String_1 + "modulo(" + String_2 + "," + String_3 + ")" + String_4
    return Input


## Transform entry input to form ready for eval function.
# replace x! --> factorial(x)
# replace a**b --> pow(a,b)
# replace a%b --> modulo(a,b)
# @param coming_in string from entry input
# @return String ready for eval funtion
def StrFce(coming_in):    
    if type(coming_in) == str or type(coming_in) == unicode:   # Test a type of input.     
        
        if len(coming_in)==1: # When it's a empty string,return "No date for transforming".
            print "No date for transforming"
            return False
        coming_in = coming_in.replace(",", ".") #replace  ","  on  ".".
        
        if coming_in[0] != "+" and coming_in[0] != "-":
                coming_in = "+" + coming_in
       
        coming_in=transform_abs(coming_in) #call function transform abs.
        coming_in=transform_factorial(coming_in) #call function transform factorial.
        coming_in=transform_modulo(coming_in)   #call function transform modulo.
    else:
        print "Bad input data"
        return False

        
    return coming_in
#Create safe sheet features that we have in the math library. 
safe_list = ["sin","cos","tg","cotg","ln","modulo","factorial","sqrt","e","pi"]
safe_dict = dict([(k, locals().get(k, None)) for k in safe_list])
safe_dict['abs'] = abs    
## Calculate function reaches the input string, which is converted using StrFce . Then it check the converted string and use eval ( ) it counts .
# @param coming_in input string for eval
# @return Result of converted string.
# @return "Invalid syntax on input" if in input is bad data.
 # @return "Division by zero" If there is a division by zero .
def calculate(coming_in):
    
    coming_in=coming_in.decode("utf-8") # transform input on "UTF-8" decode
    coming_in=coming_in.replace(u"π","(pi)") #replace "π" on "(pi)"
    coming_in=coming_in.replace("^","**") #replace "^" on "**"
    
    output=StrFce(coming_in) #Converts string to eval .
    
    if output==False:
        return "Invalid syntax on input"
    
    try:    #Chech the input transformed string,if it's good for eval function
        output = eval(output, {"__builtins__":None}, safe_dict)
        
    except exceptions.ZeroDivisionError: #If a division by zero return error
        return "Division by zero"
    except: #If it's bad input string return error
        return "Invalid syntax on input"
    else:
        return output
    
