""" Optional problems for Lab 3 """

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def divider(i):
        if i == 1:
            return True
        elif n % i == 0:
            return False
        else:
            return divider(i - 1)
    
    return divider(n - 1)
    

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    a, b = max(a, b), min(a, b)
    if a == b or a % b == 0:
        return b
    else:
        return gcd(b, a % b)
    

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    def pair(left_rest, digit):
        if left_rest == 0:
            return 0
        elif left_rest % 10 + digit == 10:
            return 1 + pair(left_rest // 10, digit)
        else:
            return pair(left_rest // 10, digit)

    if n < 10:
        return 0
    else:
        return ten_pairs(n // 10) + pair(n // 10, n % 10)