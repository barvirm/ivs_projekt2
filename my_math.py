# -*- coding: utf-8 -*-

## @package my_math
# Mathematical library

## @var pi
# constant π
pi = 3.14159265359
## @var e
# constant e
e =  2.71828182846

## n-th roots are treated as special cases of exponentiation, where the exponent is a fraction 1/n
# @param a number that will be root
# @param n nth root, default is 2
# @return[float] n-th root of number a 
# @return if a is negative integer return None
def sqrt(a,n=2):
    if (a < 0):
        return None
    return a**(1./ (n) )

## When a is a positive integer, exponentiation corresponds to repeated multiplication of the base n times
# @parama number that will be power
# @paramn n-th power
# @returna to the power of n
def pow(a,n):
    return (a)**(n)

## factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n
# @param n number t
# @return a to the power of n
# @return if n is float return None
# @return if n < 0 return None
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
# @param x angle in radian
# @return[float] sin(x)
def sin(x):
    x = (x) % (2*pi)
    result = 0
    for i in range(50):
        result += (-1.)**i * ( ( (x)**(2*i+1.) ) / factorial(2*i+1) )
    return result


## The cosine of an angle is the ratio of the length of the adjacent side to the length of the hypotenuse: so called because it is the sine of the complementary or co-angle.
# @param x angle in radian
# @return[float] cos(x)
def cos(x):
    result = 0

    x = (x) % (2*pi)

    for i in range(1,80):
        result += (-1.)**i * ( ( (x)**(2.*i) ) / factorial(2*i) )
    result += 1
    return result

## The tangent of an angle is the ratio of the length of the opposite side to the length of the adjacent side: so called because it can be represented as a line segment tangent to the circle, that is the line that touches the circle, from Latin linea tangens or touching line (cf. tangere, to touch).
# @param x angle in radian
# @return [float] tg(x)
# @return if x = π/2 or -π/2 return None 
def tg(x):
    if (x == pi/2 or x == -(pi/2) ):
        return None
    return (sin(x)/cos(x))

## The cotg of an angle is the ratio of the length of the adjacent side to the length of the opposite: so called because it is the tg of the complementary or co-angle.
# @param x angle in radian
# @return[float] cotg(x)
# @return if x = π or 0 return None 
def cotg(x):
    if (x == pi or x == 0 ):
        return None
    return (cos(x)/sin(x))

## The natural logarithm of a number is its logarithm to the base of the mathematical constant e, where e is an irrational and transcendental approximately equal to 2.718281828459.
# @param x number
# @return[float] ln(x)
# @return if x<=0 return None
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
    return result

## The modulo operation finds the remainder after division of one number by another.
# if a is negative number is't transform to same non-negative number
# @param a divident
# @param n divisor
# @return remainder after division
def modulo(a,n):
    if (a < 0 ):
        a=abs(a)
    return (a)%(n)
