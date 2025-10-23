"""
Utility to detect close elements in a numeric list.
"""

from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Return True if any two distinct numbers in *numbers* are closer than
    *threshold*; otherwise False.

    Examples
    ---------
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # Quick exit for trivial cases
    if len(numbers) < 2 or threshold <= 0:
        return False

    # Sort to compare only neighbours
    sorted_nums = sorted(numbers)
    for i in range(len(sorted_nums) - 1):
        # Difference between consecutive sorted elements
        if sorted_nums[i + 1] - sorted_nums[i] < threshold:
            return True
    return False