# HumanEval/13
def greatestCommonDivisor(a: int, b: int) -> int:
    """ Return the greatest common divisor of two integers a and b """
    assert type(a) == int and type(b) == int, "invalid inputs"
    assert a > 0 and b > 0, "invalid inputs"
    while b != 0:
        a, b = b, a % b
    return a
