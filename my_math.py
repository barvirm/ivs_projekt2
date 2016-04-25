#!/usr/bin/env python
# -*- coding: utf-8 -*-
## @package my_math
# Implementation of basic matematic function

"""
License: GPL-3.0+
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 .
 This package is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 .
 You should have received a copy of the GNU General Public License
 along with this program. If not, see <http://www.gnu.org/licenses/>.
 .
 On Debian systems, the complete text of the GNU General
 Public License version 3 can be found in "/usr/share/common-licenses/GPL-3".
"""

## @var pi
# Constant π
pi = 3.14159265359
## @var e
# Constant e
e =  2.71828182846
## @var digits
# Number of decimeter digits 
digits = 8
## N-th roots are treated as special cases of exponentiation, where the exponent is a fraction \f$ \frac{1}{n} \f$
# @note \f$ \sqrt[n]{a} \f$
# @param a Number that will be root
# @param n N-th root, default is 2
# @return[float] N-th root of number a 
# @return If a is negative integer return None
def sqrt(a,n=2):
    if (a < 0):
        return None
    return round(a**(1./ (n) ),digits)

## When a is a positive integer, exponentiation corresponds to repeated multiplication of the base n times
# @note \f$ a^n \f$
# @param a Number that will be power
# @param n N-th power
# @return a to the power of n
def pow(a,n):
    return round((a)**(n),digits)

## factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n
# @note n!
# @param n Number t
# @return a to the power of n
# @return If n is float return None
# @return If n < 0 return None
def factorial(n):
    if (n < 0):
        return None
    if ( n == 0 ):
        return 1
    if ( isinstance(n,float) ):
        return None
    res = 1
    for i in range(1,n+1):
        res = res * i
    return res

## Sine, is a trigonometric function of an angle. The sine of an angle is defined in the context of a right triangle: for the specified angle, it is the ratio of the length of the side that is opposite that angle (that is not the hypotenuse) to the length of the longest side of the triangle.
# @note \f$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots  \f$
# @param x Angle in radian
# @return [float] sin(x)
def sin(x):
    x = (x) % (2*pi)
    result = 0
    for i in range(50):
        result += (-1.)**i * ( ( (x)**(2*i+1.) ) / factorial(2*i+1) )
    return round(result,digits)


## The cosine of an angle is the ratio of the length of the adjacent side to the length of the hypotenuse: so called because it is the sine of the complementary or co-angle.
# @note \f$ cos x  = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots \f$
# @param x Angle in radian
# @return [float] cos(x)
def cos(x):
    result = 0

    x = (x) % (2*pi)

    for i in range(1,80):
        result += (-1.)**i * ( ( (x)**(2.*i) ) / factorial(2*i) )
    result += 1
    return round(result,8)

## The tangent of an angle is the ratio of the length of the opposite side to the length of the adjacent side: so called because it can be represented as a line segment tangent to the circle,
# that is the line that touches the circle, from Latin linea tangens or touching line.
# @note \f$ \frac{sin(x)}{cos(x)}\f$
# @param x Angle in radian
# @return [float] tg(x)
# @return If x = π/2 or -π/2 return None 
def tg(x):
    if (x == pi/2 or x == -(pi/2) ):
        return None
    return (sin(x)/cos(x))

## The cotg of an angle is the ratio of the length of the adjacent side to the length of the opposite: so called because it is the tg of the complementary or co-angle.
# @note \f$ \frac{cos(x)}{sin(x)}\f$
# @param x Angle in radian
# @return [float] cotg(x)
# @return If x = π or 0 return None 
def cotg(x):
    if (x == pi or x == 0 ):
        return None
    return (cos(x)/sin(x))

## The natural logarithm of a number is its logarithm to the base of the mathematical constant e, where e is an irrational and transcendental approximately equal to 2.718281828459.
# @note \f$ \log(\frac{1+z}{1-z}) = \cfrac{2z}{1-\cfrac{z^2}{3-\cfrac{4z^2}{5-\cfrac{9z^2}{7-\cfrac{16z^2}{9-\cfrac{25z^2}{11-\cfrac{36z^2}{13-\cdots}}}}}}} \f$
# @param x Number
# @return [float] ln(x)
# @return If x<=0 return None
def ln(x):
    if ( x == 1):
        return 0;
    if ( x <= 0):
        return None
    result = 0
    x = (x-1)/float(x+1)
    n = 250
    liche=2*n-1

    while ( n > 1 ):
        n=n-1
        result= (n**2 * x*x) / float( liche - result )
        liche-=2
    result = 2*x / (1-result)
    return round(result,digits)

## The modulo operation finds the remainder after division of one number by another.
# If a is negative number is't transform to same non-negative number
# If Divisor is negative it's same result as non-negative just with - infront of result
# @note \f$ a\%n \f$
# @param a Divident
# @param n Divisor
# @return Remainder after division
def modulo(a,n):
    if ( (n) == 0 ):
        return None
    if ((a) < 0 ):
        a=abs(a)
    if ( (n) < 0):
        return -( (a) % (abs(n)) )
    return (a)%(n)
