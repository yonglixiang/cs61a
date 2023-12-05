"""My first Python source file."""


from operator import floordiv, mod

"This code is a example of -m doctest."
from operator import floordiv, mod
def divide_exact(n, d=10):
    """Return the quotient and remainder of diving N by D.
    >>> q, r = divide_exact(2023)
    >>> q
    202
    >>> r
    2
    """
    return floordiv(n, d), mod(n, d)

"This code is a example of conditional statement."
def absolute_value(x):
    """return the absoulte value of x."""
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x

"This code show the the differences between call and control statement."
from math import sqrt

def if_(a, b, c):
    "If a,return b, else return c."
    if a:
        return b
    else:
        return c

def call_real_sqrt(x):
    "Use if_ funvtion to calculate the sqrt."
    return if_(x > 0, sqrt(x), 0.0)

def control_real_sqrt(x):
    "Use contrl statement to calculate the sqrt"
    if x > 0:
        return sqrt(x)
    else:
        return 0.0

"This code is a example of iteration statement."
i, total = 0 , 0
while i < 3 and total < 10:
    i = i + 1
    total = total + i
print(i, total)