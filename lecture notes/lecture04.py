"""The advantage of deviding functions reasonally"""
def prime_factors(n):
    """Print the prime the factor of n in non-decreasing order.
    >>> prime_factors(8)
    2
    2
    2
    >>> prime_factors(9)
    3
    3
    >>> prime_factors(10)
    2
    5
    >>> prime_factors(11)
    11
    >>> prime_factors(858)
    2
    3
    11
    13
    """
    num = n
    while num > 1:
        k = smallest_prime_factor(num) 
        num = num // k
        print(k)

def smallest_prime_factor(n):
    count = 2
    while n % count != 0:
            count = count + 1
    return count

"""The Iteration function example"""
def fib(n):
    """Compute the nth FIbonacci sequence number, for n >= 0
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(5)
    5
    >>> fib(6)
    8
    """
    pred, curr = 1, 0 # 0th and 1st fibonacci number, give a suppose number 1 to help to calculate the 1st number
    count = 0 # curr is the count th number 
    while count < n:
        pred, curr = curr, curr + pred
        count = count + 1
    return curr


"""A function that takes a function as an argument value or
"""
def cube(n):
    return pow(n, 3)
def summation(k, term):
    """sum the first k terms of sequence"""
    cal = 0
    for i in range(1, k + 1):
        cal += term(i)
    return cal

summation(2, cube)

"""Names can be Bound to Functional Arguments"""
def applyTwice(f, x):
    return f(f(x))
def square(x):
    return x * x
# result = applyTwice(square, 2)

"""A function that returns a function as a return value
-- Nested Definitions"""
def makeAdder(n):
    """
    >>> addThree = makeAdder(3)
    >>> addThree(4)
    """
    def adder(k):
        return k + n
    return adder

addThree = makeAdder(3)
addThree(4)

def square(x):
    return x * x

def makeAdd(n):
    def Add(k):
        return n + k
    return Add

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

# compose1(square, makeAdd(2))(3) # square(2+3)

"""Lambda Expressions"""
squareA = lambda x: x * x
squareA(4)
