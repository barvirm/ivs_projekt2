#Made by Marek Barvir

import unittest as ut
import my_math as m

class TestMyMath(ut.TestCase):

    def test_add(self):
        self.assertEqual(m.add(1,5),6)
        self.assertEqual(m.add(-5,5),0)
        self.assertEqual(m.add(123,0),123)

    def test_odd(self):
        self.assertEqual(m.odd(1,5),-4)
        self.assertEqual(m.odd(-5,-5),0)
        self.assertEqual(m.odd(5,-5),10)

    def test_division(self):
        self.assertAlmostEqual(m.division(5,6),0.83333333)
        self.assertEqual(m.division(5,0),None)
        self.assertEqual(m.division(6,5),1.2)
        self.assertAlmostEqual(m.division(-2,5),-0.4)

    def test_multiplication(self):
        self.assertEqual(m.multiplication(5,6),30)
        self.assertEqual(m.multiplication(5,0),0)
        self.assertEqual(m.multiplication(-2,6),-12)
        self.assertEqual(m.multiplication(-6,-3),18)
        self.assertAlmostEqual(m.multiplication(-2.12,5),-10.6)

    def test_sqrt(self):
        self.assertAlmostEqual(m.sqrt(5),2.236067977)
        self.assertAlmostEqual(m.sqrt(25),5)
        self.assertEqual(m.sqrt(-2),None)
        self.assertEqual(round(m.sqrt(64,3),8) ,4)
        self.assertAlmostEqual(m.sqrt(54,3),3.7797631)

    def test_pow(self):
        self.assertEqual(round(m.pow(2,5),8),32)
        self.assertAlmostEqual(round(m.pow(2.15,5),8),45.94013843)
        self.assertAlmostEqual(round(m.pow(2.15,5.2),8),53.54020029)

    def test_factorial(self):
        self.assertEqual(m.factorial(5),120)
        self.assertEqual(m.factorial(-2),None)
        self.assertEqual(m.factorial(1.2),None)

    def test_sin(self):
        self.assertAlmostEqual(round( m.sin(123),8)   ,-0.45990349)
        self.assertAlmostEqual(round( m.sin(-23),8)   ,0.84622040)
        self.assertAlmostEqual(round( m.sin(0),8)     ,0)
        self.assertAlmostEqual(round( m.sin(m.pi),8)  ,0)
        self.assertAlmostEqual(round( m.sin(m.pi/2),8),1)

    def test_cos(self):
        self.assertAlmostEqual(round( m.cos(123),8)   ,-0.8879689)
        self.assertAlmostEqual(round( m.cos(-23),8)   ,-0.53283302)
        self.assertAlmostEqual(round( m.cos(0),8)     ,1)
        self.assertAlmostEqual(round( m.cos(m.pi),8)  ,-1)
        self.assertAlmostEqual(round( m.cos(m.pi/2),8),0)
    
    def test_tan(self):
        self.assertAlmostEqual(m.tan(m.pi/2),None)
        self.assertAlmostEqual(m.tan(2),-2.18503986)
        self.assertAlmostEqual(m.tan(123),0.51792747)
        self.assertAlmostEqual(m.tan(-1),-1.55740772)
        self.assertAlmostEqual(m.tan(-32),-0.66100604)
    
#    def cotg(self):
        #TODO       

    def test_ln(self):
        self.assertAlmostEqual(m.ln(0.123),-2.0955709)
        self.assertAlmostEqual(m.ln(123),4.81218435)
        self.assertAlmostEqual(m.ln(0),None)
        self.assertAlmostEqual(m.ln(-10),None)
    
    def test_abx(self):
        self.assertEqual(m.abx(-2),2)
        self.assertEqual(m.abx(2),2)
        self.assertEqual(m.abx(0),0)

    def test_modulo(self):
        self.assertEqual(m.modulo(32,16),0)
        self.assertEqual(m.modulo(33,16),1)
        self.assertEqual(m.modulo(-2,16),2)


if ( __name__ == '__main__' ):
    ut.main()
