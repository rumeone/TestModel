# HumanEval/2
import math

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    assert number > 0, "invalid inputs"
    assert isinstance(number, float), "invalid inputs"
    assert number != float("+inf"), "invalid inputs"
    
    integer_part = math.floor(number)
    decimal_part = number - integer_part
    return decimal_part

