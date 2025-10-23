def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Ensure a and b are non-negative by taking absolute values
    # Use the Euclidean algorithm to compute the GCD
    # Continue dividing until b becomes 0, then return a
    while b:
        a, b = b, a % b
    return abs(a)