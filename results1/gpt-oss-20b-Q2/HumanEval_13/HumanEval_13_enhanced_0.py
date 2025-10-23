"""
Utility module for basic number theory operations.
"""

def greatest_common_divisor(a: int, b: int) -> int:
    """Return the greatest common divisor of two integers a and b.

    Uses the Euclidean algorithm, which repeatedly replaces the larger
    number by the remainder of the division until the remainder is zero.
    The last non‑zero remainder is the GCD.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Ensure inputs are integers
    a, b = int(a), int(b)

    # Handle zero cases explicitly
    if a == 0:
        return abs(b)
    if b == 0:
        return abs(a)

    # Euclidean algorithm
    while b:
        a, b = b, a % b  # swap and reduce
    return abs(a)