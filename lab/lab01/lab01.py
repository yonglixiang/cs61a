"Q4's solution."
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    
    if k == 0: # special condition
        return 1
    else:
        cal = n # use cal to recorsd the result, the original value is n
        num = n # use num to record the next numbers
        count = 1 # Count begin with 1 means the first time to calculate is the n it self
        while count < k:
            num -= 1 # number falling
            cal *= num
            count += 1 # count rising
        return cal


"Q5's solution."
def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    cal = int(0)
    num = y
    while num > 0:
        cal = cal + num % 10
        num = num // 10 #notice,use // to solve the differences between int and float
    return cal

"Q7's solution."
def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"
    if k > n: # special condition
        return 0
    elif k == n: # special condition
        print(k)
        return 1
    else:
        num = k
        count = 1 # use count to recode the times and help to calculate each number of print
        while num < n: # num = n is the end of the iteration
            num = k * count
            print(num)
            count += 1
        return (count - 1) # notice, in the lastest time of the iteration, the count were added by 1, which should means it should return num-1
        

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    num = n
    while num > 0:
        if num % 100 == 88: # Use % 100 tio find the latest two digits whether 88
            return True
        else:
            num = num // 10 # Use // 10 to decease the digit of the number, from right to left
    return False