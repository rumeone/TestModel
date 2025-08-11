"""
Module providing a function to compute the mean absolute deviation of a list of floats.
"""

from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """Calculate the mean absolute deviation of a list of numbers.

    The mean absolute deviation is the average of the absolute differences
    between each element and the mean of the list.

    Parameters
    ----------
    numbers : List[float]
        A non-empty list of floating point numbers.

    Returns
    -------
    float
        The mean absolute deviation.

    Examples
    --------
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    assert all(isinstance(x, float) for x in numbers), "invalid inputs"
    assert numbers != [], "invalid inputs"

    mean_val = sum(numbers) / len(numbers)
    total_abs_diff = 0.0
    for x in numbers:
        total_abs_diff += abs(x - mean_val)
    return total_abs_diff / len(numbers)
