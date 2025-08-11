"""
Utility module for computing the greatest common divisor (GCD) of two positive integers.
"""

def greatest_common_divisor(a: int, b: int) -> int:
    """Return the greatest common divisor of two positive integers a and b."""
    assert type(a) == int and type(b) == int, "invalid inputs"
    assert a > 0 and b > 0, "invalid inputs"
    while b:
        a, b = b, a % b
    return a
