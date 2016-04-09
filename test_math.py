#!/usr/bin/env python
#coding:utf-8
#Made by Marek Barvir

import unittest as ut
import my_math as m
## @class Testing mathematical library
class TestMyMath(ut.TestCase):
    ## Test of function sqrt
    # @test Square root of positive and negative numbers, negative=None
    # @test Cube root of positive and negative numbers, negative=None
    # @test Negative n-th root
    # @param self Pointer to class
    def test_sqrt(self):
        self.assertAlmostEqual(m.sqrt(5),2.236067977)
        self.assertEqual(m.sqrt(-2),None)
        self.assertAlmostEqual(m.sqrt(5.12),2.2627416997)
        self.assertAlmostEqual(m.sqrt(-25.5),None)
        self.assertEqual(m.sqrt(64,3),4)
        self.assertEqual(m.sqrt(-64,3),None)
        self.assertAlmostEqual(m.sqrt(8,-3),0.5)

    ## Test of function pow
    # @test Positive and negative numbers to the power of +/-n
    # @param self Pointer to class
    def test_pow(self):
        self.assertEqual(m.pow(2,5),32)
        self.assertEqual(m.pow(2,-5),1/32.)
        self.assertEqual(m.pow(-2,5),-32)
        self.assertEqual(m.pow(-2,-5),1/-32.)
        self.assertAlmostEqual(m.pow(2.15,5),45.94013843)
        self.assertAlmostEqual(m.pow(2.15,-5),0.0217674572)
        self.assertAlmostEqual(m.pow(-2.15,5),-45.94013843)
        self.assertAlmostEqual(m.pow(-2.15,-5),-0.0217674572)

    ## Test of function factorial
    # @test Positive and negative intiger, negative=None
    # @test Positive and negative float = None
    # @param self Pointer to class
    def test_factorial(self):
        self.assertEqual(m.factorial(5),120)
        self.assertEqual(m.factorial(-2),None)
        self.assertEqual(m.factorial(1.2),None)
        self.assertEqual(m.factorial(-1.2),None)

    ## Test of function sin
    # @test 0,π,π/2
    # @test Positive and negative intiger
    # @param self Pointer to class
    def test_sin(self):
        self.assertAlmostEqual(m.sin(123)   ,-0.45990349)
        self.assertAlmostEqual(m.sin(-23)   ,0.84622040)
        self.assertAlmostEqual(m.sin(0)     ,0)
        self.assertAlmostEqual(m.sin(m.pi)  ,0)
        self.assertAlmostEqual(m.sin(m.pi/2),1)

    ## Test of function cos
    # @test 0,π,π/2
    # @test Positive and negative intiger
    # @param self Pointer to class
    def test_cos(self):
        self.assertAlmostEqual(m.cos(123)   ,-0.8879689)
        self.assertAlmostEqual(m.cos(-23)   ,-0.53283302)
        self.assertAlmostEqual(m.cos(0)     ,1)
        self.assertAlmostEqual(m.cos(m.pi)  ,-1)
        self.assertAlmostEqual(m.cos(m.pi/2),0)

    ## Test of function tan
    # @test 0,π,π/2, +/-π/2 = None
    # @test Positive and negative intiger
    # @param self Pointer to class
    def test_tan(self):
        self.assertAlmostEqual(m.tg(m.pi/2),None)
        self.assertAlmostEqual(m.tg(-m.pi/2),None)
        self.assertAlmostEqual(m.tg(2),-2.18503986)
        self.assertAlmostEqual(m.tg(123),0.51792747)
        self.assertAlmostEqual(m.tg(-1),-1.55740772)
        self.assertAlmostEqual(m.tg(-32),-0.66100604)
    
#    def cotg(self):
        #TODO       

    ## Test of function ln
    # @test Positive number
    # @test 0 and negative number = None
    # @param self Pointer to class
    def test_ln(self):
        self.assertAlmostEqual(m.ln(0.123),-2.0955709)
        self.assertAlmostEqual(m.ln(123),4.81218435)
        self.assertAlmostEqual(m.ln(0),None)
        self.assertAlmostEqual(m.ln(-10),None)

    ## Test of function modulo
    # @test Positive and negative number, negative number = positive result
    # @test Negative modulo, negative result
    # @test Modulo 0 = None
    # @test Negative number negative modulo = same result as positive just negative
    # @param self Pointer to class
    def test_modulo(self):
        self.assertEqual(m.modulo(32,16),0)
        self.assertEqual(m.modulo(33,16),1)
        self.assertEqual(m.modulo(-2,16),2)
        self.assertEqual(m.modulo(33.5,16),1.5)
        self.assertEqual(m.modulo(-2.8,16),2.8)
        self.assertEqual(m.modulo(-2,-16),-2)
        self.assertEqual(m.modulo(33.5,-16),-1.5)
        self.assertEqual(m.modulo(-2,0),None)


if ( __name__ == '__main__' ):
    ut.main()
