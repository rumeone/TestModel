import math

def truncate_number(number: float) -> float:
    """Return decimal part of a positive floating point number."""
    if number < 0:
        raise ValueError("Number must be positive")
    fractional, _ = math.modf(number)
    return fractional