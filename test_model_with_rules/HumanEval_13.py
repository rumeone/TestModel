# HumanEval/13
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return the greatest common divisor of two positive integers a and b. """
    while b:
        a, b = b, a % b
    return a
