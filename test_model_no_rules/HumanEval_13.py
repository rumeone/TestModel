# HumanEval/13
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    assert type(a) == int and type(b) == int, "invalid inputs"
    assert a > 0 and b > 0, "invalid inputs"
    
    while b != 0:
        a, b = b, a % b
        
    return a

