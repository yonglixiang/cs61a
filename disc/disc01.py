"""Discussion 1 code."""

"""Q1's solution. 
1. the result of the three pieces of code is following 12, 19, 12.
2. 1st and 3rd result in the same result
In the 1st piece of code, 
when x > 10, the program just exclute the first conditional suit, it didn't exclute the following elif suits. 
So in the end of this function, it returned x + 2.
--In the 3rd piece of code, 
when x > 10, the program return the value of x + 2, and then ended this function.
3. If the suits of each header include a return statement, it would be the same as both if and elif cases
"""

"Q2's solution."
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    "*** YOUR CODE HERE ***"
    if temp < 50 or raining == True:
        return True
    else:
        return False

"Q3's solution."
def nearest_ten(n):
    """
    >>> nearest_ten(0)
    0
    >>> nearest_ten(4)
    0
    >>> nearest_ten(5)
    10
    >>> nearest_ten(61)
    60
    >>> nearest_ten(2023)
    2020
    """
    "*** YOUR CODE HERE ***"
    if n % 10 < 5:
        return n // 10 * 10
    else:
        return n // 10 * 10 + 10

"""Q4's solution.
x wered added many many times in this code.
When the x = 5, the header's expression of while statement in so_slow() function is a true value permanently,
so the suit of this header were evaluated many many times.
"""
    
"Q5's solution."
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return False
    else:
        i = 2
        while i < n:
            if n % i == 0:
                return False
            else:
                i = i + 1
        return True

"Q6's solution."
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result is None  # No return value
    True
    """
    "*** YOUR CODE HERE ***"
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
        i = i + 1

"Q7's solution."
def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    num = n
    numset = set([]) #use set() to remove duplicate numbers.
    while num > 0:
        numset.add(num % 10) #Use % to find each digit, and add it to numset.
        num = num // 10
    return len(numset)


def has_digit(n, k):
    """Returns whether K is a digit in N.
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    "*** YOUR CODE HERE ***"
    num = n
    numset = set([]) #use set() to remove duplicate numbers.
    while num > 0:
        numset.add(num % 10) #Use % to find each digit, and add it to numset.
        num = num // 10
    return k in numset #Use in to check whether numset has k or not.


"""Q8's solution:
x = 3
y = 3
x = 9
"""

"""Q9's solution:
doule     function double
triple    function triple
hat       function double
double    function triple
"""