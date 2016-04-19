#!/usr/bin/env python
# -*- coding: utf-8 -*-

from my_math import *
## Transform entry input to factorial  for eval
# @param coming_in string from entry input
# @return String ready for eval funtion
def transform_factorial(coming_in):
      while "!" in coming_in:               
            if len(coming_in) <= 1: #Test of input string 
                return False
                          
            if coming_in[0] != "+" and coming_in[0] != "-": #Test the first operand
                coming_in = "+" + coming_in
            
            i_end = coming_in.find("!") #First ! in input       
            i = i_end-1    #First index before !
            
            while coming_in[i] >= '0' and coming_in[i] <= '9' or coming_in[i] == '.':
                if i > 0:
                    i -= 1
                else:
                    break
        
            i_bracket=1   #@param First index on bracket
            o=0
            i_str=0 #First index of factorial string
            o_z=0   #Index of operand
            a=0
            #Find number for factorial
            while coming_in[i_end-i_str-1]>="0" and coming_in[i_end-i_str-1]<="9":  #Find a start index of number before factorial
                if  coming_in[i_end-i_str-1]=="+":
                    i_str-=1
                i_str += 1
                
            if coming_in[i_end-i_bracket] == ")" : # Find a end index of number before factorial
                while coming_in[i_end-i_bracket] !="(":
                    if coming_in[i_end-i_bracket-1]>="a" and coming_in[i_end-i_bracket-1]<="z":
                        i_bracket +=1
                    if coming_in[i_end-i_bracket] =="+" or coming_in[i_end-i_bracket]=="-" or coming_in[i_end-i_bracket]=="*" or coming_in[i_end-i_bracket]=="/" or coming_in[i_end-i_bracket] == "|":
                        o_z=1
                        
                    i_bracket +=1
                while coming_in[i_end-i_bracket-1]>="a" and coming_in[i_end-i_bracket-1]<="z":
                    i_bracket +=1
                    a=1
                    
                    
           
            p1 = coming_in[:i_end-i_bracket-i_str+1-o_z]  # String before factorial function
            p2 = coming_in[i_end-i_bracket+o-i_str+1-a:i_end-o-o_z+a] #String for factorial function
            p3 = coming_in[i_end+1:]    #String after factorial function
           
   
            if p2 == "":
                return False
            
            coming_in =  p1 + "factorial(" + p2 + ")" + p3  #Compose all strings 
         
            if coming_in[0] == "+": #Delete first index,If it's +
                coming_in = coming_in[1:]
            
      return coming_in
      
## Transform entry input to abs  for eval
# @param coming_in string from entry input
# @return String ready for eval funtion
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
    if type(coming_in) == str:        
        
        if len(coming_in)<=1:
            print "No date for transforming"
            return False
        coming_in = coming_in.replace(",", ".")
        
        if coming_in[0] != "+" and coming_in[0] != "-":
                coming_in = "+" + coming_in
       
        
        while "π" in coming_in:
            i_pi = coming_in.find("π")
            st_b=coming_in[:i_pi]
            st_a=coming_in[i_pi+1:]
            coming_in=st_b + "(pi)" + st_a
        
        while "Ï" in coming_in:
            i_pi = coming_in.find("Ï")
            st_b=coming_in[:i_pi]
            st_a=coming_in[i_pi+1:]
            coming_in=st_b + "(pi)" + st_a
        
        coming_in=transform_abs(coming_in)
        coming_in=transform_factorial(coming_in)
        coming_in=transform_modulo(coming_in)
    else:
        print "Bad input data"
        return False

        
    return coming_in
    
safe_list = ["sin","cos","tg","cotg","ln","modulo","factorial","sqrt"]
safe_dict = dict([(k, locals().get(k, None)) for k in safe_list])    
## Calculate input string.
# @param coming_in input string for eval
# @return Counted string
def calculate(coming_in):
    output=StrFce(coming_in)
    if output==False:
        print "Bad data for count"
        return False
   
    print output
    try:
        output = eval(output, {"__builtins__":None}, safe_dict)
        
    except:
        return "Invalid syntax on input"
    else:
        return output
    
    

txt ="sin(|(2-1)*|2||)"
print txt
txt = calculate(txt)
print "txt:",txt
#print eval(txt)"""