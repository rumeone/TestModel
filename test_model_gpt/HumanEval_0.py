"""
Utility module for numeric list operations.
"""

from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check if any two numbers in `numbers` are closer than `threshold`.

    Parameters
    ----------
    numbers : List[float]
        List of numeric values.
    threshold : float
        Positive threshold value.

    Returns
    -------
    bool
        True if any pair of numbers is closer than `threshold`, otherwise False.
    """
    assert isinstance(threshold, float) and threshold > 0, "invalid inputs"
    assert isinstance(numbers, list), "invalid inputs"
    assert all(isinstance(v, (int, float)) for v in numbers), "invalid inputs"

    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False
