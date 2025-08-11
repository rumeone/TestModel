"""
Utility module for numeric operations.
"""

import math

def truncate_number(number: float) -> float:
    """Return the decimal part of a positive floating point number.

    The decimal part is the fractional component of the number,
    i.e. the part that is smaller than 1.0.  For example,
    truncate_number(3.5) returns 0.5.

    Parameters
    ----------
    number : float
        A positive floating point number.

    Returns
    -------
    float
        The decimal part of ``number``.
    """
    assert number > 0, "invalid inputs"
    assert isinstance(number, float), "invalid inputs"
    assert not math.isinf(number), "invalid inputs"

    # The integer part is the floor of the number for positives.
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part
