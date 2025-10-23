"""
Utility module for basic statistical calculations.
"""

from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the mean absolute deviation (MAD) of a list of numbers.

    MAD is the average of the absolute differences between each element
    and the mean of the dataset.

    Parameters
    ----------
    numbers : List[float]
        List of numeric values.

    Returns
    -------
    float
        The mean absolute deviation.

    Examples
    --------
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    if not numbers:
        # Empty input is undefined for MAD; raise a clear error.
        raise ValueError("Input list must contain at least one number.")

    # Compute the mean of the dataset.
    mean_val = sum(numbers) / len(numbers)

    # Sum absolute deviations from the mean.
    total_abs_dev = 0.0
    for num in numbers:
        total_abs_dev += abs(num - mean_val)

    # Return the average absolute deviation.
    return total_abs_dev / len(numbers)