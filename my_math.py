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
    for i in range(n):
        n += n*n
    return n
