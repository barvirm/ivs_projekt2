def add(a,b):
    """ return a + b """
    return a+b
def odd(a,b):
    """ return a - b """
    return a-b
def sqrt(a,n):
    """ return sqrt of a """
    return a**(1/n)
def pow(a,n):
    """ return pow of a """
    return a**n
def factorial(n):
    """ return factorial of number n """
    res = 1
    for i in range(1,n+1):
        res = res * i
    return res

def sin(x):
    # bad for high number, fix by divizion pre = 2kpi
    result = 0
    for i in range(10):
        result += (-1.)**i * ( (x**(2*i+1.) ) / factorial(2*i+1) )
    return result

def cos(x):
    # bad for high number, fix by divizion pre = 2kpi
    result = 0
    for i in range(1,11):
        result += (-1.)**i * ( (x**(2.*i) ) / factorial(2*i) )
    result += 1
    return result

print sin(4567981.4567789)
