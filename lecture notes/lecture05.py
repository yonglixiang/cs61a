from operator import add

def applyTwice(f, x):
    return f(f(x))

def square(x):
    return x * x

""" result = applyTwice(square, 2) """

def makeAdder(n):
    def adder(k):
        return n + k
    return adder

adderThree = makeAdder(3)
result = adderThree(4)

def triple(x):
    return 3 * x

def compose1(f=square, g=triple):
    def h(x):
        return f(g(x))
    return h

squile = compose1()
result = squile(5)

"""lambda statement"""
squareLambda = lambda x: x * x
squareLambda(10)

"""Currying Function"""
"This function method is to get special function for fixed items"
def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

addCurrying = curry2(add)
add3 = addCurrying(3)
result = add3(2)
        