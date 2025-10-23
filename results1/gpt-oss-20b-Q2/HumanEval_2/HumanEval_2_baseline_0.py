import math

def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    if number < 0:
        raise ValueError("Number must be positive")
    # Use floor to avoid issues with floating point representation
    integer_part = math.floor(number)
    return number - integer_part