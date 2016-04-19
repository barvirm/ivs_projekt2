#!/usr/bin/env python
#coding:utf-8
#Made by Petr Malaník, Marek Barvir

import unittest as ut
import transform_string as s
## @class Testing string transform for eval
class TestMyMath(ut.TestCase):
	#section 0
	def test_modulo(self):
		self.assertEqual(s.StrFce("2+5"),"2+5")										#0
		self.assertEqual(s.StrFce("2%5"),"modulo(2,5)")								#1
		self.assertEqual(s.StrFce("(2%5)"),"(modulo(2,5))")							#2
		self.assertEqual(s.StrFce("2+5%2"),"2+modulo(5,2)")							#3
		self.assertEqual(s.StrFce("5%2*2"),"modulo(5,2)*2")							#4
		self.assertEqual(s.StrFce("5%(2/2)"),"modulo(5,(2/2))")						#5
		self.assertEqual(s.StrFce("2+5%(2*2)"),"2+modulo(5,(2*2))")					#6
		self.assertEqual(s.StrFce("2%3+5%2"),"modulo(2,3)+modulo(5,2)")				#7
		self.assertEqual(s.StrFce("(2%3)+(5%2)"),"(modulo(2,3))+(modulo(5,2))")		#8
		self.assertEqual(s.StrFce("(2%3**2)+5%2"),"(modulo(2,3**2))+modulo(5,2)")	#9
		self.assertEqual(s.StrFce("(2%3)**(5%2)"),"(modulo(2,3))**(modulo(5,2))")	#10
		self.assertEqual(s.StrFce("(3-1)%(2-1)"),"modulo((3-1),(2-1))")				#11

	#section 1
	def test_factorial(self):
		self.assertEqual(s.StrFce("2+5"),"2+5")										#0
		self.assertEqual(s.StrFce("2!"),"factorial(2)")								#1
		self.assertEqual(s.StrFce("2!+5!"),"factorial(2)+factorial(5)")				#2
		self.assertEqual(s.StrFce("(2!)"),"(factorial(2))")							#3
		self.assertEqual(s.StrFce("2!+5"),"factorial(2)+5")							#4
		self.assertEqual(s.StrFce("1-2!+5"),"1-factorial(2)+5")						#5
		self.assertEqual(s.StrFce("-20!"),"-factorial(20)")							#6
		self.assertEqual(s.StrFce("(20-5)!"),"factorial(20-5)")						#7
		self.assertEqual(s.StrFce("1-(20-5)!+2**5"),"1-factorial(20-5)+2**5")		#8
		self.assertEqual(s.StrFce("(20*5)!**2!"),"factorial(20*5)**factorial(2)")	#9

	#section 2
	def test_abs(self):
		self.assertEqual(s.StrFce("2+5"),"2+5")										#0
		self.assertEqual(s.StrFce("|2|"),"abs(2)")									#1
		self.assertEqual(s.StrFce("|2|+|5|"),"abs(2)+abs(5)")						#2
		self.assertEqual(s.StrFce("(|2|)"),"(abs(2))")								#3
		self.assertEqual(s.StrFce("|2|+5"),"abs(2)+5")								#4
		self.assertEqual(s.StrFce("1-|-2|+5"),"1-abs(-2)+5")						#5
		self.assertEqual(s.StrFce("|-|-20||"),"abs(-abs(-20))")						#6
		self.assertEqual(s.StrFce("|(20-5)|"),"abs((20-5))")						#7
		self.assertEqual(s.StrFce("|(3*5)|*|1-2|-(2*5)"),"abs((3*5))*abs(1-2)-(2*5)")	#8
		self.assertEqual(s.StrFce("|1-|5-2|+|-2**5||"),"abs(1-abs(5-2)+abs(-2**5))")#9
		                                                                            
	def test_complete_calculating(self):
		self.assertEqual(s.calculate("exit()"),"Invalid syntax on input")			#0
		self.assertEqual(s.calculate("Hi guys()"),"Invalid syntax on input")		#1
		self.assertEqual(s.calculate("tg(π/2)"),None)								#2
		self.assertEqual(s.calculate("tg(π/2)*5"),"Invalid syntax on input")		#3
		self.assertEqual(s.calculate("e*5"),13.5914091423)							#4
		self.assertEqual(s.calculate("|3!*-8|"),48)									#5
		self.assertEqual(s.calculate("sin(|(2-1)*|2||)"),0.90929743)    			#6
		self.assertEqual(s.calculate("((25-12)%5)!"),6)								#7
		self.assertEqual(s.calculate("((25-12)%5)%2"),1)							#8
		self.assertEqual(s.calculate("|(2-7)|**((6-1)%(7-5))"),5)					#9
		self.assertEqual(s.calculate("2/0"),"Division by zero")						#10

if ( __name__ == '__main__' ):
    ut.main()