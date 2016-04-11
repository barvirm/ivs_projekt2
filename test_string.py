#!/usr/bin/env python
#coding:utf-8
#Made by Marek Barvir

import unittest as ut
import transform_string as s
## @class Testing string transform for eval
class TestMyMath(ut.TestCase):
	def test_modulo(self):
		self.assertEqual(s.StrFce("2+5"),"2+5")
		self.assertEqual(s.StrFce("2%5"),"modulo(2,5)")
		self.assertEqual(s.StrFce("(2%5)"),"modulo(2,5)")
		self.assertEqual(s.StrFce("2+5%2"),"2+modulo(5,2)")
		self.assertEqual(s.StrFce("2+5%(2*2)"),"2+modulo(5,2*2)")
		self.assertEqual(s.StrFce("2%3+5%2"),"modulo(2,3)+modulo(5,2)")
		self.assertEqual(s.StrFce("(2%3)+(5%2)"),"(modulo(2,3))+(modulo(5,2))")
		self.assertEqual(s.StrFce("(2%3**2)+5%2"),"(modulo(2,3**2))+modulo(5,2)")



if ( __name__ == '__main__' ):
    ut.main()