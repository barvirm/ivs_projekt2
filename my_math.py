
pi = 3.14159265359

def add(a,b):
    """ return a + b """
    return (a) + (b)
def odd(a,b):
    """ return a - b """
    return (a) - (b)
def division(a,b):
    """ return a / b """
    if (b == 0 ):
        return None
    return ( float(a) / float(b) )
def multiplication(a,b):
    """ return a * b """
    return a*b
def sqrt(a,n=2):
    """ return sqrt of a """
    if (a < 0):
        return None
    return a**(1./ (n) )
def pow(a,n):
    """ return pow of a """
    return (a)**(n)
def factorial(n):
    """ return factorial of number n """
    if (n <= 0):
        return None
    if ( isinstance(n,float) ):
        return None
    res = 1
    for i in range(1,n+1):
        res = res * i
    return res

def sin(x):
    """ return sin(x) x --> radian """
    x = (x) % (2*pi)
    result = 0
    for i in range(50):
        result += (-1.)**i * ( ( (x)**(2*i+1.) ) / factorial(2*i+1) )
    return result

def cos(x):
    """ return cos(x) x --> radian """
    result = 0

    x = (x) % (2*pi)

    for i in range(1,80):
        result += (-1.)**i * ( ( (x)**(2.*i) ) / factorial(2*i) )
    result += 1
    return result

def tan(x):
    if (x == pi/2 or x == -(pi/2) ):
        return None
    return (sin(x)/cos(x))

def cotg(x):
    if (x == pi or x == 0 ):
        return None
    return (cos(x)/sin(x))

def ln(x):
    if ( x <= 0):
        return None
    result = 0
    x = (x-1)/float(x+1)
    n = 250
    liche=2*n-1
    while (n > 1 ):
        n=n-1
        result= (n**2 * x*x) / float( liche - result )
        liche-=2
    result = 2*x / (1-result)
    return result

def abx(x):
    if (x<0):
        return -(x)
    else:
        return x

def modulo(a,n):
    if (a < 0 ):
        a=abx(a)
    return (a)%(n)
