"""
Utility functions for list manipulation.
"""

from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number `delimeter` between every two consecutive elements of input list `numbers`.

    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:  # Empty list edge case
        return []

    result: List[int] = []
    for idx, value in enumerate(numbers):
        result.append(value)          # original element
        if idx < len(numbers) - 1:  # not last element
            result.append(delimeter)   # insert delimiter

    return result